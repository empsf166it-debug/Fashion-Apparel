import os
import glob
files = glob.glob('*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    old_code = '''                <div class="flex items-center gap-3 mb-6">
                    <i data-lucide="scissors" class="w-6 h-6 text-terracotta"></i>
                    <span class="font-serif text-2xl font-bold tracking-tight">Sartoria</span>
                </div>'''
    new_code = '''                <a href="index.html" class="flex items-center gap-3 mb-6 hover:opacity-80 transition-opacity">
                    <i data-lucide="scissors" class="w-6 h-6 text-terracotta"></i>
                    <span class="font-serif text-2xl font-bold tracking-tight">Sartoria</span>
                </a>'''
    
    if old_code in content:
        content = content.replace(old_code, new_code)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f'Updated {f}')
