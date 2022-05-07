import http.client
import json



conn = http.client.HTTPSConnection("fastapi-jd.herokuapp.com")
payload = json.dumps({
  "name": "prueba de registro app",
  "country": "Colombia",
  "phone": "2332222",
  "user_create": "2022-04-07",
  "email": "juan@torovalencia.com",
  "password": "juan@torovalencia.com",
  "tipo_user": 0
})
headers = {
  'Content-Type': 'application/json'
}
conn.request("POST", "/api/register", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))



