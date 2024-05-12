#!/usr/bin/env python3
"""test client"""
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """test github org client"""
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org_name: str, mock_get_json: Mock) -> None:
        """test org"""
        json_data = {'login': org_name, 'id': 12345}
        mock_get_json.return_value = json_data
        client = GithubOrgClient(org_name)
        response = client.org()
        url = "https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(url)
        self.assertEqual(response, json_data)
