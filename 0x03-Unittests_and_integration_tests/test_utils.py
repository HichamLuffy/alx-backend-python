#!/usr/bin/python3
"""test utils """
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Any, Tuple, Dict


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
