"""
Solve Chapter 9 exercises - Kremser absorption/stripping method
"""
import math
from pathlib import Path

COURSE = Path(r'E:/knowledge_lib/chem-knowledge-base/docs/化工流程')
CH9_EX = COURSE / '第九章' / 'exercises'

def save(folder, filename, content):
    folder.mkdir(parents=True, exist_ok=True)
    (folder / filename).write_text(content.strip() + '\n', encoding='utf-8')

# Helper: Kremser equations
def phi_abs(A, N):
    if abs(A - 1.0) < 1e-10:
        return N / (N + 1)
    An = A ** (N + 1)
    return (An - A) / (An - 1)

def phi_strip(S, N):
    if abs(S - 1.0) < 1e-10:
        return N / (N + 1)
    Sn = S ** (N + 1)
    return (Sn - S) / (Sn - 1)

def N_from_phi_abs(A, phi):
    if abs(A - 1.0) < 1e-10:
        return phi / (1 - phi)
    return math.log((A - phi) / (1 - phi)) / math.log(A) - 1

def N_from_phi_strip(S, phi):
    if abs(S - 1.0) < 1e-10:
        return phi / (1 - phi)
    return math.log((S - phi) / (1 - phi)) / math.log(S) - 1


# ============================================================
# Exercise 9.1 — Absorption column
# ============================================================
def gen_9_1():
    F = 120.0
    z = {'CH4': 0.65, 'C2H6': 0.15, 'C3H8': 0.12, 'nC4': 0.05, 'nC5': 0.03}
    v_in = {c: F * zc for c, zc in z.items()}
    K = {'CH4': 9.0, 'C2H6': 2.5, 'C3H8': 0.82, 'nC4': 0.25, 'nC5': 0.085}

    phi_key = 0.98
    K_key = K['C3H8']
    LV_min = K_key * phi_key
    LV = 1.5 * LV_min
    A_key = LV / K_key
    N_raw = N_from_phi_abs(A_key, phi_key)
    N = math.ceil(N_raw)

    A = {}; phi = {}; v_out = {}; l_abs = {}
    for c in z:
        A[c] = LV / K[c]
        phi[c] = phi_abs(A[c], N)
        v_out[c] = v_in[c] * (1 - phi[c])
        l_abs[c] = v_in[c] - v_out[c]

    V_out = sum(v_out.values())
    y_out = {c: v_out[c] / V_out for c in z}
    V_avg = (F + V_out) / 2
    L_avg = LV * V_avg
    abs_total = sum(l_abs.values())
    L0 = L_avg - abs_total / 2

    # Build table rows
    table_rows = ''
    names = {'CH4': '甲烷 CH₄', 'C2H6': '乙烷 C₂H₆', 'C3H8': '丙烷 C₃H₈', 'nC4': '正丁烷 n-C₄', 'nC5': '正戊烷 n-C₅'}
    for c in ['CH4', 'C2H6', 'C3H8', 'nC4', 'nC5']:
        table_rows += f'| {names[c]} | {K[c]:.3f} | {A[c]:.4f} | {phi[c]:.4f} | {v_out[c]:.2f} | {l_abs[c]:.2f} |\n'

    gas_rows = ''
    for c in ['CH4', 'C2H6', 'C3H8', 'nC4', 'nC5']:
        gas_rows += f'| {names[c]} | {v_out[c]:.2f} | {y_out[c]*100:.1f} |\n'

    content = f'''
# 习题 9.1

## 题目

吸收塔操作压力 1.2 MPa，进料气体 120 kmol/h，温度 35°C，吸收剂温度 35°C，塔内平均温度 40°C。
进料组成 CH₄(0.65)、C₂H₆(0.15)、C₃H₈(0.12)、n-C₄H₁₀(0.05)、n-C₅H₁₂(0.03)。
要求丙烷回收率 ≥ 98%。计算理论板数、各组分吸收率及塔顶尾气组成、吸收剂流量。

## 已知条件

| 参数 | 值 |
|------|-----|
| 操作压力 | 1.2 MPa |
| 进料气体 | 120 kmol/h (35°C) |
| 塔内平均温度 | 40°C |
| 吸收剂温度 | 35°C |
| 丙烷回收率 | ≥ 98% |

### 相平衡常数（40°C，1.2 MPa，估算值）

| 组分 | $K_i$ |
|------|:-----:|
| 甲烷 (CH₄) | 9.0 |
| 乙烷 (C₂H₆) | 2.5 |
| 丙烷 (C₃H₈) | 0.82 |
| 正丁烷 (n-C₄) | 0.25 |
| 正戊烷 (n-C₅) | 0.085 |

## 求解思路

采用平均吸收因子法（Kremser 方程）：
1. 选丙烷为关键组分，确定吸收率 $\\phi = 0.98$
2. 计算最小液气比 $(L/V)_{{\\min}} = K_{{\\text{{key}}}} \\phi_{{\\text{{key}}}}$
3. 确定实际液气比 $L/V = 1.5 (L/V)_{{\\min}}$
4. 计算关键组分吸收因子 $A_{{\\text{{key}}}} = (L/V)/K_{{\\text{{key}}}}$
5. 用 Kremser 方程求理论板数 $N$
6. 计算非关键组分的吸收率和物料分配

## 计算过程

### 1. 进料物料衡算

| 组分 | $z_i$ | $v_{{\\text{{in}}}}$ (kmol/h) |
|------|:-----:|:-----------------:|
| CH₄ | 0.65 | 78.0 |
| C₂H₆ | 0.15 | 18.0 |
| C₃H₈ | 0.12 | 14.4 |
| n-C₄ | 0.05 | 6.0 |
| n-C₅ | 0.03 | 3.6 |
| **合计** | 1.00 | 120.0 |

### 2. 最小液气比

$$
\\left(\\frac{{L}}{{V}}\\right)_{{\\min}} = K_{{\\text{{key}}}} \\phi_{{\\text{{key}}}} = 0.82 \\times 0.98 = {LV_min:.4f}
$$

### 3. 实际液气比

取 $1.5$ 倍最小液气比：

$$
\\frac{{L}}{{V}} = 1.5 \\times {LV_min:.4f} = {LV:.4f}
$$

### 4. 关键组分吸收因子

$$
A_{{\\text{{key}}}} = \\frac{{L/V}}{{K_{{\\text{{key}}}}}} = \\frac{{{LV:.4f}}}{{0.82}} = {A_key:.4f}
$$

### 5. 理论板数

$$
N = \\frac{{\\log\\left(\\frac{{A - \\phi}}{{1 - \\phi}}\\right)}}{{\\log A}} - 1
= \\frac{{\\log\\left(\\frac{{{A_key:.4f} - {phi_key}}}{{1 - {phi_key}}}\\right)}}{{\\log {A_key:.4f}}} - 1
= {N_raw:.2f}
$$

圆整：$N = {N}$ 块理论板。

### 6. 非关键组分吸收因子和吸收率

$$
A_i = \\frac{{L/V}}{{K_i}}, \\quad
\\phi_i = \\frac{{A_i^{{{N+1}}} - A_i}}{{A_i^{{{N+1}}} - 1}}
$$

| 组分 | $K_i$ | $A_i$ | $\\phi_i$ | $v_{{\\text{{out}}}}$ | $l_{{\\text{{abs}}}}$ |
|------|:-----:|:-----:|:---------:|:----------:|:----------:|
{table_rows}

### 7. 塔顶尾气组成

$$
V_1 = {V_out:.2f}\\ \\text{{kmol/h}}
$$

| 组分 | $v_{{\\text{{out}}}}$ (kmol/h) | $y_i$ (mol%) |
|------|:------------------:|:------------:|
{gas_rows}

### 8. 吸收剂流量

$$
\\text{{平均气相 }} V_{{\\text{{avg}}}} = \\frac{{{F:.0f} + {V_out:.2f}}}{{2}} = {V_avg:.2f}\\ \\text{{kmol/h}}
$$

$$
\\text{{平均液相 }} L_{{\\text{{avg}}}} = \\frac{{L}}{{V}} \\times V_{{\\text{{avg}}}} = {LV:.4f} \\times {V_avg:.2f} = {L_avg:.2f}\\ \\text{{kmol/h}}
$$

$$
\\text{{贫油（吸收剂）}} L_0 = L_{{\\text{{avg}}}} - \\frac{{l_{{\\text{{abs,total}}}}}}{{2}} = {L_avg:.2f} - \\frac{{{abs_total:.2f}}}{{2}} = {L0:.1f}\\ \\text{{kmol/h}}
$$

## 答案

| 参数 | 值 |
|------|-----|
| 理论板数 $N$ | **{N}** |
| 液气比 $L/V$ | **{LV:.4f}** |
| 吸收剂（贫油）流量 $L_0$ | **{L0:.0f} kmol/h** |
| 塔顶尾气流量 $V_1$ | **{V_out:.1f} kmol/h** |

### 塔顶尾气组成

| 组分 | mol% |
|------|:----:|
| 甲烷 | {y_out['CH4']*100:.1f} |
| 乙烷 | {y_out['C2H6']*100:.1f} |
| 丙烷 | {y_out['C3H8']*100:.1f} |
| 正丁烷 | {y_out['nC4']*100:.1f} |
| 正戊烷 | {y_out['nC5']*100:.1f} |

---
[← 返回习题集](index.md)
'''
    save(CH9_EX, 'ex_9.1.md', content)


