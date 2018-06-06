'''https://stackoverflow.com/questions/25471450/python-getting-all-links-from-a-google-search-result-page?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
https://www.google.com/search?ei=-4QVW_SFO9CkzwLMopbICA&q=python+program+to+save+google+search+links&oq=python+program+to+save+google+search+links&gs_l=psy-ab.3...6820.7630.0.8074.6.6.0.0.0.0.100.575.5j1.6.0....0...1c.1.64.psy-ab..0.0.0....0.B3707fUQpj8
https://stackoverflow.com/questions/45468005/parse-url-beautifulsoup?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
'''


import requests, re
from bs4 import BeautifulSoup
query = input("Input the word: ")
page = requests.get("https://www.google.dz/search?q="+query)
soup = BeautifulSoup(page.content, "html5lib")
outFile = open(query+'.txt','w') 
for link in  soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
    wordList = link["href"].replace("/url?q=","").split('&')[0]
    #wordList = re.split(":(?=http)",link["href"].replace("/url?q=","").split('&')[0])
    print(wordList)
    outFile.write("%s\n" % wordList)

