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
        'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI3NjhlOTcxZi0zNzcyLTRmYjMtOTlhNC04OGQ5MDMzYjBkNzEiLCJleHAiOjE3MDkzMjI4NDh9.lw0ASVR4slqyLzlnDArRJ3u943fj5Lwlc8X9DUzyqyrcpzmvsIdrCpRAYEmbUH6AOQWZgiY3b4mcJuyT955Syqxkk_G0G_Jx5iPia5QJjOdzy1VafRQPVIxt4vHlu36LiKY6qOUotfH_HPWKssbkGqHl3Sqc2ojpS_uqx0-j41rVS2rqFYWVnE7DfZGd3kE7YRsWbIGO1T4OO4Gh4P_9TbWdYBs8ykFiK391yqdQUEszIhxha2UBps07jSVEZ8gmeceP5JtCiplrdpdM_RgY3canF0rpU7IFJTK2NEgH_kj1rXCfttoO3_sgZrx_I-A8Ao3mbDQHzJhDjpgnrYMVaMpb8-oHBNNmyIhtZsPkKotcLVXJrMDXYiIisZ__HtlHrSrLOsT7oB5HG_5hVCdsKNNFpp5SffpH1mlwE-_R_zkNf8_ZHsVeqJ2CnyiI20gBcB141Tk1qShuDTCw-V0ITzBChpeeygWtGipdJIomhgCeV1hiGylsXHJd5vGj7MLniBhqWaHxduNjM9R5JLF5KplupvTLd6hV-PDx8c2tYkB96KC7-a03-nVST9AE6oeAZEpSQJdpTovNwXzqT3QuDr4IVtujmk_kX3mhpYFAtSeseT-olW-MAY0FyYB89HW8wo0ykahfGIlKEKMtLuPC5zaXm07jAGosExuIA8wb1V8',
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
