import requests
import json

def get_deployments(username, token):
    get_url = "https://api.github.com/repos/UserName/RepoName/deployments"

    return requests.get(get_url, auth=(username, token))

def inactive_deployment(username, token, deployment_id):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/vnd.github.ant-man-preview+json"
    }
    
    data = json.dumps({"state": "inactive"})
    
    post_url = f"https://api.github.com/repos/UserName/RepoName/deployments/{deployment_id}/statuses"
    return requests.post(post_url, auth=(username, token), headers=headers, data=data)

def delete_deployment(username, token, deployment_id):
    inactivate_response = inactive_deployment(username, token, deployment_id)
    
    if inactivate_response.status_code == 201:
        print(f"Deployment {deployment_id} marked as inactive.")
        
        delete_url = f"https://api.github.com/repos/UserName/RepoName/deployments/{deployment_id}"
        return requests.delete(delete_url, auth=(username, token))
    else:
        print(f"Failed to update deployment {deployment_id}. Status Code:", inactivate_response.status_code)
        return None

def delete_all_deployments(github_username, github_token):
    response = get_deployments(github_username, github_token)
    
    if response.status_code == 200:
        deployments = response.json()
        deployment_ids = [deployment['id'] for deployment in deployments]
        print("Deployment IDs:", deployment_ids)

        if len(deployment_ids) == 0:
            return False
        
        for id in deployment_ids:
            delete_response = delete_deployment(github_username, github_token, id)

            if delete_response.status_code in [204, 200]:
                print(f"Deployment {id} successfully deleted.")
            else:
                print(f"Failed to delete deployment {id}. Status Code:", delete_response.status_code)
                
        return True
    else:
        print("Failed to retrieve deployments. Status Code:", response.status_code)
        return False

while delete_all_deployments(github_username = 'UserNamme', 
                       github_token = 'Token'):
    pass
