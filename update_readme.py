import requests

def update_readme():
    try:
        # 1. Pega a frase nova
        resp = requests.get("https://zenquotes.io/api/random")
        quote = f"> \"{resp.json()[0]['q']}\" — *{resp.json()[0]['a']}*"

        # 2. Lê o arquivo atual
        with open("README.md", "r", encoding="utf-8") as f:
            lines = f.readlines()

        # 3. Reconstrói o arquivo mantendo apenas o que está fora das tags
        new_lines = []
        skip = False
        
        for line in lines:
            if "" in line:
                new_lines.append(line)
                new_lines.append(quote + "\n")
                skip = True # Começa a pular o que já existia lá dentro
            elif "" in line:
                new_lines.append(line)
                skip = False # Para de pular
            elif not skip:
                new_lines.append(line)

        # 4. Salva o arquivo limpo
        with open("README.md", "w", encoding="utf-8") as f:
            f.writelines(new_lines)
            
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    update_readme()
    
