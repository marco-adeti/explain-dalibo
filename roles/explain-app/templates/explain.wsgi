#!/usr/bin/env python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/srv/{{app_name}}/")

from app import app as application
