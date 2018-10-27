import unittest
from unittest import TestCase
from fillerapi.client import FillerClient


class TestRepitClient(TestCase):
    def setUp(self):
        self.client = FillerClient()
        super().setUp()

    def test_get_filler_game(self):
        self.client.filler_game.get_objects()


if __name__ == '__main__':
    unittest.main()
