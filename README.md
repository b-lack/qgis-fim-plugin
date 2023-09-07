# LFB Verjüngungszustands- und Wildeinfluss Monitoring


## Requirements

If you do not have the python module ``jsonschema`` installed, you will get an error message when you try to start the plugin.


In this case go to ``Manage and Install Plugins...`` -> ``Python Console``

In the console type

```py
import subprocess
```
and 

```py
subprocess.check_call(['python', '-m', 'pip', 'install', 'jsonschema'])
```

Restart QGIS

## Installation from Repository

QGIS: ``Plugins`` -> ``Manage and Install Plugins...`` -> ``Settings``

In the **Plugin Repositories** section click `+Add`.

- Name: `LFB - VWM`
- URL: `https://raw.githubusercontent.com/b-lack/qgis-fim-plugin/main/plugins.xml`

Check: "Allow experimental plugins"

Confirm by clicking `OK`

Restart QGIS

QGIS: ``Plugins`` -> ``Manage and Install Plugins...`` -> ``ALL``

Search for `FIM` and select `FIM - Forest Inventory and Monitoring`

Confirm by clicking `Install Plugin`

Done: 

## Development Installation

For the installation from the repository ``pb_tool`` must be installed. For this follow the instructions in [pb_tool.cfg](pb_tool.cfg).

After making sure you have installed pb_tool, you can deploy the cloned plugin to your QGIS plugins folder:

```bash
$ pb_tool deploy
```
The plugin will be copied to your QGIS plugins folder.

QGIS: ``Settings`` -> ``User Profiles`` -> ``Open Active Profile Folder`` -> ``python`` -> ``plugins``

At this point you should restart QGIS.

### Activate Plugin

QGIS: ``Plugins`` -> ``Manage and Install Plugins...`` -> ``Installed``

Make sure that ``FIM`` is selected.


## Release

```bash
$ git log --pretty="- %s" > CHANGELOG.md
```

## Generate Changelog

```bash
$ git log --pretty="- %s" > CHANGELOG.md
```

## 

pg_dump --schema-only lfb > schema.sql