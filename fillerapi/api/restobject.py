class GameQueueStatus:
    def __init__(self, id, game, processing, locked, jobs_available):
        self.id = id
        self.game = game
        self.processing = processing
        self.locked = locked
        self.jobs_available = jobs_available


class CustomQueueStatus:
    def __init__(self, id, game, streamer, user, processing, locked, jobs_available):
        self.id = id
        self.game = game
        self.streamer = streamer
        self.user = user
        self.processing = processing
        self.locked = locked
        self.jobs_available = jobs_available


class FillerGame:
    def __init__(self, name):
        self.name = name


class FillerStreamer:
    def __init__(self, name):
        self.name = name
