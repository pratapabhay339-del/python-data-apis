"""Simple REST API client and JSON processing utilities."""

from typing import Any

import pandas as pd
import requests

DEFAULT_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_json(url: str = DEFAULT_URL, timeout: int = 10) -> list[dict[str, Any]]:
    """GET a JSON endpoint and return the decoded list."""
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    payload = response.json()
    if not isinstance(payload, list):
        raise ValueError("Expected the API response to be a JSON list")
    return payload


def json_to_dataframe(payload: list[dict[str, Any]]) -> pd.DataFrame:
    """Convert a list of JSON objects to a Pandas DataFrame."""
    return pd.json_normalize(payload)


def get_api_preview(limit: int = 5) -> pd.DataFrame:
    """Fetch the public API and return a small preview."""
    payload = fetch_json()
    return json_to_dataframe(payload).head(limit)
