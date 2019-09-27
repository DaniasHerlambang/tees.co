# importing the requests library
import requests
import base64
import json
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "task.settings")
django.setup()
from profil.models import *
from customer.models import *

import requests

TOKEN = []
PROFIL_PUBLIK_ID = []

#-------------------------------------------------------------------------------------add token
def add_token():
    # username = input("username> ")
    # password = input("password> ")
    API_ENDPOINT = "http://127.0.0.1:8000/api/token/"
    data = {
                "username": 'dns' ,
                "password": 'herlambang',
            }
    requests.post(url = API_ENDPOINT, json = data)

    # sending post request and saving response as response object
    send = requests.post(url = API_ENDPOINT, json = data)
    # print(send.text)
    parsed = json.loads(send.text)
    print (json.dumps(parsed, indent=2, sort_keys=True))

    for key, value in parsed.items():
        if key == 'access':
            print (value)
            TOKEN.append(value)

#-------------------------------------------------------------------------------------list profil
def get_profil():
    # token = input("token> ")
    API_ENDPOINT = "http://127.0.0.1:8000/profil/api/"
    headers={"Content-Type":"application/x-www-form-urlencoded",
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + TOKEN[0],
            }

    # sending post request and saving response as response object
    send = requests.get(url = API_ENDPOINT,  headers=headers)
    parsed = json.loads(send.text)
    print (json.dumps(parsed, indent=2, sort_keys=True))

#-------------------------------------------------------------------------------------add profil
def add_profil():
    API_ENDPOINT = "http://127.0.0.1:8000/profil/api/"
    headers={"Content-Type":"application/x-www-form-urlencoded",
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + TOKEN[0],
            'x-access-token': TOKEN[0],

            }
    PARAMS = {'nama_lengkap':'gusti',
            'telp': '0858909378',
            'email': "hehe@gmail.com",
            'alamat':'samarinda',
            'foto':''}
    # sending post request and saving response as response object
    send = requests.post(url = API_ENDPOINT, data = PARAMS ,  headers=headers)
    parsed = json.loads(send.text)
    print (json.dumps(parsed, indent=2, sort_keys=True))

#-------------------------------------------------------------------------------------update profil
def update_profil():
    data_updates = Profil.objects.get(email='hehe@gmail.com')
    API_ENDPOINT = "http://127.0.0.1:8000/profil/api/%s" % data_updates.id_publik
    headers={"Content-Type":"application/x-www-form-urlencoded",
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + TOKEN[0],
            'x-access-token': TOKEN[0],

            }
    PARAMS = {'nama_lengkap':'gustafo',}
    # sending post request and saving response as response object
    send = requests.put(url = API_ENDPOINT, data = PARAMS ,  headers=headers)
    parsed = json.loads(send.text)
    print (json.dumps(parsed, indent=2, sort_keys=True))

#-------------------------------------------------------------------------------------delete profil
def delete_profil():
    data_delete = Profil.objects.get(email='hehe@gmail.com')
    API_ENDPOINT = "http://127.0.0.1:8000/profil/api/%s" % data_delete.id_publik
    headers={"Content-Type":"application/x-www-form-urlencoded",
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + TOKEN[0],
            'x-access-token': TOKEN[0],

            }
    # sending post request and saving response as response object
    send = requests.delete(url = API_ENDPOINT,  headers=headers)
    parsed = json.loads(send.text)
    print (json.dumps(parsed, indent=2, sort_keys=True))

#-------------------------------------------------------------------------------------list customer
def get_customer():
    # token = input("token> ")
    API_ENDPOINT = "http://127.0.0.1:8000/customer/api/"
    headers={"Content-Type":"application/x-www-form-urlencoded",
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + TOKEN[0],
            }

    # sending post request and saving response as response object
    send = requests.get(url = API_ENDPOINT,  headers=headers)
    parsed = json.loads(send.text)
    print (json.dumps(parsed, indent=2, sort_keys=True))

#-------------------------------------------------------------------------------------add customer
def add_customer():
    API_ENDPOINT = "http://127.0.0.1:8000/customer/api/"
    headers={"Content-Type":"application/x-www-form-urlencoded",
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + TOKEN[0],
            'x-access-token': TOKEN[0],

            }
    PARAMS = {'nama':'hoho',
            'email': "boboho@gmail.com",
            'ukuran_baju':30}
    # sending post request and saving response as response object
    send = requests.post(url = API_ENDPOINT, data = PARAMS ,  headers=headers)
    parsed = json.loads(send.text)
    print (json.dumps(parsed, indent=2, sort_keys=True))

#-------------------------------------------------------------------------------------update customer
def update_customer():
    data_updates = Customer.objects.get(email='boboho@gmail.com')
    API_ENDPOINT = "http://127.0.0.1:8000/customer/api/%s" % data_updates.id_publik
    headers={"Content-Type":"application/x-www-form-urlencoded",
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + TOKEN[0],
            'x-access-token': TOKEN[0],

            }
    PARAMS = {'nama':'boboho',}
    # sending post request and saving response as response object
    send = requests.put(url = API_ENDPOINT, data = PARAMS ,  headers=headers)
    parsed = json.loads(send.text)
    print (json.dumps(parsed, indent=2, sort_keys=True))

#-------------------------------------------------------------------------------------delete customer
def delete_customer():
    data_delete = Customer.objects.get(email='boboho@gmail.com')
    API_ENDPOINT = "http://127.0.0.1:8000/customer/api/%s" % data_delete.id_publik
    headers={"Content-Type":"application/x-www-form-urlencoded",
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + TOKEN[0],
            'x-access-token': TOKEN[0],

            }
    # sending post request and saving response as response object
    send = requests.delete(url = API_ENDPOINT,  headers=headers)
    parsed = json.loads(send.text)
    print (json.dumps(parsed, indent=2, sort_keys=True))

# fungsi untuk menampilkan menu
def show_menu(infunc=input):
    print ("\n")
    print ("[add_token]                       menampilkan token")
    print ("[get_profil]                       menampilkan profil")
    print ("[add_profil]                       tambah profil")
    print ("[update_profil]                       update profil")
    print ("[delete_profil]                       delete profil")

    print ("[get_customer]                       menampilkan customer")
    print ("[add_customer]                       tambah customer")
    print ("[update_customer]                       update customer")
    print ("[delete_customer]                       delete customer")
    menu = infunc("PILIH MENU> ")
    # print ("\n")

    if menu == "add_token":
        add_token()
    elif menu == "get_profil":
        get_profil()
    elif menu == "add_profil":
        add_profil()
    elif menu == "update_profil":
        update_profil()
    elif menu == "delete_profil":
        delete_profil()
    elif menu == "get_customer":
        get_customer()
    elif menu == "add_customer":
        add_customer()
    elif menu == "update_customer":
        update_customer()
    elif menu == "delete_customer":
        delete_customer()
    elif menu == "x":
        exit()
    else:
        print ("Salah pilih!")

# if __name__ == "__main__":
#     while(True):
#         show_menu()

show_menu(lambda prompt: "add_token")
show_menu(lambda prompt: "get_profil")
show_menu(lambda prompt: "add_profil")
show_menu(lambda prompt: "update_profil")
show_menu(lambda prompt: "delete_profil")
show_menu(lambda prompt: "get_customer")
show_menu(lambda prompt: "add_customer")
show_menu(lambda prompt: "update_customer")
show_menu(lambda prompt: "delete_customer")
