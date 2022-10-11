from django.test import TestCase, Client
from mywatchlist.views import show_data_json, show_data_xml, show_mywatchlist


# Create your tests here.
class StatusCodeTest(TestCase):
    def test_xml_status_code(self):
        response = self.client.get('/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)

    def test_json_status_code(self):
        response = self.client.get('/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)
    
    
    def test_html_status_code(self):
        response = self.client.get('/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)

    
# c = Client()
# response = c.get('/mywatchlist/html/')
# response.status_code