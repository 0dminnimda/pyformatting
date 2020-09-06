# pyformatting

**Pyformatting** is a collection of useful formatting features.

```python
>>> from pyformatting import optional_format, defaultformatter
>>> optional_format('{:.3f}{other:.5f}{}', .12345)
'0.123{other:.5f}{}'
>>> optional_format('{0[0]}{1!a}{2}{0[1]!r}', 'cool')
"c{1!a}{2}'o'"
>>> default_format = defaultformatter(str)
>>> default_format('{nothing}{data}{quotes!r}', data={1: 2})
"{1: 2}''"
```

## Installing Pyformatting

Pyformatting is available on PyPI:

```console
python -m pip install -U pyformatting
```

## Supported Versions

Pyformatting supports Python 3.1+.

## Development Status

Pre-Alpha
