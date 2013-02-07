import unittest
from mysite import app

class MySiteTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SERVER_NAME'] = 'mysite.com'
        self.domain = 'http://mysite.com/'
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_en_index(self):
        rv = self.app.get('/en/', self.domain)
        self.assertEqual(rv.data, 'lang = en')
        print self.domain, rv.data

    def test_fr_index(self):
        rv = self.app.get('/fr/', self.domain)
        self.assertEqual(rv.data, 'lang = fr')
        print self.domain, rv.data

    def test_default(self):
        rv = self.app.get('/', self.domain)
        self.assertEqual(rv.data, 'lang = en')
        print self.domain, rv.data

class MyOtherSiteTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SERVER_NAME'] = 'myothersite.com'
        self.domain = 'http://myothersite.com/'
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_en_index(self):
        rv = self.app.get('/en/', self.domain)
        self.assertEqual(rv.data, 'lang = en')
        print self.domain, rv.data

    def test_fr_index(self):
        rv = self.app.get('/fr/', self.domain)
        self.assertEqual(rv.data, 'lang = fr')
        print self.domain, rv.data

    def test_default(self):
        rv = self.app.get('/', self.domain)
        self.assertEqual(rv.data, 'lang = fr')
        print self.domain, rv.data

if __name__ == '__main__':
    unittest.main()