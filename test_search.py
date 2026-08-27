from tools.search_tool import SearchTool


tool = SearchTool()

results = tool.search(

    "TCS AI Strategy",

    max_results=5

)

print()

print(f"Found {len(results)} results\n")

for i, result in enumerate(results, start=1):

    print("=" * 80)

    print(f"Result {i}")

    print("Title:", result["title"])

    print("URL:", result["url"])

    print("Content:", result["content"][:300])

    print()