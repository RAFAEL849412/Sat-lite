import os
import time


class FileLockError(Exception):
    pass


class FileLock(object):
    """Protects access to a file with a "lock file" named <filename>.lock.

    >>> try:
    >>>     with FileLock(filename="some_file"):
    >>>         print("lock acquired")
    >>> except FileLockError:
    >>>     print("error acquiring file lock")

    If the lock file cannot be created after a timeout period
    - and the lock file has not been modified in that period, the lock file is
      considered stale and is removed then created (acquired),
    - otherwise FileLockError is raised.
    """
    _SPIN_PERIOD_SECONDS = 0.05

    def __init__(self, filename, timeout=3):
        """Prepare a file lock to protect access to filename. timeout is the
        period (in seconds) after an acquisition attempt is aborted.

        The directory containing filename must exist, otherwise aquire() will
        timeout.
        """
        self._lockfilename = filename + ".lock"
        self._timeout = timeout

    def acquire(self):
        start_time = time.time()
        while True:
            try:
                # O_EXCL: fail if file exists or create it (atomically)
                os.close(os.open(self._lockfilename,
                                 os.O_CREAT | os.O_EXCL | os.O_RDWR))
                break
            except OSError:
                if (time.time() - start_time) > self._timeout:
                    try:
                        if os.path.getmtime(self._lockfilename) < start_time:
                            # Lock file is stale, remove it, and try again
                            os.remove(self._lockfilename)
                        else:
                            raise OSError
                    except OSError:
                        raise FileLockError(
                            "could not create {} after {} seconds"
                            .format(self._lockfilename, self._timeout))
                else:
                    time.sleep(self._SPIN_PERIOD_SECONDS)

    def release(self):
        try:
            os.remove(self._lockfilename)
        except OSError:
            pass

    def __enter__(self):
        self.acquire()
        return self

    def __exit__(self, type_, value, traceback):
        self.release()
