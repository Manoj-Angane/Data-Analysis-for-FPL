import pandas as pd,os
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
os.chdir('D:/Python/Data_Analysis/venv')
result=pd.DataFrame()
for f in ['current','next']:
    file=f+'_fixture.csv'
    temp=pd.read_csv(file, header=0, sep=',', index_col=False)
    temp=temp[temp['is_home']==True]
    temp=temp[['id','ID','opponent']]
    temp.rename(index=str, columns={"ID":"team_h","opponent":"team_a"}, inplace=True)
    next=temp[['id','team_a','team_h']].sort_values('id')
    temp=pd.read_csv('teams.csv', header=0, sep=',', index_col=False)
    teams=temp[['id','name','strength_attack_away','strength_attack_home','strength_defence_away','strength_defence_home','strength_overall_away','strength_overall_home']].sort_values('id')
    temp = next.merge(teams, left_on='team_a', right_on='id', how='inner',suffixes=['','_away'] )
    temp = temp.merge(teams, left_on='team_h', right_on='id', how='inner',suffixes=['','_home'])
    temp.drop(['id_away','id_home'],axis=1,inplace=True)
    temp = temp[['id', 'team_h', 'name_home', 'strength_attack_home_home', 'strength_defence_home_home',
                 'strength_overall_home_home', 'team_a', 'name', 'strength_attack_away', 'strength_defence_away',
                 'strength_overall_away']]
    temp.rename(index=str, columns={"name": "name_away","strength_attack_home_home":"strength_attack_home","strength_defence_home_home":"strength_defence_home","strength_overall_home_home":"strength_overall_home"},inplace=True)

    temp['match']=f
    result=result.append(temp,ignore_index=True)

result.to_csv('schedule.csv', sep=',', encoding='utf-8',index=False)

