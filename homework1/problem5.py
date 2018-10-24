import requests
import sqlite3
import os

# download beers.txt if it doesn't exist
if not os.path.isfile('beers.txt'):
    print 'Downloading beers.txt ...'
    url = 'http://aris.me/contents/teaching/data-mining-2018/protected/beers.txt'
    text = requests.get(url, auth=('datamining2018','Data-Mining-2018')).content
    file = open('beers.txt','w')
    file.write(text)
    file.close()

# creates sql database in memory
conn = sqlite3.connect(':memory:')
com = conn.cursor()
com.executescript('''
    create table beers (name text primary key, nr_reviews int, avg_score real);
    create index names on beers (name);
    --create index scores on beers (avg_score);
''')

# parses file into the database
print 'Reading beers.txt ...'
file = open('beers.txt','r')
for line in file:
    substr = line.split('\t')
    name = substr[0]
    score = substr[1].replace('\n','')
    com.execute('''
    update beers
    set
        avg_score = (avg_score * nr_reviews + ?)/(nr_reviews + 1),
        nr_reviews = nr_reviews + 1
    where name = ?;    
    ''',(score,name))
    com.execute('insert or ignore into beers values (?,1,?);',(name,score))
file.close()

# final query
com.execute('select * from beers where nr_reviews >= 100 order by avg_score desc limit 10;')
results = com.fetchall()

print 'Results: (<name>, <nr_reviews>, <avg_score>)'
for result in results:
    print result
