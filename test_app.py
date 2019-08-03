from app import app
import unittest


class FlaskTestCase(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_date(self):
        tester = app.test_client(self)
        response = tester.get('/2019-1-1', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_date_media(self):
        tester = app.test_client(self)
        response = tester.get('/2019-1-1/media', content_type='html/text')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
