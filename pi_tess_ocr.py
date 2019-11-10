try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import io
import unicodedata
import json
import requests
from firebase import firebase
import sys

# image_loc = sys.argv[1]
# title = sys.argv[2]
# page = sys.argv[3]

stuff = []
good = []
a = pytesseract.image_to_data(Image.open('/home/tyler/Desktop/third.png'))

buf2 = io.StringIO(a)
buf = io.StringIO(a)
for x in range(0, len(buf2.read())):
    g = buf.readline().encode('utf-8').split()
    dontadd = False
    for c in g:
        if c == "\n":
            dontadd = True
            break
    if dontadd == False:
        stuff.append(g)
for g in reversed(stuff):
    if g == []:
        stuff.remove(g)
    elif len(g) < 12:
        stuff.remove(g)

keys = stuff[0]
dict = {}
for k in range(1,len(stuff)):
    dict = {}
    for d in range(0,len(stuff[k])):
        dict[keys[d]] = stuff[k][d]
    good.append(dict)

#image
image_loc_database = ["gs://microfilm-fab15.appspot.com/Auto-Scan000.jpg","gs://microfilm-fab15.appspot.com/Auto-Scan001","jpg,gs://microfilm-fab15.appspot.com/Auto-Scan002.jpg"]
image = {}
image["image"] = image_loc_database[2]
good.append(image)
#title
title = {}
title["title"] = 'Maryville Daily pg3'
good.append(title)

#print(json.dumps(good).encode())
json_data = json.dumps(good).encode()
r = requests.post(url = "https://microfilm-fab15.firebaseio.com/Newspapers.json", data=json_data)
pastebin_url = r.text
print("The pastebin URL is:%s"%pastebin_url)

# firebase = firebase.FirebaseApplication('https://microfilm-fab15.firebaseio.com', None)
# new_user = "frog"
#
# result = firebase.get('/Newspapers/Newspaper1',None)
# print(result)
