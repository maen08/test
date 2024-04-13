import requests

def get_repo_info(repo_url):
    parts = repo_url.split('/')
    owner = parts[-2]
    repo = parts[-1]

    pass
