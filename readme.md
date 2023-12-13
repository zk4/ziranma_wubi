
效果如下

![iShot_2023-12-12_18.53.55](assets/iShot_2023-12-12_18.53.55.gif)

用了15年五笔，放弃了，严重影响思维。简单字还行，打复杂的成语，速度骤降。
改用双拼，能说基本能打。但五笔可以做为辅助码。两不误。
研究了一堆 MAC 下的输入法，最终还是手心最简单也合适。



## 目标

自然码+五笔辅助码. 能快速定位单字, 词组

## 要求
1. 越少待选越好，只过滤简体。
2. 能过滤单字，也能过滤词组。
3. 辅助码越简单越好。只过滤第一笔. 当然，还是会有重码，但基本上少到可以忽略不记。


## 实验
1. rime，本来寄希望于此。但是折腾了半天，只能定义单字辅助码。词频我实在是看不懂。文档也非常隐晦。看的我脑壳疼。半放弃。以后有空研究下lua 脚本看能不能解决。
2. 落格，提示太跳了，而且还要付费。而且付费了还得每次验证。放弃
3. 搜狗，微信输入法，没有辅助码，而且还收集个人信息，有广告。 完全放弃



## 直接使用
手心输入法导入shouxin_wubi.txt 为辅助码即可使用


注意：**手心输入法风险**
1. 未开源
2. 有云输入，可能有隐私风险
3. 2015 年就停止更新了


## 码表生成
如果觉得 shouxin_wubi.txt 不给力。可以修改以下代码重新生成。
```
python convert_wubi.py
```

