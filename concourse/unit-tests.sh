#!/bin/bash

pip install poetry
poetry install
poetry run pytest
