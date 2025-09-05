# utils.py

import requests
import re

BLYNK_AUTH_TOKEN = 'lBVKmsFQXYhEksQ_dLvxij46zkryBl76'
#BLYNK_BASE_URL = 'http://blynk-cloud.com'

def get_blynk_data(pin):
    # Blynk API endpoint for reading pin data
    url = f"https://blynk.cloud/external/api/get?token=lBVKmsFQXYhEksQ_dLvxij46zkryBl76&pin={pin}"
    
    # Make a GET request to the Blynk server
    try:
        response = requests.get(url)
        if response.status_code == 200:
            
            data = response.text.strip()
            
            print(f"Raw data from Blynk: {data}")  # Debugging line
            return {"value": data}
           
           
        else:
            print(f"⚠️ Error {response.status_code} fetching {pin}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Connection error: {e}")
        return None