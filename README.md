# RBAC PoC

[![PyPI - Version](https://img.shields.io/pypi/v/rbac-poc.svg)](https://pypi.org/project/rbac-poc)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/rbac-poc.svg)](https://pypi.org/project/rbac-poc)

---

## Table of Contents

- [Installation](#installation)
- [Running](#running)
- [License](#license)

## Installation

```bash
python3 -m pip install -e .
python3 -m pip list | egrep 'hatch|hatchling|pyright|black|ruff|psutil|tomli|tomli_w|uvicorn|fastapi|pydantic|pydantic_core|pydantic-settings|SQLAlchemy'
```

## Running

```bash
python3 run_rbac_poc.py
```

Open in WebBrowser:

```txt
http://localhost:8097/docs
```

## License

`rbac-poc` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
