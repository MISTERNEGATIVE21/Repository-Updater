# Github Repository Updater

This Python script updates all forked GitHub repositories by merging upstream changes.

## Prerequisites

- Python 3.x
- `requests` library (will be installed automatically in the workflow)

## Creating a GitHub Personal Access Token

To run this script, you'll need to create a GitHub Personal Access Token with appropriate permissions. Follow these steps:

1. **Sign in to GitHub**: Log in to your GitHub account.

2. **Navigate to Developer Settings**:
   - Click on your profile picture in the top-right corner.
   - Go to **Settings**.
   - In the left sidebar, scroll down and click on **Developer settings**.

3. **Create a New Token**:
   - Click on **Personal access tokens**.
   - Click on **Tokens (classic)**, then **Generate new token**.
   - Enter a note for the token (e.g., "Update Forks Script").
   - Set the expiration period as per your needs (recommended: no expiration for long-term scripts).
   - **Select Scopes**: 
     - Check the box for **repo** (this gives full control of private repositories) or just the scopes you need, such as **repo:public** if you only work with public repositories.
   - Click **Generate token**.

4. **Copy the Token**: Make sure to copy the token as you won’t be able to see it again.
5. **Fork this Repo**: Make a fork of this repo.
6.  **Navigate to Github Actions**: On the left window see a Script click there and input your credentials and hit run workflow.

## Usage
![image](https://github.com/user-attachments/assets/1200b449-71c5-4687-a3a7-000ad10a0abe)


### Running the Script Locally

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   
   pip install requests
   
   python main.py <github_token> <github_username>

   
### If it Helps You please Fork it and Give Stars Thankyou .
