import glob
import re

files = glob.glob('*.html')

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We want to replace the size classes in h1 tags.
    # Look for <h1 class="text-3xl md:text-3xl 
    # Or just replace text-3xl md:text-3xl within h1.
    def replace_h1(match):
        inner = match.group(1)
        # replace any text- size classes with text-5xl md:text-7xl
        inner = re.sub(r'text-\d+xl( md:text-\d+xl)?', 'text-5xl md:text-7xl', inner)
        return f'<h1{inner}>'
        
    content = re.sub(r'<h1([^>]+)>', replace_h1, content)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print(f"Restored hero h1 heading sizes to text-5xl md:text-7xl in {len(files)} files.")
