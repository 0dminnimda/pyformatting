# pyformatting

**Pyformatting** is a collection of useful formatting features.

```python
>>> from pyformatting import optional_format
>>> optional_format('{number:.3f}{other}', number=.12345)
'0.123{other}'
>>> optional_format('{0.imag}{1}{2}{0.real}', 1+3j)
'3.0{1}{2}1.0'
>>> optional_format('{first}{string!r}{4}', string='cool')
"{first}'cool'{4}"
```

## Installing Pyformatting and Supported Versions

Pyformatting is available on PyPI:

```console
python -m pip install -U pyformatting
```

Pyformatting supports Python 3.0+.
