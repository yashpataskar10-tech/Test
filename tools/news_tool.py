from tools.search_tool import SearchTool


class NewsTool:

    def __init__(self):

        self.search = SearchTool()

    def latest(self, company):

        return self.search.search(
            f"{company} latest news",
            max_results=5
        )