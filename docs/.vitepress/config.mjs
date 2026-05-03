import { defineConfig } from 'vitepress'
import katex from 'markdown-it-katex'

const sidebar = {
  '/化工流程/': [
    {
      text: '化工流程',
      items: [
        { text: '课程首页', link: '/化工流程/' },
        {
          text: '第四章 相平衡基础',
          collapsed: false,
          items: [
            { text: '4.1.1 相平衡常数', link: '/化工流程/第四章_相平衡/4.1.1_相平衡常数' },
            { text: '4.1.2 泡点与露点', link: '/化工流程/第四章_相平衡/4.1.2_泡点与露点' },
            { text: '4.2 闪蒸计算', link: '/化工流程/第四章_相平衡/4.2_闪蒸计算' },
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
            { text: '5.5 竖管冷凝器', link: '/化工流程/第五章/5.5_竖管管外冷凝器' },
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
          ]
        },
        {
          text: '第九章 习题',
          collapsed: true,
          items: [
            { text: '习题 9.1 — 吸收塔设计', link: '/化工流程/第九章/exercises/ex_9.1' },
            { text: '习题 9.2 — H₂ 纯化吸收', link: '/化工流程/第九章/exercises/ex_9.2' },
            { text: '习题 9.3 — VOC 空气解吸', link: '/化工流程/第九章/exercises/ex_9.3' },
            { text: '习题 9.4 — N₂ 解吸丁二烯', link: '/化工流程/第九章/exercises/ex_9.4' },
            { text: '习题 9.5 — 丙烷解吸塔', link: '/化工流程/第九章/exercises/ex_9.5' },
          ]
        },
      ]
    },
  ],
  '/化工原理/': [
    {
      text: '化工原理',
      items: [
        { text: '课程首页', link: '/化工原理/' },
        { text: '🚧 内容即将上线', link: '/化工原理/' },
      ]
    }
  ],
  '/有机化学/': [
    {
      text: '有机化学',
      items: [
        { text: '课程首页', link: '/有机化学/' },
        { text: '🔮 规划中', link: '/有机化学/' },
      ]
    }
  ],
}

export default defineConfig({
  title: '化学知识库',
  description: '化工流程 · 化工原理 · 有机化学 — 可增长的化学维基百科',
  lang: 'zh-CN',
  cleanUrls: true,

  themeConfig: {
    nav: [
      { text: '首页', link: '/' },
      { text: '化工流程', link: '/化工流程/' },
      { text: '化工原理', link: '/化工原理/' },
      { text: '有机化学', link: '/有机化学/' },
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
      pattern: 'https://github.com/KlaunAbstrad/chem-knowledge-base/edit/main/docs/:path',
      text: '在 GitHub 上编辑此页',
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/KlaunAbstrad/chem-knowledge-base' },
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

  head: [
    ['link', { rel: 'stylesheet', href: 'https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css' }],
  ],
})
