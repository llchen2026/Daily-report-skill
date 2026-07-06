# 关键资产状态滚动核实清单

> 看板基线可能滞后。以下资产的状态变更会实质影响投资观点，每次执行必须逐项搜索核实。
> 核实结果用于覆盖/修正基线，在看板"资产状态核实"板块展示基线vs核实状态。

## 核实优先级

- **P0（必须核实）**：产能损失 >500 kbd 的上游资产 + 全部"全境熔断/完全停产/完全摧毁"资产
- **P1（应当核实）**：产能损失 100-500 kbd 的资产 + 所有修复ETA临近（≤30天）的资产
- **P2（滚动覆盖）**：其余中游炼化/下游枢纽/化工装置

## 一、上游资产（P0/P1）

| 优先级 | 国家 | 资产 | 看板基线状态 | 看板基线损失 | 搜索关键词（EN） | 搜索关键词（CN） |
|--------|------|------|-------------|-------------|-----------------|-----------------|
| P0 | 沙特 | Safaniya/Marjan | 物流性停产 | -2,500 kbd | "Safaniya oil field production status", "Saudi Safaniya restart" | "萨法尼亚 油田 复产 最新" |
| P0 | 沙特 | Khurais | 物理损毁 | -300 kbd | "Khurais oil field damage repair", "Saudi Khurais production" | "库赖斯 油田 损毁 修复" |
| P0 | 沙特 | Ghawar | 正常/调峰 | 0 | "Ghawar oil field production capacity", "Saudi Ghawar output" | "加瓦尔 油田 产量 最新" |
| P0 | 伊拉克 | Rumaila/W.Qurna2 | 库满/FM | -1,800 kbd | "Rumaila oil field production force majeure", "Iraq Rumaila export" | "鲁迈拉 油田 不可抗力 出口" |
| P0 | 伊拉克 | Maysan油田群 | 不可抗力 | -200 kbd | "Maysan oil field Iraq production" | "米桑 油田 伊拉克 产量" |
| P0 | 科威特 | Greater Burgan | 全境熔断 | 100%出口 | "Kuwait Burgan oil field production shutdown", "Kuwait oil export force majeure" | "科威特 布尔甘 油田 熔断 出口" |
| P0 | 俄罗斯 | 西西伯利亚集群 | 减产 | -1,500 kbd | "Russia oil production western Siberia", "Russian crude oil output latest" | "俄罗斯 原油产量 西西伯利亚 减产" |
| P1 | 伊朗 | South Pars | 正常/内供 | 0 | "Iran South Pars gas field production", "Iran oil export sanctions" | "伊朗 南帕尔斯 气田 产量 制裁" |
| P1 | 伊拉克 | Khor Mor(气田) | 暂停 | -750 mcm/d | "Khor Mor gas field Iraq", "Iraq gas production Kurdish region" | "霍尔莫尔 气田 伊拉克 库尔德" |

### 一-B、卡塔尔LNG/天然气资产（P0）

> 卡塔尔LNG受损情况有充分的T1来源支撑（QatarEnergy能源部长声明+Reuters/Bloomberg/Offshore Energy），不得标注为UNVERIFIED。
> 核实时需区分三起独立事件：3月导弹袭击（LNG出口产能受损）、12月-6月Barzan维护-重启-爆炸（国内天然气，非LNG出口）、霍尔木兹海峡关闭（物流性停产叠加）。

| 优先级 | 资产 | 事件 | 看板基线状态 | 已确认损失 | 搜索关键词（EN） | 搜索关键词（CN） |
|--------|------|------|-------------|-----------|-----------------|-----------------|
| P0 | Ras Laffan LNG Trains 4 & 6 | 3月18-19日伊朗导弹袭击 | 受损停产 | -12.8 MTPA（≈17%出口产能） | "Qatar LNG Train 4 6 damage missile attack Ras Laffan", "QatarEnergy LNG capacity offline 2026" | "卡塔尔 LNG 生产线 导弹 袭击 拉斯拉凡" |
| P0 | Pearl GTL（Shell运营） | 3月18-19日伊朗导弹袭击 | 1条train受损，至少1年离线 | GTL产能损失（非LNG但计入天然气加工） | "Pearl GTL Qatar damage Shell offline", "Qatar Pearl gas-to-liquids repair" | "卡塔尔 Pearl GTL 壳牌 损毁 修复" |
| P0 | Barzan Gas Plant | 12月停机维护→6月19日重启→6月21日爆炸 | 重启失败，停产中 | 1.4 BCF/d国内管道气（非LNG出口），13死66伤 | "Barzan gas plant explosion QatarEnergy June 2026", "Barzan restart failure Ras Laffan" | "卡塔尔 Barzan 爆炸 重启 2026" |
| P0 | 卡塔尔LNG整体出口 | 霍尔木兹海峡关闭+设施受损双重影响 | FM声明+出口基本停滞 | 看42.5 mtpa口径含物流性停产折算 | "Qatar LNG export force majeure 2026", "Qatar LNG shipping resumption Hormuz" | "卡塔尔 LNG 不可抗力 出口 恢复" |

