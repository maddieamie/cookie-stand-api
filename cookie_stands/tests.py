from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import CookieStand

class CookieStandTests(TestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = get_user_model().objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpass123"
        )
        # Create a CookieStand object for testing
        self.cookie_stand = CookieStand.objects.create(
            location="Test Location",
            owner=self.user,
            description="Test description",
            hourly_sales=[10, 20, 30],
            minimum_customers_per_hour=5,
            maximum_customers_per_hour=25,
            average_cookies_per_sale=2.5
        )

    def test_string_representation(self):
        """Test the string representation of a CookieStand object."""
        self.assertEqual(str(self.cookie_stand), "Test Location")

    def test_get_absolute_url(self):
        """Test the get_absolute_url method of the model."""
        self.assertEqual(self.cookie_stand.get_absolute_url(), reverse('cookie_detail', args=[self.cookie_stand.id]))

    def test_cookie_stand_list_view(self):
        """Test that the CookieStand list view displays correctly for logged-in users."""
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse('cookie_stand_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Location")
        self.assertTemplateUsed(response, "cookie_stands/cookie_stand_list.html")

    def test_cookie_stand_detail_view(self):
        """Test that the CookieStand detail view works correctly for logged-in users."""
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse('cookie_stand_detail', args=[self.cookie_stand.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test description")
        self.assertTemplateUsed(response, "cookie_stands/cookie_stand_detail.html")

    def test_cookie_stand_create_view(self):
        """Test the CookieStand create view."""
        self.client.login(username="testuser", password="testpass123")
        response = self.client.post(reverse('cookie_stand_create'), {
            'location': "New Location",
            'owner': self.user.id,
            'description': "A new test cookie stand",
            'hourly_sales': [15, 30, 45],
            'minimum_customers_per_hour': 5,
            'maximum_customers_per_hour': 20,
            'average_cookies_per_sale': 3.0,
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after creation
        new_cookie_stand = CookieStand.objects.get(location="New Location")
        self.assertEqual(new_cookie_stand.description, "A new test cookie stand")

    def test_cookie_stand_update_view(self):
        """Test updating a CookieStand."""
        self.client.login(username="testuser", password="testpass123")
        response = self.client.post(reverse('cookie_stand_update', args=[self.cookie_stand.id]), {
            'location': "Updated Location",
            'description': "Updated description",
            'hourly_sales': [5, 10, 15],
            'minimum_customers_per_hour': 4,
            'maximum_customers_per_hour': 15,
            'average_cookies_per_sale': 2.0,
        })
        self.assertEqual(response.status_code, 302)
        updated_cookie_stand = CookieStand.objects.get(id=self.cookie_stand.id)
        self.assertEqual(updated_cookie_stand.location, "Updated Location")
        self.assertEqual(updated_cookie_stand.description, "Updated description")

    def test_cookie_stand_delete_view(self):
        """Test that deleting a CookieStand works correctly."""
        self.client.login(username="testuser", password="testpass123")
        response = self.client.post(reverse('cookie_stand_delete', args=[self.cookie_stand.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(CookieStand.objects.filter(id=self.cookie_stand.id).exists())

    def test_redirect_if_not_logged_in(self):
        """Test that non-logged-in users are redirected to the login page."""
        response = self.client.get(reverse('cookie_stand_list'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/cookie_stands/')
