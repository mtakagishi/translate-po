# translate-po

Simple quick script for automatically translating .po files using Google. It speeds up internationalization by giving translators machine translated base version to correct.

## Features of This Fork

> This is a fork of [zcribe/translate-po](https://github.com/zcribe/translate-po) by Erlend Eelmets, modified to support Python 3.13 and `googletrans==4.0.2` with full async/await support.

- Uses `googletrans==4.0.2` (no `cgi` dependency) & async/await support
- Compatible with Python 3.13

## Usage

Installation
```cmd
pip install git+https://github.com/mtakagishi/translate-po.git
```

Usage
```python
from translate_po.main import run

run(fro="en" to="et" src="./untranslated" dest="./translated")
```

### Changelog
1.0.13-post1 - 2025-03-23
- Migrated `googletrans` to version 4.0.2 to avoid deprecated `cgi` usage
- Rewrote translation logic to use `async/await`
- Made the entire tool compatible with Python 3.13
- Updated `README.md` to reflect fork and new usage

1.0.13
- Fixed typo in the readme

1.0.11
- Fixed distributable not including parts of code
- Build script improvements
- Fixed dependencies not automatically installing
- Added .po file recognition
- Changed default constants for simpler use

1.0.4 
- Swapped out my own implementation of .po file parser for polib one. 
- Fixed metadata writing into new files.