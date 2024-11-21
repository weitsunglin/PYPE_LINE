from stage import Stage
from status import Status

class Pipeline:

    def __init__(self):
        self.stages = []

    def add_stage(self, stage: Stage):
        self.stages.append(stage)

    def run(self, update_ui, finished_callback=None):
        for stage in self.stages:
            update_ui(stage, Status.RUNNING)
            stage.run(update_ui)
        if finished_callback:
            finished_callback()