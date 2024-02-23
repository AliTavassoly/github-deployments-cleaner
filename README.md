# GitHub Deployment Cleaner

This Python script automates the process of clearing deployments in a GitHub repository. It marks deployments as inactive and then deletes them, making it an efficient tool for managing deployment history.

## Features

- Retrieves a list of all deployments in a specified GitHub repository.
- Marks each deployment as inactive.
- Deletes all inactive deployments.
- Repeats the process until all deployments are cleared.

## Requirements

- Python 3
- `requests` library

## Setup

1. Ensure Python 3 is installed on your system.
2. Install the `requests` library using pip:

## Usage

1. Clone or download this repository to your local machine.
2. Open the script and replace `'UserName'`, `'RepoName'`, `'UserNamme'`, and `'Token'` with your GitHub username, repository name, and [personal access token](https://github.com/settings/tokens) respectively.
3. Run the script:


## Important Notes

- Use this script responsibly as it will permanently delete deployment records from your repository.
- Ensure you have the necessary permissions to modify deployment information in the target repository.
- Your personal access token should have the appropriate scopes for deployment management.

## Disclaimer

This script is provided "as is", without warranty of any kind. Use it at your own risk.
