# Data Cleaning Techniques workshop

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/afeld/data-cleaning/HEAD)

From the [NYC Open Data Week 2022 event page](https://2022.open-data.nyc/event/data-cleaning-techniques/):

> You’ve got your data loaded, you start on your analysis, and… WHAM, missing values. WHAM, junk entries. WHAM, capitalization inconsistencies.
>
> Data cleaning often feels like a chore, and we will often do as little as necessary. What if we took a more systemic approach? In this hands-on workshop, we’ll explore some common data issues to look for, tools, and techniques for cleaning it up, giving us better understanding of our data in the process and clearing the path for smoother data analysis and manipulation.

These examples use [NYC's 311 dataset](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9/data).

## Running locally

1. [Install repo2docker](https://repo2docker.readthedocs.io/en/latest/install.html)
1. `cd` into this directory and run `jupyter-repo2docker -E .`
1. After you open the provided URL, change the path in your browser to `/lab`.
