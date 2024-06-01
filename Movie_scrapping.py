from bs4 import BeautifulSoup
import requests
import pandas as pd

data = []

try:
    source = requests.get('https://www.hoyts.com.au/movies')
    source.status_code

    soup = BeautifulSoup(source.text, 'html.parser')
    
    movies = soup.find_all('li', class_= "movies-list__item")
    
    for movie in movies:
        item = {}
        
        item['Name'] = movie.find('a', class_= "movies-list__link").text
        item['Rating'] = movie.find('svg').attrs["title"]
        item['Duration'] = movie.find('span', class_= "movies-list__duration").text[:3]
        item['Release Date'] = movie.find('span', class_= "movies-list__release-date").text
        
        data.append(item) 
            
except Exception as e:
    print(e)

df = pd.DataFrame(data)
print(df)

df.to_csv("Hoyts Movies.csv")