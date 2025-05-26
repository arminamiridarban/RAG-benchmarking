import time
from retrieval.duckduckgo import retrieve_snippets
from synthesis.mistral_runner import run_mistral

query = input("Query: ")
start = time.time()

snippets = retrieve_snippets(query)
context = "\n".join(snippets)
prompt = f"Answer this question using the context below:\n\n{context}\n\nQuestion: {query}"

answer = run_mistral(prompt)
end = time.time()

print("\nAnswer:\n", answer)
print(f"\nLatency: {end - start:.2f} sec")