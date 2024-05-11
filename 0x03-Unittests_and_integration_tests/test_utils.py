#!/usr/bin/env python3
"""test utils """
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Any, Tuple, Dict
from unittest.mock import patch
from utils import get_json


class TestAccessNestedMap(unittest.TestCase):
    """test access netedmap"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
        self, nested_map: Dict[str, Any], path: Tuple[str], expected: Any
    ) -> None:
        """ FUNC """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(
        self, nested_map: Dict[str, Any], path: Tuple[str]) -> None:
        """FUNC """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """tEST GET JSON"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(
        self, test_url: str, test_payload: Dict[str, Any])-> None:
        """FUNC """
        with patch('requests.get') as mocked_get:
            mocked_get.return_value.json.return_value = test_payload
            response = get_json(test_url)
            self.assertEqual(response, test_payload)
            mocked_get.assert_called_once_with(test_url)
