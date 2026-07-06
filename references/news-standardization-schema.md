# 新闻标准化沉淀 Schema

> 用于将每日搜索到的新闻标准化后沉淀为 JSONL 格式，作为后续去重、边际变化追踪和置信度分层的清洗底座。
> 文件存储路径: `outputs/news-store/YYYY-MM.jsonl`（按月归档，每行一条JSON记录）

## 一、字段定义

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `event_id` | string | ✅ | 事件唯一ID，格式 `EVT-YYYYMMDD-XXXX`（XXXX为当日序号） |
| `dedup_hash` | string | ✅ | 去重哈希，基于 `实体集合+事件类型+数值变化` 的 MD5 前12位 |
| `title` | string | ✅ | 标题（保留原文，不做翻译） |
| `summary` | string | ✅ | 3-5句事件摘要 |
| `publish_time` | ISO8601 | ✅ | 发布时间，统一转为北京时间(GMT+8) |
| `fetch_time` | ISO8601 | ✅ | 抓取时间 |
| `source_name` | string | ✅ | 来源名称（如 Reuters, Bloomberg, CNBC, OilPrice） |
| `source_url` | string | ✅ | 原文链接 |
| `source_tier` | enum | ✅ | 来源层级: `T1-权威` / `T2-行业` / `T3-区域` / `T4-社交` |
| `confidence` | enum | ✅ | 事件置信度: `confirmed` / `likely` / `unconfirmed` / `speculative` |
| `region` | array | ✅ | 相关区域（如 `["中东","沙特"]`） |
| `category` | enum | ✅ | 内容类别: `crude` / `refined` / `chemical` / `geopolitics` / `macro` / `shipping` |
| `entities` | object | ✅ | 命中实体（资产名/国家/品种/公司，用于去重和关联） |
| `event_type` | enum | ✅ | 事件类型（见下方枚举表） |
| `marginal_type` | enum | ✅ | 边际判定: `new_edge` / `confirms_baseline` / `no_change` |
| `baseline_ref` | string | ⬜ | 当 marginal_type 为 confirms/no_change 时，引用基线表中的资产条目 |
| `value_change` | object | ⬜ | 数值变化 `{metric, old, new, unit}` |
| `asset_refs` | array | ⬜ | 关联看板资产（资产修复进度表中的资产名称列表） |
| `analysis_dims` | object | ✅ | 分析维度标注（见第三节） |
| `related_news_ids` | array | ⬜ | 关联的其他 event_id（同一事件不同来源） |

## 二、枚举值定义

### source_tier（来源层级）

| 层级 | 代码 | 说明 | 示例来源 |
|------|------|------|----------|
| T1-权威 | `T1` | 通讯社/官方统计/运营商公告 | Reuters, Bloomberg, EIA, IEA, OPEC, 官方声明 |
| T2-行业 | `T2` | 行业专业媒体 | Argus, Platts/S&P Global, OilPrice, WorldOil, ICIS, RBN Energy |
| T3-区域 | `T3` | 区域性新闻/财经媒体 | CNBC, Livemint, TimesKuwait, MarineInsight, Jujindata |
| T4-社交 | `T4` | 社交媒体/开源情报 | Telegram频道, X/Twitter, United24Media, OSINT账号 |

### confidence（事件置信度）

| 置信度 | 代码 | 判定标准 |
|--------|------|----------|
| Confirmed | `confirmed` | T1来源确认 / 运营商官方公告 / 现场影像证据 |
| Likely | `likely` | T2来源交叉验证 / 单一T1来源但证据链较完整 |
| Unconfirmed | `unconfirmed` | 仅T3-T4来源 / 缺少独立交叉验证 / "据消息人士" |
| Speculative | `speculative` | 分析师推测 / 假设性推演 / "可能"/"预计" |

### event_type（事件类型）

| 类型 | 代码 | 说明 |
|------|------|------|
| 资产受袭 | `asset_strike` | 炼厂/油田/港口遭无人机/导弹袭击 |
| 产能变化 | `capacity_change` | 停产/复产/减产/降负/提负 |
| 不可抗力 | `force_majeure` | 运营商发布FM通知 |
| 修复进展 | `recovery_update` | 修复ETA变化 / 修复阶段更新 |
| 海峡通行 | `hormuz_transit` | 海峡状态变化/通行数变化/滞留变化 |
| 航运事件 | `shipping_incident` | 油轮遭袭/扣押/绕行变化 |
| 价格变动 | `price_move` | 原油/成品油/化工品价格大幅变动 |
| 库存变化 | `inventory_change` | EIA/ARA/JODI/SPR库存数据 |
| 政策决议 | `policy_decision` | OPEC+决议/燃料优先指令/出口禁令/制裁 |
| 宏观数据 | `macro_data` | 就业/CPI/PMI/利率决议 |
| 地缘升级 | `geopolitical_escalation` | 军事行动升级/停火/外交突破 |
| 永久退出 | `permanent_exit` | 产能永久关闭/企业清退 |

### category（内容类别）

