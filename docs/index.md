# pyformatting

**Pyformatting** is a collection of useful formatting features.

```python
>>> from pyformatting import optional_format, defaultformatter
>>> optional_format('{number:.3f}{other}', number=.12345)
'0.123{other}'
>>> optional_format('{0.imag}{1}{2}{0.real}', 1+3j)
'3.0{1}{2}1.0'
>>> optional_format('{first}{string!r}{42}', string='cool')
"{first}'cool'{42}"
>>> default_format = defaultformatter(int)
>>> default_format('{zero}{data}{zero_again}', data={1: 2})
'0{1: 2}0'
```

python >= 3.4:

```python
>>> from pyformatting import optional_format
>>> optional_format('{}{other}{some}', some=[1, 2])
'{}{other}[1, 2]'
```

## Installing Pyformatting and Supported Versions

Pyformatting is available on PyPI:

```console
python -m pip install -U pyformatting
```

Pyformatting supports Python 3.0+.
