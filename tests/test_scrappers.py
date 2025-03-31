import unittest
from app.scrappers.comfy import ComfyScrapper


class TestScrappers(unittest.TestCase):
    def test_200(self):
        url = "https://comfy.ua/ua/smartfon-apple-iphone-15-128gb-black.html?gad_source=1&gclid=Cj0KCQjwtJ6_BhDWARIsAGanmKcsb_jmALhbcD3dXJM5cDbbprWXUi-6bDzIVoY2E5RdCOUa58Q9P0UaAsMXEALw_wcB"
        scrapper = ComfyScrapper(url)
        scrapper.scrape()
        status = scrapper.response.status_code

        self.assertEqual(status, 200, f"Expected 'success' but got {status}")

    def test_continuous_connection_rozetka(self):
        url = "https://comfy.ua/ua/smartfon-apple-iphone-15-128gb-black.html?gad_source=1&gclid=Cj0KCQjwtJ6_BhDWARIsAGanmKcsb_jmALhbcD3dXJM5cDbbprWXUi-6bDzIVoY2E5RdCOUa58Q9P0UaAsMXEALw_wcB"
        test_connections = 100
        connections_made = 0

        for i in range(test_connections):
            scrapper = ComfyScrapper(url)
            scrapper.scrape()
            if scrapper.is_scrape_valid():
                connections_made += 1
            else:
                break

        self.assertEqual(connections_made, test_connections, f"Made only {connections_made} connections")
