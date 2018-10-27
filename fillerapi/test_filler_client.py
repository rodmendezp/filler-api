import unittest
from unittest import TestCase
from fillerapi.client import FillerClient


class TestRepitClient(TestCase):
    def setUp(self):
        self.client = FillerClient()
        super().setUp()

    def test_get_filler_game(self):
        games = self.client.filler_game.get_objects()
        pass

    def test_get_filler_streamer(self):
        streamers = self.client.filler_streamer.get_objects()
        pass

    def test_get_game_filtered_streamers(self):
        streamers = self.client.filler_streamer.get_game_default_streamers('Fortnite')
        pass



if __name__ == '__main__':
    unittest.main()
