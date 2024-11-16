import logging
from stage import Stage
from pipeline import Pipeline
from pipeline_ui import PipelineUI

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_stage(script_path):
    spec = __import__(script_path, fromlist=['run'])
    return spec.run

if __name__ == "__main__":
    pipeline = Pipeline()

    stage1 = Stage(name="List File", action=load_stage("stages.list_files"))
    stage2 = Stage(name="failing_stage", action=load_stage("stages.failing_stage"), pre_task=[stage1])
    stage3 = Stage(name="python_task", action=load_stage("stages.python_task"), pre_task=[stage2])

    pipeline.add_stage(stage1)
    pipeline.add_stage(stage2)
    pipeline.add_stage(stage3)

    pipeline_ui = PipelineUI(pipeline)
    pipeline_ui.start()
