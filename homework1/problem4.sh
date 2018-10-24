#!/bin/sh

# download beers.txt if it doesn't exist 
test -e beers.txt || curl -o beers.txt -u datamining2018:Data-Mining-2018 http://aris.me/contents/teaching/data-mining-2018/protected/beers.txt

# return top 10 beers with the most reviews
cat beers.txt | cut -f1 | sort | uniq -c | sort -nr | head -10
