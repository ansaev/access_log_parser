import pytest
from access_log_parser import AccessLogParser


class TestClass:
    @pytest.fixture(params=[{"line": '127.0.0.1 <<6113>> [16/Aug/2013:15:45:34 +0000] 1966093us "GET / HTTP/1.1" 200 3478  "https://example.com/" "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.18)" - -', "host": "127.0.0.1"}])
    def file_content(self, request):
        return request.param

    def test_page_contentParser(self, file_content):
        parser = AccessLogParser()
        parsed = parser._parse_file_content([file_content['line']])[0]
        print(parsed)
        assert parsed['remote_host'] == file_content['host']
