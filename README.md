# 化学知识库 (Chem Knowledge Lib)

**可增长的化学/化工维基百科**，面向化工专业学习者与从业者。

在线访问：**[klaunabstrad.github.io/chem-knowledge-lib](https://klaunabstrad.github.io/chem-knowledge-lib/)**

---

## 课程覆盖

| 课程 | 状态 | 已建设内容 |
|------|:----:|-----------|
| **化工流程** | ✅ 建设中 | 4 章 · 25 篇条目 · 21 道习题 |
| **化工原理** | 🚧 待建设 | 目录框架就绪 |
| **有机化学** | 🔮 规划中 | 目录框架就绪 |

### 化工流程已建设章节

- **第 4 章 · 相平衡基础** — 相平衡常数、泡点/露点、闪蒸计算、Wilson 方程
- **第 5 章 · 换热器设计** — 能量衡算、对流传热关联式、流动阻力、竖管冷凝器
- **第 7 章 · 多组分精馏简捷计算** — 关键组分、Fenske 方程、Underwood 方程、Gilliland 关联式（FUG 法）
- **第 9 章 · 多组分吸收和解吸简捷计算** — 平均吸收因子法、解吸因子法、Kremser 方程

---

## 功能特性

- **百科浏览** — 四级层级结构（课程-章-节-条目），左侧树形导航
- **数学公式** — KaTeX 实时渲染，支持 LaTeX 语法
- **习题系统** — 21 道配套习题，解答默认折叠，鼓励自主练习
- **反馈机制** — 每篇条目底部可提交纠错、评分、补充建议
- **本地搜索** — VitePress 内置全文搜索

---

## 技术栈

| 层级 | 技术 |
|------|------|
| 静态站点框架 | [VitePress](https://vitepress.dev) |
| 数学渲染 | [KaTeX](https://katex.org) + markdown-it-katex |
| 前端组件 | Vue 3 |
| 部署 | GitHub Pages + GitHub Actions |
| 内容格式 | Markdown + LaTeX |
| 构建工具 | Vite |

---

## 本地开发

```bash
# 安装依赖
npm install

# 启动开发服务器 (http://localhost:5173)
npm run dev

# 构建静态站点
npm run build

# 预览构建结果
npm run preview
```

---

## 项目结构

```
chem-knowledge-lib/
├── docs/                          ← VitePress 站点内容
│   ├── .vitepress/
│   │   ├── config.mjs             ← 站点配置（导航、侧边栏、KaTeX）
│   │   └── theme/                 ← 自定义主题（反馈表单组件）
│   ├── index.md                   ← 知识库首页（课程选择器）
│   ├── about.md                   ← 关于页面
│   ├── 化工流程/                   ← 课程 1
│   │   ├── index.md
│   │   ├── 第四章_相平衡/          ← 章 → 节 → 条目 + 习题
│   │   ├── 第五章/
│   │   ├── 第七章/
│   │   └── 第九章/
│   ├── 化工原理/                   ← 课程 2（待建设）
│   └── 有机化学/                   ← 课程 3（规划中）
├── raw/                           ← 原始资料
│   └── <课程名>/
│       ├── ebook/                 ← PDF 电子书（不进 git）
│       ├── scan/                  ← 扫描件（不进 git）
│       └── text/                  ← OCR 文本（进 git）
├── scripts/                       ← Python 工具脚本
│   └── 化工流程/                   ← OCR、条目生成、习题生成
├── .github/workflows/deploy.yml   ← CI/CD 自动部署
├── CHANGELOG.md                   ← 更新日志
└── CLAUDE.md                      ← AI 生成规则文件
```

---

## 内容规范

所有知识条目遵循统一的格式标准（详见 [CLAUDE.md](chem-knowledge-lib/CLAUDE.md)）：

- **标题** + **定义/概述**（1~2 句）
- **详细说明**（推导、适用条件、工程意义）
- **相关公式**（LaTeX `$$...$$` 渲染，带 `\tag` 编号）
- **关键参数**（符号、单位、含义表格）
- **计算示例**（逐步讲解）
- **关联条目**（内部链接）

---

## 部署

推送 `master` 分支后，GitHub Actions 自动执行：

1. `npm ci` — 安装依赖
2. `npm run build` — 构建站点
3. 部署到 GitHub Pages

---

## 添加新课程的流程

```bash
# 1. 放入原始 PDF
cp <教材>.pdf raw/<课程名>/ebook/

# 2. 运行 OCR 提取文本
python scripts/<课程名>/ocr_process.py

# 3. AI 辅助生成百科条目（按 CLAUDE.md 规范）
python scripts/<课程名>/generate_wiki.py

# 4. 生成习题解答
python scripts/<课程名>/gen_solve_chX.py

# 5. 注册导航 — 编辑 docs/.vitepress/config.mjs

# 6. 本地预览确认
npm run dev

# 7. 推送
git add . && git commit -m "新增<课程名>" && git push
```

---

## 许可证

[MIT](LICENSE)
