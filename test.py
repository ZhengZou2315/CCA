import requests
import json

url = 'https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp2-autograder-2022-spring'

payload = {
		'ip_address1':  '54.213.180.98', 
		'ip_address2':  '18.236.136.253',
		'load_balancer' :  'loadbalancer1-382102624.us-west-2.elb.amazonaws.com',
		'submitterEmail':  'zheng.zou3459@gmail.com',
		'secret': 'PhFXsvTssW8Z9fJb'
		}

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)