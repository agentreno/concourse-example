#!/bin/bash

cd app/app
pip install poetry
poetry install
poetry run pytest
