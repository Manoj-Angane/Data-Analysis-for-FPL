import pandas as pd,os,write
os.chdir('D:/Python/Data_Analysis/venv')
elements=pd.read_csv('elements.csv', header=0, sep=',', index_col=False)
teams=pd.read_csv('teams.csv', header=0, sep=',', index_col=False)
teams=teams[['id','name','strength_attack_away','strength_attack_home','strength_defence_away','strength_defence_home','strength_overall_away','strength_overall_home']]
#print(list(elements))
#pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
hit=elements[['id','web_name','element_type','team','minutes','creativity','threat','influence','form','points_per_game','value_season']]
print(hit['id'].max())