# url https://developer.nutritionix.com/admin/access_details

import requests
from datetime import datetime as dt
import os

NUTRITIONIX_API_ID = os.environ.get("NUTRITIONIX_API_ID", "Update ENV variables from secrets. Add NUTRITIONIX_API_ID")
NUTRITIONIX_API_KEY = os.environ.get("NUTRITIONIX_API_KEY", "Update ENV variables from secrets. Add NUTRITIONIX_API_KEY")
URl = 'https://trackapi.nutritionix.com/v2/natural/exercise'

G_SHEET_PROJECT = 'trofimovWorkouts'
G_SHEET_NAME = 'workouts'
G_SHEET_USER_NAME = os.environ.get("G_SHEET_USER_NAME", "Update ENV variables from secrets. Add G_SHEET_USER_NAME")
G_SHEET_TOKEN = os.environ.get("G_SHEET_TOKEN", "Update ENV variables from secrets. Add G_SHEET_TOKEN")
G_SHEET_URL = f'https://api.sheety.co/{G_SHEET_USER_NAME}/{G_SHEET_PROJECT}/{G_SHEET_NAME}'

nut_headers = {
    'x-app-id': NUTRITIONIX_API_ID,
    'x-app-key': NUTRITIONIX_API_KEY,
    'x-remote-user-id': '0'
}

user_input = input("Tell me which exercises you did? ")
body = {
    'query': user_input,
    'weight_kg': 80,
    'height_cm': 190,
    'age': 30
}
print(user_input) # Ran 12 miles and walked for 2 km

response = requests.post(url=URl, headers=nut_headers, data=body)
print(response.json())

# response = {"exercises":[{"tag_id":317,"user_input":"ran","duration_min":120.01,"met":9.8,"nf_calories":1568.13,"photo":{"highres":"https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_highres.jpg","thumb":"https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_thumb.jpg","is_user_uploaded":'false'},"compendium_code":12050,"name":"running","description":'',"benefits":''},{"tag_id":100,"user_input":"walked","duration_min":24.85,"met":3.5,"nf_calories":115.97,"photo":{"highres":"https://d2xdmhkmkbyw75.cloudfront.net/exercise/100_highres.jpg","thumb":"https://d2xdmhkmkbyw75.cloudfront.net/exercise/100_thumb.jpg","is_user_uploaded":'false'},"compendium_code":17190,"name":"walking","description":'',"benefits":''}]}
today_date = dt.today().strftime("%d/%m/%Y")
today_time = dt.today().strftime("%H:%M:%S")
print(f'date = {today_date}, time = {today_time}')

g_sheet_headers = {
    'Authorization': f'Bearer {G_SHEET_TOKEN}'
}

for activity in response.json()['exercises']:
    one_row = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": str.title(activity['name']),
            "duration": activity['duration_min'],
            "calories": activity['nf_calories']
        }
    }

    respo = requests.post(url=G_SHEET_URL, json=one_row, headers=g_sheet_headers)
    print(f'Post new activity: {respo.text}')


get_all = requests.get(url=G_SHEET_URL, headers=g_sheet_headers)
print(f'All activities in google sheets: {get_all.text}')