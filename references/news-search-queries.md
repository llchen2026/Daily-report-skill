# 分区域新闻搜索查询模板

> 每次运行技能时，对以下区域和品类执行 WebSearch。
> 时间窗口: 过去32小时。
> 使用 `query_keyword_groups` 参数同时搜索多个关键词组。

## 一、原油 (Crude Oil)

### 全球/基准
```
query: "crude oil price Brent WTI latest news"
query_keyword_groups: [
  "Brent crude oil price today",
  "WTI crude oil price latest",
  "OPEC crude oil production decision latest",
  "布伦特原油 WTI原油 最新价格"
]
```

### 中东原油
```
query: "Middle East crude oil supply disruption Saudi Iran Iraq latest"
query_keyword_groups: [
  "Saudi Arabia crude oil production news",
  "Iran oil export sanctions latest news",
  "Iraq Basra oil export disruption",
  "中东 原油 供应 最新动态"
]
```

### 俄罗斯原油
```
query: "Russia crude oil export production news latest"
query_keyword_groups: [
  "Russia oil refinery attack drone latest",
  "Russian crude oil export sanctions news",
  "俄罗斯 炼厂 袭击 最新消息"
]
```

## 二、成品油 (Refined Products)

### 全球成品油
```
query: "refined products gasoline diesel jet fuel price news latest"
query_keyword_groups: [
  "gasoline crack spread latest news",
  "diesel gasoil price Europe ARA latest",
  "jet fuel aviation fuel supply disruption",
  "成品油 汽油 柴油 航煤 价格 最新"
]
```

### 区域裂解价差
```
query: "regional refining margin crack spread Singapore Rotterdam latest"
query_keyword_groups: [
  "Singapore complex refining margin latest",
  "Rotterdam gasoline crack spread news",
  "US Gulf Coast refining margin latest",
  "新加坡 鹿特丹 炼化利润 裂解价差"
]
```

## 三、霍尔木兹海峡 (Strait of Hormuz)

```
query: "Strait of Hormuz shipping traffic closure latest"
query_keyword_groups: [
  "Hormuz strait shipping disruption latest news",
  "Persian Gulf tanker attack incident latest",
  "霍尔木兹海峡 通航 油轮 最新动态",
  "Fujairah Yanbu oil tanker departure latest"
]
```

## 四、地缘冲突事件 (Geopolitical Events)

### 以色列-伊朗
```
query: "Israel Iran conflict oil infrastructure attack latest"
query_keyword_groups: [
  "Israel Iran military strike latest news",
  "Iran oil facility attack damage assessment",
  "以色列 伊朗 军事冲突 油田设施 最新"
]
```

### 红海/胡塞武装
```
query: "Red Sea Houthi shipping attack oil tanker latest"
query_keyword_groups: [
  "Houthi Red Sea attack oil tanker latest",
  "Suez Canal shipping disruption latest news",
  "红海 胡塞武装 油轮 袭击 最新"
]
```

### 更广泛中东
```
query: "Middle East geopolitics oil supply risk latest"
query_keyword_groups: [
  "Saudi Arabia oil facility security threat latest",
  "Iraq oil pipeline attack latest news",
  "Gulf cooperation council oil policy latest",
  "中东 地缘政治 石油供应 风险 最新"
]
```

## 五、美国经济指标 (US Economic Indicators)

```
query: "US economic indicators oil demand GDP inflation latest release"
query_keyword_groups: [
  "US CPI inflation data latest release oil impact",
  "US jobless claims nonfarm payrolls latest",
  "EIA crude oil inventory report this week",
  "美联储 利率决议 原油需求 影响 最新"
]
```

### EIA周报特别关注
```
query: "EIA weekly petroleum status report crude inventory latest"
query_keyword_groups: [
  "EIA crude oil inventory change latest week",
  "US gasoline distillate inventory EIA report",
  "美国 EIA 原油库存 周报 最新"
]
```

## 六、全球重点国家库存 (Global Inventory)

### 美国
```
query: "US crude oil gasoline inventory EIA latest week"
query_keyword_groups: [
  "Cushing Oklahoma crude oil inventory latest",
  "US strategic petroleum reserve SPR latest",
  "美国 战略石油储备 SPR 库存 最新"
]
```

### 欧洲
```
query: "Europe ARA gasoline naphtha diesel inventory latest"
query_keyword_groups: [
  "Europe ARA product stocks latest week",
  "Europe natural gas storage GIE AGSI latest",
  "欧洲 ARA 油品 库存 天然气 储存 最新"
]
```

### 新加坡/亚洲
```
query: "Singapore fuel oil inventory residuals latest week"
query_keyword_groups: [
  "Singapore light middistillate fuel oil stock latest",
  "Japan Korea crude oil inventory latest",
  "India crude oil strategic reserve latest",
  "新加坡 燃料油 库存 日韩 原油 印度 最新"
]
```

### 中国
```
query: "China crude oil inventory SPR independent refinery teapot latest"
query_keyword_groups: [
  "China crude oil stockpile SPR latest news",
  "China independent refinery teapot utilization rate latest",
  "中国 原油库存 独立炼厂 开工率 最新"
]
```

## 七、重点化工品 (Key Chemicals)

### 烯烃链
```
query: "ethylene propylene butadiene price news naphtha cracker latest"
query_keyword_groups: [
  "ethylene price Asia naphtha cracker news latest",
  "propylene price polymer grade latest",
  "butadiene price Asia supply disruption",
  "乙烯 丙烯 丁二烯 价格 裂解装置 最新"
]
```

### 芳烃/醇类
```
query: "methanol acetic acid acrylic acid price news latest"
query_keyword_groups: [
  "methanol price Asia supply news latest",
  "acetic acid price supply disruption latest",
  "甲醇 醋酸 丙烯酸 价格 供应 最新"
]
```

### 聚氨酯/氯碱
```
query: "MDI TDI PVC price news force majeure latest"
query_keyword_groups: [
  "MDI TDI price Wanhua force majeure latest",
  "PVC price Asia Europe supply news latest",
  "MDI TDI PVC 价格 万华 不可抗力 最新"
]
```

## 八、搜索结果处理规则

1. **去重规则**: 同一事件被多个来源报道时，保留最早来源 + 最权威来源（Reuters > Bloomberg > 官方声明 > 本地媒体）
2. **时间过滤**: 只保留发布时间在过去32小时内的新闻
3. **可信度标记**: A=Reuters/Bloomberg/官方; B=行业媒体; C=本地媒体/社交媒体
4. **边际变化标注**: 与看板基线对照后，标注是否为"新边际变化"或"仅确认旧状态"
5. **关联性过滤**: 排除与能源化工无关的地缘新闻
