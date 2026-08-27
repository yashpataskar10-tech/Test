from tavily import TavilyClient

from config import TAVILY_API_KEY


class SearchTool:

    def __init__(self):

        self.client = TavilyClient(
            api_key=TAVILY_API_KEY
        )

    def search(
        self,
        query,
        max_results=5
    ):

        response = self.client.search(
            query=query,
            search_depth="advanced",
            max_results=max_results
        )

        results = []

        for item in response.get("results", []):

            results.append({

                "title": item.get("title", ""),

                "url": item.get("url", ""),

                "content": item.get("content", "")

            })

        return results