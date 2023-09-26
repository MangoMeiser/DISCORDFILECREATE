import requests
import json
from textblob import TextBlob
import sys
import os
authtoken = 'INSERT AUTH TOKEN HERE'
sys.stdout.reconfigure(encoding="utf-8")
def discfilecreate(channelid1, NAME):
    listnames = []
    LISTS = []
    channelinfo = open('dataset\channelids.txt', 'a', encoding = 'utf8')
    channelinfo.write(f'{NAME} {channelid1}\n')
    def retrieve_message(channelid, LISTNAME):
        listnames.append(f'{LISTNAME}')
        headers = {
            'authorization': authtoken
        }
        r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages', headers = headers)
        jsonn = json.loads(r.text)
        i = 0
        LISTNAME = [*range(0, 50, 1)]
        for value in reversed(jsonn):
            LISTNAME[i] = (f"{value['author']['username']}/{value['author']['global_name']}: {value['content']}")
            i = i + 1
        
        return LISTNAME
    LISTS.append(retrieve_message(channelid1, NAME))
    #POMPOMGENERAL
    MAKEFILE(LISTS,listnames)
def discfileupdate(channelid1, NAME):
    with open(f'dataset\{NAME}.txt', 'r', encoding="utf8") as f:
        original = []
        for line in f:
            original.append(line)
    headers = {
    'authorization': authtoken
    }
    r = requests.get(f'https://discord.com/api/v9/channels/{channelid1}/messages', headers = headers)
    jsonn = json.loads(r.text)
    LISTNAME = [*range(0, 50, 1)]
    i = 0
    for value in reversed(jsonn):
        value['content'] = value['content'].replace('\n', ' ')
        LISTNAME[i] = f"{value['author']['username']}/{value['author']['global_name']}: {value['content']}\n"
        i = i + 1
    if LISTNAME[-1] == original[-1]:
        return print(f'{NAME} update redundant')
    LISTNAME = [x for x in LISTNAME if x not in original]
    file1 = open(f'dataset\{NAME}.txt', 'a', encoding="utf8")
    b=0
    for e in LISTNAME:
        file1.write(f'{LISTNAME[b]}')
        b+=1
    return print(f'UPDATE SUCCESSFUL FOR {NAME}')
def MAKEFILE(listimp,listnames):
    woop = len(listimp)
    for intz in range(0,woop):
        leest = open(f'dataset\{listnames[intz]}.txt', 'x', encoding='utf-8')
        numeme = 0
        for nume in listimp[intz]:
            listimp[intz][numeme] = listimp[intz][numeme].replace('\n', ' ')
            leest.write(f'{listimp[intz][numeme]}\n')
            numeme +=1
def updateall():
    with open(f'dataset\channelids.txt', 'r', encoding="utf8") as f:
        channelidtemp = []
        for line in f:
            channelidtemp.append(line)
    b=0
    channelids = []
    for channelid in channelidtemp:
        channelids.append(channelidtemp[b].split())
        b+=1
    i=0
    for file in range(0,len(channelids)):
        discfileupdate(channelids[i][1],channelids[i][0])
        i+=1