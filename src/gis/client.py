"""
ArcGIS REST Client

Provides a reusable client for querying ArcGIS Feature Services.

Author: MCD Stormwater Intelligence Platform
"""

from __future__ import annotations

from typing import Any

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
class ArcGISClient:
    """
    Reusable ArcGIS Feature Service client.
    """

    def __init__(self, base_url: str, timeout: int = 60):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

        self.session = requests.Session()

        retry_strategy = Retry(
            total=5,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET", "POST"],
        )

        adapter = HTTPAdapter(max_retries=retry_strategy)

        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)
    
    def get(self, endpoint: str, params: dict[str, Any]) -> dict:
        """
        Execute a GET request against an ArcGIS REST endpoint.
        """

        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        response = self.session.get(
            url,
            params=params,
            timeout=self.timeout,
        )

        response.raise_for_status()

        return response.json()

    def post(self, endpoint: str, data: dict[str, Any]) -> dict:
        """
        Execute a POST request against an ArcGIS REST endpoint.
        """

        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        response = self.session.post(
            url,
            data=data,
            timeout=self.timeout,
        )

        response.raise_for_status()

        return response.json()
      