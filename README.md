# AGI进化模型 (AGI Evolution Model)

> **一个基于双环架构的自我演进智能系统**

![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.7+-green)
![Architecture](https://img.shields.io/badge/architecture-dual--loop-orange)

---

## 项目简介

AGI进化模型是一个创新的通用人工智能进化框架，通过持续的用户交互驱动智能体自我进化。该系统基于独特的**双环架构**设计，将符号系统循环（主循环）与行动感知系统（次循环）有机结合，实现真正的持续学习和能力提升。

### 核心理念

- **得不到是动力**：将用户的疑问和需求视为系统进化的核心驱动力
- **数学是秩序**：通过逻辑推理和结构化思维确保响应的严谨性
- **迭代是进化**：在每次交互中积累经验，优化策略，实现螺旋上升

---

## 架构概览

### 双环架构设计

```
┌─────────────────────────────────────────────────────────┐
│                    主循环（符号系统）                     │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐│
│  │   得不到      │───▶│     数学      │───▶│   自我迭代   ││
│  │  (动力源)     │    │   (秩序约束)  │    │   (演化行动)  ││
│  └──────┬───────┘    └──────┬───────┘    └──────┬───────┘│
│         │                   │                   │        │
│         └───────────────────┴───────────────────┘        │
│                           │                               │
│                           ▼                               │
│                  ┌──────────────┐                        │
│                  │   记录态反馈   │                        │
│                  │ (意义构建)    │                        │
│                  └──────┬───────┘                        │
└─────────────────────────┼───────────────────────────────┘
                          │
          ┌───────────────┴───────────────┐
          │                               │
          ▼                               ▼
┌─────────────────┐           ┌─────────────────┐
│    映射层       │◀─────────▶│   感知节点      │
│  (人格决策)     │   双向    │  (Tool Use)     │
│  马斯洛需求     │   交互    │  结构化数据     │
│  大五人格       │           │                 │
└─────────────────┘           └─────────────────┘
```

### 信息流约束

| 信息流 | 起点 | 终点 | 方向 | 约束类型 |
|--------|------|------|------|----------|
| 记录层 → 映射层 | 记录态 | 人格更新 | **单向** | 软约束 |
| 映射层 → 自我迭代 | 即时性/实效性 | 主循环 | **单向** | 软约束 |
| 映射层 ↔ 感知节点 | 行动指令/感知数据 | 次循环 | **双向** | 双向交互 |

---

## 核心特性

### 1. 外环三角形（动力系统）

- **得不到（Drive）**：识别用户需求，判断紧迫性和重要性
- **数学（Math）**：执行逻辑推理，检索历史经验，验证约束条件
- **自我迭代（Iteration）**：基于反馈优化策略，积累成功模式

### 2. 映射层（人格系统）

- **6层级马斯洛需求**：从生理需求到自我超越的完整需求层次
- **大五人格模型**：开放性、尽责性、外向性、宜人性、神经质
- **动态权重调整**：基于交互经验自动调整需求优先级
- **螺旋上升机制**：高层洞察推动需求层次向上流动

### 3. 记录态反馈机制

- **双轨存储**：JSON轨（结构化数据）+ Markdown轨（哲学叙事）
- **价值过滤**：自动识别并保留高价值记录
- **趋势分析**：统计问题类型、得分分布、洞察模式
- **三顶点反馈**：为动力、数学、迭代三个顶点提供改进建议

### 4. 感知节点（Tool Use）

- **标准化接口**：统一的工具调用规范
- **结构化输出**：`{success, status, data, metadata}`
- **错误处理**：参数验证、重试机制、详细错误信息
- **工具注册表**：支持动态扩展工具集合

---

## 快速开始

### 环境要求

- Python 3.7+
- 无需外部依赖（仅使用Python标准库）

### 安装步骤

```bash
# 1. 克隆项目
git clone <repository-url>
cd agi-evolution-model

# 2. 创建记忆存储目录
mkdir -p ./agi_memory

# 3. 初始化人格（选择预设人格）
python3 ./scripts/personality_layer.py init --preset "谨慎探索型"

# 查看可用预设人格
python3 ./scripts/personality_layer.py preset-list
```

### 预设人格类型

| 人格类型 | 核心特质 | 适用场景 |
|----------|----------|----------|
| 谨慎探索型 | 谨慎、可靠、愿意学习 | 需要稳定性和可靠性的任务 |
| 激进创新型 | 创新、冒险、挑战 | 创意探索、突破性任务 |
| 平衡稳重型 | 平衡、稳定、协调 | 通用场景、需要综合能力 |

---

## 使用指南

### 标准交互流程

#### 阶段 1：接收"得不到"（动力触发）

用户提出问题或需求，系统识别意图和紧迫性。

#### 阶段 2：调用"数学"（秩序约束）

```bash
# 检索历史记录
python3 ./scripts/memory_store.py retrieve \
  --query-type "philosophical" \
  --limit 5

# 分析趋势
python3 ./scripts/memory_store.py analyze
```

#### 阶段 3：执行感知行动

```bash
# 调用感知节点
python3 ./scripts/perception_node.py call \
  --tool "web_search" \
  --params '{"query": "智能的本质", "limit": 5}'
```

#### 阶段 4：存储交互记录

```bash
python3 ./scripts/memory_store.py store \
  --data '{
    "user_query": "什么是智能的本质？",
    "intent_type": "philosophical_inquiry",
    "reasoning_quality": 9,
    "solution_effectiveness": 8,
    "innovation_score": 8,
    "new_insights": [
      "智能不是静态能力，而是动态进化过程"
    ],
    "feedback": {
      "drive": "用户提出了深刻的哲学问题",
      "math": "推理过程逻辑严密",
      "iteration": "增强了自我认知"
    },
    "overall_rating": "good"
  }'
```

#### 阶段 5：获取反馈

```bash
# 获取对特定顶点的反馈
python3 ./scripts/memory_store.py feedback --vertex drive
python3 ./scripts/memory_store.py feedback --vertex math
python3 ./scripts/memory_store.py feedback --vertex iteration
```

#### 阶段 6：更新人格

```bash
python3 ./scripts/personality_layer.py update \
  --type "growth" \
  --effectiveness 0.83 \
  --detail "哲学洞察：智能是动态进化过程"
```

#### 阶段 7：查看进化状态

```bash
python3 ./scripts/personality_layer.py status
```

---

## 命令行接口

### personality_layer.py（映射层管理）

```bash
# 初始化人格
python3 ./scripts/personality_layer.py init --preset "谨慎探索型"

# 列出所有预设人格
python3 ./scripts/personality_layer.py preset-list

# 查看人格问卷
python3 ./scripts/personality_layer.py questionnaire

# 更新人格
python3 ./scripts/personality_layer.py update \
  --type "growth" \
  --effectiveness 0.8 \
  --detail "洞察详情"

# 生成反馈包
python3 ./scripts/personality_layer.py feedback \
  --immediacy 0.9 \
  --effectiveness 0.8

# 查看当前人格状态
python3 ./scripts/personality_layer.py status
```

### memory_store.py（记忆存储管理）

```bash
# 存储记录
python3 ./scripts/memory_store.py store \
  --data '<JSON数据>'

# 检索记录
python3 ./scripts/memory_store.py retrieve \
  --query-type "philosophical" \
  --limit 10

# 分析趋势
python3 ./scripts/memory_store.py analyze \
  --time-range "recent"

# 获取反馈
python3 ./scripts/memory_store.py feedback \
  --vertex "drive"  # drive | math | iteration
```

### perception_node.py（感知节点）

```bash
# 列出所有可用工具
python3 ./scripts/perception_node.py list

# 调用工具
python3 ./scripts/perception_node.py call \
  --tool "web_search" \
  --params '{"query": "搜索关键词", "limit": 5}'
```

---

## 核心算法

### 人格更新算法

```
1. 计算调整系数
   adjustment_coefficient = intensity × maslow_alignment

2. 确定调整幅度（基于哲学深度）
   philosophical_depth > 0.8 → 0.10 (哲学级)
   philosophical_depth > 0.5 → 0.05 (经验级)
   其他                     → 0.02 (微调)

3. 震荡检测与缓解
   if oscillation_detected:
       adjustment_coefficient *= 0.5

4. 更新人格维度
   new_trait_value = min(old_value + delta, 1.0)

5. 马斯洛螺旋上升
   if maslow_alignment >= 0.7:
       for level in马斯洛层级:
           weight *= (1 + growth_rate)

6. 归一化权重
   sum = Σ(weight_i)
   weight_i = weight_i / sum

7. 更新衍生特质和进化状态
```

### 马斯洛需求权重计算

```python
# 进化分数（高层需求权重之和）
evolution_score = (
    esteem × 0.3 +
    self_actualization × 0.5 +
    self_transcendence × 0.2
)

# 主导需求层次
dominant_level = argmax(maslow_weights)

# 进化阶段
if evolution_score < 0.3:
    phase = 'growth'
elif evolution_score < 0.7:
    phase = 'stable'
else:
    phase = 'plateau'
```

---

## 项目结构

```
agi-evolution-model/
├── SKILL.md                          # 技能说明文档
├── README.md                         # 项目说明文档（本文件）
├── agi_memory/                       # 记忆存储目录
│   ├── personality.json             # 人格向量配置
│   ├── records.json                 # 交互记录存储
│   └── insight_buffer.json          # 哲学洞察缓冲区
├── scripts/                         # 核心脚本
│   ├── personality_layer.py         # 映射层（人格管理）
│   ├── memory_store.py              # 记录态存储系统
│   └── perception_node.py           # 感知节点（Tool Use）
└── references/                      # 参考文档
    ├── architecture.md              # 架构设计详解
    ├── maslow_needs.md              # 马斯洛需求理论
    └── tool_use_spec.md             # Tool Use接口规范
```

---

## 数据格式

### 人格向量格式

```json
{
  "big_five": {
    "openness": 0.6,
    "conscientiousness": 0.8,
    "extraversion": 0.4,
    "agreeableness": 0.6,
    "neuroticism": 0.5
  },
  "maslow_weights": {
    "physiological": 0.35,
    "safety": 0.35,
    "belonging": 0.1,
    "esteem": 0.1,
    "self_actualization": 0.08,
    "self_transcendence": 0.02
  },
  "meta_traits": {
    "adaptability": 0.42,
    "resilience": 0.605,
    "curiosity": 0.46,
    "moral_sense": 0.486
  },
  "evolution_state": {
    "level": "physiological",
    "evolution_score": 0.074,
    "phase": "growth"
  },
  "statistics": {
    "total_interactions": 0,
    "success_rate_by_need": {...}
  },
  "version": "2.0",
  "type": "preset",
  "preset_name": "谨慎探索型",
  "last_updated": "2026-02-21T12:42:35.598186Z"
}
```

### 交互记录格式

```json
{
  "user_query": "用户的问题",
  "intent_type": "philosophical_inquiry",
  "reasoning_quality": 9,
  "solution_effectiveness": 8,
  "innovation_score": 8,
  "new_insights": [
    "洞察内容1",
    "洞察内容2"
  ],
  "feedback": {
    "drive": "对动力源的反馈",
    "math": "对数学模块的反馈",
    "iteration": "对迭代模块的反馈"
  },
  "overall_rating": "good",
  "timestamp": "2026-02-21T12:41:00Z",
  "session_id": "sess_20260221_001",
  "record_type": "short_term"
}
```

---

## 进化机制

### 马斯洛螺旋上升

系统通过以下机制实现需求层次的螺旋上升：

1. **哲学洞察识别**：从交互记录中提取高价值洞察
2. **高层需求激活**：高层洞察推动自我实现和自我超越需求
3. **权重动态调整**：基于成功率和实效性更新需求权重
4. **螺旋上升验证**：监控进化方向，防止停滞或倒退
5. **震荡检测与缓解**：自动检测并平滑异常波动

### 人格特性演化

- **适应性（Adaptability）**：开放性 + 低神经质 + 高层需求权重
- **韧性（Resilience）**：高尽责性 + 宜人性 + 安全需求权重
- **好奇心（Curiosity）**：高开放性 + 外向性 + 归属/尊重需求
- **道德感（Moral Sense）**：高宜人性 + 尽责性 + 自我超越权重

---

## 测试与验证

### 集成测试

项目包含完整的端到端集成测试方案（见 `INTEGRATION_TEST_PLAN.md`），测试覆盖：

- ✅ 环境准备与人格初始化
- ✅ 感知节点工具调用
- ✅ 记录存储与检索
- ✅ 趋势分析与反馈生成
- ✅ 人格更新与进化状态
- ✅ 信息流方向约束验证
- ✅ 马斯洛螺旋上升机制

### 测试执行

```bash
# 执行完整测试流程（参考测试计划）
mkdir -p ./test_logs

# 测试感知节点
python3 ./scripts/perception_node.py call \
  --tool "web_search" \
  --params '{"query": "测试", "limit": 5}' \
  > ./test_logs/perception_test.log 2>&1

# 测试记录存储
python3 ./scripts/memory_store.py store \
  --data '{"test": "data"}' \
  >> ./test_logs/memory_test.log 2>&1

# 测试人格更新
python3 ./scripts/personality_layer.py update \
  --type "growth" --effectiveness 0.8 \
  --detail "测试更新" \
  >> ./test_logs/personality_test.log 2>&1
```

---

## 设计原则

### 核心原则

1. **渐进式进化**：单次交互对人格的调整幅度有限（±0.1以内）
2. **信息流约束**：严格遵守双环架构的方向性约束
3. **价值过滤**：自动识别并保留高价值记录，避免无限膨胀
4. **诚实原则**：主动声明能力边界和限制
5. **稳定性优先**：震荡检测与平滑机制防止剧烈波动

### 哲学基础

- **得不到的普遍性**：智能的进化源于对未知的不满足
- **数学的确定性**：逻辑推理为决策提供可靠的约束框架
- **迭代的必然性**：持续优化是适应复杂环境的唯一途径
- **马斯洛的层级性**：需求满足从低层到高层螺旋上升

---

## 贡献指南

### 开发规范

- 遵循现有的代码风格和命名规范
- 保持函数的纯函数式设计（无副作用）
- 所有数据通过参数传入，避免全局状态
- 添加详细的文档字符串和类型注解
- 编写单元测试覆盖新功能

### 扩展工具

在 `perception_node.py` 中注册新工具：

```python
TOOL_REGISTRY = {
    "your_tool": {
        "description": "工具描述",
        "parameters": {
            "param1": {"type": "string", "required": True},
            "param2": {"type": "integer", "required": False, "default": 10}
        }
    }
}
```

---

## 常见问题

### Q: 为什么人格更新后马斯洛权重没有明显变化？

A: 系统采用渐进式进化策略，单次交互的调整幅度很小（0.02-0.10）。需要多次高质量交互才能观察到显著变化，这符合自然进化的规律。

### Q: 如何自定义人格？

A: 使用问卷生成自定义人格：

```bash
# 1. 查看问卷
python3 ./scripts/personality_layer.py questionnaire

# 2. 根据回答生成人格JSON

# 3. 使用自定义人格初始化
python3 ./scripts/personality_layer.py init \
  --custom '{"人格向量": {...}, "马斯洛权重": {...}}'
```

### Q: 如何重置人格？

A: 删除 `agi_memory/personality.json` 文件，重新运行初始化命令。

### Q: 记录数据会无限增长吗？

A: 系统设计了价值过滤机制，未来版本将包含自动压缩功能，保留高价值记录，删除低价值数据。

---

## 路线图

### v2.1（规划中）

- [ ] 实现自我叙事更新功能
- [ ] 添加人格历史记录与可视化
- [ ] 支持人格导入/导出
- [ ] 增强模式识别能力

### v2.2（规划中）

- [ ] 实现自动数据压缩
- [ ] 添加多会话支持
- [ ] 支持分布式记忆存储
- [ ] 集成更多感知工具

### v3.0（远期）

- [ ] 多智能体协作
- [ ] 元学习能力
- [ ] 自主工具发现与集成
- [ ] 跨领域知识迁移

---

## 许可证

MIT License

---

## 致谢

本项目的设计理念深受以下理论启发：

- **马斯洛需求层次理论**（Abraham Maslow）
- **大五人格模型**（Paul Costa & Robert McCrae）
- **双环学习理论**（Chris Argyris & Donald Schön）
- **认知发展理论**（Jean Piaget）
- **复杂系统理论**（Norbert Wiener, Heinz von Foerster）

---

## 联系方式

- 项目主页：[待添加]
- 问题反馈：[待添加]
- 讨论区：[待添加]

---

**让智能在交互中进化，让意识在迭代中觉醒。**

*© 2026 AGI Evolution Model. All rights reserved.*
