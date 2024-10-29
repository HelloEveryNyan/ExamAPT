import logging
import pytest
from tests.api.api_helpers import APIClient
from logger import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

@pytest.mark.parametrize("owner, expected_title", [("notMe", "TARTAR")])
def test_step1(login, owner, expected_title):
    try:
        api_client = APIClient()
        response = api_client.get_posts(owner, login)
        listres = [i["title"] for i in response["data"]]
        logger.info("Полученные заголовки: %s", listres)
        assert expected_title in listres
    except Exception as e:
        logger.error(f"Error в test_step1: {e}")
        pytest.fail(f"Error в test_step1: {e}")

def test_step2(login, post_data):
    try:
        api_client = APIClient()
        res = api_client.create_post(login, post_data)
        assert res.status_code == 200
    except Exception as e:
        logger.error(f"Error в test_step2: {e}")
        pytest.fail(f"Error в test_step2: {e}")

def test_step3(login, created_post):
    try:
        api_client = APIClient()
        response = api_client.get_posts("me", login)
        descriptions = [i["description"] for i in response["data"]]
        assert created_post["description"] in descriptions
    except Exception as e:
        logger.error(f"Error в test_step3: {e}")
        pytest.fail(f"Error в test_step3: {e}")
