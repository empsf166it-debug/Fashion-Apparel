import glob
import re

files = glob.glob('*.html')

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace md:flex with lg:flex for the nav
    content = content.replace('<nav class="hidden md:flex items-center gap-8', '<nav class="hidden lg:flex items-center gap-8')
    
    # Replace gap-2 md:gap-4 with gap-2 lg:gap-4
    content = content.replace('<div class="flex items-center gap-2 md:gap-4">', '<div class="flex items-center gap-2 lg:gap-4">')
    
    # Replace md:inline-flex with lg:inline-flex for Contact Us
    content = content.replace('class="hidden md:inline-flex px-5 py-2.5', 'class="hidden lg:inline-flex px-5 py-2.5')
    
    # Replace md:hidden with lg:hidden for hamburger
    content = content.replace('<button id="mobile-menu-btn" class="md:hidden p-2">', '<button id="mobile-menu-btn" class="lg:hidden p-2">')
    
    # Replace md:hidden with lg:hidden for mobile menu wrapper
    content = content.replace('class="hidden md:hidden absolute w-full', 'class="hidden lg:hidden absolute w-full')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print(f"Updated breakpoints for {len(files)} files.")
