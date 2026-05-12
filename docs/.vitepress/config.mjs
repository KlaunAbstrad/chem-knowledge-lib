import { defineConfig } from 'vitepress'
import katex from 'markdown-it-katex'

const sidebar = {
  '/化工流程/': [
    {
      text: '化工流程',
      items: [
        { text: '课程首页', link: '/化工流程/' },
        { text: '术语索引 (A-Z)', link: '/化工流程/术语索引' },
        {
          text: '第四章 相平衡基础',
          collapsed: false,
          items: [
            { text: '4.1.1 相平衡常数', link: '/化工流程/第四章_相平衡/4.1.1_相平衡常数' },
            { text: '4.1.2 泡点与露点', link: '/化工流程/第四章_相平衡/4.1.2_泡点与露点' },
            { text: '4.1.3 Peng-Robinson 状态方程', link: '/化工流程/第四章_相平衡/4.1.3_Peng-Robinson状态方程' },
            { text: '4.2 闪蒸计算', link: '/化工流程/第四章_相平衡/4.2_闪蒸计算' },
            { text: '例 4.1 Antoine 方程', link: '/化工流程/第四章_相平衡/例4.1_Antoine方程' },
            { text: '例 4.2 PR 方程求摩尔体积', link: '/化工流程/第四章_相平衡/例4.2_Peng-Robinson摩尔体积' },
          ]
        },
        {
          text: '第四章 习题',
          collapsed: false,
          items: [
            { text: '习题 4.1 — 相平衡常数', link: '/化工流程/第四章_相平衡/exercises/ex_4.1' },
            { text: '习题 4.2 — 露点压力', link: '/化工流程/第四章_相平衡/exercises/ex_4.2' },
            { text: '习题 4.3 — Wilson 泡点', link: '/化工流程/第四章_相平衡/exercises/ex_4.3' },
            { text: '习题 4.4 — 闪蒸条件判断', link: '/化工流程/第四章_相平衡/exercises/ex_4.4' },
            { text: '习题 4.5 — 泡露点与闪蒸', link: '/化工流程/第四章_相平衡/exercises/ex_4.5' },
          ]
        },
        {
          text: '第五章 换热器设计',
          collapsed: true,
          items: [
            { text: '5.1.1 能量衡算', link: '/化工流程/第五章/5.1.1_能量衡算' },
            { text: '5.1.2 总传热系数', link: '/化工流程/第五章/5.1.2_总传热系数' },
            { text: '5.1.3 平均温度差', link: '/化工流程/第五章/5.1.3_平均温度差' },
            { text: '5.2.1 管内传热系数', link: '/化工流程/第五章/5.2.1_管内传热系数' },
            { text: '5.2.2 壳程传热系数', link: '/化工流程/第五章/5.2.2_壳程传热系数' },
            { text: '5.3.1 管内阻力', link: '/化工流程/第五章/5.3.1_管内阻力' },
            { text: '5.3.2 壳程阻力', link: '/化工流程/第五章/5.3.2_壳程阻力' },
            { text: '5.4 遗传算法优化换热器', link: '/化工流程/第五章/5.4_遗传算法优化换热器' },
            { text: '5.5 竖管冷凝器', link: '/化工流程/第五章/5.5_竖管管外冷凝器' },
            { text: '例 5.1 管内压降计算', link: '/化工流程/第五章/例5.1_管内压降计算' },
            { text: '例 5.3 套管换热器设计', link: '/化工流程/第五章/例5.3_套管换热器设计' },
          ]
        },
        {
          text: '第五章 习题',
          collapsed: true,
          items: [
            { text: '习题 5.1 — 管内对流传热', link: '/化工流程/第五章/exercises/ex_5.1' },
            { text: '习题 5.2 — 管束对流传热', link: '/化工流程/第五章/exercises/ex_5.2' },
            { text: '习题 5.3 — 摩擦系数计算', link: '/化工流程/第五章/exercises/ex_5.3' },
            { text: '习题 5.4 — 换热器设计', link: '/化工流程/第五章/exercises/ex_5.4' },
            { text: '习题 5.5 — 管排列对比', link: '/化工流程/第五章/exercises/ex_5.5' },
            { text: '习题 5.6 — 竖管冷凝器', link: '/化工流程/第五章/exercises/ex_5.6' },
          ]
        },
        {
          text: '第七章 多组分精馏',
          collapsed: true,
          items: [
            { text: '7.1 关键组分与清晰分割', link: '/化工流程/第七章/7.1_关键组分与清晰分割' },
            { text: '7.2 Fenske 方程', link: '/化工流程/第七章/7.2_Fenske方程' },
            { text: '7.3 Underwood 方程', link: '/化工流程/第七章/7.3_Underwood方程' },
            { text: '7.4 Gilliland 关联式', link: '/化工流程/第七章/7.4_Gilliland关联式' },
            { text: '例 7.1 FUG 全流程计算', link: '/化工流程/第七章/例7.1_FUG全流程计算' },
          ]
        },
        {
          text: '第七章 习题',
          collapsed: true,
          items: [
            { text: '习题 7.1 — 脱乙烷塔', link: '/化工流程/第七章/exercises/ex_7.1' },
            { text: '习题 7.2 — 脱丁烷塔', link: '/化工流程/第七章/exercises/ex_7.2' },
            { text: '习题 7.3 — FUG 全计算', link: '/化工流程/第七章/exercises/ex_7.3' },
            { text: '习题 7.4 — 苯-甲苯-二甲苯', link: '/化工流程/第七章/exercises/ex_7.4' },
            { text: '习题 7.5 — 脱丁烷塔 FUG', link: '/化工流程/第七章/exercises/ex_7.5' },
          ]
        },
        {
          text: '第九章 吸收与解吸',
          collapsed: true,
          items: [
            { text: '9.1 平均吸收因子法', link: '/化工流程/第九章/9.1_平均吸收因子法' },
            { text: '9.2 解吸因子法', link: '/化工流程/第九章/9.2_解吸因子法' },
            { text: '例 9.1 多组分吸收塔设计', link: '/化工流程/第九章/例9.1_多组分吸收塔设计' },
            { text: '例 9.2 VOC 解吸塔设计', link: '/化工流程/第九章/例9.2_VOC解吸塔设计' },
          ]
        },
        {
          text: '第九章 习题',
          collapsed: true,
          items: [
            { text: '习题 9.1 — 吸收塔设计', link: '/化工流程/第九章/exercises/ex_9.1' },
            { text: '习题 9.2 — H2 纯化吸收', link: '/化工流程/第九章/exercises/ex_9.2' },
            { text: '习题 9.3 — VOC 空气解吸', link: '/化工流程/第九章/exercises/ex_9.3' },
            { text: '习题 9.4 — N2 解吸丁二烯', link: '/化工流程/第九章/exercises/ex_9.4' },
            { text: '习题 9.5 — 丙烷解吸塔', link: '/化工流程/第九章/exercises/ex_9.5' },
          ]
        },
      ]
    },
  ],
  '/化工原理/': [
    {
      text: '化工原理（下）',
      items: [
        { text: '课程首页', link: '/化工原理/' },
        {
          text: '第六章 蒸馏',
          collapsed: false,
          items: [
            { text: '章节首页', link: '/化工原理/第六章_蒸馏/' },
            { text: '6.1 简单蒸馏与闪蒸', link: '/化工原理/第六章_蒸馏/6.1_简单蒸馏与闪蒸' },
            { text: '6.2 精馏原理', link: '/化工原理/第六章_蒸馏/6.2_精馏原理' },
            { text: '6.3 二元精馏计算', link: '/化工原理/第六章_蒸馏/6.3_二元精馏计算' },
            { text: '6.4 多组分精馏', link: '/化工原理/第六章_蒸馏/6.4_多组分精馏' },
            { text: '6.5 特殊精馏', link: '/化工原理/第六章_蒸馏/6.5_特殊精馏' },
            { text: '例 6.1 闪蒸计算', link: '/化工原理/第六章_蒸馏/例6.1_闪蒸计算' },
            { text: '例 6.2 二元精馏塔设计', link: '/化工原理/第六章_蒸馏/例6.2_二元精馏塔设计' },
          ]
        },
        {
          text: '第六章 习题',
          collapsed: true,
          items: [
            { text: '习题 6.1 — 简单蒸馏', link: '/化工原理/第六章_蒸馏/exercises/ex_6.1' },
            { text: '习题 6.2 — 闪蒸条件', link: '/化工原理/第六章_蒸馏/exercises/ex_6.2' },
            { text: '习题 6.3 — 二元精馏', link: '/化工原理/第六章_蒸馏/exercises/ex_6.3' },
            { text: '习题 6.4 — 多组分精馏', link: '/化工原理/第六章_蒸馏/exercises/ex_6.4' },
            { text: '习题 6.5 — 特殊精馏', link: '/化工原理/第六章_蒸馏/exercises/ex_6.5' },
          ]
        },
      ]
    },
  ],
  '/有机化学/': [
    {
      text: '有机化学',
      items: [
        { text: '课程首页', link: '/有机化学/' },
        {
          text: '第 1 章 有机分子的结构与成键',
          collapsed: true,
          items: [
            { text: '章节首页', link: '/有机化学/第1章_结构与成键/' },
            { text: '1.1 原子轨道与电子构型', link: '/有机化学/第1章_结构与成键/1.1_原子轨道与电子构型' },
            { text: '1.2 杂化轨道理论', link: '/有机化学/第1章_结构与成键/1.2_杂化轨道理论' },
            { text: '1.3 σ 键与 π 键', link: '/有机化学/第1章_结构与成键/1.3_σ键与π键' },
            { text: '1.4 共轭与共振', link: '/有机化学/第1章_结构与成键/1.4_共轭与共振' },
            { text: '1.5 官能团概述', link: '/有机化学/第1章_结构与成键/1.5_官能团概述' },
            { text: '1.6 有机酸碱理论', link: '/有机化学/第1章_结构与成键/1.6_有机酸碱理论' },
            { text: '1.7 命名法基础', link: '/有机化学/第1章_结构与成键/1.7_命名法基础' },
          ]
        },
      ]
    }
  ],
}

