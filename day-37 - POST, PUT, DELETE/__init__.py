import requests
from datetime import datetime as dt

PIXELA_USERNAME = 'grap from secrets'
PIXELA_GRAPH_ID = 'graph-test-1'
PIXELA_GRAPH_NAME = 'my-test-graph'
PIXELA_TOKEN = 'grap from secrets'
PIXELA_URL = 'https://pixe.la'
CREATE_USER = '/v1/users'
CREATE_GRAPH = f'/v1/users/{PIXELA_USERNAME}/graphs'
GET_GRAPH = f'/v1/users/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}'
AUTH_HEADER = 'X-USER-TOKEN'

create_user_params = {
    'token': PIXELA_TOKEN,
    'username': PIXELA_USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# create_user_response = requests.post(url=PIXELA_URL + CREATE_USER, json=create_user_params)
# print(create_user_response.text) # {"message":"Success. Let's visit https://pixe.la/@mykhailo-trofimov , it is your profile page!","isSuccess":true}

create_graph_params = {
    'id': PIXELA_GRAPH_ID,
    'name': PIXELA_GRAPH_NAME,
    'unit': 'km',
    'type': 'float',
    'color': 'kuro'  # shibafu (green), momiji (red), sora (blue), ichou (yellow), ajisai (purple) and kuro (black)
}

headers = {
    AUTH_HEADER: PIXELA_TOKEN
}

# create_graph_response = requests.post(url=PIXELA_URL + CREATE_GRAPH, json=create_graph_params,
#                                       headers=headers)
# print(create_graph_response.text)  # {"message":"Success.","isSuccess":true}

# res = requests.get(url=PIXELA_URL + GET_GRAPH, headers=headers)
# print(res.text) # return xml document

today_ = dt.today()
formatted_date = f'{today_.strftime("%Y%m%d")}'  # DOC: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

post_pixel_params = {
    'date': formatted_date,  # yyyyMMdd
    'quantity': '14.6'  # int ^\-?[0-9]+, float ^\-?[0-9]+\.[0-9]+
}

# post_pixel = requests.post(url=PIXELA_URL + GET_GRAPH, json=post_pixel_params, headers=headers)
# print(post_pixel.text)

put_pixel_params = {
    'quantity': '32'  # int ^\-?[0-9]+, float ^\-?[0-9]+\.[0-9]+
}

put_pixel = requests.put(url=PIXELA_URL + GET_GRAPH + f'/{formatted_date}', json=put_pixel_params, headers=headers)
print(put_pixel.text)

# delete_pixel = requests.delete(url=PIXELA_URL + GET_GRAPH + f'/{formatted_date}', headers=headers)
