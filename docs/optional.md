# Optional formatting

The [optional_format()](#optional_format) method, the [str.format()](https://docs.python.org/3/library/stdtypes.html#str.format) method and the [OptionalFormatter](#optionalformatter) class share the same syntax for format strings.

## optional_format

The [optional_format()](#optional_format) method is equivalent to [OptionalFormatter().format](#optionalformatter) method

Does not require entering all the variables represented by replacement fields in the string.
The rest is [str.format](https://docs.python.org/3/library/stdtypes.html#str.format) functionality.

## OptionalFormatter

Inherits from [BaseFormatter](/base) and changes its behavior.  

## Examples

Accessing arguments by position:

```python
>>> from pyformatting import optional_format
>>> optional_format('{0}{2}{1}', 'first')  # only one replacement field will be formatted
'first{2}{1}'
>>> optional_format('first{2}{1}', '--', 'third')  # only the second argument will be used
'second{1}first'
>>> optional_format('{}{}{}', 'first')
'first{}{}'
>>> optional_format('first{}{}', '--', 'third')  # empty replacement fields will use all arguments
'first--third'
```

Accessing arguments by name:

```python
>>> optional_format('{a}{b}{c}', a='first')
'first{b}{c}'
>>> optional_format('first{b}{c}', a='--', c='third')
'first{b}third'
```
