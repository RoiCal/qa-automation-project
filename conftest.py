import os
import pytest

from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session")
def app_url() -> str:
	url = os.getenv("BASE_URL")

	if not url:
		raise ValueError("BASE_URL is not defined in the .env file")
	
	return url