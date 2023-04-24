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

PyKagi is a Python library that simplifies the use of the Kagi API. With this library, you can easily implement features like text summarization, web content summarization, and search with just a few lines of code.


<br>

## Installation

```bash
pip install PyKagi --upgrade
```

<br>

## Usage

### Universal Summarizer API

- Text summarization

With the Universal Summarizer, you can generate a summary of a given text. You can specify the summarization engine, target language for translation, and caching preferences. Here's an example of how to use the Universal Summarizer to summarize a text.

```python
from PyKagi import UniversalSummarizer

API_KEY = "your api key"
US = UniversalSummarizer(API_KEY)

text = f"""Thank you. I'm honored to be with you today for your commencement from one of the finest universities in the world. Truth be told, I never graduated from college, and this is the closest I've ever gotten to a college graduation. Today I want to tell you three stories from my life. That's it. No big deal. Just three stories. (...)"""
engine = "agnes"
target_language = "KO"
cache = True

result = US.summarize(
    text = text,
    engine = engine,
    target_language = target_language,
    cache = cache
)
result
```

- Web content summarization

The Universal Summarizer also provides the capability to summarize web page content. In the example code below, you can pass the URL of a web page to generate a summary of its content. Additionally, you can obtain a summary translated into the desired language.


```python
from PyKagi import UniversalSummarizer

API_KEY = "your api key"
US = UniversalSummarizer(API_KEY)

url = "https://namu.wiki/w/Midjourney"
engine = "agnes"
target_language = "KO"
cache = True

result = US.summarize(
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