import requests
import string
import random
import time 

DISCORD_WEBHOOK_URL = ""
DISCORD_WEBHOOK_URL2 = ""

def send_to_discord(message):
    payload = {
        "content": message
    }
    response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
    if response.status_code != 200:
        print("Failed")
        
def send_to_discord_fail(message):
    payload = {
        "content": message
    }
    response = requests.post(DISCORD_WEBHOOK_URL2, json=payload)
    if response.status_code != 200:
        print("Failed")
        
        
def generate_random():
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(18))

def check_gift(code):
    
    url =  f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application"
    response = requests.get(url)
    if response.status_code == 200:
        send_to_discord(f"CARALHOOO ACHOU CODIGO VALIDO: discord.gift/{code} @everyone")
        
    else:
        send_to_discord_fail(f"Invalido: discord.gift/{code}")
        print(f"invalido: {code}")
        
def main():
    while True:
        code = generate_random()
        check_gift(code)
        
if __name__ == "__main__":
    main()   
