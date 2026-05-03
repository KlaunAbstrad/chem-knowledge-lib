# 更新日志

## 2026-05-03

### 修复

- **KaTeX 公式渲染彻底修复**：
  1. CSS 从本地 npm 加载（消除 0.16.45 vs 0.16.11 CDN 版本不匹配）
  2. 替换 `markdown-it-katex` 内嵌的 **KaTeX 0.6.0（2016 年）** → **0.16.45**，解决 `\tag` 不被识别、下标/求和符号定位错误等问题
  3. 添加 `postinstall` 脚本确保 `npm install` 后自动修复嵌套版本
- **GitHub Pages 自动启用**：`deploy.yml` 添加 `enablement: true` 参数，自动启用 Pages
- **VitePress 配置修正**：`base` 路径设为 `/chem-knowledge-lib/`，`editLink` 和 `socialLinks` 指向正确的仓库地址

### 部署

- 仓库创建并推送到 GitHub ([KlaunAbstrad/chem-knowledge-lib](https://github.com/KlaunAbstrad/chem-knowledge-lib))
- GitHub Actions 自动部署到 GitHub Pages：`https://klaunabstrad.github.io/chem-knowledge-lib/`

### 初始内容

- 化工流程：第 4 章（相平衡基础）、第 5 章（换热器设计）、第 7 章（多组分精馏简捷计算）、第 9 章（多组分吸收和解吸简捷计算）
- 共 25 篇知识条目 + 21 道习题详细解答
- VitePress 站点框架：KaTeX 数学公式渲染、本地搜索、侧边栏导航、反馈表单组件
- 化工原理、有机化学保留目录框架，内容待建设
