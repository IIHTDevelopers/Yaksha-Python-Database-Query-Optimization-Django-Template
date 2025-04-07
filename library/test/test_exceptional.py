from rest_framework.test import APITestCase
from django.db import IntegrityError
from library.test.TestUtils import TestUtils
from django.urls import reverse
from unittest.mock import patch
from django.urls import get_resolver
from django.test import TestCase


class EventExceptionalTest(APITestCase):

    def test_empty_event_list(self):
        """Test if the event list view works when there are no events"""
        test_obj = TestUtils()
        try:
            response = self.client.get(reverse('event_list'))
            self.assertEqual(response.status_code, 200)
            test_obj.yakshaAssert("TestEmptyEventList", True, "exceptional")
            print("TestEmptyEventList = Passed")
        except Exception as e:
            test_obj.yakshaAssert("TestEmptyEventList", False, "exceptional")
            print(f"TestEmptyEventList = Failed")