import sys
import requests
import os
import json

# Usage: python create_repo.py <github_token> <repo_name>

if len(sys.argv) != 3:
    print("Usage: python create_repo.py <github_token> <repo_name>")
    sys.exit(1)

github_token = sys.argv[1]
repo_name = sys.argv[2]

url = f"https://github.com/sivacloudops59"
headers = {
    "Authorization": f'Bearer {github_token}',
    "Accept": "application/vnd.github+json"
}
data = {
    "name": repo_name,
    "private": False  # Set to True if you want the repo to be private
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 201:
        print(f" Repository '{repo_name}' created successfully.")
else:
    print(f" Failed to create repository. Status Code: {response.status_code}")
    print("Response:", response.json())


