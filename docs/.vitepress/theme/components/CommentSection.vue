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

const { page, isDark } = useData()
const giscusContainer = ref(null)

let scriptLoaded = false

function loadGiscus() {
  if (!giscusContainer.value) return

  // Remove previous giscus widget if any
  const existing = giscusContainer.value.querySelector('giscus-widget')
  if (existing) existing.remove()

  const script = document.createElement('script')
  script.src = 'https://giscus.app/client.js'
  script.setAttribute('data-repo', 'KlaunAbstrad/chem-knowledge-lib')
  script.setAttribute('data-repo-id', 'R_kg_DOON_TEST') // 替换为实际 Repo ID
  script.setAttribute('data-category', 'Announcements')
  script.setAttribute('data-category-id', 'DIC_kw_DOON_TEST') // 替换为实际 Category ID
  script.setAttribute('data-mapping', 'pathname')
  script.setAttribute('data-strict', '0')
  script.setAttribute('data-reactions-enabled', '1')
  script.setAttribute('data-emit-metadata', '0')
  script.setAttribute('data-input-position', 'top')
  script.setAttribute('data-theme', isDark.value ? 'dark' : 'light')
  script.setAttribute('data-lang', 'zh-CN')
  script.setAttribute('crossorigin', 'anonymous')
  script.async = true

  giscusContainer.value.appendChild(script)
  scriptLoaded = true
}

onMounted(() => {
  loadGiscus()
})

watch(isDark, () => {
  if (scriptLoaded) {
    // Send theme change message to giscus
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
