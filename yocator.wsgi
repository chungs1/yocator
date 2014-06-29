#!flask/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)

from app import app as yocator
