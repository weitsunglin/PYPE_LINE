# PYPE_LINE
由於架設 jenkins 流程過於繁瑣， 因此自製 windows pipeline 工具，可 call Windows CLI 及 Python api。

- 有三個pending的stage準備被執行
![demo1](https://github.com/weitsunglin/PYPE_LINE/blob/main/demo1.jpg)

- List File 正在被執行
![demo2](https://github.com/weitsunglin/PYPE_LINE/blob/main/demo2.jpg)

- List File 執行完，費時58.61秒，執行到failing_stage失敗，所以python_task 跟著被SKIPPED
![demo3](https://github.com/weitsunglin/PYPE_LINE/blob/main/demo3.jpg)
