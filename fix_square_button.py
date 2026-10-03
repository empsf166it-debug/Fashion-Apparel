import glob
import re

files = glob.glob('*.html')

square_button = '''<a href="#" onclick="window.scrollTo({top: 0, behavior: 'smooth'}); return false;" class="ml-4 p-2 bg-graphite hover:bg-terracotta text-white transition-colors" aria-label="Back to top">
                    <i data-lucide="arrow-up" class="w-4 h-4"></i>
                </a>'''

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # regex to match the round button
    pattern = r'<button onclick="window\.scrollTo\(\{top: 0, behavior: \'smooth\'\}\)" class="ml-4 w-8 h-8 rounded-full bg-graphite flex items-center justify-center text-white hover:bg-terracotta transition-all duration-300" aria-label="Back to top">\s*<svg[^>]*>.*?<\/svg>\s*<\/button>'
    
    content = re.sub(pattern, square_button, content)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print(f"Updated back-to-top button in {len(files)} files.")