**核实要点**：
1. Train 4/6的12.8 MTPA是能源部长Al-Kaabi亲自确认的（T1），$200亿/年收入损失，**已有充分来源支撑**
2. Pearl GTL的"至少1年离线"是QatarEnergy官方声明（T1），需核实最新修复进展
3. Barzan爆炸（6月21日）QatarEnergy官方声明LNG出口不受影响——Barzan是**国内天然气**设施，不直接向LNG出口线供气
4. 看板42.5 mtpa口径需拆解：12.8 MTPA（Trains物理受损）+ Pearl GTL折算 + 物流性停产折算（海峡关闭导致出口停滞的等效产能损失）
5. 6月底-7月初的复供进展：空载LNG船返回波斯湾、QatarEnergy计划数周内恢复主要产能，需搜索最新进展

## 二、中游炼化资产（P1/P2）

| 优先级 | 国家 | 资产 | 看板基线状态 | 修复ETA | 搜索关键词（EN） | 搜索关键词（CN） |
|--------|------|------|-------------|---------|-----------------|-----------------|
| P1 | 俄罗斯 | Kirishi/KINEF | 完全停产 | T+270 | "Kirishi KINEF refinery attack drone", "Russia Kirishi refinery status" | "基里什 炼厂 袭击 无人机" |
| P1 | 俄罗斯 | Ryazan | 完全停产 | T+210 | "Ryazan refinery attack damage", "Russia Ryazan refinery status" | "梁赞 炼厂 袭击 状态" |
| P1 | 俄罗斯 | Lukoil-NORSI/Kstovo | 受袭待核→确认停产 | T+120 | "Lukoil NORSI Kstovo refinery drone attack", "Nizhny Novgorod refinery" | "下诺夫哥罗德 炼厂 无人机 NORSI" |
| P1 | 俄罗斯 | Lukoil-Permnefteorgsintez | 完全停运 | T+210 | "Permnefteorgsintez refinery attack", "Lukoil Perm refinery status" | "彼尔姆 炼厂 卢克 袭击" |
| P1 | 俄罗斯 | Tuapse | 停运/严重受限 | T+180 | "Tuapse refinery Rosneft attack", "Russia Tuapse refinery status" | "图阿普谢 炼厂 袭击 状态" |
| P2 | 俄罗斯 | Slavneft-YANOS | 严重降负 | T+120 | "Slavneft Yaroslavl refinery attack" | "斯拉夫石油 雅罗斯拉夫尔 炼厂" |
| P2 | 俄罗斯 | Novokuybyshevsk | 主加工停运 | T+120 | "Novokuybyshevsk refinery Rosneft" | "新古比雪夫 炼厂" |
| P2 | 俄罗斯 | Syzran | CDU-6停运 | T+150 | "Syzran refinery attack" | "塞兹兰 炼厂 袭击" |
| P2 | 俄罗斯 | Saratov | CDU停运待核 | T+120 | "Saratov refinery attack damage" | "萨拉托夫 炼厂 袭击" |
| P2 | 俄罗斯 | Volgograd | CDU-1受损 | T+150 | "Volgograd refinery Lukoil attack" | "伏尔加格勒 炼厂 袭击" |
| P2 | 俄罗斯 | Moscow/Kapotnya | 保护性停工 | T+14 | "Moscow Kapotnya refinery" | "莫斯科 卡波特尼亚 炼厂" |
| P1 | 科威特 | Mina Al-Ahmadi | 完全熔断 | T+165 | "Mina Al Ahmadi refinery Kuwait status", "Kuwait National Petroleum refinery" | "艾哈迈迪 港口 炼厂 科威特 熔断" |
| P1 | 阿联酋 | Ruwais | 部分损毁 | T+75 | "Ruwais refinery ADNOC damage", "UAE Ruwais petrochemical status" | "鲁韦斯 炼厂 阿布扎比 损毁" |
| P1 | 中国 | 万华化学 | 交付端FM(3月7日生效) | 持续监控 | "Wanhua Chemical force majeure Middle East delivery", "Wanhua MDI PP PDH Yantai production status" | "万华化学 不可抗力 中东 交付 MDI 聚丙烯" |
| P1 | 韩国 | 乐天大山NCC | NCC永久关停并入重组 | 2026年内完成 | "Lotte Chemical Daesan NCC closure merger Hyundai", "Lotte Daesan ethylene propylene capacity shutdown" | "乐天化学 大山 NCC 关停 合并 现代 乙烯 丙烯" |
| P2 | 比利时 | Vynova Beek | 永久关闭 | N/A | "Vynova Beek PVC plant closure" | "Vynova Beek 永久关闭 PVC" |
| P2 | 比利时 | Dow Tertre | 永久关闭 | N/A | "Dow Tertre plant closure Belgium" | "陶氏 Tertre 关闭 比利时" |
| P2 | 伊朗 | Asaluyeh(SPGC) | 系统性损毁 | Q4-2027Q1 | "Asaluyeh SPGC gas processing damage", "Iran South Pars phases status" | "阿萨卢耶 SPGC 气体处理 损毁" |
| P2 | 沙特 | Jubail肥料厂 | 不可抗力 | 取决气田修复 | "Jubail fertilizer plant force majeure SABIC" | "朱拜勒 肥料厂 不可抗力 SABIC" |

