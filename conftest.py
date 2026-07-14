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

@pytest.fixture(scope="session")
def bank_credentials() -> tuple[str, str]:
    username = os.getenv("BANK_USERNAME")
    password = os.getenv("BANK_PASSWORD")

    if not username or not password:
        raise ValueError(
            "BANK_USERNAME and BANK_PASSWORD must be defined in the .env file"
        )

    return username, password