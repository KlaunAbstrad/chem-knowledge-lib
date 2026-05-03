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

### 新增

- **4 道章节例题**：
  - 例 7.1 FUG 全流程计算（物料衡算→露点/泡点迭代→Antoine→α→Fenske→Underwood→Gilliland→Kirkbride）
  - 例 4.1 Antoine 方程计算饱和蒸气压
  - 例 4.2 Peng-Robinson 状态方程求摩尔体积
  - 例 9.1 多组分吸收塔设计（K值→液气比→Kremser板数→非关键组分吸收率）
- **补遗漏知识点**：
  - 第 4 章新增 Peng-Robinson 状态方程条目（Z 三次方程、α(T) 修正因子）
  - 第 9 章补充 Horton-Franklin 通用多板方程推导
- 每道例题完整演示 **Antoine → Psat → K → α** 的计算链条，"计算"而非"查表"
- 习题索引页补充"计算说明"，链接到对应例题的方法讲解
- 第 9 章补充 Horton-Franklin 通用多板方程推导
- 第 9 章新增例 9.2（VOC 解吸塔设计）