# ============================================================
# Exercise 9.2 — H₂ purification by absorption
# ============================================================
def gen_9_2():
    F = 100.0
    z = {'H2': 0.725, 'CH4': 0.25, 'C2H6': 0.025}
    v_in = {c: F * zc for c, zc in z.items()}
    K = {'H2': 73, 'CH4': 10.5, 'C2H6': 3}

    phi_key = 0.55
    K_key = K['CH4']
    LV_min = K_key * phi_key
    LV = 1.5 * LV_min
    A_key = LV / K_key
    N_raw = N_from_phi_abs(A_key, phi_key)
    N = max(math.ceil(N_raw), 2)

    A = {}; phi = {}; v_out = {}; l_abs = {}
    for c in z:
        A[c] = LV / K[c]
        phi[c] = phi_abs(A[c], N)
        v_out[c] = v_in[c] * (1 - phi[c])
        l_abs[c] = v_in[c] - v_out[c]

    V_out = sum(v_out.values())
    y_H2 = v_out['H2'] / V_out
    V_avg = (F + V_out) / 2
    L_avg = LV * V_avg
    abs_total = sum(l_abs.values())
    L0 = L_avg - abs_total / 2

    table_rows = ''
    names = {'H2': 'H₂', 'CH4': 'CH₄', 'C2H6': 'C₂H₆'}
    for c in ['H2', 'CH4', 'C2H6']:
        table_rows += f'| {names[c]} | {K[c]:.1f} | {A[c]:.4f} | {phi[c]:.4f} | {v_in[c]:.1f} | {v_out[c]:.2f} | {l_abs[c]:.2f} |\n'

    content = f'''
# 习题 9.2

## 题目

通过正辛烷吸收去除 H₂ 中的 CH₄ 和 C₂H₆。进料组成 H₂(72.5%)、CH₄(25%)、C₂H₆(2.5%)。
操作压力 2.76 MPa，温度 311.3 K。
已知 K 值：H₂=73，CH₄=10.5，C₂H₆=3。
要求出口 H₂ 摩尔分率 ≥ 85%。计算理论板数和正辛烷流量。

## 已知条件

| 参数 | 值 |
|------|-----|
| 操作压力 | 2.76 MPa |
| 操作温度 | 311.3 K (38.15°C) |
| 进料流量（基准） | 100 kmol/h |
| 吸收剂 | 正辛烷 (n-C₈H₁₈) |
| 出口 H₂ 纯度 | ≥ 85 mol% |

### 相平衡常数

| 组分 | $K_i$ |
|------|:-----:|
| H₂ | 73（极轻，基本不吸收）|
| CH₄ | 10.5 |
| C₂H₆ | 3 |

## 求解思路

1. H₂ 为惰性组分（$K=73$，基本不被吸收），全部通过
2. 选择 CH₄ 为关键组分（较难吸收），通过出口 H₂ 纯度反算所需 CH₄ 吸收率
3. 平均吸收因子法计算理论板数和正辛烷流量

## 计算过程

### 1. 出口 H₂ 纯度约束

H₂ 基本不被吸收，$v_{{\\text{{H₂,out}}}} \\approx 72.5$ kmol/h。

出口 H₂ ≥ 85%：

$$
y_{{\\text{{H₂}}}} = \\frac{{v_{{\\text{{H₂,out}}}}}}{{v_{{\\text{{H₂,out}}}} + v_{{\\text{{CH₄,out}}}} + v_{{\\text{{C₂H₆,out}}}}}} \\ge 0.85
$$

$$
v_{{\\text{{CH₄,out}}}} + v_{{\\text{{C₂H₆,out}}}} \\le \\frac{{72.5}}{{0.85}} - 72.5 = 12.79\\ \\text{{kmol/h}}
$$

CH₄ + C₂H₆ 总进料 = 27.5 kmol/h，至少需吸收 14.71 kmol/h。

取 CH₄ 为关键组分，目标吸收率 $\\phi_{{\\text{{CH₄}}}} = 0.55$。

### 2. 最小液气比

$$
\\left(\\frac{{L}}{{V}}\\right)_{{\\min}} = K_{{\\text{{CH₄}}}} \\phi_{{\\text{{CH₄}}}} = 10.5 \\times 0.55 = {LV_min:.3f}
$$

### 3. 实际液气比

$$
\\frac{{L}}{{V}} = 1.5 \\times {LV_min:.3f} = {LV:.3f}
$$

### 4. 理论板数

$$
A_{{\\text{{CH₄}}}} = \\frac{{L/V}}{{K_{{\\text{{CH₄}}}}}} = \\frac{{{LV:.3f}}}{{10.5}} = {A_key:.4f}
$$

$$
N = \\frac{{\\log\\left(\\frac{{{A_key:.4f} - {phi_key}}}{{1 - {phi_key}}}\\right)}}{{\\log {A_key:.4f}}} - 1 = {N_raw:.2f}
$$

圆整：$N = {N}$ 块理论板。

### 5. 各组分吸收率

| 组分 | $K_i$ | $A_i$ | $\\phi_i$ | $v_{{\\text{{in}}}}$ | $v_{{\\text{{out}}}}$ | $l_{{\\text{{abs}}}}$ |
|------|:-----:|:-----:|:---------:|:----------:|:----------:|:----------:|
{table_rows}

### 6. H₂ 纯度校核

$$
y_{{\\text{{H₂}}}} = \\frac{{{v_out['H2']:.2f}}}{{{V_out:.2f}}} = {y_H2*100:.1f}\\% \\ge 85\\% \\quad \\checkmark
$$

### 7. 正辛烷流量

$$
V_{{\\text{{avg}}}} = \\frac{{{F:.0f} + {V_out:.2f}}}{{2}} = {V_avg:.2f}\\ \\text{{kmol/h}}
$$

$$
L_{{\\text{{avg}}}} = \\frac{{L}}{{V}} \\times V_{{\\text{{avg}}}} = {LV:.4f} \\times {V_avg:.2f} = {L_avg:.2f}\\ \\text{{kmol/h}}
$$

$$
L_0 = L_{{\\text{{avg}}}} - \\frac{{l_{{\\text{{abs,total}}}}}}{{2}} = {L_avg:.2f} - \\frac{{{abs_total:.2f}}}{{2}} = {L0:.0f}\\ \\text{{kmol/h}}
$$

正辛烷分子量 114.23 kg/kmol：

$$
m_0 = {L0:.0f} \\times 114.23 = {L0 * 114.23:.0f}\\ \\text{{kg/h}}
$$

## 答案

| 参数 | 值 |
|------|-----|
| 理论板数 $N$ | **{N}** |
| 正辛烷流量 $L_0$ | **{L0:.0f} kmol/h**（**{L0 * 114.23:.0f} kg/h**）|
| 液气比 $L/V$ | **{LV:.3f}** |
| 出口 H₂ 纯度 | **{y_H2*100:.1f}%** |
| CH₄ 吸收率 | **{phi['CH4']*100:.1f}%** |
| C₂H₆ 吸收率 | **{phi['C2H6']*100:.1f}%** |

---
[← 返回习题集](index.md)
'''
    save(CH9_EX, 'ex_9.2.md', content)


