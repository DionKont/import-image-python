import argparse
import requests
import zipfile
import sys

class Utils:
    @staticmethod
    def get_command_line_arguments():
        parser = argparse.ArgumentParser(description='ACR Image Importer Utility')
        parser.add_argument('--subscription_id', required=True, help='Azure Subscription ID')
        parser.add_argument('--resource_group', required=True, help='Azure Resource Group Name')
        parser.add_argument('--acr_name', required=True, help='Azure Container Registry Name')
        parser.add_argument('--source_image_uri', default='docker.io/library/ubuntu:latest', help='Source Image URI')
        parser.add_argument('--target_tags', default='ubuntu:latest', help='Target Tags for the ACR Image', nargs='+')

        return parser.parse_args()

    @staticmethod
    def download_file(url, file_path):
        try:
            response = requests.get(url)
            with open(file_path, 'wb') as file:
                file.write(response.content)
        except requests.RequestException as e:
            print(f"Failed to download file: {e}")
            sys.exit(1)

    @staticmethod
    def extract_zip(zip_path, extract_to):
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_to)
        except zipfile.BadZipFile as e:
            print(f"Failed to extract file: {e}")
            sys.exit(1)