## 三、下游枢纽（P1/P2）

| 优先级 | 国家 | 资产 | 看板基线状态 | 搜索关键词（EN） | 搜索关键词（CN） |
|--------|------|------|-------------|-----------------|-----------------|
| P1 | 伊拉克 | Basra港口系统 | 完全摧毁 | "Basra oil port export status", "Iraq Basra terminal operations" | "巴士拉 港口 原油出口 恢复" |
| P1 | 伊朗 | Kharg Island | 物流链路损毁 | "Kharg Island oil export terminal", "Iran Kharg Island tanker loading" | "哈尔克岛 原油出口 油轮 装载" |
| P1 | 阿联酋 | Fujairah | 停摆中 | "Fujairah port operations status", "UAE Fujairah oil terminal" | "富查伊拉 港口 运营 停摆" |
| P2 | 沙特 | Ras Tanura | 运行受限 | "Ras Tanura terminal operations", "Saudi Ras Tanura export" | "拉斯坦努拉 港口 出口 运行" |
| P2 | 沙特 | Petroline(E-W) | 初步恢复 | "Petroline East West pipeline Saudi", "Saudi East West pipeline capacity" | "东西管道 沙特 石油管道 恢复" |

## 四、航运状态（P0）

| 优先级 | 指标 | 看板基线 | 搜索关键词（EN） | 搜索关键词（CN） |
|--------|------|----------|-----------------|-----------------|
| P0 | 霍尔木兹海峡通行状态 | 限制通行 | "Strait of Hormuz shipping status today", "Hormuz transit war risk" | "霍尔木兹海峡 通航 状态 今日" |
| P0 | 海峡通行船舶数 | 快照值 | "Hormuz strait vessel traffic count" | "霍尔木兹 船舶 通行 数量" |
| P0 | 吞吐恢复度 | 56.1% | "Hormuz oil shipping throughput recovery" | "霍尔木兹 吞吐 恢复 原油运输" |

## 五、核实协议

### 5.1 核实流程

1. **读取基线**：从 `references/dashboard-structure.md` 第三、四章读取每个资产的基线状态
2. **按优先级搜索**：P0全部搜索 → P1全部搜索 → P2视搜索预算滚动覆盖
3. **对照判定**：
   - **基线确认（CONFIRMED）**：最新信息与基线一致，无变化
   - **基线更新（UPDATED）**：资产状态有变化（复产/恶化/修复ETA变更/产能损失修正）
   - **基线存疑（STALE）**：搜索不到任何近期信息（>30天无更新），可能看板数据已过时但无法确认方向
4. **覆盖基线**：UPDATED的资产用核实结果覆盖基线，进入观点生成

### 5.2 搜索策略

- 每个P0资产执行1次定向搜索（WebSearch），关键词为上表EN+CN组合
- 使用 `query_keyword_groups` 参数同时覆盖中英文
- 时间窗口放宽到90天（资产状态变化不像新闻那么频繁）
- 对STALE资产在看板中标注"⚠️ 基线可能滞后，近期无验证信息"

