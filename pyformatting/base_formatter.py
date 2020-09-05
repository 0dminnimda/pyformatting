# -*- coding: utf-8 -*-

from .helpers import PY_34, PY_37, PY_38

try:  # 3.0, 3.1
    _formatter_parser = str._formatter_parser
    _formatter_field_name_split = str._formatter_field_name_split
except AttributeError:  # 3.2+
    from _string import (
        formatter_parser as _formatter_parser,
        formatter_field_name_split as _formatter_field_name_split)

__all__ = (
    "BaseFormatter",
    "_formatter_parser",
    "_formatter_field_name_split")


class BaseFormatter:
    def format(*args, **kwargs):
        if not args:
            raise TypeError("descriptor 'format' of 'Formatter' object "
                            "needs an argument")
        self, *args = args  # allow the "self" keyword be passed
        try:
            format_string, *args = args  # allow the "format_string" keyword be passed
        except ValueError:
            raise TypeError("format() missing 1 required positional "
                            "argument: 'format_string'") from None
        return self.vformat(format_string, args, kwargs)

    def vformat(self, format_string, args, kwargs):
        return self._vformat(format_string, args, kwargs, 2)[0]

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
                obj = self.get_field(field_name, args, kwargs)

                # do any conversion on the resulting object
                obj = self.convert_field(obj, conversion)

                # expand the format spec, if needed
                format_spec, auto_arg_index = self._vformat(
                    format_spec, args, kwargs, recursion_depth-1,
                    auto_arg_index=auto_arg_index)

                # format the object and append to the result
                result.append(self.format_field(obj, format_spec))

        return ''.join(result), auto_arg_index

    def get_value(self, key, args, kwargs):
        if isinstance(key, int):
            return args[key]
        else:
            return kwargs[key]

    def format_field(self, value, format_spec):
        return format(value, format_spec)

    def convert_field(self, value, conversion):
        # do any conversion on the resulting object
        if conversion is None:
            return value
        elif conversion == 's':
            return str(value)
        elif conversion == 'r':
            return repr(value)
        elif conversion == 'a':
            return ascii(value)
        raise ValueError("Unknown conversion specifier {0!s}".format(conversion))

    def parse(self, format_string):
        """returns an iterable that contains tuples of the form:
        (literal_text, field_name, format_spec, conversion)
        literal_text can be zero length
        field_name can be None, in which case there's no
         object to format and output
        if field_name is not None, it is looked up, formatted
         with format_spec and conversion and then used
        """
        return _formatter_parser(format_string)

    def get_field(self, field_name, args, kwargs):
        """given a field_name, find the object it references.
         field_name:   the field being looked up, e.g. "0.name"
                        or "lookup[3]"
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

        return obj


if PY_38:
    from .format_38 import _format

    class BaseFormatter(BaseFormatter):
        format = _format
elif PY_34 and not PY_37:  # 3.4, 3.5, 3.6
    def _format(*args, **kwargs):
        if not args:
            raise TypeError("descriptor 'format' of 'Formatter' object "
                            "needs an argument")
        self, *args = args  # allow the "self" keyword be passed
        try:
            # allow the "format_string" keyword be passed
            format_string, *args = args
        except ValueError:
            if 'format_string' in kwargs:
                format_string = kwargs.pop('format_string')
                import warnings
                warnings.warn("Passing 'format_string' as keyword argument is "
                              "deprecated", DeprecationWarning, stacklevel=2)
            else:
                raise TypeError("format() missing 1 required positional "
                                "argument: 'format_string'") from None
        return self.vformat(format_string, args, kwargs)

    class BaseFormatter(BaseFormatter):
        format = _format
