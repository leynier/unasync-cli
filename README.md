# CLI for unasync

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Test](https://github.com/leynier/unasync-cli/workflows/CI/badge.svg)](https://github.com/leynier/unasync-cli/actions?query=workflow%3ACI)
[![codecov](https://codecov.io/gh/leynier/unasync-cli/branch/main/graph/badge.svg?token=Z1MEEL3EAB)](https://codecov.io/gh/leynier/unasync-cli)
[![Version](https://img.shields.io/pypi/v/unasync-cli?color=%2334D058&label=Version)](https://pypi.org/project/unasync-cli)
[![Last commit](https://img.shields.io/github/last-commit/leynier/unasync-cli.svg?style=flat)](https://github.com/leynier/unasync-cli/commits)
[![GitHub commit activity](https://img.shields.io/github/commit-activity/m/leynier/unasync-cli)](https://github.com/leynier/unasync-cli/commits)
[![Github Stars](https://img.shields.io/github/stars/leynier/unasync-cli?style=flat&logo=github)](https://github.com/leynier/unasync-cli/stargazers)
[![Github Forks](https://img.shields.io/github/forks/leynier/unasync-cli?style=flat&logo=github)](https://github.com/leynier/unasync-cli/network/members)
[![Github Watchers](https://img.shields.io/github/watchers/leynier/unasync-cli?style=flat&logo=github)](https://github.com/leynier/unasync-cli)
[![Website](https://img.shields.io/website?up_message=online&url=https%3A%2F%2Fleynier.github.io/unasync-cli)](https://leynier.github.io/unasync-cli)
[![GitHub contributors](https://img.shields.io/github/contributors/leynier/unasync-cli?label=code%20contributors)](https://github.com/leynier/unasync-cli/graphs/contributors) <!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

Command line interface for unasync

## Getting started

### Install

Run the following command to install the package with [pip](https://pip.pypa.io):

```bash
pip install unasync-cli
```

Or with [conda](https://conda.io):

```bash
conda install unasync-cli
```

Or with [poetry](https://python-poetry.org):

```bash
poetry add unasync-cli --dev
```

Or any other package manager you prefer.

### Usage

For usage information, run the following command:

```bash
unasync --help
```

```txt
Usage: unasync [OPTIONS] PATHS...

Arguments:
  PATHS...  The folders where it will check for folders with the name _async
            to generate its equivalent _sync.  [required]

Options:
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.
```

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="http://leynier.github.io"><img src="https://avatars.githubusercontent.com/u/36774373?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Leynier Gutiérrez González</b></sub></a><br /><a href="#maintenance-leynier" title="Maintenance">🚧</a> <a href="https://github.com/leynier/unasync-cli/commits?author=leynier" title="Code">💻</a> <a href="#infra-leynier" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
