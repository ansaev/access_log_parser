import pytest
from access_log_parser import AccessLogParser


class TestClass:
    @pytest.fixture(params=["<body> <p style='font-size: 12pt'>Example</p></body>"])
    def file_content(self, request):
        return request.param

    @pytest.fixture(params=["http://habrahabr.ru/some/", "http://www.oracle.com/some/index.html"])
    def line_content(self, request):
        return request.param

    def test_style_cleaner(self, page):
        page = StyleCleanerService._clear_page(page)
        assert "style=" not in page
