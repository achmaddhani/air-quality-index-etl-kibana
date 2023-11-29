"""
Achmad Dhani

Objective: Creating a function file to for cleaning data
"""

import pandas as pd
import requests

# required function for cleaning
def get_country_from_city(city):
    '''Getting country name of a city with Geoname API

    Args:
        city (type: string): inputs a city name

    Returns:
        type: string: returns a country name
    '''
    url = f"http://api.geonames.org/searchJSON?q={city}&maxRows=1&username=achmaddhani" # api for geonames
    response = requests.get(url)
    data = response.json()
    if 'geonames' in data and len(data['geonames']) > 0:
        geoname = data['geonames'][0]
        return geoname.get('countryName')
    else:
        print(f"No results for {city}: {data}")
        return None

def cleaning_data():
    '''
    A function for automation with the flow:
    - starts with reading the csv file
    - normalizing the column names with lowercase
    - replacing spaces with underscore and removing dot from column names
    - dropping duplicates of cities and keeping only one
    - drop any duplicates that exist
    - making sure the columns has the correct data type
    - imputing missing columns in country with geonames api function
    - dropping missing values that isnt in geoname
    - saving the cleaned csv
    '''
    df= pd.read_csv('/opt/airflow/data/P2M3_Dhani_data_raw.csv') # read the csv
    data_types= {
        'aqi_value':'int64',
        'co_aqi_value':'int64',
        'ozone_aqi_value':'int64',
        'no2_aqi_value':'int64',
        'pm25_aqi_value':'int64',
        'lat':'float64',
        'lng':'float64'
    } # columns of each data types
    df.columns = df.columns.map(str.lower) # turning all columns to lowercase
    trans_table = str.maketrans(' ', '_', '.')
    df.columns = [col.translate(trans_table) for col in df.columns] # replacing spaces with underscore and removing dot
    df.drop_duplicates(subset='city', keep='first', inplace=True) # removing city duplicates and keeping only one 
    df.drop_duplicates(inplace=True) # removing duplicates overall
    df= df.astype(data_types) # fixing the data type
    df['country'] = df.apply(lambda row: get_country_from_city(row['city']) if pd.isnull(row['country']) else row['country'], axis=1) # imputing missing value with api
    df.dropna(inplace=True) # drop missing values that's not registered on geo name
    df.to_csv('/opt/airflow/data/P2M3_dhani_data_clean.csv', index=False) # saving the cleaned data