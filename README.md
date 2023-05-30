# LFB Verjüngungszustands- und Wildeinfluss Monitoring



## Development Installation



```bash
$ pb_tool deploy
```
The plugin will be copied to your QGIS profile folder.

Profile Folder: Select ``Settings`` -> ``User Profiles`` -> ``Open Active Profile Folder`` -> ``Python`` -> ``Plugin``

## Activate Plugin

QGIS: ``Plugins`` -> ``Manage and Install Plugins...`` -> ``Installed``



Check: ``Lfb Regeneration and Wildlife Impact Monitoring``


## Tests

![test workflow](https://github.com/b-lack/lfb-regeneration_wildlife_impact_monitoring/actions/workflows/run-all-tests.yml/badge.svg)

Run pytest in the root directory of the project.

```bash
pytest
```