| 代码 | 覆盖范围 |
|------|----------|
| `crude` | 原油（Brent/WTI/SC/OPEC+产量） |
| `refined` | 成品油（汽油/柴油/航煤/燃料油/裂解价差） |
| `chemical` | 化工品（烯烃/芳烃/醇类/氯碱/聚氨酯） |
| `geopolitics` | 地缘冲突（以伊/红海/胡塞/制裁） |
| `macro` | 宏观经济（就业/CPI/PMI/利率） |
| `shipping` | 航运物流（海峡/港口/油轮/管网） |

## 三、analysis_dims（分析维度标注）

每条新闻需标注其对四个分析面的影响方向：

```json
"analysis_dims": {
    "fundamental": {
        "direction": "bullish|bearish|neutral",
        "impact": "high|medium|low",
        "note": "基本面影响说明"
    },
    "policy": {
        "direction": "bullish|bearish|neutral",
        "impact": "high|medium|low",
        "note": "政策面影响说明"
    },
    "sentiment": {
        "direction": "bullish|bearish|neutral",
        "impact": "high|medium|low",
        "note": "情绪面影响说明"
    },
    "cost_chain": {
        "direction": "bullish|bearish|neutral",
        "impact": "high|medium|low",
        "note": "成本链路传导说明"
    }
}
```

### 四维分析框架定义

| 维度 | 定义 | 关键信号 |
|------|------|----------|
| **基本面 (Fundamental)** | 供需平衡、产能利用率、库存水平 | 供应缺口、装置开工率、库存可用天数、OPEC+产量 |
| **政策面 (Policy)** | 政府/OPEC/运营商的行政性决策 | OPEC+增产/减产、出口禁令、制裁、燃料优先指令、利率路径 |
| **情绪面 (Sentiment)** | 市场预期、风险溢价、资金流向 | Polymarket概率、风险溢价、CFTC持仓、期权偏度、新闻密度 |
| **成本链路 (Cost Chain)** | 从原料到终端的成本传导路径 | 石脑油→烯烃→聚合物传导、乙烷→乙烯、煤炭→甲醇→烯烃 |

## 四、去重哈希算法

```
dedup_hash = MD5(
    sorted(entities).join("|")     # 实体集合（排序后）
    + event_type                    # 事件类型
    + value_change.metric           # 变化指标（如有）
    + date(publish_time)            // 日期级粒度（同一天的同实体同类型事件视为重复）
)[:12]
```

**示例**:
- NORSI炼厂7月3日遭袭 → 实体: `["NORSI","Kstovo","Russia"]`, 类型: `asset_strike`
- 同一事件被 Reuters 和 United24 报道 → 生成相同的 dedup_hash → 自动识别为重复

## 五、JSONL 记录示例

```json
{
    "event_id": "EVT-20260703-0001",
    "dedup_hash": "a3f8b2c1d9e0",
    "title": "Major Russian oil refinery suspends operations again after Ukrainian drone strike",
    "summary": "Lukoil-NORSI/Kstovo炼厂7月3日遭乌克兰无人机袭击，AVT-6一次加工装置受损起火，全厂停产。这是6月25日CDU-5受损后的第二次停产。该厂年加工能力约1700万吨，为俄罗斯第四大炼厂。",
    "publish_time": "2026-07-03T08:00:00+08:00",
    "fetch_time": "2026-07-04T21:15:00+08:00",
    "source_name": "Reuters",
    "source_url": "https://www.yahoo.com/news/world/articles/major-russian-oil-refinery-suspends-201152742.html",
    "source_tier": "T1",
    "confidence": "confirmed",
    "region": ["俄罗斯","乌克兰"],
    "category": "refined",
    "entities": {"assets": ["NORSI","Kstovo"], "countries": ["Russia","Ukraine"], "companies": ["Lukoil"]},
    "event_type": "asset_strike",
    "marginal_type": "new_edge",
    "baseline_ref": "Lukoil-NORSI/Kstovo",
    "value_change": {"metric": "capacity_status", "old": "受袭待核T+120", "new": "全厂停产确认", "unit": "status"},
    "asset_refs": ["Lukoil-NORSI / Kstovo"],
    "analysis_dims": {
        "fundamental": {"direction": "bullish", "impact": "high", "note": "俄第四大炼厂停产，进一步收紧全球成品油供给"},
        "policy": {"direction": "neutral", "impact": "low", "note": "无直接政策影响"},
        "sentiment": {"direction": "bullish", "impact": "medium", "note": "市场担忧俄炼系统性瘫痪"},
        "cost_chain": {"direction": "bullish", "impact": "high", "note": "汽油/柴油出口收紧→裂解价差走阔→石脑油分流加剧→烯烃成本上行"}
    },
    "related_news_ids": ["EVT-20260703-0002"]
}
```

## 六、沉淀文件管理

1. **文件位置**: `outputs/news-store/YYYY-MM.jsonl`（按月归档）
2. **写入规则**: 每次技能执行时，将当日标准化后的新闻追加写入当月文件
3. **去重检查**: 写入前，读取当月+上月文件，对新记录的 `dedup_hash` 做集合比对，跳过已存在的
4. **边际追踪**: 读取最近30天的记录，构建"资产→最新状态"映射表，用于与看板基线对照
5. **文件大小**: 单月预计约 200-500 条记录，JSONL 格式天然适合流式读取和增量写入
