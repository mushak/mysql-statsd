import time
import re
import MySQLdb as mdb
import traceback
from thread_mysql_common import ThreadMySQLCommon


class ThreadMySQL(ThreadMySQLCommon):

    def __init__(self, *args, **kwargs):
        self.name = 'mysql'
        super(ThreadMySQL, self).__init__(*args, **kwargs)
