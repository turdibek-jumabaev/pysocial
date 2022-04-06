import requests


class YouTube:

    def __init__(self, url: str):

        self.url = url
        self.title = None
        self.video_url = None

    def get_video_id(self):
        if self.url is None:
            raise Exception("URL kiritilmagan")
        else:
            self.video_url = self.url.split("=")[1]
            return self.video_url
