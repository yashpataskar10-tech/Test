import requests
from bs4 import BeautifulSoup


class CompanyTool:

    def scrape(self, url):

        html = requests.get(
            url,
            timeout=20
        ).text

        soup = BeautifulSoup(
            html,
            "html.parser"
        )

        paragraphs = soup.find_all("p")

        text = "\n".join(
            p.get_text()
            for p in paragraphs
        )

        return text[:8000]