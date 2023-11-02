<h1>
  <img src="./fim/icon.png" alt="Logo Plugin"/>
  FIM - Forest Inventory and Monitoring
</h1>

## Description

Das Plugin „Forest Inventory Monitoring“ (FIM) dient der Aufnahme in Brandenburg als Waldinventur nach § 30 LWaldG durchgeführten Waldinventur „Verjüngungszustands- und Wildeinflussmonitoring“ (VWM).

Es ist geplant es so weiterzuentwickeln, dass es

1. für Inventuraufnahmen durch Interessierte (Waldbesitzer, Jäger) und
2. für unabhängige, eigenständige Inventuren genutzt werden kann.

Die Dokumentation zum Verfahren VWM findet sich unter [https://gitlab.opencode.de/lfe/vwm-verfahren](https://gitlab.opencode.de/lfe/vwm-verfahren).

Die technische Dokumentation zu FIM findet sich unter: URL

Rückmeldungen an den Entwickler: [support@gruenecho.de](mailto:support@gruenecho.de)

Rückmeldungen an den Verfahrensverantwortlichen zur VWM: [landeswaldinventur@lfb.brandenburg.de](mailto:landeswaldinventur@lfb.brandenburg.de)

----
The plug-in "Forest Inventory Monitoring" (FIM) is used for the forest inventory "Regeneration Status and Game Influence Monitoring" (VWM) carried out in Brandenburg as a forest inventory according to § 30 LWaldG.

It is planned to develop it further in such a way that it can be used for

1. for inventories by interested parties (forest owners, hunters) and
2. for independent, autonomous inventories.

The documentation on the VWM procedure can be found at [https://gitlab.opencode.de/lfe/vwm-verfahren](https://gitlab.opencode.de/lfe/vwm-verfahren).

The technical documentation on FIM can be found at: URL

Feedback to the developer: [support@gruenecho.de](mailto:support@gruenecho.de)

Feedback to the person responsible for the VWM procedure: [landeswaldinventur@lfb.brandenburg.de](mailto:landeswaldinventur@lfb.brandenburg.de)

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