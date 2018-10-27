from fillerapi.api.filler import TaskAPI, StatusAPI, ProcessAPI
from fillerapi.api.filler import GameQueueAPI, CustomQueueAPI, FillerGameAPI, FillerStreamerAPI


class FillerClient(object):
    def __init__(self):
        self._task = None
        self._status = None
        self._process = None
        self._game_queue = None
        self._custom_queue = None
        self._filler_game = None
        self._filler_streamer = None

    @property
    def task(self):
        if not self._task:
            self._task = TaskAPI()
        return self._task

    @property
    def status(self):
        if not self._status:
            self._status = StatusAPI()
        return self._status

    @property
    def process(self):
        if not self._process:
            self._process = ProcessAPI()
        return self._process

    @property
    def game_queue(self):
        if not self._game_queue:
            self._game_queue = GameQueueAPI()
        return self._game_queue

    @property
    def custom_queue(self):
        if not self._custom_queue:
            self._custom_queue = CustomQueueAPI()
        return self._custom_queue

    @property
    def filler_game(self):
        if not self._filler_game:
            self._filler_game = FillerGameAPI()
        return self._filler_game

    @property
    def filler_streamer(self):
        if not self._filler_streamer:
            self._filler_streamer = FillerStreamerAPI()
        return self._filler_streamer

