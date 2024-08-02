## Calculus of differences
### Hexlet tests and linter status:
[![Actions Status](https://github.com/sergeikuz/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/sergeikuz/python-project-50/actions)
[![Actions Status](https://github.com/sergeikuz/python-project-50/actions/workflows/first-workflow.yml/badge.svg)](https://github.com/sergeikuz/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/b1590b07c51f7935365d/maintainability)](https://codeclimate.com/github/sergeikuz/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/b1590b07c51f7935365d/test_coverage)](https://codeclimate.com/github/sergeikuz/python-project-50/test_coverage)
<hr>

### Description
The computer of the differences is a program that determines the difference between the two data structures. This is a popular task, for the solution of which there are many online services, for example, jsondiff. A similar mechanism, for example, is used in the output of tests or in automatic monitoring of changes in configuration files.

### Utility opportunities:
*1. Support for different input formats: yml(yaml), json*

*2. Generation of the report in the form of plain text, stylish and json*
<hr>



This is project ["Calculus of differences"](https://ru.hexlet.io/programs/python/projects/50) on the Python Development course on [Hexlet.io](https://ru.hexlet.io/programs/python)


### Used technologies:
![](https://img.shields.io/badge/language-python-blue)
![](https://img.shields.io/badge/lybrary-argparse-red)
![](https://img.shields.io/badge/lybrary-PyYAML-yellow)
![](https://img.shields.io/badge/lybrary-json-brightgreen)
![](https://img.shields.io/badge/lybrary-yaml-orange)
![](https://img.shields.io/badge/lybrary-os.path-ff67b4)

This project was built using these tools:

| Tool                                                                        | Description                                             |
|-----------------------------------------------------------------------------|---------------------------------------------------------|
| [poetry](https://poetry.eustace.io/)                                        | "Python dependency management and packaging made easy"  |
| [Py.Test](https://pytest.org)                                               | "A mature full-featured Python testing tool"            |
| [Flake8](https://flake8.pycqa.org/en/latest/)               | "Your Tool For Style Guide Enforcement"|


---
## Install
```
git clone https://github.com/sergeikuz/python-project-50
cd python-project-50
make setup
```

[![asciicast](https://asciinema.org/a/670403.svg)](https://asciinema.org/a/670403)

## They are launched with simple commands:*
```commandline
usage: gendiff [-h] [-f FORMAT] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

options:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output, you can choose formats: stylish, plain, json, (default format: stylish)
```
```
gendiff tests/fixtures/file1.yml tests/fixtures/file2.yml
gendiff -f plain tests/fixtures/file1.yml tests/fixtures/file2.yml
gendiff --format plain tests/fixtures/file1.json tests/fixtures/file2.json
gendiff --format json tests/fixtures/file1.json tests/fixtures/file2.json

```
:pencil2:*_Make sure that you have Python version 3.10 or higher installed._


## Examples of teams for different output formats:

[![asciicast](https://asciinema.org/a/667800.svg)](https://asciinema.org/a/667800)

1. **Stylish style:** *Compares two configuration files and shows a difference in stylish format.
```commandline
*stylish is default format
gendiff tests/fixtures/file1.yml tests/fixtures/file2.yml
gendiff -f stylish tests/fixtures/file1.yml tests/fixtures/file2.yml
gendiff --format stylish tests/fixtures/file1.json tests/fixtures/file2.json
gendiff --format stylish tests/fixtures/file1.json tests/fixtures/file2.json

```
[![asciicast](https://asciinema.org/a/670392.svg)](https://asciinema.org/a/670392)

2. **Plain style:** *Compares two configuration files and shows a difference in plain format.*
```commandline
gendiff -f plain tests/fixtures/file1.yml tests/fixtures/file2.yml
gendiff --format plain tests/fixtures/file1.json tests/fixtures/file2.json

```
[![asciicast](https://asciinema.org/a/670385.svg)](https://asciinema.org/a/670385)

3. **Json style:** *Compares two configuration files and shows a difference in json format.*

```commandline
gendiff -f json tests/fixtures/file1.yml tests/fixtures/file2.yml
gendiff --format json tests/fixtures/file1.json tests/fixtures/file2.json

```

[![asciicast](https://asciinema.org/a/670384.svg)](https://asciinema.org/a/670384)

### How to find differences between two files:
Place two files that you want to compare in the tests/fixtures folder.
Follow the team to search for differences:
```commandline
gendiff -f plain tests/fixtures/file1.json tests/fixtures/file2.json

```
Replace file1.json and file2.json with your files

### Good luck and have a fun! 🤚
