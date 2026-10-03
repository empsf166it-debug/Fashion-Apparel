import glob
import re

files = glob.glob('*.html')

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Hero / Huge headings
    content = content.replace('text-5xl md:text-7xl', 'text-4xl md:text-6xl')
    content = content.replace('text-5xl md:text-6xl', 'text-4xl md:text-5xl')
    content = content.replace('text-4xl md:text-6xl', 'text-3xl md:text-5xl')
    
    # Standard Section headings
    content = content.replace('text-4xl md:text-5xl', 'text-3xl md:text-4xl')
    
    # Standalone large headings
    content = content.replace('text-5xl font-serif', 'text-4xl font-serif')
    content = content.replace('text-4xl font-serif', 'text-3xl font-serif')
    
    # Also some text-3xl font-serif could be reduced to text-2xl font-serif if the user meant ALL headings?
    # "reduce all the section heading size in all pages". Let's stick to the main 4xl/5xl ones which are the typical section headings.
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print(f"Reduced heading sizes in {len(files)} files.")
