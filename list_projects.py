import requests as r
username = "bakare-rasheed"
url = f'https://api.github.com/users/{username}/repos'
response = r.get(url)
bakare = response.json()
for repos in bakare:
    print(repos['html_url'])