import pytest
from access_log_parser import AccessLogParser


class TestClass:
    @pytest.fixture(params=[{'name': 'file_test', 'content': ['file_content']}])
    def file(self, request):
        return request.param

    @pytest.fixture(params=[
        {"data": [
            '127.0.0.1 <<6113>> [16/Aug/2013:15:45:34 +0000] 1966093us "GET / HTTP/1.1" 200 3478  "https://example.com/" "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.18)" - -',
            '127.0.0.1 <<6113>> [16/Aug/2013:15:45:34 +0000] 1966093us "GET / HTTP/1.1" 200 3478  "https://example.com/" "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.18)" - -',
            '192.0.0.1 <<6113>> [16/Aug/2013:15:45:34 +0000] 1966093us "GET / HTTP/1.1" 200 3478  "https://example.com/" "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.18)" - -',
                  ],
            "group_by": {"param": "remote_host", "rez": [{"host": "127.0.0.1", "requests": 2}, {"host": "192.0.0.1", "requests": 1}]},
            "hosts": ["127.0.0.1", "127.0.0.1", "192.0.0.1"],
            "top_hosts": [{"host": "127.0.0.1", "requests": 2}, {"host": "192.0.0.1", "requests": 1}]
         }
    ])
    def file_content(self, request):
        return request.param

    def test_page_content_parser(self, file_content):
        parser = AccessLogParser()
        parsed = parser._parse_file_content(file_content['data'])
        assert [pars['remote_host'] for pars in parsed] == file_content['hosts']

    def test_group_by(self, file_content):
        parser = AccessLogParser()
        parser._parse_file_content(file_content['data'])
        group_by = file_content["group_by"]
        parser.group_by(group_by['param'])
        parsed_data = parser.access_events
        rez = group_by['rez']
        assert len(parsed_data) == len(rez)
        for item in rez:
            assert item['requests'] == len(parsed_data[item['host']])

    def test_top_hosts(self, file_content):
        parser = AccessLogParser()
        parsed = parser._parse_file_content(file_content['data'])
        top_req = parser.get_top_requested_hosts()
        assert top_req == file_content["top_hosts"]

    def test_get_file_content(self, file):
        parser = AccessLogParser()
        content = parser._get_file_content(file['name'])
        assert content == file['content']

