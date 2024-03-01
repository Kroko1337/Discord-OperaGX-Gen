import requests
import datetime
import time


def generate_nitro_gift():
    url = 'https://discord.opr.gg/v2/direct-fulfillment'
    headers = {
        'authority': 'discord.opr.gg',
        'accept': '*/*',
        'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
        'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI3NjhlOTcxZi0zNzcyLTRmYjMtOTlhNC04OGQ5MDMzYjBkNzEiLCJleHAiOjE3MDkzMDE3NDJ9.tfimKKamOYLzPxevebOtxJn3kZu-FlYK2_jS8dUOQozDf326QIHDN8DVq0qejrfYHdgQZkLHbrSeCdDV31OZgquR03cM0Fp93lBPoJEfdFnbh4BkCCLuHUyddf0EoCLy5uM1HpufIdNWS9IjDseuOl85OMWRocvZXIzMGUukNgwF6d1MZsE-8NThkd8uK5wt0SJdganvVDToPNaMK277hlaZkeFwtrJuKmvrp6M48ECLo-GaT9D9fwLg2N2pf7MZSYwMwKQj1pt4UuTZ1xrm8olIBS-ZhnfsAU7cH0F1ZrxrEnCk8UC0YfZXx96bR0Dlt5rubxFGf5DjXKx2AvlloyoAFKRsxXH71jvmvF9EjlsRj3A12H4x7UMKm42O9JiyI2nhc87jiUXYz6OqUknDwW8czCl5Jdd8nyGA34mtTDGluUhKM14Pcp4whuZ9a-zMiqpM1236_fpN1sG7fzlIT9zxACRkTfVShgf2u0m6IArFa8h1nJ5xG0pUF3-IbuCwUuVSFawCpsizcAU2XuaofMGfKWh2AjZJ1oM5shnz9ftZd5ulHl5XlcdJcOjRACsJCfDM3BRxdk3SJ16sgQtEdqBFA-vKhx6jZRl20RZRiocJd_1pYNHVQtj5zEQojVXxzRMrvRJkaGHBbITpR7GivDL4VPT5wP_YwT0LdGEw3ck',
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
