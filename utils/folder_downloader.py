import requests
from pathlib import Path

from utils.print_message import print_message
from constants import Message

def download_github_folder(folder_url, download_path=None, branch='main'):
    """
    Downloads a specific folder from a GitHub repository given the folder URL.
    Creates a new folder in the download_path and downloads all contents into that folder.

    Parameters:
    folder_url (str): The URL of the folder in the GitHub repository.
    download_path (str, optional): The directory to download the folder into.
                                   Defaults to the current working directory.
    branch (str, optional): The branch to download from. Defaults to 'main'.
    """
    # Remove trailing slash if present
    folder_url = folder_url.rstrip('/')

    # Extract the owner, repo name, and folder path from the URL
    try:
        parts = folder_url.split('/')
        owner = parts[3]
        repo_name = parts[4]
        folder_path = '/'.join(parts[7:])
    except IndexError:
        print_message("[ERROR] Unable to parse folder URL.", Message.ERROR)
        return

    # Create a new folder in the download path
    new_folder_name = Path(folder_path).name
    new_folder_path = Path(download_path) / new_folder_name

    if new_folder_path.exists():
        print_message(f"[WARNING] Folder '{new_folder_name}' already exists in {download_path}.", Message.WARNING)
    else:
        new_folder_path.mkdir(parents=True, exist_ok=True)

    # GitHub API URL for listing the contents of the folder
    api_url = f'https://api.github.com/repos/{owner}/{repo_name}/contents/{folder_path}?ref={branch}'

    try:
        response = requests.get(api_url)
        response.raise_for_status()

        folder_contents = response.json()

        if isinstance(folder_contents, dict) and 'message' in folder_contents:
            print_message(f"[ERROR]: {folder_contents['message']}", Message.ERROR)
            return

        # Iterate through the folder contents
        for item in folder_contents:
            if item['type'] == 'file':
                file_url = item['download_url']
                relative_path = Path(item['path']).relative_to(folder_path)
                file_path = new_folder_path / relative_path
                file_path.parent.mkdir(parents=True, exist_ok=True)

                file_response = requests.get(file_url)
                file_response.raise_for_status()

                # Write the file to the local filesystem
                with open(file_path, 'wb') as file:
                    file.write(file_response.content)

            elif item['type'] == 'dir':
                # Recur for subfolders
                subfolder_url = f'https://github.com/{owner}/{repo_name}/tree/{branch}/{item["path"]}'
                download_github_folder(subfolder_url, new_folder_path, branch)

        print_message(f'[SUCCESS] Folder {folder_path} downloaded to {new_folder_path}', Message.SUCCESS)
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print_message("[ERROR] The specified folder or repository was not found.", Message.ERROR)
        else:
            print_message(f"[ERROR] Error accessing the GitHub API: {e}", Message.ERROR)
    except requests.exceptions.RequestException as e:
        print_message(f'[ERROR] Error accessing the GitHub API: {e}', Message.ERROR)
    except OSError as e:
        print_message(f'[ERROR] Error writing files to the filesystem: {e}', Message.ERROR)
