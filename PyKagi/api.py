import requests


class UniversalSummarizer:

    def __init__(self, api_token=None):
        self.api_token = api_token
        self.base_url = "https://kagi.com/api/v0/summarize"

    def summarize(self, url=None, text=None, engine="agnes", summary_type="summary", target_language=None, cache=True):
        if url is None and text is None:
            raise ValueError("Either 'url' or 'text' must be provided.")
        if url is not None and text is not None:
            raise ValueError(
                "'url' and 'text' are exclusive. Provide only one of them.")

        headers = {
            "Authorization": f"Bot {self.api_token}"
        }

        if text is None:
            headers["Content-Type"] = "application/json"
            params = {
                "url": url,
                "engine": engine,
                "summary_type": summary_type,
                "target_language": target_language,
                "cache": str(cache).lower()
            }
            response = requests.get(
                self.base_url, headers=headers, params=params)
        else:
            headers["Content-Type"] = "application/json"
            data = {
                "text": text,
                "engine": engine,
                "summary_type": summary_type,
                "target_language": target_language,
                "cache": str(cache).lower(),
            }
            response = requests.post(self.base_url, headers=headers, json=data)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(
                f"Request failed with status code {response.status_code}")


class Search:

    def __init__(self, api_token=None):
        self.api_token = api_token
        self.base_url = "https://kagi.com/api/v0/search"

    def search(self, query, limit=None):
        headers = {
            "Authorization": f"Bot {self.api_token}"
        }

        params = {
            "q": query,
            "limit": limit,
        }

        response = requests.get(self.base_url, headers=headers, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(
                f"Request failed with status code {response.status_code}")

class FastGPT:

    def __init__(self, api_token=None):
        self.api_token = api_token
        self.base_url = "https://kagi.com/api/v0/fastgpt"

    def fastgpt(self, query, **kwargs):
        headers = {
            "Authorization": f"Bot {self.api_token}"
        }
        data = {
            "query": query,
        }
        data.update(kwargs)

        response = requests.post(self.base_url, headers=headers, json=data)
    
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(
                f"Request failed with status code {response.status_code}")
