# Optional formatting

## optional_format

this function - [`OptionalFormatter().format`](#optionalformatter)

Does not require entering all the variables represented by fields in the string.
The rest is [str.format](https://docs.python.org/3/library/stdtypes.html#str.format) functionality.

### Example 1

```python
>>> from pyformatting import optional_format
>>> txt = optional_format('{1}{2}{0}', 'first')
>>> txt
'{1}{2}first'
>>> optional_format(txt, '--', 'second')
'second{2}first'
```

In the first case, only one field was formatted.
In the second case, only the second argument was used for formatting.

### Example 2

```python
>>> txt = optional_format('{b}{c}{a}', a='first')
>>> txt
'{b}{c}first'
>>> optional_format(txt, a='--', b='second')
'second{c}first'
```

Here is the same as in the [first example](#example-1), only with keyword arguments.

### Example 3

requires python >= 3.4

```python
>>> txt = optional_format('{}{}{}', 'first')
>>> txt
'first{}{}'
>>> optional_format(txt, '--', 'second')
'first--second'
```

Empty fields will use all arguments, regardless of position.

## OptionalFormatter

Inherits from [string.Formatter](https://docs.python.org/3/library/string.html#string.Formatter) and changes its behavior.  
Has different implementations depending on the python version.
