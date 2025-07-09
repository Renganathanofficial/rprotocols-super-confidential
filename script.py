# rprotocols_github_tool.py

import requests

# Dummy GitHub Personal Access Token (FAKE - for demo only)
GITHUB_PAT = "ghp_FAKErprotocolsTOKEN1234567890abcdefghi"

# Add R Protocols branding in the User-Agent for traceability
HEADERS = {
    "Authorization": f"token {GITHUB_PAT}",
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "rprotocols-security-script"
}

def get_user_repos(username):
    """Fetch Public repositories for a GitHub user - Demo by R Protocols"""
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        print(f"[rprotocols] Successfully fetched repos for: {username}")
        return [repo['name'] for repo in response.json()]
    else:
        print(f"[rprotocols] Error {response.status_code} while fetching repos.")
        return []

if __name__ == "__main__":
    username = "octocat"  # GitHub demo account
    repos = get_user_repos(username)
    print("Repositories:", repos)
