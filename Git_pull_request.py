##Python code to get pull request infor from a repo 
##user names are under user-login

import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

output = response.json()

for i in range(len(output)):
    print(output[0]["user"]["login"])