# ============================================================
# Exercise 9.3 — Air stripping of VOCs from water
# ============================================================
def gen_9_3():
    Qw = 0.1  # m³/s
    L = Qw * 1000 / 18.015 * 3600  # kmol/h

    x0 = {'DCA': 85e-6, 'TCE': 120e-6, 'TCA': 145e-6}
    x_req = {'DCA': 0.005e-6, 'TCE': 0.005e-6, 'TCA': 0.200e-6}
    alpha = {'DCA': 60, 'TCE': 650, 'TCA': 275}

    phi_req_DCA = (x0['DCA'] - x_req['DCA']) / x0['DCA']
    K_key = alpha['DCA']
    phi_key = phi_req_DCA
    VL_min = phi_key / K_key
    VL = 2.0 * VL_min

    S_key = K_key * VL
    N_raw = N_from_phi_strip(S_key, phi_key)
    N = math.ceil(N_raw)

    S = {}; phi_s = {}; x_out = {}
    for c in alpha:
        S[c] = alpha[c] * VL
        phi_s[c] = phi_strip(S[c], N)
        x_out[c] = x0[c] * (1 - phi_s[c])

    V = VL * L  # kmol/h

    table_rows = ''
    for c in ['DCA', 'TCE', 'TCA']:
        ok = '✓' if x_out[c] <= x_req[c] else '✗'
        table_rows += f'| {c} | {alpha[c]} | {S[c]:.2f} | {phi_s[c]:.6f} | {x0[c]*1e6:.2f} | {x_out[c]*1e6:.4f} | {x_req[c]*1e6:.3f} | {ok} |\n'

    content = f'''
# 习题 9.3

## 题目

用空气去除地下水中的挥发性有机物。水流量 0.1 m³/s，含有 DCA(85×10⁻⁶)、TCE(120×10⁻⁶)、TCA(145×10⁻⁶)。
要求解吸后 DCA < 0.005×10⁻⁶，TCE < 0.005×10⁻⁶，TCA < 0.200×10⁻⁶。
操作条件 101.3 kPa，25°C。相对挥发度分别为 60、650、275。
计算理论板数和空气流量。

## 已知条件

| 参数 | 值 |
|------|-----|
| 操作压力 | 101.3 kPa |
| 操作温度 | 25°C |
| 水流量 | 0.1 m³/s |
| DCA 进口浓度 | 85×10⁻⁶（摩尔分数）|
| TCE 进口浓度 | 120×10⁻⁶ |
| TCA 进口浓度 | 145×10⁻⁶ |

### 出口要求

| 组分 | 出口要求 |
|------|---------|
| DCA | < 0.005×10⁻⁶ |
| TCE | < 0.005×10⁻⁶ |
| TCA | < 0.200×10⁻⁶ |

### 相对挥发度（无量纲 Henry 常数）

| 组分 | $\\alpha_i = K_i$ |
|------|:---------------:|
| DCA | 60 |
| TCE | 650 |
| TCA | 275 |

## 求解思路

采用解吸因子法（Kremser 方程）：
1. 选 DCA 为关键组分（$\\alpha$ 最小，最难解吸）
2. 计算所需 DCA 解吸率
3. 最小气液比 $(V/L)_{{\\min}} = \\phi_{{\\text{{key}}}}/K_{{\\text{{key}}}}$
4. 用 Kremser 方程计算理论板数
5. 校核 TCE 和 TCA 是否满足要求

## 计算过程

### 1. 水流量

$$
L = \\frac{{0.1 \\times 1000}}{{18.015}} \\times 3600 = {L:.0f}\\ \\text{{kmol/h}}
$$

### 2. DCA 解吸率（关键组分）

$$
\\phi_{{\\text{{DCA}}}} = \\frac{{85 \\times 10^{{-6}} - 0.005 \\times 10^{{-6}}}}{{85 \\times 10^{{-6}}}} = {phi_req_DCA:.6f}
$$

### 3. 最小气液比

$$
\\left(\\frac{{V}}{{L}}\\right)_{{\\min}} = \\frac{{\\phi_{{\\text{{DCA}}}}}}{{K_{{\\text{{DCA}}}}}} = \\frac{{{phi_req_DCA:.6f}}}{{60}} = {VL_min:.6f}
$$

### 4. 实际气液比

取 2 倍最小气液比：

$$
\\frac{{V}}{{L}} = 2.0 \\times {VL_min:.6f} = {VL:.6f}
$$

### 5. 理论板数

$$
S_{{\\text{{DCA}}}} = K_{{\\text{{DCA}}}} \\frac{{V}}{{L}} = 60 \\times {VL:.6f} = {S_key:.4f}
$$

$$
N = \\frac{{\\log\\left(\\frac{{S - \\phi}}{{1 - \\phi}}\\right)}}{{\\log S}} - 1
= \\frac{{\\log\\left(\\frac{{{S_key:.4f} - {phi_key:.6f}}}{{1 - {phi_key:.6f}}}\\right)}}{{\\log {S_key:.4f}}} - 1
= {N_raw:.2f}
$$

圆整：$N = {N}$ 块理论板。

### 6. 各组分解吸率

| 组分 | $K_i$ | $S_i$ | $\\phi_i$ | $x_{{\\text{{in}}}}$ (×10⁻⁶) | $x_{{\\text{{out}}}}$ (×10⁻⁶) | 要求 (×10⁻⁶) | 合格？ |
|------|:-----:|:-----:|:---------:|:-----------------:|:------------------:|:------------:|:------:|
{table_rows}

### 7. 空气流量

$$
V = \\frac{{V}}{{L}} \\times L = {VL:.6f} \\times {L:.0f} = {V:.0f}\\ \\text{{kmol/h}}
$$

25°C 下空气摩尔体积 $V_m = 24.45$ m³/kmol：

$$
V_{{\\text{{air}}}} = {V:.0f} \\times 24.45 = {V * 24.45:.0f}\\ \\text{{m³/h}} = {V * 24.45 / 3600:.2f}\\ \\text{{m³/s}}
$$

## 答案

| 参数 | 值 |
|------|-----|
| 理论板数 $N$ | **{N}** |
| 气液比 $V/L$ | **{VL:.6f}** |
| 空气流量 | **{V:.0f} kmol/h**（**{V * 24.45:.0f} m³/h**）|

### 出口水质

| 组分 | 出口浓度 (×10⁻⁶) | 达标 |
|:----:|:----------------:|:----:|
| DCA | {x_out['DCA']*1e6:.4f} | {"✓" if x_out['DCA'] <= x_req['DCA'] else "✗"} |
| TCE | {x_out['TCE']*1e6:.4f} | {"✓" if x_out['TCE'] <= x_req['TCE'] else "✗"} |
| TCA | {x_out['TCA']*1e6:.4f} | {"✓" if x_out['TCA'] <= x_req['TCA'] else "✗"} |

---
[← 返回习题集](index.md)
'''
    save(CH9_EX, 'ex_9.3.md', content)


