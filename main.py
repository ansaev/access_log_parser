from access_log_parser import AccessLogParser


parser = AccessLogParser()
parser.parse_file("access.log.test")
top_hosts = parser.get_top_requested_hosts()
for host in top_hosts[:10]:
    print(host['host'])
