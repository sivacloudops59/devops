import sys
import requests
import json
import os
import urllib3

# Usage: python create_branch.py <github_token> <repo_name> <new_branch_name> <base_branch>

if len(sys.argv) != 5:
    print("Usage: python create_branch.py <github_token> <repo_name> <new_branch_name> <base_branch>")
    sys.exit(1)

token = sys.argv[1]
repo_name = sys.argv[2]
new_branch = sys.argv[3]
base_branch = sys.argv[4]

username_url = "https://github.com/sivacloudops59"
headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github+json"
}

# Step 1: Get username
response = requests.get(username_url, headers=headers)
if response.status_code != 200:
    print(" Failed to fetch user info.")
    sys.exit(1)
username = response.json()["login"]

# Step 2: Get base branch SHA
ref_url = f"https://api.github.com/repos/{username}/{repo_name}/git/ref/heads/{base_branch}"
response = requests.get(ref_url, headers=headers)
if response.status_code != 200:
    print(f" Failed to fetch base branch '{base_branch}'")
    print(response.json())
    sys.exit(1)

sha = response.json()["object"]["sha"]

# Step 3: Create new branch
create_ref_url = f"https://api.github.com/repos/{username}/{repo_name}/git/refs"
data = {
    "ref": f"refs/heads/{new_branch}",
    "sha": sha
}

response = requests.post(create_ref_url, headers=headers, json=data)
if response.status_code == 201:
    print(f"Branch '{new_branch}' created from '{base_branch}'")
else:
    print(f" Failed to create branch. Status: {response.status_code}")
    print(response.json())
