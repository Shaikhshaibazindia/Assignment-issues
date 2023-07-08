#!/usr/bin/env python
# coding: utf-8

# Question 1 display all header tags from wikipedia

# In[1]:


from bs4 import BeautifulSoup


# In[2]:


import requests


# In[3]:


import pandas as pd


# In[4]:


wikipedia_page=requests.get("https://en.wikipedia.org/wiki/Main_Page")
wikipedia_page


# In[5]:


header=BeautifulSoup(wikipedia_page.content,"html.parser")
header


# # Header 

# In[6]:


header_tags = header.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])


# In[7]:


header_texts = [tag.text.strip() for tag in header_tags]


# In[8]:


df = pd.DataFrame(header_texts, columns=["Header"])


# In[9]:


df


# # Question 2 Former presidents of India

# In[10]:


from bs4 import BeautifulSoup


# In[11]:


import requests


# In[12]:


Presidents=requests.get("https://presidentofindia.nic.in/former-presidents.htm")
Presidents


# In[13]:


former=BeautifulSoup(Presidents.content)
former


# In[14]:


first=former.find('div',class_="presidentListing")
first


# In[15]:


first.text.split('|')[0]


# In[16]:


Name=[]

for i in former.find_all("div",class_="presidentListing"):
    Name.append(i.text)
    
Name


# In[17]:


replacements = [
    "Shri Ram Nath Kovind",
    "Shri Pranab Mukherjee",
    "Smt Pratibha Devisingh Patil",
    "DR. A.P.J. Abdul Kalam",
    "Shri K. R. Narayanan",
    "Dr Shankar Dayal Sharma",
    "Shri R Venkataraman",
    "Giani Zail Singh",
    "Shri Neelam Sanjiva Reddy",
    "Dr. Fakhruddin Ali Ahmed",
    "Shri Varahagiri Venkata Giri",
    "Dr. Zakir Husain",
    "Dr. Sarvepalli Radhakrishnan",
    "Dr. Rajendra Prasad"]


# In[18]:


new_list = []
for item, replacement in zip(Name, replacements):
    new_item = item.replace(item.strip(), replacement)
    new_list.append(new_item)


# In[19]:


for item in new_list:
    print(item)


# In[20]:


Term = [] # creating the empty list

    

for i in former.find_all("div",class_="presidentListing"):

     Term.append(i.find_all("p")[0].text.split(":")[1])


# In[21]:


Term


# In[22]:


import pandas as pd


# In[23]:


df1=pd.DataFrame({"Name":new_list,"Term":Term})
df1


# Question 3 ICC sports

# # Top 10 ODI teams

# In[1]:


from bs4 import BeautifulSoup


# In[2]:


import requests


# In[6]:


Odi_team=requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')
Odi_team


# In[7]:


Teams=BeautifulSoup(Odi_team.content)
Teams


# In[40]:


x=0

Names=[]

for i in Teams.find_all('span',class_="u-hide-phablet"):
    Names.append(i.text)
    x+=1
    
    if x==10:
        break
    
Names


# In[43]:


Points1=[]

for i in Teams.find('td',class_="rankings-block__banner--points"):
    Points1.append(i.text)
    
Points1


# In[44]:


Points2=[]

for i in Teams.find_all('td',class_="table-body__cell u-center-text"):
    Points2.append(i.text)
    
Points2


# In[38]:


j=0

for points in Points2:
    points==points.replace(',','')
    
    if len(points)!=2 or not points.isdigit():
        print(points)
        j +=1
        
    if j==10:
        break
    


# In[46]:


points_final=Points1+points


# In[30]:


type(Points2)


# In[19]:


rating=[]

for i in Teams.find_all("td",class_="rankings-block__banner--rating u-text-right"):
    rating.append(i.text.strip())
    
rating


# In[59]:


m=0
rating2=[]

for i in Teams.find_all("td",class_="table-body__cell u-text-right rating"):
    rating2.append(i.text)
    m+=1
    
    if m==9:
        break
        
rating2


# In[60]:


rating1=rating+rating2
rating1


