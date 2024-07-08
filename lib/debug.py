#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
import ipdb
from models.people import People
from models.birthday import Birthday

People.create_table()
Birthday.create_table()
ipdb.set_trace()
