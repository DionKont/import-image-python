import logging
from azure.identity import DefaultAzureCredential
from azure.mgmt.containerregistry import ContainerRegistryManagementClient
from azure.mgmt.containerregistry.models import ImportImageParameters, ImportSource
from azure.core.exceptions import HttpResponseError


class ACRImageImporter:
    def __init__(self, subscription_id, resource_group, acr_name):
        self.subscription_id = subscription_id
        self.resource_group = resource_group
        self.acr_name = acr_name
        self.client = ContainerRegistryManagementClient(
            credential=DefaultAzureCredential(),
            subscription_id=subscription_id
        )
        logging.basicConfig(level=logging.INFO)

    def import_image(self, source_image_uri, target_tags):
        try:
            import_params = ImportImageParameters(
                source=ImportSource(source_image=source_image_uri, registry_uri=""),
                target_tags=target_tags,
                mode="Force"  # overwriting if already exists
            )
            result = self.client.registries.begin_import_image(
                self.resource_group,
                self.acr_name,
                parameters=import_params
            )
            result.wait()  # Wait for the import to complete
            logging.info(f"Imported image: {source_image_uri} to {self.acr_name} with tags {target_tags}")
        except HttpResponseError as e:
            logging.error(f"Failed to import image: {e.message}")
        except Exception as e:
            logging.error(f"An error occurred: {e}")
