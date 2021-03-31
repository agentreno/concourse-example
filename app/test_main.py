import pytest

import responses

from app import main


@responses.activate
def test_fetch_ip():
    responses.add(responses.GET, "http://icanhazip.com", body="1.1.1.1\n")

    ip = main.fetch_ip()

    assert ip == "1.1.1.1\n"
