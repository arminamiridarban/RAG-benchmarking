from duckduckgo_search import DDGS

def retrieve_snippets(query: str, max_results: int = 3) -> list[str]:
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=max_results)
        return [r["body"] for r in results if "body" in r]