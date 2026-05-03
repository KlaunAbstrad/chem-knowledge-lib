<template>
  <div class="comment-section">
    <h3>讨论与反馈</h3>
    <p class="hint">
      对本文内容有疑问或建议？请在此留言。评论使用
      <a href="https://github.com/KlaunAbstrad/chem-knowledge-lib/discussions" target="_blank">
        GitHub Discussions
      </a>
      存储。
    </p>
    <div ref="giscusContainer" class="giscus"></div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useData } from 'vitepress'

const { isDark } = useData()
const giscusContainer = ref(null)

const GISCUS_CONFIG = {
  repo: 'KlaunAbstrad/chem-knowledge-lib',
  repoId: 'R_kgDOSS5fwA',
  category: 'General',
  categoryId: 'DIC_kwDOB',   // ← 待你从 giscus.app 获取
}

let scriptLoaded = false

function loadGiscus() {
  if (!giscusContainer.value) return

  const existing = giscusContainer.value.querySelector('giscus-widget')
  if (existing) existing.remove()

  const script = document.createElement('script')
  script.src = 'https://giscus.app/client.js'
  script.setAttribute('data-repo', GISCUS_CONFIG.repo)
  script.setAttribute('data-repo-id', GISCUS_CONFIG.repoId)
  script.setAttribute('data-category', GISCUS_CONFIG.category)
  script.setAttribute('data-category-id', GISCUS_CONFIG.categoryId)
  script.setAttribute('data-mapping', 'pathname')
  script.setAttribute('data-strict', '0')
  script.setAttribute('data-reactions-enabled', '1')
  script.setAttribute('data-emit-metadata', '0')
  script.setAttribute('data-input-position', 'top')
  script.setAttribute('data-theme', isDark.value ? 'dark' : 'light')
  script.setAttribute('data-lang', 'zh-CN')
  script.setAttribute('crossorigin', 'anonymous')
  script.async = true

  script.onerror = () => {
    giscusContainer.value.innerHTML =
      '<p style="color:var(--vp-c-text-3);font-size:14px;">评论区暂未配置完成。请确认 GitHub Discussions 已启用、Giscus App 已安装、且 category-id 已正确填入。</p>'
  }

  giscusContainer.value.appendChild(script)
  scriptLoaded = true
}

onMounted(() => {
  loadGiscus()
})

watch(isDark, () => {
  if (scriptLoaded) {
    const iframe = document.querySelector('iframe.giscus-frame')
    if (iframe) {
      iframe.contentWindow.postMessage(
        { giscus: { setConfig: { theme: isDark.value ? 'dark' : 'light' } } },
        'https://giscus.app'
      )
    }
  }
})
</script>

<style scoped>
.comment-section {
  margin-top: 48px;
  padding-top: 24px;
  border-top: 1px solid var(--vp-c-divider);
}

.comment-section h3 {
  margin: 0 0 8px;
  font-size: 16px;
}

.hint {
  font-size: 13px;
  color: var(--vp-c-text-3);
  margin-bottom: 20px;
}

.hint a {
  color: var(--vp-c-brand);
  text-decoration: underline;
}

.giscus {
  min-height: 200px;
}
</style>
