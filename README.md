# Update Forks Script

This Python script updates all forked GitHub repositories by merging upstream changes.

## Prerequisites

- Python 3.x
- `requests` library (will be installed automatically in the workflow)

## Usage

### Running the Script Locally

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   
   pip install requests
   
   python main.py <github_token> <github_username>
