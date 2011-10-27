from unittest import TestCase

__author__ = 'barzoque'

class Conference(object):
    def __init__(self):
        self.talks = []

    def get_talk_at(self, time):
        for start, end, name in self.talks:
            if time >= start and time < end:
                return name

    def add_talk(self, start, end, name):
        self.talks.append((start, end, name))


class ConferenceTest(TestCase):
    def setUp(self):
        self.conference = Conference()

    def test_empty(self):
        self.assertEqual(None, self.conference.get_talk_at(10))

    def test_talk(self):
        talk_name = "PyCharm Demo"
        self.conference.add_talk(10, 12, talk_name)
        self.assertEqual(talk_name, self.conference.get_talk_at(11))