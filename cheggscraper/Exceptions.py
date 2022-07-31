import requests
import sys
sys.path.append("/chegg-scraper/Downloader")
from main import TOKEN,groupID

class FailedToParse(Exception):
    def __init__(self):
        self.message = 'Failed to parse data'
        requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage',data={'chat_id': f'{groupID}', 'text': f"Failed to Parse Data."})


class UnableToParseUUID(FailedToParse):
    def __init__(self):
        self.message = 'Unable to get question uuid'
        requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage',data={'chat_id': f'{groupID}', 'text': f"Unable to get Question UUID"})


class UnexpectedStatusCode(Exception):
    def __init__(self, status_code: int):
        self.message = 'Unexpected status code: {}'.format(status_code)
        requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage',data={'chat_id': f'{groupID}', 'text': "Unexpected status code: {}'.format(status_code)"})


class UnableToGetLegacyQuestionID(FailedToParse):
    def __init__(self):
        self.message = 'Unable to get question legacy id'
        requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage',data={'chat_id': f'{groupID}', 'text': f"Unable to get Question Legacy ID"})


class FailedToParseAnswer(FailedToParse):
    def __init__(self):
        self.message = 'Failed to parse answer'
        requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage',data={'chat_id': f'{groupID}', 'text': f"Failed to Parse Answer"})


class JsonParseError(Exception):
    ...


class UnableToGetToken(FailedToParse):
    def __init__(self):
        self.message = 'Unable to get token'
        requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage',data={'chat_id': f'{groupID}', 'text': f"Unable to get Token"})


class UrlNotSupported(ValueError):
    def __init__(self, url):
        self.message = f'URL NOT SUPPORTED: {url}'
        requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage',data={'chat_id': f'{groupID}', 'text': f"URL NOT SUPPORTED: {url}"})


class DeviceAllowedQuotaExceeded(Exception):
    def __init__(self):
        self.message = 'Device allowed quota exceeded'
        requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage',data={'chat_id': f'{groupID}', 'text': f"Device Allowed Quota Exceeded"})


class CookieFileDoesNotExist(FileNotFoundError):
    def __init__(self, path):
        self.message = f'File does not exist: {path}'
        requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage',data={'chat_id': f'{groupID}', 'text': f"File does not Exist"})


class BotFlagError(Exception):
    def __init__(self):
        self.message = 'The account is flagged as bot, open you chegg account with same browser where you get the cookies and fill the captcha'
        requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage',data={'chat_id': f'{groupID}', 'text': f"The account is flagged as bot, open you chegg account with same browser where you get the cookies and fill the captcha"})