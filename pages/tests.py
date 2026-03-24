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
        self.assertContains(response, 'No News Published Yet')

        response = self.client.get(reverse('venue'))
        self.assertContains(response, '911 Washington Ave')
        self.assertContains(response, 'St. Louis, MO 63101')

        response = self.client.get(reverse('speaking'))
        self.assertContains(response, 'Submit Your Proposal')
        self.assertContains(response, 'https://forms.gle/D1EHzv4JxFH66u6f9')

    def test_pages_include_core_seo_tags(self):
        expected_descriptions = {
            'home': 'St. Louis Python conference',
            'about': 'local St. Louis Python conference',
            'news': 'latest conference updates',
            'venue': 'Venue details for Python 4 Almost Everything',
            'speaking': 'Apply to speak at Python 4 Almost Everything',
        }
        for name, expected_description in expected_descriptions.items():
            with self.subTest(route=name):
                response = self.client.get(reverse(name))
                self.assertContains(response, '<meta name="description"', html=False)
                self.assertContains(response, expected_description)
                self.assertContains(response, '<link rel="canonical" href="http://testserver', html=False)
                self.assertContains(response, '<meta property="og:title"', html=False)
                self.assertContains(response, '<meta property="og:description"', html=False)
                self.assertContains(response, '<meta name="twitter:card" content="summary">', html=False)

    def test_each_page_has_single_h1(self):
        for name in ['home', 'about', 'news', 'venue', 'speaking']:
            with self.subTest(route=name):
                response = self.client.get(reverse(name))
                html = response.content.decode('utf-8')
                self.assertEqual(html.count('<h1'), 1)
