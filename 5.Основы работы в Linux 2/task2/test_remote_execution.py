import unittest

from remote_execution import app


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


class TestRemoteExecutionApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        self.base_url = '/run_code'

    def test_with_correct_timeout(self):
        data = {"code": "import time; time.sleep(2)", "timeout": 5}
        response_text = self.app.post(self.base_url, json=data).data.decode()
        self.assertTrue('Результат:' in response_text)

    def test_with_wrong_timeout_type(self):
        data = {"code": "import time; time.sleep(2)", "timeout": 'timeout'}
        response = self.app.post(self.base_url, json=data)
        self.assertTrue(response.status_code == 400)

    def test_with_wrong_big_timeout(self):
        data = {"code": "import time; time.sleep(2)", "timeout": '31'}
        response = self.app.post(self.base_url, json=data)
        self.assertTrue(response.status_code == 400)

    def test_shell_is_true(self):
        response = self.app.post(self.base_url, data={"code": 'print()"; echo "hacked', "timeout": 1})
        self.assertTrue('hacked' not in response.text)


if __name__ == '__main__':
    unittest.main()
