import glob
import re

files = glob.glob('*.html')

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Add overflow-x-hidden to body
    content = content.replace('<body class="bg-ivory dark:bg-charcoal text-charcoal dark:text-ivory antialiased">', 
                              '<body class="bg-ivory dark:bg-charcoal text-charcoal dark:text-ivory antialiased overflow-x-hidden">')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print(f"Added overflow-x-hidden to {len(files)} files.")
