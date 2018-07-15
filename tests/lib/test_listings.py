from unittest import TestCase
from resources.lib.Listings import Listings
from os import getcwd

class TestListings(TestCase):

    def test_fetch_categories(self):
        given_url = 'file://' + getcwd() + '/../test_data/'
        listings = Listings(given_url)
        categories = listings.fetch_categories()
        assert len(categories) == 20
