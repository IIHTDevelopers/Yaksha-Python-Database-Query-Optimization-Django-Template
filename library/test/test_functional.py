from django.test import TestCase
from django.urls import reverse
from library.test.TestUtils import TestUtils
from library.models import Event
from rest_framework.test import APITestCase
from django.test import TestCase
from django.http import HttpResponse
from django.contrib.auth.models import User  # Import User model


class EventFunctionalTest(APITestCase):



    def setUp(self):
        # Set up a user instance for test
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_event_list_view(self):
        """Test if the event list view works and returns the correct number of queries"""
        test_obj = TestUtils()
        try:
            # Create an event and add participants
            event = Event.objects.create(name='Test Event', date='2025-03-25')
            event.participants.add(self.user)  # Add the user as a participant

            # Test if the view returns the expected number of queries
            with self.assertNumQueries(2):  # Should only trigger two queries, one for events and one for participants
                # Ensure we aren't caching the response by disabling cache in the test settings
                response = self.client.get(reverse('event_list'))

            # Ensure the correct response is returned
            self.assertEqual(response.status_code, 200)
            test_obj.yakshaAssert("TestEventListView", True, "functional")
            print("TestEventListView = Passed")
        except Exception as e:
            test_obj.yakshaAssert("TestEventListView", False, "functional")
            print(f"TestEventListView = Failed")