# In[35]:


match=[]

for i in Teams.find_all('td',class_="rankings-block__banner--matches"):
    match.append(i.text)
    
match


# In[41]:


match2=[]

for i in Teams.find_all('td',class_="table-body__cell u-center-text"):
    match2.append(i.text)
    
match2


# In[50]:


k=0

for matchs in match2:
    matchs=matchs.replace(',','')
    
    if len(matchs)==2 and matchs.isdigit():
        print(matchs)
        k+=1
        
    if k==10:
        break
    


# In[52]:


import pandas as pd


# In[66]:


df3=pd.DataFrame({'Teams':Names,'Matchs':matchs,'Points':points,'Rating':rating1})

df3


# Top 10 Odi batsman

# In[67]:


from bs4 import BeautifulSoup


# In[68]:


import requests


# In[69]:


Mens_bat=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi')
Mens_bat


# In[70]:


bat=BeautifulSoup(Mens_bat.content)
bat


# In[78]:


batsman=bat.find('div',class_="rankings-block__banner--name")
    
batsman


# In[79]:


batsman.text


# In[80]:


b=0
batsman2=[]
for i in bat.find_all('td',class_="table-body__cell name"):
    batsman2.append(i.text)
    b+=1
    
    if b==9:
        break
        
batsman2


# In[81]:



batsman1=batsman+batsman2
batsman1


# In[ ]:





# # Question 5 scrapping of news

# In[43]:


import pandas as pd


# In[44]:


from bs4 import BeautifulSoup


# In[45]:


import requests


# In[46]:


news_page=requests.get("https://www.cnbc.com/world/?region=world")

news_page


# In[51]:


latest_news=BeautifulSoup(news_page.content)
latest_news


# In[58]:


Headline=[]

for i in latest_news.find_all('a',class_="LatestNews-headline"):
    Headline.append(i.text)
    
Headline


# In[60]:


time=[]
for i in latest_news.find_all('time',class_="LatestNews-timestamp"):
    time.append(i.text)
    
time


# In[67]:


URL=[]

for i in latest_news.find_all("a",class_="LatestNews-headline"):
    URL.append(i.get("href"))
    
URL


# In[68]:


print(len(Headline),len(time),len(URL))


# In[69]:


df5=pd.DataFrame({"Headlines":Headline,"Time":time,"URLS":URL})

df5


# # Downloaded Articles from AI

# In[74]:


from bs4 import BeautifulSoup


# In[76]:


import pandas as pd


# In[77]:


import requests


# In[79]:


articles=requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')
articles


# In[82]:


new_AI=BeautifulSoup(articles.content)
new_AI


# Paper Title

# In[83]:


Paper_title=[]

for i in new_AI.find_all('h2',class_="sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg"):
    Paper_title.append(i.text)
    
Paper_title


# Authors

# In[84]:


Authors=[]

for i in new_AI.find_all('span',class_="sc-1w3fpd7-0 dnCnAO"):
    Authors.append(i.text)
    
Authors


# # Published Date

# In[87]:


date=[]

for i in new_AI.find_all('span',class_="sc-1thf9ly-2 dvggWt"):
    date.append(i.text)
    
date


# # Paper URL

# In[90]:


P_URL=[]

for i in new_AI.find_all('a',class_="sc-5smygv-0 fIXTHm"):
    P_URL.append(i.get("href"))
    
P_URL


# In[93]:


df6=pd.DataFrame({"Paper Title":Paper_title,"Authors":Authors,"Published Date":date,"Paper URL":P_URL})
df6


# # Restuarants Data

# In[94]:


from bs4 import BeautifulSoup


# In[95]:


import pandas as pd


# # import requests

# In[99]:


page=requests.get("https://www.dineout.co.in/delhi-restaurants/buffet-special")
page


# In[100]:


page_html=BeautifulSoup(page.content)
page_html


# # Restaurant Name

# In[101]:


R_Name=[]

for i in page_html.find_all('a',class_="restnt-name ellipsis"):
    R_Name.append(i.text)
    
R_Name


# Cuisine

# In[ ]:




