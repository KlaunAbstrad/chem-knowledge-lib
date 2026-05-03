import DefaultTheme from 'vitepress/theme'
import { h } from 'vue'
import FeedbackForm from './components/FeedbackForm.vue'
import 'katex/dist/katex.min.css'
import './custom.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('FeedbackForm', FeedbackForm)
  },
  Layout() {
    return h(DefaultTheme.Layout, null, {
      'doc-after': () => h('div', { class: 'feedback-wrapper' }, [
        h(FeedbackForm)
      ]),
    })
  },
}
