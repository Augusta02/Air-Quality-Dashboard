# Description: This is a simple Streamlit app that provides air quality forecast for different states in Nigeria
import json
import requests
import os 
from dotenv import load_dotenv
from streamlit_echarts import st_echarts
import streamlit as st
import random
import pandas as pd
import datetime 
import time


load_dotenv()
FORECAST_API = os.getenv("FORECAST_API")
AIR_QUALITY_API = os.getenv("NINJA_API")
RAPID_HOST = os.getenv("RAPID_HOST")

headers = {
    'x-rapidapi-key': FORECAST_API,
    'x-rapidapi-host': RAPID_HOST
}


BASE_URL = "https://air-quality.p.rapidapi.com/forecast/airquality"

states = [
    "Abia","Abuja", "Adamawa", "Akwa Ibom", "Anambra", "Bauchi", "Bayelsa", "Benue", "Borno", "Cross River", "Delta", "Ebonyi", "Edo", 
    "Ekiti", "Enugu", "Gombe", "Imo", "Jigawa", "Kaduna", "Kano", "Katsina", "Kebbi", "Kogi", "Kwara", "Lagos", "Nassarawa", "Niger", 
    "Ogun", "Ondo", "Osun", "Oyo", "Plateau", "Rivers", "Sokoto", "Taraba", "Yobe", "Zamfara"]

CACHE_FILE = "air_quality_cache.json"

