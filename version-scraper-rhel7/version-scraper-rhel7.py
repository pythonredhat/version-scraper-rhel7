import requests
from bs4 import BeautifulSoup
import json

url = 'https://access.redhat.com/articles/3078'
rhelpage = requests.get(url)

soup = BeautifulSoup(rhelpage.content, 'html.parser')

rhel7table = soup.find_all('table')[1]

rhel7_latest_version = rhel7table.find_all('td')[0].get_text()
rhel7_latest_kernel = rhel7table.find_all('td')[3].get_text()

rhel7_latest_version_and_kernel = f"{rhel7_latest_version}, Kernel {rhel7_latest_kernel}"

print(rhel7_latest_version_and_kernel)


#part 2: get the current version in the web api
rhel7_url= 'http://localhost:8000/api/v1/version_lord/8'

response = requests.get(url=rhel7_url)

json_data = json.loads(response.text)

print(json_data)

print(json_data['software'])

if json_data['current_version'] == rhel7_latest_version_and_kernel:
    print("All good in the hood!")
else:
    print("Version Lord is not up to date with RHEL site")
    data = {'current_version': rhel7_latest_version_and_kernel, 'software': 'Red Hat Enterprise Linux 7'}
    payload = requests.put(url=rhel7_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
    print (payload.status_code)
    print(payload.content)
