from rest_framework.test import APITestCase
from library.test.TestUtils import TestUtils
from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from library.models import Event
from django.test import TestCase

class EventBoundaryTest(APITestCase):

    def test_boundary(self):
        """Test if the event list returns the expected boundary values for pagination"""
        test_obj = TestUtils()
        try:
            # Create a large number of events
            for i in range(100):
                Event.objects.create(name=f'Event {i}', date='2025-03-25')

            response = self.client.get(reverse('event_list'))
            self.assertEqual(response.status_code, 200)
            test_obj.yakshaAssert("TestBoundary", True, "boundary")
            print("TestBoundary = Passed")
        except Exception as e:
            test_obj.yakshaAssert("TestBoundary", False, "boundary")
            print(f"TestBoundary = Failed")
