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

```json
{'meta': {'id': '703a85c1-4548-4803-8309-2cc0481eaf60',
  'node': 'asia-southeast1',
  'ms': 0,
  'api_balance': 13.058023},
 'data': {'output': '연설자는 세계 최고의 대학 중 하나의 졸업식에 참석할 수 있어 영광으로 생각한다. 그는 대학을 졸업하지 못했지만 이번 졸업식이 대학 졸업에 가장 가까운 경험이라 생각한다. 그는 청중들과 자신의 삶에서 세 가지 이야기를 나눌 계획이다. 연설자는 이것이 큰 일이라고 생각하지 않는다. 그가 나눌 이야기는 청중들에게 흥미로울 수 있다. 연설자는 그가 나눌 이야기에 대해 추가적인 세부 정보를 제공하지 않는다. 청중들은 그 이야기들이 통찰력 있거나 매력적일 수 있다. 연설자의 대학 학위 부재는 그의 삶의 경험의 가치를 떨어뜨리지 않는다. 연설자는 청중들에게 영감과 동기부여를 주기 위해 연설할 의도이다.',
  'tokens': 0}}
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

```json
{'meta': {'id': '6cb208c8-ec06-4bcd-a2f7-cdf5d5ee9feb',
  'node': 'asia-southeast1',
  'ms': 0,
  'api_balance': 13.058023},
 'data': {'output': 'Midjourney는 텍스트에서 이미지를 생성하거나 이미지를 텍스트에 삽입할 수 있는 인공지능 연구소입니다. 이 소프트웨어는 현실적이고 추상적인 예술적 표현에 특화되어 있으며, 입력 키워드에 따라 만화 스타일의 그림도 생성할 수 있습니다. Midjourney는 무료 체험 버전을 제공하여 사용자가 최대 25개의 이미지를 생성할 수 있지만, 더 많은 이미지를 생성하려면 유료 구독이 필요합니다. 그러나 이 소프트웨어는 완벽하지 않으며, 만족스러운 결과를 보장할 수 없어 돈을 낭비할 수 있습니다. Midjourney는 콜로라도 주 박람회의 디지털 아트 부문에서 1위를 차지한 우주 오페라 극장을 비롯한 다양한 예술 작품을 만드는 데 사용되었습니다. 그러나 Midjourney의 사용에 대한 논란이 있었으며, 일부 예술가들은 이 소프트웨어가 저작권을 침해한다고 주장했습니다. 한 사례에서는 Midjourney에서 생성된 이미지를 사용한 소설의 저작권이 미국 저작권국에 의해 취소되었지만, 저자가 직접 편집하고 쓴 부분의 저작권은 인정되었습니다. Midjourney는 Waifu Labs와 협력하여 Midjourney의 애니메이션 스타일 그림에 특화된 AI 모델인 Niji Journey를 만들었습니다. 이 소프트웨어는 Ilya Kuvshinov와 Mika Pikazo와 같은 인기 일러스트레이터와 유사한 다양한 그림 스타일을 생성할 수 있지만, 손으로 그린 이미지와 R-18 태그 인식에는 여전히 약점이 있습니다. 다른 AI 드로잉 봇과 마찬가지로 Niji Journey는 일정 횟수 이후에는 유료 결제가 필요합니다.',
  'tokens': 0}}
```

### FastGPT API

```python
from PyKagi import FastGPT

API_KEY = "your api key"
FGPT = FastGPT(API_KEY)

query = "python 3.11"
result = FGPT.fastgpt(
    query = query,
)
result
```

```json
{'meta': {'id': '8ee670fe-0dd4-469b-a076-2a0b0d410e66',
  'node': 'asia-southeast1',
  'ms': 0,
  'api_balance': 13.058023},
 'data': {'output': 'According to the provided context:\n\nPython 3.11 is a newer major release of the Python programming language. It contains many new features and optimizations compared to previous versions. Sources state that Python 3.11 is between 10-60% faster than Python 3.10, with an average speedup of around 25% [1].',
  'tokens': 0,
  'references': [{'title': "What's New In Python 3.11 — Python 3.11.4 documentation",
    'snippet': 'Python 3.11 is between 10-60% faster than Python 3.10. On average, we measured a 1.25x speedup on the standard benchmark suite. See Faster CPython for...',
    'url': 'https://docs.python.org/3/whatsnew/3.11.html'}]}}
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