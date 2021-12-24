import os
from pathlib import Path
import threading
import subprocess

class ReadWriteLock:
    """ A lock object that allows many simultaneous "read locks", but
    only one "write lock." """

    def __init__(self):
        self._read_ready = threading.Condition(threading.Lock())
        self._readers = 0

    def acquire_read(self):
        """ Acquire a read lock. Blocks only if a thread has
        acquired the write lock. """
        self._read_ready.acquire()
        try:
            self._readers += 1
        finally:
            self._read_ready.release()

    def release_read(self):
        """ Release a read lock. """
        self._read_ready.acquire()
        try:
            self._readers -= 1
            if not self._readers:
                self._read_ready.notifyAll()
        finally:
            self._read_ready.release()

    def acquire_write(self):
        """ Acquire a write lock. Blocks until there are no
        acquired read or write locks. """
        self._read_ready.acquire()
        while self._readers > 0:
            self._read_ready.wait()

    def release_write(self):
        """ Release a write lock. """
        self._read_ready.release()

MAX_TEMPERATURE_STATUS_KEPTED = 25
def update_temperature_status(lines):
	status = subprocess.run(os.path.join(Path(__file__).parent.parent.absolute(), 'instant-get.sh'), capture_output=True, text=True).stdout
	lines.insert(0, status)
	if len(lines) > MAX_TEMPERATURE_STATUS_KEPTED:
		del lines[MAX_TEMPERATURE_STATUS_KEPTED:]
