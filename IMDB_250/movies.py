from flask import Flask, render_template, request, redirect
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    response = requests.get('https://www.imdb.com/chart/top/')
    webpage = response.text

    soup = BeautifulSoup(webpage, 'html.parser')
    td_data = soup.find_all(name='td', class_='titleColumn')

    movies = []

    for data in td_data:
        movie = data.find(name='a').getText()
        movies.append(movie)

    return render_template('index.html', data=movies)

'''
# Write data to a text film
with open('movie_data.txt', 'w') as file:
    file.write('\n')
    for i in range(len(movies)):
        file.write(f'{i+1}. {movies[i]}\n')
    file.close()

print("Data successfully saved")
'''


if __name__ == "__main__":
    app.debug = True
    app.run()