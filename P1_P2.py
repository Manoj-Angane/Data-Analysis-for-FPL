import pandas as pd
import os
import csv
os.chdir('D:/Python/Data_Analysis/venv/History')
a=pd.read_json('result_p2.json',orient='columns',typ = 'series')
dict_=dict()
if os.path.isfile('list.txt'):
    os.remove('list.txt')
for y in a.keys():
    try:
        x=pd.DataFrame.from_dict(a[y], orient='columns', dtype=None, columns=None)
        name = y+'.csv'
        x.to_csv(name, sep=',', encoding='utf-8',index=False)
        print("success :" + y + str(type(a[y])))
        with open('list.txt','a') as k:
            k.write(name+'\n')
    except ValueError:
        dict_[y]=str(a[y])
        print("error :"+y+str(type(a[y]))+str(a[y]))
with open('variable2.csv', 'w') as f:
    w=csv.DictWriter(f,dict_.keys())
    w.writeheader()
    w.writerow(dict_)