import  csv
import json
import pandas as pd
import os

#df = pd.read_json(os.getcwd() +  '/kkbox_2019h2_hot50k.json', lines=True)
path = os.getcwd() +  '/kkbox_2019h2_hot50k.json'
with open(path, 'r') as kkbox:
    data = {}
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
                if track['artist_name'] + track['album_name'] + track['track_name'] in data:
                    print(json.dumps(track,ensure_ascii=False), file=conflict)
                    print(json.dumps(data[track['artist_name'] + track['album_name'] + track['track_name']],ensure_ascii=False), file=conflict)
                else:
                    track['mark'] = '0'
                    data[track['artist_name'] + track['album_name'] + track['track_name']] = track
        print (len(data))        
    # load old file and print old data and mark the same data
    
    with open(os.getcwd() + '/kkbox_utf8_0123.csv', 'r') as first:
        with open(os.getcwd() + "/old_data.txt", "w") as old:
            first.readline()
            for line in first:
                tmp = line.split(',')
                if not tmp[1]:
                    continue
                map(str.strip, tmp)
                #if len(tmp) < 8 or ( tmp[7] + tmp[4] + tmp[1] not in data.keys() and tmp[4] + tmp[1] not in album_name and tmp[1] not in track_name):
                count = 0
                mark = ''
                for key in data.keys():
                    if len(tmp) < 8 or (tmp[7] + tmp[4] + tmp[1] not in key and tmp[4]+tmp[1] not in key and tmp[1] not in key   ):
                        count+=1
                    else:
                        mark = key
                if count == len(data.keys()):
                    print(line, end='', file=old)
                else:
                    data[mark]['mark'] = '1'
                    
    #save the new data of new file
    with open(os.getcwd() + '/same_data.txt', "w") as same:
        for key in data.keys():
            jsondata = data[key]
            if jsondata['mark'] == '1' :
                print(json.dumps(jsondata, ensure_ascii=False), file=same)
    with open(os.getcwd() + '/new_data.txt', "w") as new:
        for key in data.keys():
            jsondata = data[key]
            if jsondata['mark'] == '0':
                print(json.dumps(jsondata, ensure_ascii=False), file=new)