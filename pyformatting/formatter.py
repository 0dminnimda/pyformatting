# -*- coding: utf-8 -*-

from .base_formatter import BaseFormatter, _formatter_field_name_split
from .helpers import PY_32

__all__ = ("Formatter")


class Formatter(BaseFormatter):
    def vformat(self, format_string, args, kwargs):
        used_args = set()
        result, _ = self._vformat(format_string, args, kwargs, used_args, 2)
        self.check_unused_args(used_args, args, kwargs)
        return result

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
                if field_name == '':
                    if auto_arg_index is False:
                        raise ValueError('cannot switch from manual field '
                                         'specification to automatic field '
                                         'numbering')
                    field_name = str(auto_arg_index)
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

    def check_unused_args(self, used_args, args, kwargs):
        pass

    def get_field(self, field_name, args, kwargs):
        """given a field_name, find the object it references.
         field_name:   the field being looked up, e.g. "0.name"
                        or "lookup[3]"
         used_args:    a set of which args have been used
         args, kwargs: as passed in to vformat
        """
        first, rest = _formatter_field_name_split(field_name)

        obj = self.get_value(first, args, kwargs)

        # loop through the rest of the field_name, doing
        #  getattr or getitem as needed
        for is_attr, i in rest:
            if is_attr:
                obj = getattr(obj, i)
            else:
                obj = obj[i]

        return obj, first


# add class docs
if PY_32:
    class BaseFormatter(BaseFormatter):
        """the Formatter class
        see PEP 3101 for details and purpose of this class

        The hard parts are reused from the C implementation.
        They're exposed as "_" prefixed methods of str.

        The overall parser is implemented in _string.formatter_parser.
        The field name parser is implemented in _string.formatter_field_name_split
        """
        pass
else:
    class BaseFormatter(BaseFormatter):
        """the Formatter class
        see PEP 3101 for details and purpose of this class

        The hard parts are reused from the C implementation.
        They're exposed as "_" prefixed methods of str and unicode.

        The overall parser is implemented in str._formatter_parser.
        The field name parser is implemented in str._formatter_field_name_split
        """
        pass
