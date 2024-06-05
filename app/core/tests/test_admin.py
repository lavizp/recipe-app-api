
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client

class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@admin1.com',
            password='haha123',
            name='Test User'
        )
    def test_users_list(self):
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        print(self)
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)