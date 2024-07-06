import argparse

from utils.folder_downloader import download_github_folder
from utils.repository_downloader import download_github_repository

def main():
    parser = argparse.ArgumentParser(description='Download GitHub repositories or folders.')
    parser.add_argument('--url', type=str, required=True, help='GitHub URL to download from.')
    parser.add_argument('--folder', action='store_true', help='Download a specific folder from the repository.')
    parser.add_argument('--repo', action='store_true', help='Download the entire repository.')
    parser.add_argument('--path', type=str, default='.', help='Directory to download the content into.')
    parser.add_argument('--branch', type=str, default='main', help='Branch to download from. Defaults to "main".')
    args = parser.parse_args()

    if args.folder == args.repo:
        print("Error: You must specify either --folder or --repo, but not both.")
        return

    if args.folder:
        download_github_folder(args.url)
    elif args.repo:
        download_github_repository(args.url)

if __name__ == '__main__':
    main()
