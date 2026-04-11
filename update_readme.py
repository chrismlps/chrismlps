import requests
import re

def update_readme():
    try:
        # Pega uma frase nova
        resp = requests.get("https://zenquotes.io/api/random")
        quote = f"> \"{resp.json()[0]['q']}\" — *{resp.json()[0]['a']}*"

        with open("README.md", "r", encoding="utf-8") as f:
            content = f.read()

        # Regex poderosa: ela encontra tudo entre as tags, incluindo as tags
        # e substitui pelo novo bloco limpo.
        pattern = r".*?"
        replacement = f"\n{quote}\n"
        
        # O re.DOTALL garante que o '.' pegue quebras de linha
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_content)
            
    except Exception as e:
        print(f"Erro ao atualizar: {e}")

if __name__ == "__main__":
    update_readme()