export default defineConfig({
  title: '化学知识库',
  description: '化工流程 · 化工原理 · 有机化学 — 可增长的化学维基百科',
  lang: 'zh-CN',
  base: '/chem-knowledge-lib/',
  cleanUrls: true,

  themeConfig: {
    nav: [
      { text: '首页', link: '/' },
      { text: '化工流程', link: '/化工流程/' },
      { text: '化工原理', link: '/化工原理/' },
      { text: '有机化学', link: '/有机化学/' },
      { text: '术语索引', link: '/化工流程/术语索引' },
      { text: '关于', link: '/about' },
    ],

    sidebar,

    search: {
      provider: 'local',
      options: {
        translations: {
          button: { buttonText: '搜索' },
          modal: {
            noResultsText: '未找到结果',
            resetButtonTitle: '清除',
            footer: { selectText: '选择', navigateText: '切换' },
          },
        },
      },
    },

    outline: {
      level: [2, 3],
      label: '页面导航',
    },

    docFooter: {
      prev: '上一页',
      next: '下一页',
    },

    lastUpdated: {
      text: '最后更新',
    },

    editLink: {
      pattern: 'https://github.com/KlaunAbstrad/chem-knowledge-lib/edit/master/docs/:path',
      text: '在 GitHub 上编辑此页',
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/KlaunAbstrad/chem-knowledge-lib' },
    ],
  },

  markdown: {
    config: (md) => {
      md.use(katex, {
        throwOnError: false,
        errorColor: '#cc0000',
      })
    },
  },

  head: [],
})
