import re
import requests
import json
from lbrynet.daemon.Daemon import Daemon as LBRYDaemon

for api_name, fn in LBRYDaemon.callable_methods.iteritems():
    # print("=" * 100)
    # print(fn.__doc__)
    returns = re.search(r'Returns:', fn.__doc__)
    returns_no_type = re.search(r'Returns:\n +\([A-z]+\)', fn.__doc__)
    returns_section = re.search(r'Returns:\n( +\([A-z]+\) (?:\n?.+)*)\n(?: +[^A-z])?', fn.__doc__)
    if returns_section is not None:
        print(returns_section.group(1))
        continue
        # if m.group(0) is not "Returns:\n":
        #     print("test")
        # print(m.group(0))
    else:
        continue
        if returns_no_type is None:
            print("{} docstring must specify a return value".format(api_name))
            continue
        if returns is None:
            print("{} docstring has no section matching 'Returns:'".format(api_name))
            continue

        print("{} docstring couldn't be parsed.".format(api_name))


def call(command):
    req = requests.post("http://0.0.0.0:5279/lbryapi", data=json.dumps(dict(method=command)))
    print(req.text)
