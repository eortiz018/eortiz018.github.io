#HW4 part 2
import requests
import pprint
url='https://en.wikipedia.org/wiki/Demographic_history_of_the_United_States'
r=requests.get(url)
html=r.text
from bs4 import BeautifulSoup
bs=BeautifulSoup(html) 
#-------------------------
    
#-------------------------
my_table=bs.find_all(
    'table',
    class_='wikitable sortable'
    )
my_table=my_table[:1]
bs=BeautifulSoup(str(my_table))
values=bs.find_all('td')

years= []
values_men = []
values_women = []
for index in range(0, len(values)-1,3):
    years.append(values[index])
    values_men.append(values[index+1])
    values_women.append(values[index+2])
    
#-------------------------
    
#-------------------------
years = str(years)
years = years.replace('<td>','')
years = years.replace('</td>','')
years = years.replace('[','')
years = years.replace(']','')

values_men = str(values_men)
values_men = values_men.replace('<td>','')
values_men = values_men.replace('</td>','')
values_men = values_men.replace('[','')
values_men = values_men.replace(']','')

values_women = str(values_women)
values_women = values_women.replace('<td>','')
values_women = values_women.replace('</td>','')
values_women = values_women.replace('[','')
values_women = values_women.replace(']','')
#values_women = values_women.replace(', ','')
#-------------------------

print('years=',years,'\n')
print('values_men=',values_men,'\n')
print('values_women=',values_women)

#try title.text


