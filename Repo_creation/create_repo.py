import sys
import requests
import json

# Usage: python create_repo.py <github_token> <repo_name>

if len(sys.argv) != 3:
    print("Usage: python create_repo.py <github_token> <repo_name>")
    sys.exit(1)

github_token = sys.argv[1]
repo_name = sys.argv[2]

# Correct API endpoint for user repo creation
url = "https://api.github.com/user/repos"

headers = {
    "Authorization": f"Bearer {github_token}",
    "Accept": "application/vnd.github+json"
}

data = {
    "name": repo_name,
    "private": False,  # Change to True for a private repo
    "auto_init": True
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 201:
    print(f" Repository '{repo_name}' created successfully.")
elif response.status_code == 422 and "name already exists" in response.text:
    print(f"Repository '{repo_name}' already exists. Skipping creation.")
    sys.exit(0)
else:
    print(f" Failed to create repository. Status Code: {response.status_code}")
    try:
        print("Response:", response.json())
    except Exception:
        print("Response (non-JSON):", response.text)
    sys.exit(1)
