import sys
import os
from datetime import datetime, timedelta
import threading
import util

REC_FILE = '/var/run/temperature_status'

class Checker():
    def __init__(self):
        self.rw_mutex = util.ReadWriteLock()

    def _get(self):
        try:
            with open(REC_FILE, 'r') as fin:
                return fin.read()
        except IOError:
            return '(Get recent temperature failed.)'

    def get(self):
        self.rw_mutex.acquire_read()
        content = self._get()
        self.rw_mutex.release_read()
        return content

    def _update(self):
        try:
            if not os.path.exists(REC_FILE):
                os.mknod(REC_FILE, 0o660)
            with open(REC_FILE, 'r+') as fin:
                lines = fin.readlines()
                util.update_temperature_status(lines)
                fin.seek(0)
                fin.writelines(lines)
        except PermissionError:
            sys.stderr.write('Fatal: run as a non-root user. Suicide.\n')
            sys.exit(-1)

    def update(self):
        self.rw_mutex.acquire_write()
        self._update()
        self.rw_mutex.release_write()
        self.start()

    def start(self):
        now = datetime.today()
        next_run = now.replace(day=now.day, hour=now.hour,
                    minute=0, second=0, microsecond=0) + \
                    timedelta(hours=1)
        time_left = next_run - now
        t = threading.Timer(time_left.total_seconds(),
            Checker.update, args=(self,))
        t.start()
