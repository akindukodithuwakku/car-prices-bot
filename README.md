# Car Prices Scraper

Welcome to the Car Prices Scraper project! This project is designed to scrape car prices and related information from a commercial site for educational purposes. The data is then presented through a web interface built using Flask, enabling users to visualize and analyze the scraped data.

## Features

- Scrapes car prices, mileage, location, and other relevant information.
- Provides a user-friendly web interface for searching and displaying car data.
- Generates dynamic graphs based on user-selected parameters.
- Includes a responsive design using Bootstrap.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Disclaimer](#disclaimer)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/akindukodithuwakku/car-prices-bot.git
    cd car-prices-bot
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Flask app:**

    ```bash
    flask run
    ```

    The app will be available at `http://127.0.0.1:5000`.

## Usage

### Web Interface

1. **Home Page:**
   - Select the car brand and enter the vehicle name to search for car data.

2. **Charts Page:**
   - Select parameters to generate graphs such as price vs. mileage or location vs. number of cars.

3. **About Page:**
   - Learn more about the project and its educational purpose.

### Updating the Scraped Data

To scrape new data, update the `scraper.py` script and run it:

```bash
python scraper.py


The new data will be saved and can be accessed via the web interface.

License
This project is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. See the LICENSE file for details.

Disclaimer
This project is for educational purposes only. The content displayed is sourced from riyasewana.com, and the original content is owned by them. This project aims to demonstrate web scraping, Flask, and web development techniques.

Thank you for checking out the Car Prices Scraper project! If you have any questions or suggestions, feel free to open an issue or contact the project maintainer.


