<div align="center">

<b>Kagi API Python Wrapper</b><br>
<b>🚀`pip install PyKagi --upgrade`</b>

[![PyPI Latest Release](https://img.shields.io/pypi/v/pykagi.svg)](https://pypi.org/project/pykagi/)
![](https://img.shields.io/badge/API-KAGI-orange.svg)
[![Downloads](https://static.pepy.tech/badge/pykagi)](https://pepy.tech/project/pykagi)  


</div>

<br>

<div align="left">

## PyKagi


<br>

## Installation

```bash
pip install PyKagi --upgrade
```

<br>

## Usage

### Universal Summarizer API

```python
from PyKagi import UniversalSummarizer

API_KEY = "your api key"
US = UniversalSummarizer(API_KEY)

method = "POST"
url = "https://namu.wiki/w/Midjourney"
engine = "agnes"
target_language = "KO"
cache = True

result = US.summarize(
    method = method,
    url = url,
    engine = engine,
    target_language = target_language,
    cache = cache
)
result
```

### Search API

```python
from PyKagi import Search

API_KEY = "your api key"
S = Search(API_KEY)

query = "Steve Jobs"
limit = 10
result = S.search(
    query=query, 
    limit=limit
)
result
```

<br>

## Contributors

<a href="https://github.com/wooiljeong/pykagi/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=wooiljeong/pykagi" />
</a>