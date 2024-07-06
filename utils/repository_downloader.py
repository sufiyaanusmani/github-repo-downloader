import zipfile
import requests
from zipfile import ZipFile
from pathlib import Path
from io import BytesIO

from utils.print_message import print_message
from constants import Message

def download_github_repository(repo_url, download_path=None):
    """
    Downloads a GitHub repository as a zip file and extracts it.

    Parameters:
    repo_url (str): The URL of the GitHub repository.
    download_path (str, optional): The directory to download and extract the repository into.
                                   Defaults to the current working directory.
    """
    # Extract the owner and repository name from the URL
    parts = repo_url.rstrip('/').split('/')
    owner, repo_name = parts[-2], parts[-1]

    # Construct the URL for downloading the zip archive
    zip_url = f'https://github.com/{owner}/{repo_name}/archive/refs/heads/main.zip'

    # Determine the download path
    if download_path is None:
        download_path = Path.cwd()
    else:
        download_path = Path(download_path)

    # Create the download path if it doesn't exist
    download_path.mkdir(parents=True, exist_ok=True)

    try:
        # Download the zip file
        print_message(f'[INFO] Downloading {repo_name} from {zip_url}...', Message.INFO)
        response = requests.get(zip_url)
        response.raise_for_status()

        # Extract the zip file
        with ZipFile(BytesIO(response.content)) as zip_file:
            zip_file.extractall(download_path)

        print_message(f'[SUCCESS] {repo_name} downloaded and extracted to {download_path}', Message.SUCCESS)
    except requests.exceptions.RequestException as e:
        print_message(f'[ERROR] Error downloading the repository: {e}', Message.ERROR)
    except zipfile.BadZipFile:
        print_message('[ERROR] The downloaded file is not a valid zip file.', Message.ERROR)
