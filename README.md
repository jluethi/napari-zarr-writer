# napari-zarr-writer

[![License](https://img.shields.io/pypi/l/napari-zarr-writer.svg?color=green)](https://github.com/jluethi/napari-zarr-writer/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-zarr-writer.svg?color=green)](https://pypi.org/project/napari-zarr-writer)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-zarr-writer.svg?color=green)](https://python.org)
[![tests](https://github.com/jluethi/napari-zarr-writer/workflows/tests/badge.svg)](https://github.com/jluethi/napari-zarr-writer/actions)
[![codecov](https://codecov.io/gh/jluethi/napari-zarr-writer/branch/main/graph/badge.svg)](https://codecov.io/gh/jluethi/napari-zarr-writer)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-zarr-writer)](https://napari-hub.org/plugins/napari-zarr-writer)

Napari plugin to write zarr files  
Prototype created at the napari hackathon on January 18th, 2022  
Current state: Widget has some issues being displayed within napari, but can be called using the widget_test.py script. Saves layer as a zarr file, but not yet compatible with the ome-zarr reader in napari.

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/plugins/stable/index.html
-->

## Installation

Currently needs to be installed manually:

    git clone https://github.com/jluethi/napari-zarr-writer
    cd napari-zarr-writer
    pip install -e .


## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-zarr-writer" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari]: https://github.com/napari/napari
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
