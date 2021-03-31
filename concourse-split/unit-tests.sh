#!/bin/bash

cd app
pip install poetry
poetry install
poetry run pytest
