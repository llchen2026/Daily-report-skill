# Daily Report Skill — 中东能源化工情报与投资观点生成

> WorkBuddy 技能包，适用于每日/每班次的能源化工研究与投资观点跟踪。

## 功能概述

自动执行以下完整流程：

1. **抓取看板数据** — 从全球能源化工AI看板提取聚合指标、资产修复进度、航运态势
2. **并行验证 + 价格采集** — 两层验证（看板聚合确认 + 资产级核实）确认数据可靠性；同时通过 akshare 获取国内18个能化期货实时价格
3. **合并新闻搜索** — 7大区域新闻 + 政策法规强制搜索 + 化工品强势品种专项搜索
4. **标准化去重沉淀** — 四层置信度分层(T1-T4)、四维分析(基本面/政策面/情绪面/成本链路)、JSONL清洗底座
5. **投资观点看板** — 生成原油/区域成品油/强势化工品的短期+中期观点HTML看板并截图

## 技能结构

```
middle-east-oil-intel/
├── SKILL.md                              # 技能主文件（5步执行流程 + 12条关键规则）
├── references/
│   ├── dashboard-structure.md            # 看板数据结构与基线对照表
│   ├── critical-assets-verification.md   # 关键资产状态滚动核实清单（37个资产）
│   ├── news-search-queries.md            # 分区域新闻搜索查询模板（7大区域中英双语）
│   ├── news-standardization-schema.md    # 新闻标准化沉淀Schema（含四维标注）
│   └── china-oil-pricing-mechanism.md    # 中国成品油定价机制（发改委[2016]64号）
├── assets/
│   └── dashboard-template.html           # 投资观点看板HTML模板（浅色主题）
└── scripts/
    ├── generate_dashboard.py             # HTML模板填充脚本
    ├── fetch_akshare_data.py             # 18个能化期货品种实时价格采集
    └── deduplicate_news.py              # 新闻去重与JSONL沉淀管理
```

## 安装方式

### 方式一：安装到 WorkBuddy

将整个目录复制到 WorkBuddy 的技能目录：

```bash
# 用户级（全局可用）
cp -r middle-east-oil-intel ~/.workbuddy/skills/

# 或项目级（仅当前项目）
cp -r middle-east-oil-intel <workspace>/.workbuddy/skills/
```

### 方式二：通过技能管理器导入

在 WorkBuddy 中使用 `expert-manager` 技能导入。

## 依赖

- **Python 3.11+**：运行 akshare 采集和去重脚本
- **akshare**：国内能化期货数据 `pip install akshare`
- **Playwright**：看板截图 `pip install playwright && playwright install chromium`

## 使用方式

在 WorkBuddy 对话中触发：

```
执行中东能源看板
来一份能化日报
oil intelligence report
```

或直接说："执行 middle-east-oil-intel 技能"。

## 关键规则摘要

- **两层验证**：看板数据必须经过独立搜索double check才能用于观点，无法验证的数据改用 IEA/EIA/OPEC 权威数据
- **化工品分化**：品种间存在显著分化，筛选2-3个强势品种独立分析
- **政策法规强制搜索**：涉及政策/法规/制裁的内容严禁依赖模型内置知识，必须搜索法规原文
- **中国成品油定价**：公式化联动机制（Brent+Dubai+Minas十日均价），禁主观表述

## 免责声明

生成的看板底部包含"不构成投资建议"声明，仅供研究参考。
