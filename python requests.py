import requests
import json

# passing payloads in url
payload = {"key1": "value1", "key2": ["value2", "value3"]}
# r = requests.get("https://httpbin.org/get", params = payload)
# print(r.url)


# response content

# r = requests.get("https://api.github.com/events")
#print(r.text)
# print(r.encoding)
# r.encoding = "ISO-8859-1"
#print(r.text)

# Binary response content
# print(r.content)


# JSON Response Content

r = requests.get("https://api.publicapis.org/entries")
# print(r.json())
#print(r.status_code)


# Raw Response Content

r = requests.get('https://api.github.com/events', stream=True)
r.raw
# print(r.raw.read(10))


# Custom Headers

url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}

r = requests.get(url, headers=headers)


# More complicated POST requests

payload = {'key1':'value1', 'key2':'value2'}
r = requests.post("https://httpbin.org/post", data=payload)
# print(r.text)

payload_tuples =  [('key1', 'value1'), ('key1', 'value2')]
r1 = requests.post('https://httpbin.org/post', data=payload_tuples)

payload_dict = {'key1': ['value1', 'value2']}
r2 = requests.post('https://httpbin.org/post', data = payload_dict)

# print(r1.text)
# print(r2.text)

# print(r1.text == r2.text)

url = 'https://api.github.com/some/endpoint/post'
payload = {'some':'data'}

r = requests.post(url, json=payload)
# print(r.json)


# POST a Multipart-Encoded File
# url = 'https://httpbin.org/post'
# files = {'file': open('report.xls', 'rb')}

# r = requests.post(url, files=files)
# print(r.text)


# Response Status Codes
r = requests.get("https://httpbin.org/get")
# print(r.status_code)
# print(r.status_code == requests.codes.ok)


bad_r = requests.get("https://httpbin.org/status/404")
# print(bad_r.status_code)

# print(bad_r.raise_for_status())

#print(r.raise_for_status())


# Response Headers
# print(r.headers)

# print(r.headers['Content-Type'])

# print(r.headers.get('content-type'))


# Cookies
url = 'http://example.com/some/cookie/setting/url'
r = requests.get(url)

# (r.cookies['example_cookie_name'])

url = 'https://httpbin.org/cookies'
cookies = dict(cookies_are='working')

r = requests.get(url, cookies=cookies)
# print(r.text)


jar = requests.cookies.RequestsCookieJar()
jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
url = 'https://httpbin.org/cookies'
r = requests.get(url, cookies=jar)
# print(r.text)


# Redirection and History
r = requests.get('http://github.com/')

# print(r.url)
# print(r.status_code)
# print(r.history)

r = requests.get('http://github.com/', allow_redirects=True)
# print(r.status_code)
# print(r.history)


# Timeouts

print(requests.get("https://github.com/", timeout = 0.001))


