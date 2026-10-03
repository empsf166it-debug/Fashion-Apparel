import glob
import re

files = glob.glob('*.html')

new_header_right = '''<div class="flex items-center gap-2 md:gap-4">
                <a href="contact.html" class="hidden md:inline-flex px-5 py-2.5 bg-charcoal text-ivory dark:bg-ivory dark:text-charcoal text-xs tracking-wider uppercase hover:bg-terracotta dark:hover:bg-terracotta transition-colors">Contact Us</a>
                <button id="theme-toggle" class="p-2 hover:text-terracotta transition-colors"><i data-lucide="moon" class="w-5 h-5"></i></button>
                <button id="mobile-menu-btn" class="md:hidden p-2"><i data-lucide="menu" class="w-6 h-6"></i></button>
            </div>'''

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # regex to match from the old div to the end of the mobile menu btn
    pattern = r'<div class="hidden md:flex items-center gap-4">\s*<a href="contact\.html"[^>]*>Contact Us</a>\s*<button id="theme-toggle"[^>]*>[\s\S]*?</button>\s*</div>\s*<button id="mobile-menu-btn"[^>]*>[\s\S]*?</button>'
    
    content = re.sub(pattern, new_header_right, content)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print(f"Moved theme toggle for {len(files)} files.")
