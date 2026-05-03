import DefaultTheme from 'vitepress/theme'
import { h } from 'vue'
import CommentSection from './components/CommentSection.vue'
import 'katex/dist/katex.min.css'
import './custom.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('CommentSection', CommentSection)
  },
  Layout() {
    return h(DefaultTheme.Layout, null, {
      'doc-after': () => h('div', { class: 'comment-wrapper' }, [
        h(CommentSection)
      ]),
    })
  },
}
