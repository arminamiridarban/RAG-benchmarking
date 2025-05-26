import subprocess

def run_mistral(prompt: str) -> str:
    cmd = ["ollama", "run", "mistral", prompt]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)
    return result.stdout