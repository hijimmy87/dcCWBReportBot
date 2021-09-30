from typing import List, Union
import requests as req
from base64 import b64decode
import time, datetime






# Username -> UUID
def getUUID(Username: str, timestamp: int = None) -> Union[str, None]:
    url = 'https://api.mojang.com/users/profiles/minecraft/{}'.format(Username)
    if timestamp:
        url = url + '?at={}'.format(timestamp)
    result = req.get(url)
    return result.json()['id'] if result.status_code == 200 else None



# UUID -> Name History
def getNameHistory(UUID) -> dict:
    url = 'https://api.mojang.com/user/profiles/{}/names'.format(UUID)
    result = req.get(url)
    return result.json()





# UUID -> Profile and Skin/Cape
def getProfile(UUID) -> Union[dict, None]:
    url = 'https://sessionserver.mojang.com/session/minecraft/profile/{}'.format(UUID)
    result = req.get(url)
    return result.json() if result.status_code == 200 else None

{
    'id': '2fae43920610415589d723095c8259d3',
    'name': 'Hi_Jimmy_87',
    'properties': [
        {
            'name': 'textures',
            'value': 'ewogICJ0aW1lc3RhbXAiIDogMTYyMjk5MzE0NzI3NCwKICAicHJvZmlsZUlkIiA6ICIyZmFlNDM5MjA2MTA0MTU1ODlkNzIzMDk1YzgyNTlkMyIsCiAgInByb2ZpbGVOYW1lIiA6ICJIaV9KaW1teV84NyIsCiAgInRleHR1cmVzIiA6IHsKICAgICJTS0lOIiA6IHsKICAgICAgInVybCIgOiAiaHR0cDovL3RleHR1cmVzLm1pbmVjcmFmdC5uZXQvdGV4dHVyZS8zM2ZjMThjNWZmMWM5NmZkYzkyMTFiYTQ1ZmVjZWQ4NGU0NmVjNjE0MTUzNTYwMDU5MmY3ZGQxYmM4YTQwYmJjIgogICAgfQogIH0KfQ==',
            '====>': {
                'timestamp': 1622993662204,
                'profileId': '2fae43920610415589d723095c8259d3',
                'profileName': 'Hi_Jimmy_87',
                'textures': {
                    'SKIN': {
                        'url': 'http://textures.minecraft.net/texture/33fc18c5ff1c96fdc9211ba45feced84e46ec6141535600592f7dd1bc8a40bbc'
                    }
                }
            }
        }
    ]
}

def getInfoo(Username) -> Union[dict, None]:
    result = getUUID(Username)
    if result == None:
        return None
    uuid = result['id']
    result['username_history'] = getNameHistory(uuid)
    rawTextures = getProfile(uuid)['properties']['value']
    # textures = 
    
    
    return result


# time -> timestamp
def toTimestamp(Time: str) -> int:
    time.strftime()


# timestamp -> time
def toTime(timestamp: int) -> str:
    Time = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S%z (%Z)', Time)

# request from https://github.com/Electroid/mojang-api
def getInfo(User) -> Union[dict, None]:
    url = 'https://api.ashcon.app/mojang/v2/user/{}'.format(User)
    result = req.get(url)
    return result.json()




# print(eval(base64.b64decode(value.encode('utf-8')).decode('utf-8')))

# print(getInfo('Hi_Chocolate'))

{
    'uuid': '4193aa50-f953-4da0-bebc-9f11b54501e5',
    'username': 'Hi_Chocolate',
    'username_history': [
        {
            'username': 'Hi_Chocolate'
        }
    ],
    'textures': {
        'custom': True,
        'slim': False,
        'skin': {
            'url': 'http://textures.minecraft.net/texture/97d44a9b23d01da9b3a2c674d7af7792c878f9f5ddf4447eafdfffa237a4efc5',
            'data': '...'
        },
        'raw': {
            'value': '...'
        }
    },
    'created_at': '2014-06-27',
    'requested_at': '2021-06-07'
}

def skin(User):
    info = getInfo(User)
    if 'textures' in info.keys():
        skinURL = info['textures']['skin']['url']
        # ctx.send(skinURL)
        print(skinURL)
    else:
        title = info['error']
        description = info['reason']
        print(title)
        print(description)

# skin('freeloder103')
# print(getInfo('freeloder103'))

# print(toTime(1622993662))
# import uuid
# while username := input('>>>'):
#     if id:= getUUID(username):
#         print(id)
#         id = '{}-{}-{}-{}-{}'.format(id[0:8], id[8:12], id[12:16], id[16:20], id[20:32])
#     print(id)
def getSkin(username):
    # uuid = getUUID(username)['id']
    # uuid = '{}-{}-{}-{}-{}'.format(uuid[0:8], uuid[8:12], uuid[12:16], uuid[16:20], uuid[20:32])
    # print(uuid)
    # url = 'https://namemc.com/profile/{}'.format(uuid)
    # url = 'https://render.namemc.com/skin/3d/body.png?skin=69290f16fe414000&width=400&height=800'
    # print(url)
    # print(req.get(url))
    result = req.get(url, headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'})
    print(result.status_code)
    print(result.text)

# getSkin('Eric101201')
# print(getProfile(getUUID('Eric101201')))

# import uuid

# uuid.


# print(11 ** 20 % 10)



datas=[3,5,2,1]
print("before:", "".split(datas))
n = len(datas)-1
for i in range(n):
    for j in range(n-i):
        print("i=%d j=%d" %(i,j))
        if(datas[j] > datas[j+1]):
            print("%d,%d after swiched:" %(datas[j], datas[j+1]))
            datas[j], datas[j+1] = datas[j+1], datas[j]
            print(datas)
print("after: ", "".split(datas))

import sys
print(sys.version)