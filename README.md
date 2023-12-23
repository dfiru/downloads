# Downloads Organizer

Keeps your Downloads folder sane 

---

## Badges

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](URL)
[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)](URL)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

---

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Documentation](#documentation)
- [Examples](#examples)
- [Contributing](#contributing)
- [Tests](#tests)
- [Roadmap](#roadmap)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

---

## Installation

```bash
pip install git+https://github.com/dfiru/downloads.git
```

---

## Usage

This package provides a downloads-organizer executable.
Here's how to get started:

```shell
> downloads-organizer --help

NAME
 downloads-organizer - Organize files in the downloads folder into categories.

SYNOPSIS
 downloads-organizer <flags>

DESCRIPTION
 Organize files in the downloads folder into categories.

FLAGS
 --downloads_path=DOWNLOADS_PATH
 Type: str
 Default: '~/Downloads/'
 Path to the downloads folder.
 --dry_run=DRY_RUN
 Type: bool
 Default: False
 If True, the script will simulate the organization without moving files.
 --delete_folders=DELETE_FOLDERS
 Type: bool
 Default: True
```

---

## Features

* Organizes your downloads folder into categories based on file types
* Any folders encountered not a part of one of the categories will prompt for deletion.
  * *This occurs often with zip file extraction on doubleclick in the os*
* If enoucountered folder not deleted, will prompt user to move the folder into one of the category folders
* Report files over 10MB
* Dry run that tells you what would've happened but doesn't actually do it
* An option to turn off user-prompted folder deletion after flat files are organized

---

## Documentation

Not really any right now

## Examples

```shell
## Organize your MacOS defaul downloads folder
> downloads-organizer ~/Downloads

Large Files Report (Files over 10MB):
File organization complete.
```

---

## Contributing

Fork and PR to your heart's content. 

---

## Tests

Tests? Where we're going we won't need tests.

---

## Roadmap

* User-space overlay for .categories.file_organization. Likely a json or yaml file since it is just a basic dict[str, list]
* Mind reading

File an issue if you want.

---

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/dfiru/downloads/blob/main/LICENSE) file for details. Literally do whatever you want. No warranties. I mean it. This package deletes files. Be careful.

---

## Acknowledgments

* ty GPT4
* Inspired by an inabity to find a file from 3 weeks ago in less time than it took to write all of this

---

## Contact

Daniel Firu - [@danfiru](https://twitter.com/danfiru)
