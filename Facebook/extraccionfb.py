#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install facebook-scraper


# In[ ]:



from facebook_scraper import get_posts
import couchdb
import json
import time


# In[ ]:


couch=couchdb.Server('http://ChristianSoledispa:soledispa1@localhost:5984/')
nombredb='ea_sports_fifa22'
db=couch[nombredb]


# In[1]:


i=1
for post in get_posts('easportsfifa', pages=1000, extra_info=True):
    print(i)
    i=i+1
    time.sleep(5)
    
    id=post['post_id']
    doc={}
     
    doc['id']=id
    
    mydate=post['time']
    
    try:
        doc['texto']=post['text']
        doc['date']=mydate.timestamp()
        doc['likes']=post['likes']
        doc['comments']=post['comments']
        doc['shares']=post['shares']
        try:
            doc['reactions']=post['reactions']
        except:
            doc['reactions']={}

        doc['post_url']=post['post_url']
        db.save(doc)

    
        print("guardado exitosamente")

    except Exception as e:    
        print("no se pudo grabar:" + str(e))


# In[ ]:




