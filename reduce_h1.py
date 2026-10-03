import glob
import re

files = glob.glob('*.html')

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    def replace_h1(match):
        inner = match.group(1)
        # reduce text-5xl md:text-7xl down to text-4xl md:text-6xl
        inner = re.sub(r'text-5xl md:text-7xl', 'text-4xl md:text-6xl', inner)
        return f'<h1{inner}>'
        
    content = re.sub(r'<h1([^>]+)>', replace_h1, content)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print(f"Reduced hero h1 heading sizes to text-4xl md:text-6xl in {len(files)} files.")
