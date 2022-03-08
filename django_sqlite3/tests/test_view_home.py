from django.test import TestCase


class HomeViewTestCase(TestCase):
    def test_view_redirect_admin(self):
        response = self.client.get("/admin")
        self.assertEquals(response.status_code, 301)

    def test_view_admin(self):
        response = self.client.get("/admin/login/?next=/admin/")
        self.assertEquals(response.status_code, 200)
