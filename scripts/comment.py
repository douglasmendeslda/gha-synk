import requests
import sys

def comment_on_pr(repo_token, pr_number, message):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues/{pr_number}/comments"
    headers = {
        "Authorization": f"token {repo_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "body": message
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        print("Comment successfully created.")
    else:
        print(f"Failed to create comment: {response.status_code}")
        print(response.json())

if __name__ == "__main__":
    repo_owner = "your-repo-owner"  # Replace with your repo owner
    repo_name = "your-repo-name"  # Replace with your repo name
    repo_token = sys.argv[1]
    pr_number = sys.argv[2]
    message = "hello world"
    comment_on_pr(repo_token, pr_number, message)
