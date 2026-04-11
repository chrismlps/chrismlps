import requests
import re

def update_readme():
    # Pega uma frase de programação
    resp = requests.get("https://zenquotes.io/api/random")
    quote = f"> \"{resp.json()[0]['q']}\" — *{resp.json()[0]['a']}*"

    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    # Substitui o texto entre as tags
    pattern = r".*?"
    replacement = f"\n{quote}\n"
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    update_readme()
