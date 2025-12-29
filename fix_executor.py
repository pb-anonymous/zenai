#!/usr/bin/env python3
# Fix indentation in executor.py

with open(r'd:\zen - anki\executor.py', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# Replace the problematic section - the elif block starting at line 283
old_section = '''        elif action == "create_ppt":
    # 1. Decide template
    template_type = step.get("template", "default").lower()'''

new_section = '''        elif action == "create_ppt":
            # 1. Decide template
            template_type = step.get("template", "default").lower()'''

if old_section in content:
    content = content.replace(old_section, new_section)
    print("Found and replaced the first occurrence")
    
    # Now fix the rest of the block
    lines = content.split('\n')
    fixed_lines = []
    in_create_ppt = False
    
    for i, line in enumerate(lines):
        if '        elif action == "create_ppt":' in line:
            in_create_ppt = True
            fixed_lines.append(line)
        elif in_create_ppt:
            if line.strip().startswith('elif action') or line.strip().startswith('return '):
                in_create_ppt = False
                fixed_lines.append(line)
            elif line.strip() == '':
                fixed_lines.append(line)
            elif line.startswith('    ') and not line.startswith('            '):
                # This line should have 12 spaces (3 levels of indentation)
                # Currently has 4, add 8 more
                if not line.startswith('        '):
                    fixed_lines.append('        ' + line.lstrip())
                else:
                    fixed_lines.append(line)
            else:
                fixed_lines.append(line)
        else:
            fixed_lines.append(line)
    
    content = '\n'.join(fixed_lines)

with open(r'd:\zen - anki\executor.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed executor.py indentation")