### 5.3 产量数据交叉验证

对于关键产量数字（如Safaniya -2500kbd），额外执行以下验证：
- 搜索该资产运营商/能源部官方声明
- 搜索IEA/IEA月报/OPEC月报中对该资产的描述
- 交叉验证：如果多家T1来源引用了不同的产量数字，以最新T1来源为准

### 5.4 输出格式

每个资产的核实结果格式化为一行JSON，汇入dashboard data的 `asset_verification` 数组：

```json
{
    "asset": "Safaniya/Marjan",
    "country": "沙特",
    "category": "上游",
    "priority": "P0",
    "baseline_status": "物流性停产",
    "baseline_loss": "-2,500 kbd",
    "verified_status": "物流性停产（海峡限制通行持续）",
    "verified_loss": "-2,500 kbd",
    "verification": "CONFIRMED",
    "source": "Reuters 2026-06-28",
    "source_tier": "T1",
    "note": "沙特能源部未宣布复产，海峡仍未恢复正常通行"
}
```

## 六、关键化工装置核实要点（易混淆资产）

### 万华化学（Yantai基地）

> **关键区分**：万华的FM是**交付端**（出口交付不可抗力），**不是生产端**。核实时必须区分。

| 装置/事件 | 核实要点 | 已知基线（需每次确认） |
|-----------|----------|----------------------|
| 异氰酸酯出口FM（MDI/TDI） | 3月7日生效，原因是霍尔木兹海峡航运中断，覆盖对中东客户的异氰酸酯交付。**两套裂解装置（合计220万吨/年乙烯）仍在高负荷运行**。需搜索FM是否已解除。 | 交付端FM，生产正常 |
| PDH→PP装置（75万吨/年） | 3月18日开始计划性检修，**5月7日已重启**（47天周期）。需确认是否正常运行。 | 已复产 |
| MDI/TDI产能 | 万华是全球最大MDI生产商。需确认烟台/宁波基地MDI/TDI产能是否有生产端中断。 | 生产正常 |

### 乐天化学（大山基地）

> **关键区分**：乐天大山不是简单的"60%降负"，而是**结构性重组**——NCC将被永久关停。与霍尔木兹物流危机叠加导致韩国烯烃供应进一步收紧。

| 装置/事件 | 核实要点 | 已知基线（需每次确认） |
|-----------|----------|----------------------|
| 大山NCC（110万吨/年乙烯） | 2026年2月韩国政府宣布"大山一号重组计划"，乐天NCC将被**永久关停**并并入HD Hyundai Chemical（50:50）。韩国乙烯产量-8%。计划9月成立新实体，年内完成减产。 | 永久关停进行中 |
| 大山裂解装置当前开工率 | 受霍尔木兹中断→石脑油供应紧张影响，韩国裂解装置整体降至~66%。需搜索乐天当前实际开工率。 | ~66%（受石脑油供应约束） |
| 丙烯/PP产出影响 | NCC关停+低开工率→丙烯产出减少→韩国PP供应收紧。需确认对亚洲PP供需平衡的量化影响。 | 供应收紧确认中 |

### PP/聚烯烃链原料传导路径

> PP走强的核心驱动**不是万华MDI的FM**，而是霍尔木兹→石脑油供应链断裂→韩国裂解降负→丙烯紧张。

```
霍尔木兹中断
  ↓
亚洲海运石脑油进口受阻（~60%海运量经霍尔木兹）
  ↓
韩国NCC开工率降至~66% + 乐天大山NCC永久关停(-8%韩国乙烯)
  ↓
丙烯产出减少 → PP成本推升
  ↓
中国PDH/煤制烯烃路线不受影响 → 满负荷+出口套利（3月出口40.55万吨创纪录）
  ↓
PP价格走强（但需注意：H2 2026中国新增545万吨PP产能，若海峡恢复可能反转）
```

### MDI/TDI与PP的产业链关系

```
MDI/TDI链:  石脑油 → 重整 → 苯/甲苯 → 苯胺/TDA → MDI/TDI → 聚氨酯(PU)
PP链:       石脑油/丙烷 → 裂解/PDH → 丙烯 → PP（聚丙烯）
                                    ↘ PE（线性低密度聚乙烯）
```

**两条链原料端不同**（芳烃 vs 烯烃）。万华烟台基地同时拥有两条链的产能，但FM仅覆盖异氰酸酯的出口交付，**PP/PDH装置不受FM影响**。分析PP时不得引用MDI的FM作为支撑。
