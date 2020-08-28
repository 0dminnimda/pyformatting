# -*- coding: utf-8 -*-

import string
from .helpers import PY_34

__all__ = (
    "OptionalFormatter",
)


if PY_34:
    class OptionalFormatter(string.Formatter):
        def _vformat(self, format_string, args, kwargs, used_args, recursion_depth,
                     auto_arg_index=0):
            if recursion_depth < 0:
                raise ValueError('Max string recursion exceeded')
            result = []
            for literal_text, field_name, format_spec, conversion in \
                    self.parse(format_string):

                # output the literal text
                if literal_text:
                    result.append(literal_text)

                # if there's a field, output it
                if field_name is not None:
                    # this is some markup, find the object and do
                    #  the formatting

                    # handle arg indexing when empty field_names are given.
                    self.field_name_is_empty = False
                    if field_name == '':
                        if auto_arg_index is False:
                            raise ValueError('cannot switch from manual field '
                                             'specification to automatic field '
                                             'numbering')
                        field_name = str(auto_arg_index)
                        self.field_name_is_empty = True
                        auto_arg_index += 1
                    elif field_name.isdigit():
                        if auto_arg_index:
                            raise ValueError('cannot switch from manual field '
                                             'specification to automatic field '
                                             'numbering')
                        # disable auto arg incrementing, if it gets
                        # used later on, then an exception will be raised
                        auto_arg_index = False

                    # given the field_name, find the object it references
                    #  and the argument it came from
                    obj, arg_used = self.get_field(field_name, args, kwargs)
                    used_args.add(arg_used)

                    # do any conversion on the resulting object
                    obj = self.convert_field(obj, conversion)

                    # expand the format spec, if needed
                    format_spec, auto_arg_index = self._vformat(
                        format_spec, args, kwargs,
                        used_args, recursion_depth-1,
                        auto_arg_index=auto_arg_index)

                    # format the object and append to the result
                    result.append(self.format_field(obj, format_spec))

            return ''.join(result), auto_arg_index

        def get_value(self, key, args, kwargs):
            if isinstance(key, int):
                if len(args) > key:
                    return args[key]
            else:
                get = kwargs.get(key)
                if get is not None:
                    return get

            if self.field_name_is_empty:
                return "{}"
            else:
                return "{" + "{0}".format(key) + "}"
else:
    class OptionalFormatter(string.Formatter):
        def get_value(self, key, args, kwargs):
            if isinstance(key, int):
                if len(args) > key:
                    return args[key]
            else:
                get = kwargs.get(key)
                if get is not None:
                    return get

            return "{" + "{0}".format(key) + "}"
