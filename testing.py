import json 
import requests 


def create_data():
    data = {
                'user_name':'test2345',
                'user_response':'Accept2345',
                'response_image':'image12345'
            }
    json_data = json.dumps(data)
    r = requests.post(url = 'http://127.0.0.1:8000/img/create_data/', data = json_data)
    response = r.json()
    print(response) 

def get_data(user):
    data = {
        'user_name':user
    }
    json_data = json.dumps(data)
    r = requests.get(url = 'https://pixeltech.onrender.com/img/get_data/', data = json_data)
    response = r.json()
    print(response)

def test_route():
    r = requests.post(url = 'https://pixeltech.onrender.com/img/test')
    response = r.json()
    print(response)
get_data('varun')

# get_data()