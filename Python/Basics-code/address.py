# from json format
book = {}
book['tom'] = {
    'name' : 'tom',
    'address': '1 red street, NY', 
    'phone': 98989898
}
book['bob'] ={
    'name': 'bob',
    'address': '1 green street, NY',
    'phone' : 2345612
}

import json
s =  json.dumps(book)
with open('book.txt', "w") as f:
    f.write(s)