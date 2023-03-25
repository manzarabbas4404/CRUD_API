
import requests
import json

URL = "http://127.0.0.1:3000/student/"

def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    res = requests.get(url=URL, data=json_data)
    data = res.json()
    print(data)
# get_data(2)

def post_data():
    data ={
        'name': 'Adeel',
        'age':15,
        'city':'layyah'
    }
    res = json.dumps(data)
    json_data = requests.post(url=URL, data=res)
    result = json_data.json()
    print(result)
# post_data()

def update():
    data = {
        'id':5,
        'name':'Masha',
        'age':55
    }
    res = json.dumps(data)
    json_data = requests.put(url=URL, data=res)
    result = json_data.json()
    print(result)
update()

def delete_data():
    data={'id':6}
    res = json.dumps(data)
    json_data = requests.delete(url=URL, data=res)
    result = json_data.json()
    print(result)
# delete_data()

