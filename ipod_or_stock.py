import csv
import re
import json
from datetime import datetime
from datetime import date
from datetime import timedelta

def get_stock_prices(csv_file):
    current_price = 599.55 # March 30, 2012
    prices = {}
    stockReader = csv.reader(open(csv_file), delimiter=',')
    
    stockReader.next() # Throw away column headings
    
    for i, row in enumerate(stockReader):
        if i == 0:
            current_price = row[6]
        date_object = datetime.strptime(row[0], '%Y-%m-%d')
        prices[date_object] = row[6]
        
    return (prices, float(current_price))
    
def get_products(json_file):
    products = json.load(open(json_file))
    
    for product in products:
        try:
            price =  product["original-price"]
        except KeyError:
            price =  product["original-price-us"]

        match 