import requests
import time
url='http://127.0.0.1:8001/users'
data={"name":"Ana","email":"ana@email.com","age":25}
for i in range(10):
    try:
        resp = requests.post(url, json=data, timeout=2)
        print(resp.status_code)
        print(resp.json())
        break
    except Exception as e:
        print('retry', i, e)
        time.sleep(0.5)
