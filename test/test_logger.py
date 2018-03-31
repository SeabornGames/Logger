import unittest

from seaborn_logger.logger import *


def hello():
    log.trace('Hello!')


class TraceTest(unittest.TestCase):
    def test_basic(self):
        log_file = os.path.join(os.path.split(__file__)[0],
                                __file__[:-3].replace('.','')+'.log')
        format = SeabornFormatter(relative_pathname= "/seaborn/seaborn/")
        format.setup_logging(log_filename=log_file,
                             log_level='TRACE',
                             log_stdout_level='TRACE')
        msg = 'testing'
        log.trace(msg)
        hello()
        return log

    def test_rotating_import(self):
        log = self.test_basic()
        try:
            from test.data import A
            from test.data import B_2
        except BaseException as e:
            log.trace(e.message)

    def test_request(self):
        import requests
        log_file = os.path.join(os.path.split(__file__)[0], '_test.log')
        SeabornFormatter(relative_pathname="/seaborn/seaborn/"
                         ).setup_logging(log_filename=log_file,
                                         silence_modules=['requests'],
                                         log_level='TRACE',
                                         log_stdout_level='TRACE')
        msg = "Test: Hello World (Logger Worked)"
        log.trace(msg)
        test_exclusion = requests.get('http://google.com')
        logged_message = open(log_file, 'r').read()
        assert logged_message.strip().endswith(msg), \
            'Bad Log Message: %s' % logged_message

if __name__ == '__main__':
    unittest.main()