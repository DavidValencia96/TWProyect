import http.client
import base64 as b64
import json
from datetime import datetime


# conn = http.client.HTTPSConnection("fastapi-jd.herokuapp.com")
# payload = json.dumps({
#   "name": "prueba de registro app",
#   "country": "Colombia",
#   "phone": "2332222",
#   "user_create": "2022-04-07",
#   "email": "juan@torovalencia.com",
#   "password": "juan@torovalencia.com",
#   "tipo_user": 0
# })
# headers = {
#   'Content-Type': 'application/json'
# }
# conn.request("POST", "/api/register", payload, headers)
# res = conn.getresponse()
# data = res.read()
# print(data.decode("utf-8"))



conn = http.client.HTTPSConnection("fastapi-jd.herokuapp.com")
payload = ''
headers = {
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Imp1YW5AZDMuY29tIiwicGFzc3dvcmQiOiJnQUFBQUFCaVUxNWI1OEZsajljb2xkNU16OGhKdU93emU1SU1SMnJOdDdER0dPVWxGaCIsImV4cCI6MTY1MTg2MjY1N30.woGHuwCH07R5qeyXgEcNJjUFkA0ju9o-WtYXcfBAXj4'
}
conn.request("GET", "/api/tweet", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))