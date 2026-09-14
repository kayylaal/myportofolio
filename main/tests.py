from django.test import TestCase, Client
from django.urls import reverse
from main.models import Project, SocialWork

class TestExperiencesPage(TestCase):
    def setUp(self):
        self.client = Client()

    def test_url_uses_correct_template(self):
        response = self.client.get(reverse('main:show_experiences'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'experiences.html')

    def test_data_appears_in_html(self):
        Project.objects.create(title="Test Project", description="Desc", link="https://example.com", thumbnail="/static/img/test.png")
        response = self.client.get(reverse('main:show_experiences'))
        self.assertContains(response, "Test Project")

    def test_empty_state(self):
        response = self.client.get(reverse('main:show_experiences'))
        self.assertContains(response, "Still cooking...")

class MainTest(TestCase):
    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)
