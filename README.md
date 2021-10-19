# Find My Representative

## Overview

Build a web application that allows users to learn who represents them in the US House of Representatives.

## User Flow

1. User enters their zip code in validated form field.
1. User clicks submit button, or hits Enter key when input is focused.
1. User is returned a summary of who their representative is, including links to learn more.

## Resources

The `/data` folder in this repo contains two datasets which contains all the data you need: `legislators.json` lists current representatives associated with the states and district numbers they've served in, and `zipcodes-districts.json` lists every US zip code with its associated state and district number.

## Notes
- Please don't work on this for more than 2 hours
- Consider the current date to be 2019-01-01
- If you find issues with the data or the spec, work around them as best you can and be prepared to discuss

----------------------------------------
# Setup

### Pre-requisites
- Python >= 3.8
- NodeJS >= 14.18.1
- npm == 6.14.x (comes with node 10+)

### Create a Virtual Environment

```bash
python -m venv /path/to/new/virtual/environment
```

### Install Python and Node dependencies
```bash
make setup
```

### Run the app
```bash
make run
```

# Maintenance

### Updating requirements

This project usis `pip-tools` to manage dependencies and has some handy `make` commands for updating and installing dependencies. 

Add/edit dependencies inside `requirements/base.in` and then run
```bash
make update_requirements
make install_requirements
```
