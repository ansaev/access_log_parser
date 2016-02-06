import apache_log_parser


class AccessLogParser(object):
    def __init__(self):
        self.line_parser = None
        self.access_events = None

    def _get_file_content(self, file_name):
        assert file_name
        content = []
        return content

    def parse_file(self, file_name):
        assert file_name
        access_events = []
        content = self._get_file_content(file_name)
        access_events = self._parse_file_content(content)
        return access_events

    def _parse_file_content(self, content):
        assert content
        if self.line_parser is None:
            self.line_parser = apache_log_parser.make_parser("%h <<%P>> %t %Dus \"%r\" %>s %b  \"%{Referer}i\" \"%{User-Agent}i\" %l %u")
        self.access_events = []
        for line in content:
            access_event = self.line_parser(line)
            self.access_events.append(access_event)
        return self.access_events

    def group_by(self, parametr):
        assert self.access_events
        assert parametr




