import logging
from typing import Any
import pytest
from tests.ui.ui_helpers import UIClient
from logger import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

def test_create_post_via_ui(login: Any):
    ui_client = UIClient()
    ui_client.login()
    ui_client.close()
