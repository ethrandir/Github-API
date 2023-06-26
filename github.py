import requests

class Github:
    def __init__(self):
        self.api_url = 'https://api.github.com'
        self.token = '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'

    def getUser(self,username):
        response = requests.get(self.api_url+'/users/'+ username)
        return response.json()

    def getRepository(self,username):
        response = requests.get(self.api_url+'/users/'+username+'/repos')
        return response.json()

    def createRepository(self,name):
        response = requests.post(self.api_url + '/user/repos?access_token=' + self.token, json={
            "name": name,
            "description": "This is your first repository",
            "homepage": "https://github.com",
            "private": False,
            "has_issueas": True,
            "has_projects": True,
            "has_wiki": True
        })
        return response.json()

github = Github()

while True:
    secim = input('1- Find User\n2- Get Repository\n3- Create Repository\n4- Exit\nChoice: ')
    if secim == '4':
        break
    elif secim =='1':
        username = input('Username: ')
        result = github.getUser(username)
        print(f"Name: {result['name']}\nPublic Repos: {result['public_repos']}\nFollowers: {result['followers']}")
    elif secim =='2':
        username = input('Username: ')
        result = github.getRepository(username)
        for repo in result:
            print(repo['name'])
    elif secim =='3':
        name = input('Repository Name: ')
        result = github.createRepository(name)
        print(result)
    else:
        print('Wrong Choice')