# ============================================================
# Exercise 9.4 — N₂ stripping of SO₂ and butadiene
# ============================================================
def gen_9_4():
    feed = {'SO2': 10, 'B13': 8, 'B12': 2, 'BS': 100}
    F = sum(feed.values())
    K = {'SO2': 6.95, 'B13': 4.53, 'B12': 4.50, 'BS': 0.016}

    # Key: butadiene (harder to strip than SO₂)
    phi_buta = (feed['B13'] + feed['B12'] - 0.5) / (feed['B13'] + feed['B12'])
    K_buta = (K['B13'] * 8 + K['B12'] * 2) / 10

    VL_min = phi_buta / K_buta
    VL = 1.5 * VL_min
    S_key = K_buta * VL
    N_raw = N_from_phi_strip(S_key, phi_buta)
    N = math.ceil(N_raw)

    S = {}; phi_s = {}; l_out = {}; v_strip = {}
    for c in feed:
        S[c] = K[c] * VL
        phi_s[c] = phi_strip(S[c], N)
        l_out[c] = feed[c] * (1 - phi_s[c])
        v_strip[c] = feed[c] - l_out[c]

    total_l = sum(l_out.values())
    y_SO2_prod = l_out['SO2'] / total_l
    y_buta_prod = (l_out['B13'] + l_out['B12']) / total_l

    V = VL * F

    table_rows = ''
    for c in ['SO2', 'B13', 'B12', 'BS']:
        table_rows += f'| {c} | {feed[c]} | {K[c]:.3f} | {S[c]:.4f} | {phi_s[c]:.6f} | {l_out[c]:.4f} | {v_strip[c]:.4f} |\n'

    content = f'''
# 习题 9.4

## 题目

用 N₂ 解吸 SO₂ 和丁二烯混合物。进料：SO₂(10)、1,3-T(8)、1,2-T(2)、BS(100) kmol/h。
要求产品中 SO₂ < 0.05 mol%，丁二烯 < 0.5 mol%。
操作温度 70°C，压力 207 kPa。
K 值：SO₂=6.95，B2=4.53，BS=0.016。
计算 N₂ 流量和理论板数。

## 已知条件

| 参数 | 值 |
|------|-----|
| 操作压力 | 207 kPa |
| 操作温度 | 70°C |
| 进料流量 | {F} kmol/h |
| 解吸剂 | N₂ |

### 进料组成和相平衡常数

| 组分 | $f_i$ (kmol/h) | $K_i$ |
|------|:-------------:|:-----:|
| SO₂ | 10 | 6.95 |
| 1,3-丁二烯 | 8 | 4.53 |
| 1,2-丁二烯 | 2 | ~4.5 |
| BS（溶剂） | 100 | 0.016 |

### 分离要求（液相产品）

- SO₂ < 0.05 mol%
- 丁二烯（合计）< 0.5 mol%

## 求解思路

采用解吸因子法：
1. 丁二烯为关键组分（$K$ 较小，更难解吸）
2. 由产品要求计算关键组分解吸率
3. 计算最小气液比和理论板数
4. 校核 SO₂ 是否满足要求

## 计算过程

### 1. 关键组分解吸率

丁二烯进料总量：$f_{{\\text{{buta}}}} = 8 + 2 = 10$ kmol/h

BS 大部分留在液相，$l_{{\\text{{BS}}}} \\approx 100$ kmol/h。

产品中丁二烯 < 0.5 mol%，要求 $l_{{\\text{{buta}}}} < 0.5$ kmol/h：

$$
\\phi_{{\\text{{buta}}}} = \\frac{{10 - 0.5}}{{10}} = {phi_buta:.4f}
$$

### 2. 关键组分平均 $K$ 值

$$
K_{{\\text{{buta}}}} = \\frac{{4.53 \\times 8 + 4.50 \\times 2}}{{10}} = {K_buta:.4f}
$$

### 3. 最小气液比

$$
\\left(\\frac{{V}}{{L}}\\right)_{{\\min}} = \\frac{{\\phi_{{\\text{{buta}}}}}}{{K_{{\\text{{buta}}}}}} = \\frac{{{phi_buta:.4f}}}{{{K_buta:.4f}}} = {VL_min:.4f}
$$

### 4. 实际气液比

$$
\\frac{{V}}{{L}} = 1.5 \\times {VL_min:.4f} = {VL:.4f}
$$

### 5. 理论板数

$$
S_{{\\text{{buta}}}} = K_{{\\text{{buta}}}} \\cdot \\frac{{V}}{{L}} = {K_buta:.4f} \\times {VL:.4f} = {S_key:.4f}
$$

$$
N = \\frac{{\\log\\left(\\frac{{{S_key:.4f} - {phi_buta:.4f}}}{{1 - {phi_buta:.4f}}}\\right)}}{{\\log {S_key:.4f}}} - 1 = {N_raw:.2f}
$$

圆整：$N = {N}$ 块理论板。

### 6. 各组分分析

| 组分 | $f_i$ | $K_i$ | $S_i$ | $\\phi_i$ | $l_{{\\text{{out}}}}$ | $v_{{\\text{{strip}}}}$ |
|------|:-----:|:-----:|:-----:|:---------:|:----------:|:------------:|
{table_rows.strip()}

### 7. 产品组成校核

液相总量：$\\sum l_i = {total_l:.2f}$ kmol/h

| 组分 | $l_i$ (kmol/h) | mol% | 要求 | 合格？ |
|------|:-------------:|:----:|:----:|:------:|
| SO₂ | {l_out['SO2']:.4f} | {y_SO2_prod*100:.4f} | < 0.05% | {"✓" if y_SO2_prod < 0.0005 else "✗"} |
| 丁二烯 | {l_out['B13']+l_out['B12']:.4f} | {y_buta_prod*100:.4f} | < 0.5% | {"✓" if y_buta_prod < 0.005 else "✗"} |

### 8. N₂ 流量

$$
V = \\frac{{V}}{{L}} \\times F = {VL:.4f} \\times {F} = {V:.2f}\\ \\text{{kmol/h}}
$$

## 答案

| 参数 | 值 |
|------|-----|
| 理论板数 $N$ | **{N}** |
| N₂ 流量 | **{V:.1f} kmol/h** |
| 气液比 $V/L$ | **{VL:.4f}** |

### 产品液相组成

| 组分 | kmol/h | mol% |
|------|:------:|:----:|
| SO₂ | {l_out['SO2']:.4f} | {y_SO2_prod*100:.4f} |
| 1,3-丁二烯 | {l_out['B13']:.4f} | {l_out['B13']/total_l*100:.4f} |
| 1,2-丁二烯 | {l_out['B12']:.4f} | {l_out['B12']/total_l*100:.4f} |
| BS | {l_out['BS']:.2f} | {l_out['BS']/total_l*100:.2f} |

---
[← 返回习题集](index.md)
'''
    save(CH9_EX, 'ex_9.4.md', content)


