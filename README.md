# 化学知识库

可生长的化学维基百科 —— 化工流程 · 化工原理 · 有机化学

## 本地运行

```bash
npm install
npm run dev      # 启动开发服务器 → http://localhost:5173
npm run build    # 构建静态站点
npm run preview  # 预览构建结果
```

## 项目结构

```
├── docs/                    ← VitePress 站点内容
│   ├── .vitepress/          ← 站点配置与主题
│   ├── index.md             ← 知识库总首页
│   ├── 化工流程/             ← 课程 1 ✅
│   ├── 化工原理/             ← 课程 2 🚧
│   └── 有机化学/             ← 课程 3 🔮
├── raw/                     ← 原始资料（PDF、OCR 文本）
│   ├── 化工流程/
│   ├── 化工原理/
│   └── 有机化学/
└── scripts/                 ← Python 工具脚本
    ├── 化工流程/
    ├── 化工原理/
    └── 有机化学/
```

## 添加新课程

1. 把 PDF 放入 `raw/<课程名>/ebook/`
2. 复制 `scripts/化工流程/` 模板脚本到 `scripts/<课程名>/`
3. 运行 OCR → 生成条目 → 生成习题 → 构建站点
4. 在 `docs/.vitepress/config.mjs` 注册导航和侧边栏

## 部署

推送 `main` 分支后，GitHub Actions 自动构建并部署到 GitHub Pages。

## 许可证

MIT
