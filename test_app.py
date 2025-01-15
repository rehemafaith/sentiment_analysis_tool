import unittest
import json
from app import app

class TestSentimentAnalysisAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_valid_input(self):
        response = self.app.post('/analyze',
                                 content_type='application/json',
                                 data=json.dumps({'text': 'This is great!'}))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['sentiment'], 'Positive')

    def test_empty_input(self):
        response = self.app.post('/analyze',
                                 content_type='application/json',
                                 data=json.dumps({'text': ''}))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['sentiment'], 'Neutral')

    def test_no_input(self):
        response = self.app.post('/analyze',
                                content_type='application/json',
                                data=json.dumps({}))
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['error'], 'No request body provided')
    
    def test_wrong_content_type(self):
        response = self.app.post('/analyze',
                                 content_type='text/plain',
                                 data='This is great!')
        self.assertEqual(response.status_code, 415)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['error'], 'Invalid Content-Type. Please use application/json.')


if __name__ == '__main__':
    unittest.main()