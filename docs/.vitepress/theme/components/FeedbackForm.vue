<template>
  <div class="feedback-form">
    <h3>提交反馈</h3>
    <form @submit.prevent="submitFeedback">
      <div class="field">
        <label>错误类型：</label>
        <div class="checkboxes">
          <label v-for="t in types" :key="t.value">
            <input type="checkbox" v-model="form.types" :value="t.value" /> {{ t.label }}
          </label>
        </div>
      </div>
      <div class="field">
        <label for="suggestion">修正建议：</label>
        <textarea id="suggestion" v-model="form.suggestion" rows="3" placeholder="请描述问题或提出建议…"></textarea>
      </div>
      <div class="field">
        <label>评分：</label>
        <div class="stars">
          <button type="button" v-for="n in 5" :key="n" @click="form.rating = n"
            :class="{ active: n <= form.rating }">★</button>
        </div>
      </div>
      <button type="submit" class="submit-btn" :disabled="submitted">
        {{ submitted ? '已提交' : '提交反馈' }}
      </button>
    </form>
    <div v-if="feedbacks.length > 0" class="export-area">
      <button @click="exportFeedback" class="export-btn">导出所有反馈 (JSON)</button>
      <span class="count">{{ feedbacks.length }} 条待导出</span>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'
import { useData } from 'vitepress'

const { page } = useData()
const submitted = ref(false)

const types = [
  { value: 'formula_error', label: '公式错误' },
  { value: 'description_inaccurate', label: '描述不准' },
  { value: 'missing_content', label: '缺失内容' },
  { value: 'other', label: '其他' },
]

const form = reactive({
  path: '',
  types: [],
  suggestion: '',
  rating: 0,
  timestamp: '',
})

const feedbacks = ref([])

onMounted(() => {
  form.path = page.value.relativePath
  const saved = localStorage.getItem('chem_kb_feedback')
  if (saved) {
    feedbacks.value = JSON.parse(saved)
  }
})

function submitFeedback() {
  const entry = {
    ...form,
    timestamp: new Date().toISOString(),
  }
  feedbacks.value.push(entry)
  localStorage.setItem('chem_kb_feedback', JSON.stringify(feedbacks.value))
  submitted.value = true
  // Reset
  form.types = []
  form.suggestion = ''
  form.rating = 0
  setTimeout(() => { submitted.value = false }, 2000)
}

function exportFeedback() {
  const blob = new Blob([JSON.stringify(feedbacks.value, null, 2)], { type: 'application/json' })
  const url = URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = '知识库反馈_' + new Date().toISOString().slice(0, 10) + '.json'
  a.click()
  URL.revokeObjectURL(url)
}
</script>

<style scoped>
.feedback-form {
  margin-top: 48px;
  padding: 20px 24px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  background: var(--vp-c-bg-soft);
}

.feedback-form h3 {
  margin: 0 0 16px;
  font-size: 16px;
}

.field {
  margin-bottom: 12px;
}

.field label {
  display: block;
  font-size: 14px;
  margin-bottom: 4px;
  color: var(--vp-c-text-1);
}

.checkboxes {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
}

.checkboxes label {
  font-size: 13px;
  display: inline-flex;
  align-items: center;
  gap: 4px;
  cursor: pointer;
}

textarea {
  width: 100%;
  padding: 8px 12px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 4px;
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  font-size: 14px;
  resize: vertical;
}

.stars {
  display: flex;
  gap: 4px;
}

.stars button {
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
  color: var(--vp-c-text-3);
  padding: 0;
  transition: color 0.15s;
}

.stars button.active {
  color: #f5a623;
}

.submit-btn {
  padding: 8px 20px;
  background: var(--vp-c-brand);
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
}

.submit-btn:disabled {
  opacity: 0.6;
  cursor: default;
}

.export-area {
  margin-top: 16px;
  padding-top: 12px;
  border-top: 1px solid var(--vp-c-divider);
  display: flex;
  align-items: center;
  gap: 12px;
}

.export-btn {
  padding: 6px 14px;
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-divider);
  border-radius: 4px;
  cursor: pointer;
  font-size: 13px;
  color: var(--vp-c-text-1);
}

.export-btn:hover {
  border-color: var(--vp-c-brand);
  color: var(--vp-c-brand);
}

.count {
  font-size: 12px;
  color: var(--vp-c-text-3);
}
</style>
