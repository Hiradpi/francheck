import requests
import argparse
import time



parser = argparse.ArgumentParser(description='Francheck a tool for checking frantech (Buyvm) products')

parser.add_argument('--code', help='the code on the buy link at the pid value get request https://my.frantech.ca/cart.php?a=add&pid=1411 here is 1411')
parser.add_argument('--delay', help='How much delay you want to check for avalability in secconds (recomended Is 300)')

args = parser.parse_args()




def checkav(code , delay):
    if delay == None or delay == "":
        delay = 3
    else:
        delay = int(delay)

    while True:
        Request = requests.get(f"https://buyvm.hasstock.net/api/package/{code}.json")
        data = Request.json()
        print(data)
        webhook_url = 'https://discord.com/api/webhooks/1126068796038316053/SwjllZjWm839D395pXRsvYSFKtQGZwu1gbfRicnM-qFggY_JhaoBMo_8BnEUDmnOcb3D'

        message = f"Data: {data['name']} (ID: {data['id']})\nQuantity: {data['quantity']}\nAvailable: {data['hasStock']}\nLink: {data['link']}"

        payload = {
            'content': message
        }

        response = requests.post(webhook_url, json=payload)

        if response.status_code == 204:
            print('Data sent to Discord successfully.')
        else:
            print(f'Failed to send data to Discord. Status code: {response.status_code}')
        time.sleep(delay)


def noarg():
    Request = requests.get("https://buyvm.hasstock.net/api/stock.json")
    JsonData = Request.json()
    print(Request.status_code)
    names = []
    LV = []
    NY = []
    LU = []
    MIA = []

    for key, value in JsonData.items():
        value = [value["name"] , value["id"]]
        names.append(value)

    location = input("Please select your disiered server location \n1: Las Vegas\n2: New York\n3: Luxembourg\n4: Miami\n> ")

    for i, name in enumerate(names, 1):
        if name[0].startswith("LV") and location == "1":
            LV.append((i, name))
        elif name[0].startswith("NY") and location == "2" :
            NY.append((i, name))
        elif name[0].startswith("LU") and location == "3" :
            LU.append((i, name))
        elif name[0].startswith("MIA") and location == "4" :
            MIA.append((i, name))
    if LV:
        print("\nLV Items:")
        select_and_print(LV, "LV")

    if NY:
        print("\nNY Items:")
        select_and_print(NY, "NY")

    if LU:
        print("\nLU Items:")
        select_and_print(LU, "LU")
    if MIA:
        print("\nLU Items:")
        select_and_print(MIA, "MIA")

def select_and_print(category_list, category_name):
    for i, (number, item) in enumerate(category_list, 1):
        print(f"{i}: {item[0]}")

    try:
        selected_number = int(input(f"Enter the number of the {category_name} item you want to select: "))
        if 1 <= selected_number <= len(category_list):
            selected_item = category_list[selected_number - 1][1]
            print("\nChecking avalability of",selected_item[0],"every 10 secconds")
            checkav(selected_item[1],args.delay)
        else:
            print("Invalid number. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")





if args.code == None:
    noarg()
else:
    checkav(args.code , args.delay)


