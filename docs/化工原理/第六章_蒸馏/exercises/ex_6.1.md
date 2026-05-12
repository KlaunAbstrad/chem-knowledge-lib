# 习题 6.1

## 题目

用简单蒸馏分离苯-甲苯混合物。进料 100 kmol，其中苯含量 40 mol%。要求釜残液中苯含量降至 20 mol%。已知相对挥发度 α = 2.5。

求：
1. 釜液量 L_W
2. 馏出液量 D
3. 馏出液平均组成 x_D,avg

---

::: details 点击查看解答

## 求解思路

简单蒸馏的 Rayleigh 方程用于计算分离程度。

## 计算过程

### 1. 总物料衡算

$$F = D + W \quad \Rightarrow \quad 100 = D + W \tag{E6.1.1}$$

组分衡算：
$$F z_F = D x_{D,avg} + W x_W$$

$$100 \times 0.4 = D \cdot x_{D,avg} + W \times 0.2 \tag{E6.1.2}$$

### 2. Rayleigh 方程

对于二元体系：
$$\ln\frac{F}{W} = \frac{1}{\alpha - 1}\left[\ln\frac{x_F}{x_W} + \alpha\ln\frac{1-x_W}{1-x_F}\right]$$

代入数值：
$$\ln\frac{100}{W} = \frac{1}{2.5 - 1}\left[\ln\frac{0.4}{0.2} + 2.5\ln\frac{0.8}{0.6}\right]$$

$$\ln\frac{100}{W} = \frac{1}{1.5}\left[\ln 2 + 2.5\ln\frac{4}{3}\right]$$

$$\ln\frac{100}{W} = \frac{1}{1.5}\left[0.6931 + 2.5 \times 0.2877\right] = \frac{1}{1.5}\left[0.6931 + 0.7193\right] = \frac{1.4124}{1.5} = 0.9416$$

$$100/W = e^{0.9416} = 2.563$$

$$W = \frac{100}{2.563} = 39.0\ \text{kmol/h}$$

### 3. 求解 D

$$D = 100 - 39.0 = 61.0\ \text{kmol/h}$$

### 4. 计算馏出液平均组成

由 (E6.1.2)：
$$40 = 61.0 \times x_{D,avg} + 39.0 \times 0.2$$

$$40 = 61.0 \times x_{D,avg} + 7.8$$

$$x_{D,avg} = \frac{40 - 7.8}{61.0} = \frac{32.2}{61.0} = 0.528$$

## 答案

| 参数 | 值 | 单位 |
|------|:---:|------|
| 釜液量 $W$ | **39.0** | kmol/h |
| 馏出液量 $D$ | **61.0** | kmol/h |
| 馏出液平均组成 $x_{D,avg}$ | **0.528** | — |

---

:::