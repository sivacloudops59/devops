import sys
import requests
import json

# Usage: python create_branch.py <github_token> <repo_name> <new_branch_name> <base_branch>

if len(sys.argv) != 5:
    print("Usage: python create_branch.py <github_token> <repo_name> <new_branch_name> <base_branch>")
    sys.exit(1)

github_token = sys.argv[1]
repo_name = sys.argv[2]
new_branch = sys.argv[3]
base_branch = sys.argv[4]

headers = {
    "Authorization": f"token {github_token}",
    "Accept": "application/vnd.github+json"
}

# Step 1: Get username from token
user_resp = requests.get("https://api.github.com/user", headers=headers)
if user_resp.status_code != 200:
    print(f"Failed to fetch user info. Status Code: {user_resp.status_code}")
    print(user_resp.text)
    sys.exit(1)
username = user_resp.json()["login"]

# Step 2: Get base branch SHA
ref_url = f"https://api.github.com/repos/{username}/{repo_name}/git/ref/heads/{base_branch}"
ref_resp = requests.get(ref_url, headers=headers)
if ref_resp.status_code != 200:
    print(f"Failed to fetch base branch '{base_branch}'. Status Code: {ref_resp.status_code}")
    print(ref_resp.text)
    sys.exit(1)

sha = ref_resp.json()["object"]["sha"]

# Step 3: Create new branch
create_ref_url = f"https://api.github.com/repos/{username}/{repo_name}/git/refs"
data = {
    "ref": f"refs/heads/{new_branch}",
    "sha": sha
}
create_resp = requests.post(create_ref_url, headers=headers, json=data)

if create_resp.status_code == 201:
    print(f"Branch '{new_branch}' created from '{base_branch}'")
else:
    print(f"Failed to create branch. Status Code: {create_resp.status_code}")
    print(create_resp.text)
