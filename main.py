import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import pytz
import time
url = "https://my.frantech.ca/cart.php?gid=39"  
webhook_url = ""  # Replace with your actual Discord webhook URL
#example https://discord.com/api/webhooks/420698542069/Swjl456jWm839D395pXRsvYSFKtGayPornFurryAssNiggassnM-qFggY_JhaoBMo_8BnEUDmns3D
CHECK_INTERVAL_SECONDS = 3600 #it's in secconds not ms so try this to not below 5 mins or frantech's antiflood will block you

def log(string):
    with open("~/log.txt", 'a') as file:
        file.write(string + '\n')
    print(f'String saved .')
#if you wanted to run this on systemmd on your server this will save results for you in your root path


log("running")



while True:
    time.sleep(CHECK_INTERVAL_SECONDS)
    tehran_timezone = pytz.timezone('Asia/Tehran')

    tehran_time = datetime.now(tehran_timezone)

    formatted_time = tehran_time.strftime('%Y-%m-%d %H:%M:%S')
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
        data = {"content": f"{discordmsg}"}
        headers = {"Content-Type": "application/json"}

        response = requests.post(webhook_url, data=json.dumps(data), headers=headers)

        if response.status_code == 204:
            log(discordmsg)
        else:
            log("Failed to send availability to Discord webhook.")

    log(availability)

