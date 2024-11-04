from netbox.plugins import PluginConfig
from .version import version_semver


class FloorplanConfig(PluginConfig):

    name = "netbox_floorplan"
    verbose_name = "Netbox Floorplan"
    description = ""
    version = version_semver()
    base_url = "floorplan"
    min_version = "4.0.2"
    max_version = "4.0.11"


config = FloorplanConfig
