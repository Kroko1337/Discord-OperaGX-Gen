import requests
import datetime
import time


def generate_nitro_gift():
    url = 'https://api.discord.gx.games/v1/direct-fulfillment'
    headers = {
        'authority': 'api.discord.gx.games',
        'accept': '*/*',
        'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://www.opera.com',
        'referer': 'https://www.opera.com/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Opera GX";v="106"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0'
    }

    data = {
        'partnerUserId': 'a455f99e6168ea3f84dbcb0b9ed8aad1ce1423133d5c80af27dac748a7b42778'
    }

    response = requests.post(url, headers=headers, json=data)

    json_data = response.json()

    token = json_data["token"]

    gift = f"https://discord.com/billing/partner-promotions/1180231712274387115/{token}"

    with open(f"{datetime.datetime.now():%Y-%m-%d}.txt", "a") as file:
        file.write(f"{gift}\n")

    print(gift)


if __name__ == "__main__":
    try:
        while True:
            generate_nitro_gift()
            time.sleep(1)
    except KeyboardInterrupt:
        pass
