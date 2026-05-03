"""
Migrate project to multi-course knowledge base structure.
Run: PYTHONIOENCODING=utf-8 python scripts/migrate.py
"""
import shutil
from pathlib import Path

BASE = Path(r'E:/knowledge_lib/chem-knowledge-base')

def mv(src, dst):
    """Move file/dir, creating parent dirs."""
    if not src.exists():
        print(f'  SKIP (not found): {src}')
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        print(f'  SKIP (already exists): {dst}')
        return
    print(f'  {src.relative_to(BASE)} → {dst.relative_to(BASE)}')
    shutil.move(str(src), str(dst))

print('=== Stage 1: Move wiki content to docs/ ===')

# Move chapter dirs from wiki/化工流程/ to docs/化工流程/
wiki_src = BASE / 'wiki' / '化工流程'
docs_course = BASE / 'docs' / '化工流程'
docs_course.mkdir(parents=True, exist_ok=True)

for item in wiki_src.iterdir():
    if item.name == '.vitepress':
        continue
    mv(item, docs_course / item.name)

# Move .vitepress from wiki/化工流程/ to docs/
mv(wiki_src / '.vitepress', BASE / 'docs' / '.vitepress')

# Clean up empty wiki dirs
for d in [wiki_src, BASE / 'wiki']:
    if d.exists():
        try:
            remaining = list(d.iterdir())
            if not remaining:
                d.rmdir()
                print(f'  Removed: {d.relative_to(BASE)}')
        except:
            pass

print('\n=== Stage 2: Verify raw/ structure ===')

# raw/ should already have subdirs by course
raw_dirs = ['ebook', 'scan', 'text']
for sub in raw_dirs:
    src = BASE / 'raw' / '化工流程' / sub
    if src.exists():
        print(f'  ✓ raw/化工流程/{sub}')
    else:
        print(f'  ✗ MISSING: raw/化工流程/{sub}')

# Create placeholder raw dirs for future courses
for course in ['化工原理', '有机化学']:
    for sub in ['ebook', 'scan', 'text']:
        (BASE / 'raw' / course / sub).mkdir(parents=True, exist_ok=True)
    print(f'  Created: raw/{course}/{{ebook,scan,text}}')

print('\n=== Stage 3: Verify scripts/ structure ===')
for course in ['化工流程', '化工原理', '有机化学']:
    script_dir = BASE / 'scripts' / course
    script_dir.mkdir(parents=True, exist_ok=True)
    py_files = list(script_dir.glob('*.py'))
    if py_files:
        print(f'  ✓ scripts/{course}/ ({len(py_files)} scripts)')
    else:
        print(f'  ○ scripts/{course}/ (empty - awaiting content)')

print('\n=== Stage 4: Create placeholder pages ===')

# 化工原理 placeholder
hp_index = BASE / 'docs' / '化工原理' / 'index.md'
if not hp_index.exists():
    hp_index.parent.mkdir(parents=True, exist_ok=True)
    hp_index.write_text('''# 化工原理

> 🚧 内容即将上线

化工原理课程知识库正在建设中。敬请期待。

[← 返回知识库首页](/)
''', encoding='utf-8')
    print(f'  ✓ Created: docs/化工原理/index.md')

# 有机化学 placeholder
oc_index = BASE / 'docs' / '有机化学' / 'index.md'
if not oc_index.exists():
    oc_index.parent.mkdir(parents=True, exist_ok=True)
    oc_index.write_text('''# 有机化学

> 🔮 规划中

有机化学课程知识库将在未来建设。

[← 返回知识库首页](/)
''', encoding='utf-8')
    print(f'  ✓ Created: docs/有机化学/index.md')

print('\n=== Final structure ===')
for d in ['docs', 'docs/化工流程', 'docs/化工原理', 'docs/有机化学',
          'docs/.vitepress', 'raw/化工流程/text', 'raw/化工原理', 'raw/有机化学',
          'scripts/化工流程', 'scripts/化工原理', 'scripts/有机化学']:
    p = BASE / d
    exists = '✓' if p.exists() else '✗'
    print(f'  {exists} {d}')

print('\nMigration complete!')
