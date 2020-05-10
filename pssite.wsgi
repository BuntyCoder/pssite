#! /usr/bin/python3

import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/html/pssite/pssite')
from pssite import app as application
application.secret_key = 1234