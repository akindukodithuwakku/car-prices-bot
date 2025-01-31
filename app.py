import numpy as np
from flask import Flask , render_template , request
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import io
import os

app = Flask(__name__)


@app.route('/' , methods=["GET" , "POST"])
def home():
    table_data = []

    if request.method == "POST":
        model = request.form.get("brand")
        name = request.form.get("vehicleName")
        table_data = car_data(model , name)

    return render_template("home.html" , table_data=table_data)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/charts' , methods=['GET' , 'POST'])
def charts():
    if request.method == "POST":
        model = request.form.get("brand")
        name = request.form.get("vehicleName")
        graph = request.form.get("graphType")
        table_data = car_data(model , name)

        if graph == 'priceVsmileage':
            generate_graph_price_vs_mileage(table_data)
        elif graph == 'carVslocation':
            generate_graph_car_vs_location(table_data)
    return render_template("charts.html")


def generate_graph_price_vs_mileage( data ):
    if not data:
        return

    df = pd.DataFrame(data)
    df.replace(0 , np.nan , inplace=True)
    df.dropna(inplace=True)

    plt.switch_backend('Agg')  # Set the matplotlib backend

    plt.figure()
    plt.scatter(x=df['mileage'] , y=df['price'])
    plt.xlabel('Mileage')
    plt.ylabel('Price')
    plt.title('Price Vs Mileage')

    img = io.BytesIO()
    plt.savefig(img , format='png')
    img.seek(0)

    if not os.path.exists('static/images'):
        os.makedirs('static/images')

    with open('static/images/graph.png' , 'wb') as f:
        f.write(img.getbuffer())


def generate_graph_car_vs_location( data ):
    if not data:
        return

    df = pd.DataFrame(data)
    car_count = df['location'].value_counts()

    plt.switch_backend('Agg')  # Set the matplotlib backend

    plt.figure()
    car_count.plot(kind='bar', width=0.5)
    plt.title('No of Cars Vs Location')
    plt.xlabel('Location')
    plt.ylabel('Count')

    img = io.BytesIO()
    plt.savefig(img , format='png')
    img.seek(0)

    if not os.path.exists('static/images'):
        os.makedirs('static/images')

    with open('static/images/graph.png' , 'wb') as f:
        f.write(img.getbuffer())


def car_data( model , name ):
    data = []

    # First page URL format
    url = f'https://riyasewana.com/search/cars/{model}/{name}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Function to scrape a single page
    def scrape_page( url , data ):
        response = requests.get(url , headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content , 'html.parser')

            for elements in soup.find_all(class_="item round"):
                name = elements.find('h2' , class_='more').a.text
                location = elements.find("div" , class_="boxintxt").text.strip()
                price_text = elements.find("div" , class_="boxintxt b").text.strip()
                price = 0 if "negotiable" in price_text.lower() else float(
                    price_text.replace('Rs.' , '').replace(',' , '').strip())

                boxintxt_divs = elements.find_all('div' , class_='boxintxt')
                mileage_text = boxintxt_divs[2].text.strip() if len(boxintxt_divs) > 2 else '0 km'
                mileage = int(mileage_text.replace('(km)' , '').strip()) if '(km)' in mileage_text else 0

                link = elements.find('h2' , class_='more').a['href']

                data.append({
                    "index": len(data) + 1 ,  # Ensure unique indexing across multiple pages
                    "name": name ,
                    "location": location ,
                    "price": price ,
                    "mileage": mileage ,
                    "link": link
                })


    # Scrape the first page
    scrape_page(url , data)

    # Scrape subsequent pages
    for number in range(2 , 5):  # Scrape the next 4 pages
        url = f'https://riyasewana.com/search/cars/{model}/{name}?page={number}'
        scrape_page(url , data)
    print(data)
    return data


if __name__ == "__main__":
    app.run(debug=True)
