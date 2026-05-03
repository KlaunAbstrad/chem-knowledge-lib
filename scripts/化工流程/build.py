"""
Knowledge Base Builder for Chemical Engineering Textbook
Version 2 - Improved parsing
"""
import re
from pathlib import Path

RAW_DIR = Path(r'E:/knowledge_lib/化工流程/raw/text')
WIKI_DIR = Path(r'E:/knowledge_lib/化工流程/wiki')

CHAPTERS = [
    {'key': '第四章_相平衡', 'title': '第四章 相平衡基础', 'dir': '第四章_相平衡'},
    {'key': '第五章', 'title': '第五章 换热器设计', 'dir': '第五章'},
    {'key': '第七章', 'title': '第七章 多组分精馏简捷计算', 'dir': '第七章'},
    {'key': '第九章', 'title': '第九章 多组分吸收和解吸简捷计算', 'dir': '第九章'},
]


def slugify(text):
    text = re.sub(r'[^\w\s-]', '', text)
    return text.strip().replace(' ', '_').replace('-', '_').replace('__', '_')


def read_raw(key):
    path = RAW_DIR / f'{key}.txt'
    text = path.read_text(encoding='utf-8', errors='replace')
    # Remove null bytes and page markers
    text = text.replace('\x00', '')
    text = re.sub(r'={3,}\s*PAGE\s*\d+\s*={3,}', '', text)
    text = re.sub(r'\n\d{2,4}\n', '\n', text)
    text = re.sub(r'^\d{2,4}\n', '', text, flags=re.MULTILINE)
    text = re.sub(r'\n{4,}', '\n\n\n', text)
    return text


def parse_sections(text):
    lines = text.split('\n')
    sections = []
    cur_section = None
    cur_sub = None
    chapter_title = ''

    for i, line in enumerate(lines):
        s = line.strip()
        if not s:
            if cur_sub is not None:
                cur_sub['text_lines'].append('')
            elif cur_section is not None:
                cur_section['text_lines'].append('')
            continue

        # Chapter title
        m = re.match(r'第[一二三四五六七八九十\d]+章\s*(.+)', s)
        if m:
            chapter_title = s
            continue

        # End sections at summary (handle OCR variants)
        if re.search(r'本章小结', s) and re.match(r'\d+\.\d+\s', s):
            if cur_section:
                sections.append(cur_section)
            break

        # Section: "4.1 气液相平衡" or "7.2 DBM (Fenske)" etc.
        # Match any X.Y pattern followed by non-digit content (not table data)
        m = re.match(r'^(\d+)\.(\d+)\s+([^\d].{1,80})$', s)
        if m:
            n1, n2, title = m.groups()
            title = title.strip()
            # Skip if it looks like program output or gibberish
            if len(title) >= 2 and not re.match(r'^[\d\s+\-*/=,.%]+$', title):
                if cur_section:
                    sections.append(cur_section)
                cur_section = {
                    'type': 'section', 'id': f'{n1}.{n2}',
                    'title': f'{n1}.{n2} {title}',
                    'text_lines': [], 'subsections': [],
                }
                cur_sub = None
                continue

        # Sub-section: "4.1.1 相平衡常数" etc.
        m = re.match(r'^(\d+)\.(\d+)\.(\d+)\s+([^\d].{1,80})$', s)
        if m and cur_section:
            n1, n2, n3, title = m.groups()
            title = title.strip()
            if len(title) >= 2 and not re.match(r'^[\d\s+\-*/=,.%]+$', title):
                cur_sub = {
                    'type': 'subsection', 'id': f'{n1}.{n2}.{n3}',
                    'title': f'{n1}.{n2}.{n3} {title}',
                    'text_lines': [],
                }
                cur_section['subsections'].append(cur_sub)
                continue

        # Collect text
        if cur_sub is not None:
            cur_sub['text_lines'].append(s)
        elif cur_section is not None:
            cur_section['text_lines'].append(s)

    # Remove trailing empty lines
    for section in sections:
        for sub in section['subsections']:
            while sub['text_lines'] and sub['text_lines'][-1] == '':
                sub['text_lines'].pop()

    return chapter_title, sections


def parse_exercises(text):
    lines = text.split('\n')
    exercises = []
    in_ex = False
    cur = None

    for line in lines:
        s = line.strip()
        if not s:
            continue
        # Detect exercise section (single line or after chapter summary)
        if re.match(r'^习题$', s) or s == '习题 ':
            in_ex = True
            continue
        if in_ex:
            # Exercise header: [4.1], [7.3] etc
            m = re.match(r'\[(\d+\.\d+)\]\s*(.*)', s)
            if m:
                if cur:
                    exercises.append(cur)
                cur = {'id': m.group(1), 'text': m.group(2), 'lines': [s]}
                continue
            if cur:
                # Stop if we hit a new section or next chapter
                if re.match(r'第\d+章|^\d+\.\d+\s+\S', s):
                    in_ex = False
                    continue
                cur['lines'].append(s)

    if cur:
        exercises.append(cur)
    return exercises


def is_code(line):
    s = line.strip()
    if not s:
        return False
    if re.match(r'^(import |from |def |class |return |print|#|for |while |if |elif |else:|try:|except:|with |finally:)', s):
        return True
    if re.match(r'^[a-zA-Z_]\w*\s*=', s) and '(' in s:
        return True
    if s.startswith(('    ', '\t')):
        return True
    if re.match(r'^[a-zA-Z_]\w+\.[a-zA-Z_]\w*\(', s):
        return True
    if s.startswith('@'):
        return True
    return False


