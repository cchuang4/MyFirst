import  csv
import json
import pandas as pd
import os

#df = pd.read_json(os.getcwd() +  '/kkbox_2019h2_hot50k.json', lines=True)
path = os.getcwd() +  '/kkbox_2019h2_hot50k.json'
with open(path, 'r') as kkbox:
    data = {}
    track_name = set()
    album_name = set()
    with open(os.getcwd() + "/track_id_conflict.txt", "w") as conflict:
        tmp = ''
        for line in kkbox:
            if  '{' in line:
                tmp = '{'
                continue
            tmp += line.strip()
            if '}' in line :
    #            track = dict(item.split(':') for item in tmp.split(','))
                track = json.loads(tmp)
                track_name.add(track['track_name'])
                album_name.add( track['album_name'] + track['track_name'])
                if track['artist_name'] + track['album_name'] + track['track_name'] in data:
                    print(json.dumps(track,ensure_ascii=False), file=conflict)
                    print(json.dumps(data[track['artist_name'] + track['album_name'] + track['track_name']],ensure_ascii=False), file=conflict)
                else:
                    data[track['artist_name'] + track['album_name'] + track['track_name']] = track
        print (len(data))        
    with open(os.getcwd() + '/kkbox_utf8_0123.csv', 'r') as first:
        with open(os.getcwd() + "/old_data.txt", "w") as old:
            first.readline()
            for line in first:
                tmp = line.split(',')
                if len(tmp) < 8 or ( tmp[7] + tmp[4] + tmp[1] not in data and tmp[4] + tmp[1] not in album_name and tmp[1] not in track_name):
                    print(line, end='', file=old)
                


    

