from fillerapi.api.base import FillerAPI
from fillerapi.api.restobject import *

BASE_URL = 'filler/'
TASK_URL = BASE_URL + 'task/'
STATUS_URL = BASE_URL + 'status/'
PROCESS_URL = BASE_URL + 'process/'
GAME_QUEUE_URL = BASE_URL + 'game_queue_status/'
CUSTOM_QUEUE_URL = BASE_URL + 'custom_queue_status/'
FILLER_GAME_URL = BASE_URL + 'games/'
FILLER_STREAMER_URL = BASE_URL + 'streamers/'


class TaskAPI(FillerAPI):
    def __init__(self):
        self.path = TASK_URL

    def get(self, params):
        response = self._request_get(self.path, params)
        return response

    def post(self, data):
        response = self._request_post(self.path, data)
        return response


class StatusAPI(FillerAPI):
    def __init__(self):
        self.path = STATUS_URL

    def get(self, params):
        response = self._request_get(self.path, params)
        return response


class ProcessAPI(FillerAPI):
    def __init__(self):
        self.path = PROCESS_URL

    def get(self, params):
        response = self._request_get(self.path, params)
        return response


class BaseRESTObjectAPI(FillerAPI):
    def __init__(self, path, constructor):
        self.constructor = constructor
        self.path = path
        super().__init__()

    def get_objects(self, params=None, limit=100, offset=0):
        if limit != 100:
            params['limit'] = limit
        if offset != 0:
            params['offset'] = offset
        response = self._request_get(self.path, params)
        return [self.constructor(**x) for x in response]

    def get_object(self, pk):
        response = self._request_get(self.path + str(pk))
        return self.constructor(**response)

    def post_object(self, data):
        response = self._request_post(self.path, data)
        return response

    def put_object(self, pk, data):
        response = self._request_put(self.path + str(pk), data)
        return response

    def delete_object(self, pk):
        response = self._request_delete(self.path + str(pk))
        return response


class GameQueueAPI(BaseRESTObjectAPI):
    def __init__(self):
        super().__init__(GAME_QUEUE_URL, GameQueueStatus)


class CustomQueueAPI(BaseRESTObjectAPI):
    def __init__(self):
        super().__init__(CUSTOM_QUEUE_URL, CustomQueueStatus)


class FillerGameAPI(BaseRESTObjectAPI):
    def __init__(self):
        super().__init__(FILLER_GAME_URL, FillerGame)

    def get_objects_response(self, params=None):
        response = self._request_get(self.path, params)
        return response


class FillerStreamerAPI(BaseRESTObjectAPI):
    def __init__(self):
        super().__init__(FILLER_STREAMER_URL, FillerGame)

    def get_objects(self, params=None, limit=100, offset=0):
        if params:
            print('Params are not allowed till streamer filter returns output that can be handled by the constructor')
            params = None
        return super().get_objects(params, limit, offset)

    def get_objects_response(self, params=None):
        response = self._request_get(self.path, params)
        return response

    def get_game_default_streamers(self, game):
        response = self._request_get(self.path, {'game_defaults': game})
        return response

    def get_game_current_streamers(self, game):
        response = self._request_get(self.path, {'game': game})
        return response
