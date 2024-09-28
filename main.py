import os
import requests
import argparse
import json

def update_fork(repo, headers):
    print(f"\nUpdating fork: {repo['full_name']}")
    
    # Get the default branch
    default_branch = repo['default_branch']
    
    # Merge upstream
    merge_url = f"https://api.github.com/repos/{repo['full_name']}/merge-upstream"
    merge_data = {"branch": default_branch}
    
    try:
        response = requests.post(merge_url, headers=headers, json=merge_data)
        response.raise_for_status()
        
        result = response.json()
        if 'message' in result:
            if result['message'] == 'Not Found':
                print(f"Error: Repository not found or no access. Please check your permissions.")
            elif result['message'] == 'Conflict':
                print(f"The fork is already up to date or there are conflicts.")
            else:
                print(f"Message from GitHub: {result['message']}")
        elif 'merge_type' in result:
            if result['merge_type'] == 'none':
                print("No new commits to merge. The fork is up to date.")
            else:
                print(f"Successfully updated. Merge type: {result['merge_type']}")
                print(f"New head commit: {result['commit']['sha']}")
        else:
            print(f"Unexpected response structure. Full response: {json.dumps(result, indent=2)}")
    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {str(e)}")
    except json.JSONDecodeError:
        print(f"Error decoding JSON response. Status code: {response.status_code}")
        print(f"Response text: {response.text}")

def get_forks(username, headers):
    forks = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{username}/repos?page={page}&per_page=100"
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            repos = response.json()
            if not repos:
                break
            forks.extend([repo for repo in repos if repo['fork']])
            page += 1
        except requests.exceptions.RequestException as e:
            print(f"Error fetching repositories: {str(e)}")
            return []
    return forks

def main(github_token, username):
    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    forks = get_forks(username, headers)
    print(f"Found {len(forks)} forked repositories.")
    
    for fork in forks:
        update_fork(fork, headers)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update all forked GitHub repositories using the merge-upstream API")
    parser.add_argument("github_token", help="GitHub Personal Access Token")
    parser.add_argument("username", help="GitHub username")
    args = parser.parse_args()

    main(args.github_token, args.username)
