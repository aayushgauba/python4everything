from django.test import TestCase
from django.urls import resolve, reverse

from . import views


class ConferencePagesTests(TestCase):
    def test_named_routes_resolve_to_expected_views(self):
        self.assertEqual(resolve(reverse('home')).func, views.home)
        self.assertEqual(resolve(reverse('about')).func, views.about)
        self.assertEqual(resolve(reverse('news')).func, views.news)
        self.assertEqual(resolve(reverse('venue')).func, views.venue)
        self.assertEqual(resolve(reverse('speaking')).func, views.speaking)

    def test_pages_return_200(self):
        for name in ['home', 'about', 'news', 'venue', 'speaking']:
            with self.subTest(route=name):
                response = self.client.get(reverse(name))
                self.assertEqual(response.status_code, 200)

    def test_key_content_is_present(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Python 4 Almost Everything')
        self.assertContains(response, 'June 18')
        self.assertContains(response, 'TREX STL Convention Center')

        response = self.client.get(reverse('about'))
        self.assertContains(response, 'first STL Python conference')
        self.assertContains(response, 'students')
        self.assertContains(response, 'professionals')

        response = self.client.get(reverse('news'))
        self.assertContains(response, 'Conference News')
        self.assertContains(response, 'More Updates Soon')

        response = self.client.get(reverse('venue'))
        self.assertContains(response, '911 Washington Ave')
        self.assertContains(response, 'St. Louis, MO 63101')

        response = self.client.get(reverse('speaking'))
        self.assertContains(response, 'Submit Your Proposal')
        self.assertContains(response, '')
