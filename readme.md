![multiple_loader Logo](https://github.com/Domzou-kun/drint/blob/main/docs/img/logo.png?raw=true)

<div align="center">
   
   <a href="">![PyPI](https://img.shields.io/pypi/v/drint)</a>
   <a href="">![PyPI - Python Version](https://img.shields.io/pypi/pyversions/drint)</a>
   <a href="">![PyPI - Format](https://img.shields.io/pypi/format/drint)</a>
   <a href="">![PyPI - License](https://img.shields.io/pypi/l/drint)</a>
   <a href="">[![Downloads](https://static.pepy.tech/personalized-badge/drint?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/drint)</a>
   <a href="">![GitHub issues](https://img.shields.io/github/issues/Domzou-kun/drint)</a>
   <br>
   <a href="">![GitHub followers](https://img.shields.io/github/followers/Domzou-kun?style=social)</a>
   <a href="">[![Twitter](https://badgen.net/badge/icon/tweet?icon=twitter&label)](https://twitter.com/intent/tweet?text="drint"%20is%20a%20recommended%20repository😊👍%0a&url=https://github.com/Domzou-kun/drint&hashtags=Github,Python)
   </a>


</div>

<div align="center">
   <br>
   
   # **the latest version of 1.0.3🎉**
   ## Changes in the new version of **1.0.3**
   **- fix code -**  
   <br>

</div>

---
# drint
`drint` is a library that outputs `dict` type objects in python to console and other applications, fully formatted and displayed. This will improve debugging, output, and other tasks.

---

## Description of drint
`drint` is a library that outputs dict type objects in python to console and other applications, fully formatted and displayed. In general, dict is displayed in python using `pprint`, etc., but this library can output dict in a more complete form than `pprint`.

---

## More about drint
`drint` displays dict types in perfect alignment.
Below is a test dict and an example of its display.

```Python
from dict_viewer.drint import drint

test_d3 = {
   "e": "EEE",
   "f": "FFF",
   "g": "GGG"
}

test_d2 = {
   "c": test_d3,
   "d": "DDD" 
}

test_d1 = {
   "a": "AAA",
   "b": test_d2
}

# drint
drint(test_d1)

```
The result is as follows:

```
{
    "a": AAA
    "b": {
        "c": {
            "e": EEE
            "f": FFF
            "g": GGG
        }
        "d": DDD
    }
}
```

Compared to the output with pprint and print, it is clearly aligned.
```
# print
{'a': 'AAA', 'b': {'c': {'e': 'EEE', 'f': 'FFF', 'g': 'GGG'}, 'd': 'DDD'}}

# pprint
{'a': 'AAA', 'b': {'c': {'e': 'EEE', 'f': 'FFF', 'g': 'GGG'}, 'd': 'DDD'}}

# drint
{
    "a": AAA
    "b": {
        "c": {
            "e": EEE
            "f": FFF
            "g": GGG
        }
        "d": DDD
    }
}
```

Also, with drint, indentation can be specified.


## Optional arguments, etc
The list of arguments, etc. that can be used in `drint` is as follows.
```
from dict_viewer.drint import drint

drint(
   dict,      # Required argument
   indent     # defalut value is 4
)
```

---

## Getting Started
### Installing

### Latest drint via [PyPI](https://pypi.org/project/drint/) (pip install)
![PyPI](https://img.shields.io/pypi/v/drint)
[![Downloads](https://static.pepy.tech/badge/drint/month)](https://pepy.tech/project/drint)
```
pip install drint
```

### Install by pip from github

```
pip install git+https://github.com/Domzou-kun/drint.git
```
or install via SSH
```
pip install git+git://github.com:Domzou-kun/drint.git
```

## Authors

Domzou

## link
 - The link to PyPI is here.  
    - [PyPI project link](https://pypi.org/project/drint/)  

## Version history
If you want to know about past versions, please refer to [version history](https://github.com/Domzou-kun/drint/blob/main/docs/version_history.txt).

## LICENSE
drint has a MIT license, as found in the [LICENSE file](https://github.com/Domzou-kun/drint/blob/main/LICENSE).





