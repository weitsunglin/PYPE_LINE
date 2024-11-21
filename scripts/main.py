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
    stage1 = Stage(name="請先checkout win版環境", action=load_stage("stages.Tip"))
    stage2 = Stage(name="Visual Studio Debug ReleaseOpt", action=load_stage("stages.Debug_Release_OPT"), pre_task=[stage1])
    stage3 = Stage(name="cocos lua 加密 data", action=load_stage("stages.lua_to_dat"), pre_task=[stage2])
    stage4 = Stage(name="找出要更新的差異檔案", action=load_stage("stages.FindUpdateFile"), pre_task=[stage3])
    stage5 = Stage(name="動態更新檔到二測", action=load_stage("stages.Update_to_testing"), pre_task=[stage4])
    stage6 = Stage(name="動態更新檔到外部", action=load_stage("stages.Update_to_production"), pre_task=[stage5])
    stage7 = Stage(name="清除外部動態更新檔快取", action=load_stage("stages.Purge_Production"), pre_task=[stage6])

    pipeline.add_stage(stage1)
    pipeline.add_stage(stage2)
    pipeline.add_stage(stage3)
    pipeline.add_stage(stage4)
    pipeline.add_stage(stage5)
    pipeline.add_stage(stage6)
    pipeline.add_stage(stage7)

    #工具UI
    pipeline_ui = PipelineUI(pipeline)
    pipeline_ui.start()