def split_code(lines):
    text = []
    codes = []
    i = 0
    while i < len(lines):
        if is_code(lines[i]):
            block = [lines[i]]
            i += 1
            while i < len(lines) and (is_code(lines[i]) or lines[i].strip() == ''):
                block.append(lines[i])
                i += 1
            cb = '\n'.join(block).strip()
            if cb:
                codes.append(cb)
        else:
            text.append(lines[i])
            i += 1
    return text, codes


def gen_entry_md(title, text_lines, codes):
    lines = []
    lines.append(f'# {title}')
    lines.append('')

    # Filter text
    filtered = [l for l in text_lines if l.strip() and len(l.strip()) > 2]
    if filtered:
        lines.append('## 概述')
        lines.append('')
        lines.append(filtered[0])
        lines.append('')

    if len(filtered) > 1:
        lines.append('## 详细说明')
        lines.append('')
        for l in filtered[1:]:
            lines.append(l)
            lines.append('')
        lines.append('')

    if codes:
        lines.append('## 代码实现')
        lines.append('')
        lines.append('<details>')
        lines.append('<summary>Python 代码</summary>')
        lines.append('')
        lines.append('```python')
        for c in codes:
            lines.append(c)
        lines.append('```')
        lines.append('</details>')
        lines.append('')

    lines.append('---')
    lines.append('[返回目录](index.md)')
    lines.append('')
    return '\n'.join(lines)


def gen_ex_md(title, lines):
    body = '\n'.join(lines)
    return f'''# {title}

## 题目

{body}

## 已知条件

待补充

## 求解思路

待补充

## 计算过程

待补充

## 答案

待补充

---
[返回习题集](index.md)
'''


def process_chapter(cfg):
    d = WIKI_DIR / cfg['dir']
    d.mkdir(parents=True, exist_ok=True)
    ed = d / 'exercises'
    ed.mkdir(parents=True, exist_ok=True)

    print(f'\n=== {cfg["title"]} ===')

    text = read_raw(cfg['key'])
    title, sections = parse_sections(text)
    exercises = parse_exercises(text)

    n_sub = sum(len(s['subsections']) for s in sections)
    print(f'  Sections: {len(sections)}, Sub-sections: {n_sub}, Exercises: {len(exercises)}')

    entries = []
    for section in sections:
        for sub in section['subsections']:
            sub_id = sub['id']
            sub_title = sub['title']
            txt, codes = split_code(sub['text_lines'])
            if not txt and not codes:
                continue

            fn = f'{sub_id}_{slugify(sub_title)}.md'
            content = gen_entry_md(sub_title, txt, codes)
            (d / fn).write_text(content, encoding='utf-8')
            entries.append((sub_id, sub_title, fn))
            print(f'    + {fn}')

    for ex in exercises:
        eid = ex['id']
        fn = f'ex_{eid}.md'
        content = gen_ex_md(f'习题 {eid}', ex['lines'])
        (ed / fn).write_text(content, encoding='utf-8')
        print(f'    + exercise/{fn}')

    # Chapter index
    idx = [f'# {cfg["title"]}', '', '## 目录', '']
    for eid, etitle, fn in entries:
        idx.append(f'- [{etitle}]({fn})')
    idx.append('')

    if exercises:
        idx.append('## 习题')
        idx.append('')
        idx.append('- [全部习题](exercises/index.md)')
        for ex in exercises:
            t = ex['text'][:60] if ex['text'] else ''
            idx.append(f'  - [习题 {ex["id"]}](exercises/ex_{ex["id"]}.md) - {t}')
        idx.append('')

    idx.append('---')
    idx.append('[返回首页](../index.md)')
    idx.append('')
    (d / 'index.md').write_text('\n'.join(idx), encoding='utf-8')

    # Exercise index
    if exercises:
        exi = ['# 习题集', '', '| 编号 | 题目 | 解答 |', '|------|------|------|']
        for ex in exercises:
            t = ex['text'][:60] if ex['text'] else ''
            exi.append(f'| {ex["id"]} | {t} | [查看](ex_{ex["id"]}.md) |')
        exi.extend(['', '---', '[返回目录](../index.md)'])
        (ed / 'index.md').write_text('\n'.join(exi), encoding='utf-8')

    return n_sub, len(exercises)


def main():
    te, tx = 0, 0
    for c in CHAPTERS:
        e, x = process_chapter(c)
        te += e
        tx += x

    home = [
        '# 化工原理知识库',
        '',
        '基于化工教材构建的结构化知识库，涵盖相平衡、换热器设计、多组分精馏与吸收等核心内容。',
        '',
        '## 章节导航',
        '',
    ]
    for c in CHAPTERS:
        home.append(f'- [{c["title"]}]({c["dir"]}/index.md)')
    home.extend([
        '',
        '## 内容概览',
        '',
        '- **相平衡基础** - 相平衡常数、泡点/露点、闪蒸计算',
        '- **换热器设计** - 传热系数、对流传热、流动阻力、冷凝器',
        '- **多组分精馏简捷计算** - Fenske-Underwood-Gilliland (FUG) 法',
        '- **多组分吸收和解吸** - 平均吸收因子法、解吸因子法',
        '',
        f'共 {te} 个知识条目，{tx} 道习题。',
        '',
    ])
    (WIKI_DIR / 'index.md').write_text('\n'.join(home), encoding='utf-8')
    print(f'\n=== Done: {te} entries, {tx} exercises ===')


if __name__ == '__main__':
    main()
