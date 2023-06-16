# LFB Verjüngungszustands- und Wildeinfluss Monitoring

## Installation from Repository

QGIS: ``Plugins`` -> ``Manage and Install Plugins...`` -> ``Settings``

In the **Plugin Repositories** section click `+Add`.

- Name: `LFB - VWM`
- URL: `https://raw.githubusercontent.com/b-lack/lfb-regeneration_wildlife_impact_monitoring/main/plugins.xml`

Check: "Allow experimental plugins"

Confirm by clicking `OK`

QGIS: ``Plugins`` -> ``Manage and Install Plugins...`` -> ``ALL``

Search for `LFB` and select `LFB Verjüngungszustands- und Wildeinfluss Monitoring`

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

Make sure that ``Lfb Regeneration and Wildlife Impact Monitoring`` is selected.


## Release

```bash
$ git log --pretty="- %s" > CHANGELOG.md
```

## Generate Changelog

```bash
$ git log --pretty="- %s" > CHANGELOG.md
```

## Tests

![test workflow](https://github.com/b-lack/lfb-regeneration_wildlife_impact_monitoring/actions/workflows/run-all-tests.yml/badge.svg)

Run pytest in the root directory of the project.

```bash
$ pytest
```

## 

pg_dump --schema-only lfb > schema.sql