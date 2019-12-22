import urllib.request
import json

body = {'image_path': 'https://maiko7.com/wp-content/uploads/2019/01/people-to-people.jpg'}

myurl = "http://localhost:5000/is_person"
req = urllib.request.Request(myurl)
req.add_header('Content-Type', 'application/json; charset=utf-8')
jsondata = json.dumps(body)
jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
req.add_header('Content-Length', len(jsondataasbytes))
print (jsondataasbytes)
response = urllib.request.urlopen(req, jsondataasbytes)
