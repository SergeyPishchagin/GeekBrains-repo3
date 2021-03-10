import json
import requests


username = 'SergeyPishchagin'
link = requests.get('https://api.github.com/users/'+username+'/repos')
result = link.json()

with open('git_repos.json', 'w') as f:
    f.write(json.dumps(result))
for repos in link.json():
    print(repos['html_url'])
    
