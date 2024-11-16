import time
import subprocess
from status import Status

class Stage:
    def __init__(self, name, action, pre_task=None):
        self.name = name
        self.action = action
        self.pre_task = pre_task or []
        self.status = Status.PENDING
        self.elapsed_time = 0

    def run(self, update_ui):
        if any(task.status != Status.SUCCESS for task in self.pre_task):
            self.status = Status.SKIPPED
            if update_ui:
                update_ui(self, self.status)
            return
        start_time = time.time()
        try:
            self.status = Status.RUNNING
            while True:
                time.sleep(0.1)
                self.elapsed_time = time.time() - start_time
                if update_ui:
                    update_ui(self, self.status)
                if isinstance(self.action, str):
                    subprocess.run(self.action, shell=True, check=True, text=True)
                    break
                else:
                    self.action()
                    break
            self.status = Status.SUCCESS
        except Exception:
            self.status = Status.FAILED
        finally:
            self.elapsed_time = time.time() - start_time
            if update_ui:
                update_ui(self, self.status)
