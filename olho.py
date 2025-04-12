import os
import subprocess

AZUL = "\033[94m"
CIANO = "\033[96m"
VERMELHO = "\033[91m"
RESET = "\033[0m"

PASTA_DATABASE = "database"

# ASCII Art
ascii_art = f"""{AZUL}
▒█████      ▒█████   ██▓     ██░ ██  ▒█████       █████   █    ██ ▓█████    ▄▄▄█████▓ █    ██ ▓█████▄  ▒█████      ██▒   █▓▓█████ 
▒██▒  ██▒   ▒██▒  ██▒▓██▒    ▓██░ ██▒▒██▒  ██▒   ▒██▓  ██▒ ██  ▓██▒▓█   ▀    ▓  ██▒ ▓▒ ██  ▓██▒▒██▀ ██▌▒██▒  ██▒   ▓██░   █▒▓█   ▀ 
▒██░  ██▒   ▒██░  ██▒▒██░    ▒██▀▀██░▒██░  ██▒   ▒██▒  ██░▓██  ▒██░▒███      ▒ ▓██░ ▒░▓██  ▒██░░██   █▌▒██░  ██▒    ▓██  █▒░▒███   
▒██   ██░   ▒██   ██░▒██░    ░▓█ ░██ ▒██   ██░   ░██  █▀ ░▓▓█  ░██░▒▓█  ▄    ░ ▓██▓ ░ ▓▓█  ░██░░▓█▄   ▌▒██   ██░     ▒██ █░░▒▓█  ▄ 
░ ████▓▒░   ░ ████▓▒░░██████▒░▓█▒░██▓░ ████▓▒░   ░▒███▒█▄ ▒▒█████▓ ░▒████▒     ▒██▒ ░ ▒▒█████▓ ░▒████▓ ░ ████▓▒░      ▒▀█░  ░▒████▒
░ ▒░▒░▒░    ░ ▒░▒░▒░ ░ ▒░▓  ░ ▒ ░░▒░▒░ ▒░▒░▒░    ░░ ▒▒░ ▒ ░▒▓▒ ▒ ▒ ░░ ▒░ ░     ▒ ░░   ░▒▓▒ ▒ ▒  ▒▒▓  ▒ ░ ▒░▒░▒░       ░ ▐░  ░░ ▒░ ░
  ░ ▒ ▒░      ░ ▒ ▒░ ░ ░ ▒  ░ ▒ ░▒░ ░  ░ ▒ ▒░     ░ ▒░  ░ ░░▒░ ░ ░  ░ ░  ░       ░    ░░▒░ ░ ░  ░ ▒  ▒   ░ ▒ ▒░       ░ ░░   ░ ░  ░
░ ░ ░ ▒     ░ ░ ░ ▒    ░ ░    ░  ░░ ░░ ░ ░ ▒        ░   ░  ░░░ ░ ░    ░        ░       ░░░ ░ ░  ░ ░  ░ ░ ░ ░ ▒          ░░     ░   
    ░ ░         ░ ░      ░  ░ ░  ░  ░    ░ ░         ░       ░        ░  ░               ░        ░        ░ ░           ░     ░  ░
                                   discord: https://discord.gg/JUQNubxt9m @lobstersec                                                    ░                       ░          
{RESET}"""

def abrir_ou_executar_arquivo(nome_arquivo):
    caminho = os.path.join(PASTA_DATABASE, nome_arquivo)

    if not os.path.isfile(caminho):
        print(f"{VERMELHO}\nArquivo '{nome_arquivo}' não encontrado em '{PASTA_DATABASE}/'{RESET}")
        return

    if nome_arquivo.endswith(".py"):
        print(f"{AZUL}\nExecutando o arquivo...: {nome_arquivo}{RESET}\n")
        try:
            subprocess.run(["python3", caminho], check=True)
        except subprocess.CalledProcessError as e:
            print(f"{VERMELHO}Erro ao executar o script: {e}{RESET}")
    else:
        print(f"{AZUL}\nAbrindo o arquivo: {nome_arquivo}{RESET}\n")
        with open(caminho, 'r', encoding='utf-8') as f:
            print(f"{AZUL}{f.read()}{RESET}")

def main():
    print(ascii_art)
    escolha = input(f"{CIANO}\nOlá, o que você quer ver hoje na database?: {RESET}")
    abrir_ou_executar_arquivo(escolha.strip())

if __name__ == "__main__":
    main()
