from pprint import pprint
import unittest
import requests

from data import geo_logs, ids

from yandex_uploader import YaUploader
from token import token #Указать токен для YaUploader

def sorted_geo_logs(geo_logs):
    sorted_list = []
    tag = 'Россия'
    for log in geo_logs:
        for cities in log.values():
            if tag in cities:
                sorted_list.append(log)
    return sorted_list

def unique_ids(ids):
    result = []
    for id in ids.values():
        for number in id:
            if number not in result:
                result.append(number)
    return result

def max_stats():
    stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
    result = max(stats, key=stats.get)
    return result

class TestSum(unittest.TestCase):

    def test_tag(self):
        logs = sorted_geo_logs(geo_logs)
        for log in logs:
            for place in log.values():
                country = place[1]
                expected = 'Россия'
                self.assertEqual(country, expected)

    def test_unique_id(self):
        result = unique_ids(ids)
        expected = [213, 15, 54, 119, 98, 35]
        self.assertEqual(result, expected)

    def test_max_stats(self):
        result = max_stats()
        expected = 'yandex'
        self.assertEqual(result, expected)

    def test_yandex_uploader_succ(self):
        yandex = YaUploader(token)
        result = yandex.create_folder('test_folder')
        expected = 201
        self.assertEqual(result, expected)

    def test_yandex_uploader_fail(self):
        yandex = YaUploader(token)
        result = yandex.create_folder('test_folder')
        expected = 409
        self.assertEqual(result, expected)


