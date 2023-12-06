# Azure Container Registry Image Importer

This project automates the process of importing a Docker image into an Azure Container Registry (ACR) using Python. 
It includes a container image scanning step to ensure no images with high or critical vulnerabilities are imported into 
the ACR. The project demonstrates the use of Azure SDK with Python.

## Requirements

- Python 3.x
- An Azure account and an active subscription.
- Azure CLI installed or Azure credentials configured for programmatic access.
- An accessible URI with the Source Image
- An accessible Azure Container Registry
- Access rights to manage Azure Container Registry resources (**AcrPush** Role).
- Internet access for downloading the Trivy container scanner.



## Installation

1. **Clone this Repository**
2. **Create new Virtual Environment** (optional)
3. **Install Required Python Packages**: <br>```pip install -r requirements.txt```

## Usage

The script can be run from the command line by providing necessary Azure parameters. It scans the specified container 
image for vulnerabilities before importing it into the Azure Container Registry.

### Command-Line Arguments:

- `--subscription_id`: Your Azure subscription ID (required).
- `--resource_group`: The name of your Azure resource group (required).
- `--acr_name`: The name of your Azure Container Registry (required).
- `--source_image_uri`: The URI of the source Docker image (optional, default: 'docker.io/library/ubuntu:latest').
- `--target_tags`: Target tags for the imported image in ACR (optional, default: 'ubuntu:latest').

### Example:

Run the script with the following command:

```bash
python main.py --subscription_id "your_subscription_id" --resource_group "your_resource_group" --acr_name "your_acr_name"
```
## Project Structure
- `utils.py`: Utility class for handling command-line arguments, downloading files from the web and extracting zip files.
- `acrimageimporter.py`: Contains the ACRImageImporter class for ACR operations, including image import and scanning for vulnerabilities
- `main.py`: The main application class that orchestrates the image import process.
- `trivy.py`: Responsible for scanning the image files for vulnerabilities.
- `requirements.txt`: Lists all the Python dependencies.

## Contributing
N/A

## License
N/a