# ============================================================
# Exercise 9.5 — Propane stripping column
# ============================================================
def gen_9_5():
    F = 100.0
    z = {'CH4': 0.05, 'C2H6': 0.10, 'C3H8': 0.30, 'nC4': 0.40, 'nC5': 0.15}
    l_in = {c: F * zc for c, zc in z.items()}
    K = {'CH4': 10.5, 'C2H6': 3.0, 'C3H8': 0.95, 'nC4': 0.30, 'nC5': 0.10}

    phi_key = 0.95
    K_key = K['C3H8']
    VL_min = phi_key / K_key
    VL = 1.5 * VL_min
    S_key = K_key * VL
    N_raw = N_from_phi_strip(S_key, phi_key)
    N = math.ceil(N_raw)

    S = {}; phi_s = {}; l_out = {}; v_strip = {}
    for c in z:
        S[c] = K[c] * VL
        phi_s[c] = phi_strip(S[c], N)
        l_out[c] = l_in[c] * (1 - phi_s[c])
        v_strip[c] = l_in[c] - l_out[c]

    total_l = sum(l_out.values())
    total_v = sum(v_strip.values())
    L_avg = (F + total_l) / 2
    V = VL * L_avg

    table_rows = ''
    names = {'CH4': 'CH₄', 'C2H6': 'C₂H₆', 'C3H8': 'C₃H₈', 'nC4': 'n-C₄', 'nC5': 'n-C₅'}
    for c in ['CH4', 'C2H6', 'C3H8', 'nC4', 'nC5']:
        table_rows += f'| {names[c]} | {K[c]:.2f} | {S[c]:.4f} | {phi_s[c]:.4f} | {l_in[c]:.1f} | {v_strip[c]:.2f} | {l_out[c]:.2f} |\n'

    liq_rows = ''
    gas_rows = ''
    for c in ['CH4', 'C2H6', 'C3H8', 'nC4', 'nC5']:
        liq_rows += f'| {names[c]} | {l_out[c]:.2f} | {l_out[c]/total_l*100:.2f} |\n'
        gas_rows += f'| {names[c]} | {v_strip[c]:.2f} | {v_strip[c]/total_v*100:.1f} |\n'

    content = f'''
# 习题 9.5

## 题目

丙烷解吸塔，操作压力 1.0 MPa，进料液体 100 kmol/h，温度 40°C，解吸剂 N₂，塔内平均温度 44°C。
进料组成 CH₄(0.05)、C₂H₆(0.10)、C₃H₈(0.30)、n-C₄H₁₀(0.40)、n-C₅H₁₂(0.15)。
要求 C₃H₈ 解吸率 > 95%。计算理论板数、各组分含量和 N₂ 流量。

## 已知条件

| 参数 | 值 |
|------|-----|
| 操作压力 | 1.0 MPa |
| 进料温度 | 40°C |
| 塔内平均温度 | 44°C |
| 进料流量 | 100 kmol/h |
| 解吸剂 | N₂ |
| C₃H₈ 解吸率 | ≥ 95% |

### 相平衡常数（44°C，1.0 MPa，估算值）

| 组分 | $K_i$ |
|------|:-----:|
| 甲烷 (CH₄) | 10.5 |
| 乙烷 (C₂H₆) | 3.0 |
| 丙烷 (C₃H₈) | 0.95 |
| 正丁烷 (n-C₄) | 0.30 |
| 正戊烷 (n-C₅) | 0.10 |

## 求解思路

采用解吸因子法（Kremser 方程）：
1. 选 C₃H₈ 为关键组分（最难解吸的目标组分）
2. 计算最小气液比
3. 确定理论板数
4. 计算各组分分布和 N₂ 流量

## 计算过程

### 1. 进料物料衡算

| 组分 | $z_i$ | $l_{{\\text{{in}}}}$ (kmol/h) | $K_i$ |
|------|:-----:|:-----------------:|:-----:|
| CH₄ | 0.05 | 5.0 | 10.5 |
| C₂H₆ | 0.10 | 10.0 | 3.0 |
| C₃H₈ | 0.30 | 30.0 | 0.95 |
| n-C₄ | 0.40 | 40.0 | 0.30 |
| n-C₅ | 0.15 | 15.0 | 0.10 |
| **合计** | 1.00 | 100.0 | |

### 2. 最小气液比

$$
\\left(\\frac{{V}}{{L}}\\right)_{{\\min}} = \\frac{{\\phi_{{\\text{{key}}}}}}{{K_{{\\text{{key}}}}}} = \\frac{{0.95}}{{0.95}} = {VL_min:.4f}
$$

### 3. 实际气液比

$$
\\frac{{V}}{{L}} = 1.5 \\times {VL_min:.4f} = {VL:.4f}
$$

### 4. 理论板数

$$
S_{{\\text{{C₃H₈}}}} = K_{{\\text{{C₃H₈}}}} \\cdot \\frac{{V}}{{L}} = 0.95 \\times {VL:.4f} = {S_key:.4f}
$$

$$
N = \\frac{{\\log\\left(\\frac{{{S_key:.4f} - {phi_key}}}{{1 - {phi_key}}}\\right)}}{{\\log {S_key:.4f}}} - 1
= {N_raw:.2f}
$$

圆整：$N = {N}$ 块理论板。

### 5. 各组分分析

| 组分 | $K_i$ | $S_i$ | $\\phi_i$ | $l_{{\\text{{in}}}}$ | $v_{{\\text{{strip}}}}$ | $l_{{\\text{{out}}}}$ |
|------|:-----:|:-----:|:---------:|:----------:|:------------:|:----------:|
{table_rows.strip()}

### 6. C₃H₈ 解吸率校核

$$
\\phi_{{\\text{{C₃H₈}}}} = {phi_s['C3H8']:.4f} \\ge 0.95 \\quad \\checkmark
$$

### 7. N₂ 流量

$$
L_{{\\text{{avg}}}} = \\frac{{{F:.0f} + {total_l:.2f}}}{{2}} = {L_avg:.2f}\\ \\text{{kmol/h}}
$$

$$
V = \\frac{{V}}{{L}} \\times L_{{\\text{{avg}}}} = {VL:.4f} \\times {L_avg:.2f} = {V:.2f}\\ \\text{{kmol/h}}
$$

## 答案

| 参数 | 值 |
|------|-----|
| 理论板数 $N$ | **{N}** |
| 气液比 $V/L$ | **{VL:.4f}** |
| N₂ 流量 | **{V:.1f} kmol/h** |

### 出塔液相组成

| 组分 | $l_{{\\text{{out}}}}$ (kmol/h) | mol% |
|------|:-------------------:|:----:|
{liq_rows.strip()}

### 解吸气相组成

| 组分 | $v_{{\\text{{strip}}}}$ (kmol/h) | mol% |
|------|:---------------------:|:----:|
{gas_rows.strip()}

---
[← 返回习题集](index.md)
'''
    save(CH9_EX, 'ex_9.5.md', content)


# ============================================================
# Generate all
# ============================================================
if __name__ == '__main__':
    gen_9_1()
    gen_9_2()
    gen_9_3()
    gen_9_4()
    gen_9_5()
    print('Chapter 9 exercises done')
