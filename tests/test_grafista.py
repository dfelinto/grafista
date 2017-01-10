import os
import grafista.application
import grafista.application.main
import unittest
import tempfile


class GrafistaTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, grafista.application.app.config['DATABASE'] = tempfile.mkstemp()
        grafista.application.app.config['TESTING'] = True
        self.app = grafista.application.app.test_client()
        with grafista.application.app.app_context():
            grafista.application.main.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(grafista.application.app.config['DATABASE'])

    def test_empty_db(self):
        rv = self.app.get('/')
        assert b'<!DOCTYPE html>' in rv.data

if __name__ == '__main__':
    unittest.main()
