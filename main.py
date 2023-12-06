from utils import Utils
from acrimageimporter import ACRImageImporter
from trivy import ContainerImageScanner


class Application:
    def __init__(self):
        args = Utils.get_command_line_arguments()
        self.subscription_id = args.subscription_id
        self.resource_group = args.resource_group
        self.acr_name = args.acr_name
        self.source_image_uri = args.source_image_uri
        self.target_tags = args.target_tags.split()

    def run(self):
        ContainerImageScanner.scan_image(self.source_image_uri)

        importer = ACRImageImporter(
            subscription_id=self.subscription_id,
            resource_group=self.resource_group,
            acr_name=self.acr_name
        )
        importer.import_image(self.source_image_uri, self.target_tags)


if __name__ == "__main__":
    app = Application()
    app.run()
