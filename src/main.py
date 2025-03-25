import os
from dotenv import load_dotenv
import requests

def main():
    # Load environment variables
    load_dotenv()
    
    # Get GitHub token
    github_token = os.getenv('GITHUB_TOKEN')
    
    # Example: Get repository information
    repo_url = "https://api.github.com/repos/DRaff-BN/HelloWorld"
    headers = {"Authorization": f"token {github_token}"}
    
    try:
        response = requests.get(repo_url, headers=headers)
        if response.status_code == 200:
            repo_info = response.json()
            print(f"Repository: {repo_info['name']}")
            print(f"Description: {repo_info['description']}")
            print(f"Stars: {repo_info['stargazers_count']}")
        else:
            print(f"Error: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main() 