from constants import Directory
from utils.folder_downloader import download_github_folder

if __name__ == "__main__":
    folder_url = "https://github.com/sufiyaanusmani/nodejs-course/tree/main/9_dynamic_routes_and_advanced_models"
    download_path = Directory.DATA_DIR
    download_github_folder(folder_url, download_path)
