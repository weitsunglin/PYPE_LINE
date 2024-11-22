import logging
from stage import Stage
from pipeline import Pipeline
from pipeline_ui import PipelineUI

def load_stage(script_path):
    spec = __import__(script_path, fromlist=['run'])
    return spec.run

if __name__ == "__main__":
    pipeline = Pipeline()

    # 安裝stage
    stage1 = Stage(name="Test_1", action=load_stage("stages.Test_1"))
    stage2 = Stage(name="Test_2", action=load_stage("stages.Test_2"), pre_task=[stage1])

    pipeline.add_stage(stage1)
    pipeline.add_stage(stage2)

    #工具UI
    pipeline_ui = PipelineUI(pipeline)
    pipeline_ui.start()