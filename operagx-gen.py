import requests
import datetime
import time


def send_options():
    url = 'https://discord.opr.gg/v2/direct-fulfillment'
    headers = {
        'authority': 'discord.opr.gg',
        'method': 'OPTIONS',
        'scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'de-De;q=0.9,en-US;q=0.8;q=0.7',
        'Access-Control-Request-Headers': 'authorization',
        'Access-Control-Request-Method': 'POST',
        'origin': 'https://www.opera.com',
        'referer': 'https://www.opera.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0'
    }


def generate_nitro_gift():
    url = 'https://discord.opr.gg/v2/direct-fulfillment'
    headers = {
        'authority': 'discord.opr.gg',
        'accept': '*/*',
        'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
        'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI3NjhlOTcxZi0zNzcyLTRmYjMtOTlhNC04OGQ5MDMzYjBkNzEiLCJleHAiOjE3MDkzMjc4NTR9.EarFQ8gZSGBaKc1c9QTChHIYJEndL00xwdA0brdsGu3J2wmqUeeFHdkhtEMzlpo7NFDT_hQBLM3h_bZKNS-WmeADNnZFRM2HHTsBs1CsuEMi4KXNL5tsRykmm0G02rphODbKVMxAKj_i8cdeuYPy3ftwpcLW7NxwK_duosea3UIHhxsGjc1gydru7KvlHaqZAQDGD1Yejp_0Oh_rTkwCx_XL4eY38VZoyhOj3FmhmO6ZcPhM4FLNhFhp0G-_BgjlhtTDYdLTioiN5BEIX6hHB5GgfHKCYlNAiXl2cGFJ2hhh0OOaM_qU43Ed8V37f1fP0JEwYLDXT4mYCcJaNWjtMPNPc9H2_DhTp9xK_H7bS4y-zE1BNKJ-hrHWr9oL8Ev4sDGri5hU0Wmb9q8HmdOilzQXx3TgoWJs38IFRHOGiyY8jjANusfq5EEIMQo9LaH3SKdc3VUKjdS0D8EhuEFyvoCq36Y7Tre6CCdfHk77MvdhpVD6XuXYm4TiYbyktOcr0qSnx7weIIMq8_lX0Z7HPTEKEaEkjEGzBMXWzSRMGgELwIJB2oDQb9rLJt4QQbFTPHeaAckxGQ7yNcv7bjaDheavwQhn8zEv5VhcKjre5EM0MWbh9b2uWTb6J4zU4mx4P--RkmSDumP2czvCpJwwHtXmbMAdlxTwsVy3Et9Cf9A',
        'content-type': 'application/json',
        'origin': 'https://www.opera.com',
        'referer': 'https://www.opera.com/',
        'sec-ch-ua': '"Not A(Brand";v="99", "Opera GX";v="107", "Chromium";v="121"',
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

    if 'token' in json_data:
        token = json_data["token"]

        gift = f"https://discord.com/billing/partner-promotions/1180231712274387115/{token}"

        with open(f"{datetime.datetime.now():%Y-%m-%d}.txt", "a") as file:
            file.write(f"{gift}\n")

        print(gift)
        send_options()
    if 'token' not in json_data:
        if 'message' in json_data:
            print(json_data['message'])


if __name__ == "__main__":
    try:
        while True:
            generate_nitro_gift()
            time.sleep(1)
    except KeyboardInterrupt:
        pass
