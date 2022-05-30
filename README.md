# Auto plain nested quotes

The purpose of this package is to provide a simple way to get a correct scaped nested quoted string from an unescaped one. The input string uses a combination of single and double quotes. The output one is always using one type of quotes but scaping it wherever needed.

## Getting started

Installation via pip:

```shell
pip install plainquotes
```

Using it:

```python
from plainquotes import plain_quotes

print(plain_quotes("""'This is a "simpler" quoted string'"""))
```

Output:
```shell
'This is a \'simpler\' quoted string'
```