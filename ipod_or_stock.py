import csv
import re
import json
from datetime import datetime
from datetime import date
from datetime import timedelta

def get_stock_prices(csv_file):
    current_price = 599.55 # March 30, 2012
    pric