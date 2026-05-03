"""
Add collapsible solution sections to exercise files using VitePress ::: details syntax.
Handles different section naming conventions from different generators.
"""
from pathlib import Path

EXERCISE_DIRS = [
    'docs/化工流程/第四章_相平衡/exercises',
    'docs/化工流程/第五章/exercises',
    'docs/化工流程/第七章/exercises',
    'docs/化工流程/第九章/exercises',
]

# Possible markers where solution content begins (in order of preference)
SOLUTION_MARKERS = [
    '## 求解思路',
    '### 求解思路',
    '## 计算过程',
]

BASE = Path(r'E:/knowledge_lib/chem-knowledge-base')

for dir_path in EXERCISE_DIRS:
    full_dir = BASE / dir_path
    for ex_file in sorted(full_dir.glob('ex_*.md')):
        content = ex_file.read_text(encoding='utf-8')

        # Skip if already has details wrapper
        if '::: details' in content:
            print(f'  Skip (already wrapped): {ex_file.name}')
            continue

        lines = content.split('\n')

        # Find solution start (first matching marker)
        solution_start = None
        for marker in SOLUTION_MARKERS:
            for i, line in enumerate(lines):
                if line.strip() == marker:
                    solution_start = i
                    break
            if solution_start is not None:
                break

        # Find footer "---" that represents the end of page content
        # It's the last "---" in the file (before the back-link)
        footer_line = None
        for i in range(len(lines) - 1, -1, -1):
            stripped = lines[i].strip()
            if stripped == '---':
                footer_line = i
                break

        if solution_start is None:
            print(f'  WARNING: No solution marker found in {ex_file.name}, skipping')
            continue

        if footer_line is None or footer_line <= solution_start:
            print(f'  WARNING: No footer found after solution in {ex_file.name}, skipping')
            continue

        before = lines[:solution_start]
        solution = lines[solution_start:footer_line]
        after = lines[footer_line:]

        new_content = '\n'.join(before) + '\n\n'
        new_content += '::: details 点击查看解答\n\n'
        new_content += '\n'.join(solution) + '\n\n'
        new_content += ':::\n\n'
        new_content += '\n'.join(after)

        ex_file.write_text(new_content, encoding='utf-8')
        print(f'  Updated: {ex_file.name}')

print('Done.')
