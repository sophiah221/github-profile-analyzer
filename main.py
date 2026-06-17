import requests

username = input("GitHub-Nutzer: ")
url = f"https://api.github.com/users/{username}"
repos_url = f"https://api.github.com/users/{username}/repos"
response = requests.get(url)
data = response.json()

repos_response  = requests.get(repos_url)
repos = repos_response.json()
if response.status_code != 200:
    print("Fehler: Benutzer nicht gefunden")
    exit()

# Sprachen aufzählen
languages = {}
for repo in repos:
    language = repo["language"]
    if language:
        languages[language] = languages.get(language, 0) +1

#Ausgabe
print(f"---Github Profil von {username}:---")
print(f"Name: {data["name"]}")
print(f"Followers: {data["followers"]}")
print(f"Öffentliche Repositories: {data["public_repos"]}")
print(f"Folgt: {data["following"]}")
print()
if data["public_repos"] >0:
    print("---Repositories:---")
    for repo in repos:
        print(f"- {repo["name"]}")
    
    print()
    if data["public_repos"] >5:
        print("Top 5 Repositories nach Sternen:")
        for repo in repos[:5]:
            print(f"- {repo["name"]} ({repo["stargazers_count"]} Sterne)")
    print()
    if data["public_repos"] >0:
        print("Verwendete Sprachen:")
        for language, count in languages.items():
            if count == 1:
                print(f"{language}: {count} Repository")
            else:
                print(f"{language}: {count} Repositories")