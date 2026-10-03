import glob
import re
import os

files = glob.glob('*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove the RTL button. It can be on one line or broken across lines.
    # We use a regex that matches the button tag regardless of spacing.
    content = re.sub(r'[ \t]*<button id="rtl-toggle"[^>]*>RTL</button>\r?\n?', '', content)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print(f"Processed {len(files)} files.")
