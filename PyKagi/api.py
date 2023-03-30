import requests


class UniversalSummarizer:

    def __init__(self, api_token=None):
        self.api_token = api_token
        self.base_url = "https://kagi.com/api/v0/summarize"

    def summarize(self, method="GET", url=None, text=None, engine="agnes", summary_type="summary", target_language=None, cache=True):
        if url is None and text is None:
            raise ValueError("Either 'url' or 'text' must be provided.")
        if url is not None and text is not None:
            raise ValueError(
                "'url' and 'text' are exclusive. Provide only one of them.")
        if method not in ["GET", "POST"]:
            raise ValueError("Invalid method. Choose either 'GET' or 'POST'.")

        headers = {
            "Authorization": f"Bot {self.api_token}"
        }

        if method == "GET":
            headers["Content-Type"] = "application/json"
            params = {
                "url": url,
                "text": text,
                "engine": engine,
                "summary_type": summary_type,
                "target_language": target_language,
                "cache": cache
            }
            response = requests.get(
                self.base_url, headers=headers, params=params)
        elif method == "POST":
            headers["Content-Type"] = "application/json"
            data = {
                "url": url,
                "text": text,
                "engine": engine,
                "summary_type": summary_type,
                "target_language": target_language,
                "cache": cache
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
            "limit": limit
        }

        response = requests.get(self.base_url, headers=headers, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(
                f"Request failed with status code {response.status_code}")
