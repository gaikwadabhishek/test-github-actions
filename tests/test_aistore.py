#
# Copyright (c) 2018-2022, NVIDIA CORPORATION. All rights reserved.
#

# Default provider is AIS, so all Cloud-related tests are skipped.

import random
import string
import unittest

from aistore.client.api import Client

# from requests import get
import time

# ip = get('https://api.ipify.org').content.decode('utf8')


CLUSTER_ENDPOINT = "http://localhost:51080"
class TestObjectOps(unittest.TestCase):  # pylint: disable=unused-variable
    def setUp(self) -> None:
        letters = string.ascii_lowercase
        self.bck_name = ''.join(random.choice(letters) for _ in range(10))
        time.sleep(500)

        self.client = Client(CLUSTER_ENDPOINT)
        self.buckets = []

    def tearDown(self) -> None:
        # Try to destroy all temporary buckets if there are left.
        for bck_name in self.buckets:
            try:
                self.client.destroy_bucket(bck_name)
            except Exception:
                pass

    def test_bucket(self):
        res = self.client.list_buckets()
        count = len(res)
        self.create_bucket(self.bck_name)
        res = self.client.list_buckets()
        count_new = len(res)
        self.assertEqual(count + 1, count_new)

if __name__ == '__main__':
    unittest.main()
