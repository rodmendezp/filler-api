class GameQueueStatus:
    def __init__(self, game, processing, locked, jobs_available):
        self.game = game
        self.processing = processing
        self.locked = locked
        self.jobs_available = jobs_available


class CustomQueueStatus:
    def __init__(self, game, streamer, user, processing, locked, jobs_available):
        self.game = game
        self.streamer = streamer
        self.user = user
        self.processing = processing
        self.locked = locked
        self.jobs_available = jobs_available


class FillerGame:
    def __init__(self, id, name, twid):
        self.id = id
        self.twid = twid
        self.name = name


class FillerStreamer:
    def __init__(self, id, name):
        self.id = id
        self.name = name
