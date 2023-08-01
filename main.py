#print("running")
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import pytz
import time
def log(string):
    with open("/root/franchecker/log.txt", 'a') as file:
        file.write(string + '\n')
    print(f'String saved .')



log("running")



while True:
    time.sleep(3600)
    tehran_timezone = pytz.timezone('Asia/Tehran')

    tehran_time = datetime.now(tehran_timezone)

    formatted_time = tehran_time.strftime('%Y-%m-%d %H:%M:%S')


    url = "https://my.frantech.ca/cart.php?gid=39"  
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    package_div = soup.find('div', {'class': 'package', 'id': 'product1'})
    qty_div = package_div.find('div', {'class': 'package-qty'})
    try:
        availability = qty_div.get_text(strip=True)
    except AttributeError:
        availability = "Unlimited"


    if availability == "0 Available":
        discordmsg = "Was not avalable"
        log(discordmsg)
    else:
        discordmsg = f" @here VPS was Available at {formatted_time} and {availability.replace('Available', '')} vps's were available"
        webhook_url = "https://discord.com/api/webhooks/1126068796038316053/SwjllZjWm839D395pXRsvYSFKtQGZwu1gbfRicnM-qFggY_JhaoBMo_8BnEUDmnOcb3D"  # Replace with your actual Discord webhook URL
        data = {"content": f"{discordmsg}"}
        headers = {"Content-Type": "application/json"}

        response = requests.post(webhook_url, data=json.dumps(data), headers=headers)

        if response.status_code == 204:
            log(discordmsg)
        else:
            log("Failed to send availability to Discord webhook.")

    log(availability)

