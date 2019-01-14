import pandas as pd,os,ast
os.chdir('D:/Python/Data_Analysis/venv')
a=pd.read_csv('teams.csv', header=0, sep=',', index_col=False)
#print(list(a))

#print(a['current_event_fixture'].values[1])
count=len(a)
i=0
with open('current_fixture.csv','w') as f:
    while i < count:
        e=a['current_event_fixture'].values[i]
        c=ast.literal_eval(e)
        d=c[0]
        if i==0:
            f.write('ID,')
            for g in d.keys():
                f.write(g)
                f.write(',')
            f.write('\n')
        f.write(str(a['id'].values[i]))
        for g in d.keys():
            f.write(','+str(d[g]))
        f.write('\n')
        i+=1

i=0
with open('next_fixture.csv','w') as f:
    while i < count:
        e=a['next_event_fixture'].values[i]
        c=ast.literal_eval(e)
        d=c[0]
        if i==0:
            f.write('ID,')
            for g in d.keys():
                f.write(g)
                f.write(',')
            f.write('\n')
        f.write(str(a['id'].values[i]))
        for g in d.keys():
            f.write(','+str(d[g]))
        f.write('\n')
        i+=1

