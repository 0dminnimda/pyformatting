# -*- coding: utf-8 -*-

from .base_formatter import BaseFormatter, _formatter_field_name_split

__all__ = (
    "OptionalFormatter",
)


class OptionalFormatter(BaseFormatter):
    def _vformat(self, format_string, args, kwargs, recursion_depth,
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
                field_name_is_empty = False
                if field_name == '':
                    if auto_arg_index is False:
                        raise ValueError('cannot switch from manual field '
                                         'specification to automatic field '
                                         'numbering')
                    field_name = str(auto_arg_index)
                    auto_arg_index += 1
                    field_name_is_empty = True
                elif field_name.isdigit():
                    if auto_arg_index:
                        raise ValueError('cannot switch from manual field '
                                         'specification to automatic field '
                                         'numbering')
                    # disable auto arg incrementing, if it gets
                    # used later on, then an exception will be raised
                    auto_arg_index = False

                # given the field_name, find the object it references
                obj, apply_format = self.get_field(
                    field_name, field_name_is_empty, args, kwargs)

                # if apply format convert field, call _vformat and format field
                if apply_format:
                    # do any conversion on the resulting object
                    obj = self.convert_field(obj, conversion)

                    # expand the format spec, if needed
                    format_spec, auto_arg_index = self._vformat(
                        format_spec, args, kwargs, recursion_depth-1,
                        auto_arg_index=auto_arg_index)

                    # format the object
                    obj = self.format_field(obj, format_spec)
                else:
                    # append conversion to object if there is conversion
                    if conversion is not None:
                        obj += "!" + conversion

                    # append format_spec to object if there is format_spec
                    if format_spec is not None:
                        obj += ":" + format_spec

                    obj = "{" + obj + "}"

                # append object to the result
                result.append(obj)

        return ''.join(result), auto_arg_index

    def get_value(self, key, field_name_is_empty, args, kwargs):
        if isinstance(key, int):
            if len(args) > key:
                return args[key], True
        else:
            get = kwargs.get(key)
            if get is not None:
                return get, True

        if field_name_is_empty:
            return "", False
        else:
            return str(key), False

    def get_field(self, field_name, args, kwargs):
        """given a field_name, find the object it references.
         field_name:   the field being looked up, e.g. "0.name"
                        or "lookup[3]"
         args, kwargs: as passed in to vformat
        """
        first, rest = _formatter_field_name_split(field_name)

        obj, apply_format = self.get_value(first, args, kwargs)

        # if apply format loop through the rest of the field_name, doing
        #  getattr or getitem as needed
        if apply_format:
            for is_attr, i in rest:
                if is_attr:
                    obj = getattr(obj, i)
                else:
                    obj = obj[i]

        return obj, apply_format
