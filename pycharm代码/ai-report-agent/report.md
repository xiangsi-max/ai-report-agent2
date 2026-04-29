
一、问题分析：
本题采用SIR模型研究疫情传播。

二、数学建模：
dS/dt = -βSI
dI/dt = βSI - γI
dR/dt = γI

三、Python代码：
使用scipy求解微分方程

四、结果分析：
感染人数呈现先上升后下降趋势
