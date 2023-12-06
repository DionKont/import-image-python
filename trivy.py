import subprocess
import sys
from utils import Utils


class ContainerImageScanner:
    @staticmethod
    def scan_image(image_uri):
        try:
            # Trivy Latest windows release download
            trivy_url = "https://github.com/aquasecurity/trivy/releases/download/v0.47.0/trivy_0.47.0_windows-64bit.zip"
            trivy_zip_path = "trivy.zip"
            Utils.download_file(trivy_url, trivy_zip_path)

            # Extract Trivy
            Utils.extract_zip(trivy_zip_path, "./trivy")
            trivy_exe_path = "./trivy/trivy.exe"

            # Run Trivy scan
            print(f"Scanning container image for vulnerabilities: {image_uri}")
            subprocess.run([trivy_exe_path, "image", "--severity", "HIGH,CRITICAL", "--no-progress", image_uri], check=True)
            print("Scan completed successfully. No high or critical vulnerabilities found.")
        except subprocess.CalledProcessError:
            print("High or critical vulnerabilities found in the image.")
            sys.exit(1)
        except Exception as e:
            print(f"Error during scanning process: {e}")
            sys.exit(1)
