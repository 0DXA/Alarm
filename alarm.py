import time


class Alarm(object):
    """Base class for alarm"""

    def __init__(self, title: str):
        self.__title = title
        self.hour = int(time.strftime("%H", time.localtime()))
        self.minute = int(time.strftime("%M", time.localtime()))

    def set_title(self, title):
        self.__title = title

    def set_minute(self, minute):
        if minute == -1:
            minute = 59
        elif minute == 60:
            minute = 0
        self.minute = minute

    def set_hour(self, hour):
        if hour == 24:
            hour = 0
        if hour == -1:
            hour = 23
        self.hour = hour

    def get_hour(self):
        return self.hour

    def get_minute(self):
        return self.minute

    def get_title(self):
        return self.__title

    def get_state(self):
        return self.__activated

    def activate(self):
        self.__activated = True

    def deactivate(self):
        self.__activated = False

    def __compare_formatted(self,):
        time1 = time.strftime("%H%M", time.localtime())
        time2 = str(self.hour)+str(self.minute)
        return time1 == time2

    def tick(self):
        if self.__compare_formatted():
            return "RING"
        return "0"


