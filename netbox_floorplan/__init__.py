from netbox.plugins import PluginConfig


class FloorplanConfig(PluginConfig):

    name = "netbox_floorplan"
    verbose_name = "Netbox Floorplan"
    description = ""
    version = "0.4.0"
    base_url = "floorplan"
    min_version = "4.0.2"
    max_version = "4.1.3"


config = FloorplanConfig