def load_cache():
    try:
        with open(CACHE_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_cache(data):
    with open(CACHE_FILE, "w") as file:
        json.dump(data, file)


# Function to Assign Colors for PM2.5 Levels
# def assign_color(value):
#     if value <= 15:
#         return "green"
#     elif value > 15 and value <= 40:
#         return "yellow"
#     elif value > 40 and value <= 65:
#         return "orange"
#     elif value > 65 and value <= 150:
#         return "red"
#     elif value > 150 and value <= 250:
#         return "purple"
#     else: 
#         return "maroon"
    


#Get NO data
def get_no_data(state):
    cache = load_cache()
    # Check cache before making API request
    if state in cache and "NO2" in cache[state]:  
        return cache[state]["NO2"]
    
    api_url = 'https://api.api-ninjas.com/v1/airquality?city={}'.format(state)
    for attempt in range(3):
        response = requests.get(api_url, headers={'X-Api-Key': AIR_QUALITY_API})
        if response.status_code == 200:
            response = response.json()
            no = response.get('NO2', {}).get('concentration', None)

            # Update cache
            cache[state] = cache.get(state, {})
            cache[state]["NO2"] = no 
            save_cache(cache)
            return no
        elif response.status_code != 200:  # Too Many Requests
            retry_after = response.headers.get("Retry-After", 5)  # Default wait 5 sec
            print(f"Rate limit hit! Retrying in {retry_after} seconds...")
            time.sleep(int(retry_after))  

        else:
            print(f"Error fetching NO2 data for {state}: {response.status_code}")
            return None

# Get PM2.5 data 
def get_pm25_data(state):
    cache = load_cache()
    # Check cache before making API request
    if state in cache and "PM25" in cache[state]:  
        return cache[state]["PM25"]
    
    api_url = 'https://api.api-ninjas.com/v1/airquality?city={}'.format(state)
    for attempt in range(3):
        response = requests.get(api_url, headers={'X-Api-Key': AIR_QUALITY_API})
        if response.status_code == 200:
            response = response.json()
            pm25 = response.get('PM2.5', {}).get('concentration', None)
            # Update cache
            cache[state] = cache.get(state, {})
            cache[state]["PM25"] = pm25
            save_cache(cache)
            return pm25
        elif response.status_code != 200:  # Too Many Requests
            retry_after = response.headers.get("Retry-After", 5)  # Default wait 5 sec
            print(f"Rate limit hit! Retrying in {retry_after} seconds...")
            time.sleep(int(retry_after))  
        else:
            print(f"Error fetching PM25 data for {state}: {response.status_code}")
            return None

# Get PM10 data
def get_pm10_data(state):
    cache = load_cache()
    # Check cache before making API request
    if state in cache and "PM10" in cache[state]:  
        return cache[state]["PM10"]
    
    api_url = 'https://api.api-ninjas.com/v1/airquality?city={}'.format(state)
    for attempt in range(3):
        response = requests.get(api_url, headers={'X-Api-Key': AIR_QUALITY_API})
        if response.status_code == 200:
            response = response.json()
            pm10 = response.get('PM10', {}).get('concentration', None)
            # Update cache
            cache[state] = cache.get(state, {})
            cache[state]["PM10"] = pm10
            save_cache(cache)
            return pm10
        elif response.status_code != 200:  # Too Many Requests
            retry_after = response.headers.get("Retry-After", 5)  # Default wait 5 sec
            print(f"Rate limit hit! Retrying in {retry_after} seconds...")
            time.sleep(int(retry_after))  
        else:
            print(f"Error fetching PM10 data for {state}: {response.status_code}")
            return None

# # Get O3 data
def get_o3_data(state):
    cache = load_cache()
    # Check cache before making API request
    if state in cache and "O3" in cache[state]:  
        return cache[state]["O3"]
    
    api_url = 'https://api.api-ninjas.com/v1/airquality?city={}'.format(state)
    for attempt in range(3):
        response = requests.get(api_url, headers={'X-Api-Key': AIR_QUALITY_API})
        if response.status_code == 200:
            response = response.json()
            O3 = response.get('O3', {}).get('concentration', None)
            # Update cache
            cache[state] = cache.get(state, {})
            cache[state]["O3"] = O3
            save_cache(cache)
            return O3
        elif response.status_code != 200:  # Too Many Requests
            retry_after = response.headers.get("Retry-After", 5)  # Default wait 5 sec
            print(f"Rate limit hit! Retrying in {retry_after} seconds...")
            time.sleep(int(retry_after))  
        else:
            print(f"Error fetching O3 data for {state}: {response.status_code}")
            return None


# # # Get Air Quality forecast data
def fetch_air_quality(state):
    cache = load_cache()
    # Use cached data if available
    if state in cache:  
        return cache[state]

    querystring = {"city": state,"hours":"72"}

    response = requests.get(BASE_URL, headers=headers, params=querystring)
    if response.status_code != 200:
        print(f"Error fetching data for {state}: {response.status_code}")
        return []

    response = response.json()
    pm25_values = []
    # Get Current time 
    now = datetime.datetime.now()
    current_time = now.strftime("%Y-%m-%dT%H")
    for component in response['data']:
        datetime_str = component['timestamp_local']
        date, time = datetime_str.split("T")
        hour = time[:5]
        pm25 = component['pm25']
        # Calculate the time difference
        component_time = datetime.datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S")
        time_diff = (component_time - now).total_seconds() / 3600  # Convert to hours

        if 0 < time_diff <= 5:  # Keep only next 5 hours
            pm25_values.append([date, hour, pm25])
    return pm25_values

# print(fetch_air_quality("Lagos"))


# Application FrontEND

def main():
    st.title("Air Quality Forecast")
    st.write("This app provides air quality forecast for different states in Nigeria")
    left_column, right_column = st.columns(2)

    with right_column:
        selected_state = st.selectbox("Select State", states)
    
    with left_column:
        st.subheader(f"{selected_state}") 
        st.markdown("🇳🇬 **Nigeria**")


    # Get Individual Air Quality data
    cols = st.columns([.333, .333, .333, .333])
    with cols[0]:
        value = get_pm25_data(selected_state)
        box_title = "PM2.5"
        st.markdown(
        f"""
        <div style="
            border-radius: 12px; 
            border: 1px solid #ddd; 
            padding: 15px; 
            text-align: center;
            width: 120px;
            display: inline-block;
            background-color: white;
        ">
            <p style="color: grey; font-size: 14px; margin: 0;">{box_title}</p>
            <p style="color: black; font-size: 22px; font-weight: bold; margin: 5px 0;">{value}</p>
            <p style="color: black; font-size: 12px; margin: 0;">µg/m³</p>
        </div>
        """,
        unsafe_allow_html=True
        )


    with cols[1]:
        value = get_pm10_data(selected_state)
        box_title = "PM10"
        st.markdown(
        f"""
        <div style="
            border-radius: 12px; 
            border: 1px solid #ddd; 
            padding: 15px; 
            text-align: center;
            width: 120px;
            display: inline-block;
            background-color: white;
        ">
            <p style="color: grey; font-size: 14px; margin: 0;">{box_title}</p>
            <p style="color: black; font-size: 22px; font-weight: bold; margin: 5px 0;">{value}</p>
            <p style="color: black; font-size: 12px; margin: 0;">µg/m³</p>
        </div>
        """,
        unsafe_allow_html=True
        )
        

    with cols[2]:
        value = get_no_data(selected_state)
        box_title = "NO"
        st.markdown(
        f"""
        <div style="
            border-radius: 12px; 
            border: 1px solid #ddd; 
            padding: 15px; 
            text-align: center;
            width: 120px;
            display: inline-block;
            background-color: white;
        ">
            <p style="color: grey; font-size: 14px; margin: 0;">{box_title}</p>
            <p style="color: black; font-size: 22px; font-weight: bold; margin: 5px 0;">{value}</p>
            <p style="color: black; font-size: 12px; margin: 0;">µg/m³</p>
        </div>
        """,
        unsafe_allow_html=True
        )

    with cols[3]:
        value = get_o3_data(selected_state)
        box_title = "O3"
        st.markdown(
        f"""
        <div style="
            border-radius: 12px; 
            border: 1px solid #ddd; 
            padding: 15px; 
            text-align: center;
            width: 120px;
            display: inline-block;
            background-color: white;
        ">
            <p style="color: grey; font-size: 14px; margin: 0;">{box_title}</p>
            <p style="color: black; font-size: 22px; font-weight: bold; margin: 5px 0;">{value}</p>
            <p style="color: black; font-size: 12px; margin: 0;">µg/m³</p>
        </div>
        """,
        unsafe_allow_html=True
        )


    # Get Air Quality Forecast data
    forecast_data = fetch_air_quality(selected_state)
    time_labels = [entry[1] for entry in forecast_data]
    pm25_values = [entry[2] for entry in forecast_data]
    # colors = [assign_color(entry[2]) for entry in forecast_data]

    st.subheader("Air Quality Forecast")
    option = {
        "tooltip": {"trigger": "axis"},
        "xAxis": {"type": "category", "data": time_labels},
        "yAxis": {"type": "value"},
        "visualMap": {
            "type": "piecewise",
            "show": False,
            "pieces": [
                {"min": 0, "max": 15, "color": "#00C853"},
                {"min": 16, "lte": 40, "color": "FFD600"},
                {"min": 41, "lte": 65, "color": "FF6D00"},
                {"min": 66, "lte": 150, "color": "D50000"},
                {"min": 151, "lte": 250, "color": "#AA00FF"},
                {"min": 251, "color": "#780000"},
            ],
        },
        "series": [
            {
                "data": pm25_values,
                "type": "line",
                "smooth": True,
                "symbolSize": 8,
                "lineStyle": {"width": "3"},
            }
        ],
    }

    st_echarts(option, height="500px")




if __name__ == "__main__":
    main()

    