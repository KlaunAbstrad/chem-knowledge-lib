# 第七章 多组分精馏简捷计算

> **学习目标**：学完本章后，你将能够——
> 1. 定义轻/重关键组分并运用清晰分割假定进行物料衡算
> 2. 用 Fenske 方程计算全回流条件下的最少理论板数
> 3. 用 Underwood 方程计算最小回流比
> 4. 用 Gilliland 关联式计算实际理论板数，用 Kirkbride 方程确定进料位置
> 5. 独立完成一个多组分精馏塔的 FUG 全流程设计和校核

> **前置知识**：
> - **必修**：[第 4 章 相平衡基础](../第四章_相平衡/) — Antoine 方程、$K_i$ 计算、$\alpha_{ij}$ 计算、泡点/露点迭代
> - $\alpha_{ij}$ 必须从 Antoine 方程计算 $P^{\text{sat}} / P$ 导出，不可查表 → [例 4.1](../第四章_相平衡/4.3_例4.1_Antoine方程.md)

## 目录

- [关键组分与清晰分割](7.1_关键组分与清晰分割.md)
- [Fenske 方程 — 最少理论板数](7.2_Fenske方程.md)
- [Underwood 方程 — 最小回流比](7.3_Underwood方程.md)
- [Gilliland 关联式 — 实际理论板数](7.4_Gilliland关联式.md)
- [例 7.1 FUG 全流程计算](7.5_例7.1_FUG全流程计算.md)

### 习题
- [全部习题](exercises/index.md)

---

## 本章总结

### FUG 法四步流程

```
清晰分割 (7.1) → D, B, x_Di, x_Bi
        ↓
Fenske (7.2) → N_min (全回流最少板数)
        ↓
Underwood (7.3) → R_min (最小回流比)
        ↓
Gilliland (7.4) → N (实际板数)
        ↓
Kirkbride (7.4) → 进料位置 N_R/N_S
```

### 关键公式速查

| 公式 | 编号 | 用途 |
|------|:----:|------|
| $\dfrac{d_i}{b_i} = \alpha_i^{N_{\min}} \left(\dfrac{d}{b}\right)_{HK}$ | (7.5) | 清晰分割校验 |
| $N_{\min} = \dfrac{\log[(x_{LK}/x_{HK})_D (x_{HK}/x_{LK})_B]}{\log \alpha_{LK,HK}}$ | (7.12) | 最少理论板 |
| $\displaystyle\sum \dfrac{\alpha_i z_{iF}}{\alpha_i - \theta} = 1 - q$ | (7.20) | Underwood 第一方程 |
| $Y = 0.75(1 - X^{0.5668})$ | (7.22) | Gilliland 关联 |
| $\dfrac{N_R}{N_S} = \left[\left(\dfrac{z_{HK}}{z_{LK}}\right)_F \left(\dfrac{x_{LK}}{x_{HK}}\right)_B \left(\dfrac{B}{D}\right)^{0.206}\right]^{0.206}$ | (7.24) | Kirkbride 进料位置 |

### 后续章节

精馏与吸收同属气液传质分离，下一章 [第 9 章 多组分吸收和解吸简捷计算](../第九章/) 使用类似的概念（吸收因子替代相对挥发度）处理吸收问题。

---
[← 返回首页](../index.md)
