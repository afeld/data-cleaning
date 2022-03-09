# Data Cleaning Techniques workshop

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/afeld/data-cleaning/HEAD)

These examples use [NYC's 311 dataset](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9/data).

## Running locally

1. [Install repo2docker](https://repo2docker.readthedocs.io/en/latest/install.html)
1. `cd` into this directory and run `jupyter-repo2docker -E .`

If you get a database connection error, try [launching a terminal in JupyterHub](https://jupyterlab.readthedocs.io/en/stable/user/terminal.html) and re-creating with:

```sh
./postBuild; ./start
```
