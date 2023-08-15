import re 
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, ChannelParticipantsSearch
from telethon.tl.functions.channels import GetParticipantsRequest
import csv
print ('''




            \nThis script product by reza mazarloo
            github.com/rezamazarloo
            t.me/Py_devops\n''')
# please disable the two verification code if this enable in your telegram account before using this software

api_id = input("Enter the API ID: ") # go to the my.telegram.org and API DEVEPLOMENT then copy the apt id and paste here
api_hash = str(input("Enter the API HASH: ")) # go to the my.telegram.org and API DEVEPLOMENT then copy the apt hash and paste here
phone = str(input("Enter the Phone: ")) # enter the your account phone number + Countery code example:+449124444444
client = TelegramClient(phone, api_id, api_hash)
 
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))
 
 
chats = []
last_date = None
chunk_size = 200
groups=[]
 
result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0
         ))
chats.extend(result.chats)
 
for chat in chats:
    try:
        if chat.megagroup== True:
            groups.append(chat)
    except:
        continue
 
print('Choose a group to scrape members from:')
i=0
for g in groups:
    print(str(i) + '- ' + g.title)
    i+=1
 
g_index = input("Enter a Number: ")
target_group=groups[int(g_index)]
 
print('Fetching Members...')
all_participants = []
queryKey = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'ا', 'آ', 'ب', 'پ',
            'ت', 'ث', 'ج', 'چ', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'ژ', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف',
            'ق', 'ک', 'گ', 'ل', 'م', 'ن', 'و', 'ه', 'ی']

for key in queryKey:
    print("key", key)
    offset = 0
    # limit = 1000
    limit = 100
    while True:
        participants = client(GetParticipantsRequest(
            target_group, ChannelParticipantsSearch(key), offset, limit,
            hash=0
        ))
        if not participants.users:
            break
        for user in participants.users:
            try:
                if re.match(rf"\b{key}", user.first_name, re.I) or re.match(rf"\b{key}", user.last_name, re.I) or user.username[0].lower() == key:
                    all_participants.append(user)
    
            except:
                pass

        offset += len(participants.users)
        print(offset)

print('Saving In file...')
with open("extract_data/final.csv","w",encoding='UTF-8') as f:
    writer = csv.writer(f,delimiter=",",lineterminator="\n")
    writer.writerow(['username','user id', 'access hash','name','group', 'group id'])
    for user in all_participants:
        if user.username:
            username= user.username
        else:
            username= ""
        if user.first_name:
            first_name= user.first_name
        else:
            first_name= ""
        if user.last_name:
            last_name= user.last_name
        else:
            last_name= ""
        name= (first_name + ' ' + last_name).strip()
        writer.writerow([username,user.id,user.access_hash,name,target_group.title, target_group.id])      
print('Members scraped successfully.')
print ('''




            \nThis script product by reza mazarloo
            github.com/rezamazarloo
            t.me/Py_devops\n''')