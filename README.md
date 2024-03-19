# NetBox Floorplan Plugin

<img src="https://github.com/netboxlabs/netbox-floorplan-plugin/workflows/tests/badge.svg" alt="Tests"/>

Forked from https://github.com/tbotnz/netbox_floorplan

## Demo
![demo](/media/demo.gif)

## Summary
A netbox plugin providing floorplan mapping capability for locations and sites

- provides graphical ability to draw racks & unracked devices on a floorplan
- support for metadata such as labels, areas, walls, coloring
- floorplan object mapped to sites or locations and click through rack/devices
- keyboard controls supported
- export to svg

## Compatibility

|             |           |
|-------------|-----------|
| NetBox 3.5  | >= 0.3.2 |
| NetBox 3.6  | >= 0.3.2 |

## Installing

The plugin is available as a Python package in pypi and can be installed with pip  

```
pip install netbox-floorplan-plugin
```
Enable the plugin in /opt/netbox/netbox/netbox/configuration.py:
```
PLUGINS = ['netbox_floorplan']
```
Update the database:
```
python manage.py migrate netbox_floorplan
```

Restart NetBox and add `netbox-floorplan-plugin` to your local_requirements.txt

See [NetBox Documentation](https://docs.netbox.dev/en/stable/plugins/#installing-plugins) for details


## Mentions

Forked from https://github.com/tbotnz/netbox_floorplan

Special thanks to Ziply Fiber network automation team for helping originally helping to conceive this during the NANOG hackathon

## Release process

Update `netbox_floorplan/version.py` with a new version number, create a new Github release with the same number, the pypi publish workflow will run.
