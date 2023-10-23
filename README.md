<h1>
  <img src="./fim/icon.png" alt="Logo Plugin"/>
  FIM - Forest Inventory and Monitoring
</h1>

## Installation from Repository

QGIS: ``Plugins`` -> ``Manage and Install Plugins...`` -> ``Settings``

In the **Plugin Repositories** section click `+Add`.

- Name: `FIM`
- URL: `https://raw.githubusercontent.com/b-lack/qgis-fim-plugin/main/plugins.xml`

Confirm by clicking `OK`

Restart QGIS

QGIS: ``Plugins`` -> ``Manage and Install Plugins...`` -> ``ALL``

Search for `FIM` and select `FIM - Forest Inventory and Monitoring`

Confirm by clicking `Install Plugin`

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

### Activate Plugin

QGIS: ``Plugins`` -> ``Manage and Install Plugins...`` -> ``Installed``

Make sure that ``FIM`` is selected.


## Reporting Issues

Please report any issue regarding the FIM plugin [here](https://github.com/b-lack/qgis-fim-plugin/issues).

## License

This plugin is licensed under the [GNU GENERAL PUBLIC LICENSE](./LICENSE).

## About

Commissioned through the [Brandenburg State Forestry Office](https://forst.brandenburg.de/).

- Concept by: Torsten Wiebke
- Develpment by: [Gerrit Balindt](https://gruenecho.de/)


💚 Free to use by everyone 💚