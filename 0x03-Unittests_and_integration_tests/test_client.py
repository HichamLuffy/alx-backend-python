#!/usr/bin/env python3
"""test client"""
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """test github org client"""

    @parameterized.expand(
        [
            ("google"),
            ("abc"),
        ]
    )
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org_name: str, mock_get_json: Mock) -> None:
        """test org"""
        json_data = {'login': org_name, 'id': 12345}
        mock_get_json.return_value = json_data
        client = GithubOrgClient(org_name)
        response = client.org
        url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(url)
        self.assertEqual(response, json_data)

    @patch('client.GithubOrgClient.org',
           new_callable=unittest.mock.PropertyMock)
    def test_public_repos_url(self, mock_org: PropertyMock) -> None:
        """ test public repos url"""
        mock_org.return_value = {
            'repos_url': 'https://api.github.com/orgs/google/repos'}
        client = GithubOrgClient('google')
        self.assertEqual(
            client._public_repos_url,
            'https://api.github.com/orgs/google/repos')

    @patch("client.get_json",
           return_value=[{"name": "repo1"}, {"name": "repo2"}])
    def test_public_repos(self, mock_get_json) -> None:
        """doc doc doc"""
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = (
                "https://api.github.com/orgs/google/repos"
            )
            github_org_client = GithubOrgClient("google")
            self.assertEqual(github_org_client.public_repos(),
                             ["repo1", "repo2"])
            mock_get_json.assert_called_once()
            mock_public_repos_url.assert_called_once()
