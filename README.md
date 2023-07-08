# Self-use-ql-scripts
## 自用青龙脚本收集整理
每个脚本里面都有写有需要的具体东西和变量名


- [x] 目前有


  - [x] chinaUnicom:中国联通
  - [x] ddgy: 滴滴果园(https://raw.githubusercontent.com/leafTheFish/DeathNote/main/ddgy.js)
  - [x] dddc: 滴滴签到打卡领券周末5折、福利金领取、瓜瓜乐活动参加
  - [x] meituan: 美团领劵大额和一些领钱任务(https://raw.githubusercontent.com/leafTheFish/DeathNote/main/meituanV3.js)
  - [x] elm: 饿了么领劵大额和一些领钱任务(https://raw.githubusercontent.com/leafTheFish/DeathNote/main/elmV3.js)
  - [x] hdl：海底捞小程序
  - [x] hezj: 海尔智家
  - [x] iqiyi: 爱奇艺
  - [x] mxbc: 蜜雪冰城小程序
  - [x] sfsyV2: 顺丰速运
  - [x] xc: 喜茶小程序

## 青龙订阅任务


青龙面板，```订阅管理``` 页， 右上角 ```新建订阅```，将命令粘贴到```名称```栏，然后添加 ```定时规则```。
```
名称：自用
命令：ql repo https://github.com/milletbig/Self-use-ql-scripts.git "" "" "" "" py　js
定时规则：0 21 * * *
```