import glob
import re

files = glob.glob('*.html')

new_social = '''                <div class="flex gap-4">
                    <a href="#" class="w-10 h-10 rounded-full border border-graphite flex items-center justify-center text-gray-400 hover:text-white hover:bg-terracotta hover:border-terracotta transition-all duration-300 group">
                        <svg class="w-4 h-4 group-hover:text-white" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
                    </a>
                    <a href="#" class="w-10 h-10 rounded-full border border-graphite flex items-center justify-center text-gray-400 hover:text-white hover:bg-terracotta hover:border-terracotta transition-all duration-300 group">
                        <svg class="w-4 h-4 group-hover:text-white" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 4s-.7 2.1-2 3.4c1.6 10-9.4 17.3-18 11.6 2.2.1 4.4-.6 6-2C3 15.5.5 9.6 3 5c2.2 2.6 5.6 4.1 9 4-.9-4.2 4-6.6 7-3.8 1.1 0 3-1.2 3-1.2z"></path></svg>
                    </a>
                    <a href="#" class="w-10 h-10 rounded-full border border-graphite flex items-center justify-center text-gray-400 hover:text-white hover:bg-terracotta hover:border-terracotta transition-all duration-300 group">
                        <svg class="w-4 h-4 group-hover:text-white" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
                    </a>
                    <a href="#" class="w-10 h-10 rounded-full border border-graphite flex items-center justify-center text-gray-400 hover:text-white hover:bg-terracotta hover:border-terracotta transition-all duration-300 group">
                        <svg class="w-4 h-4 group-hover:text-white" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg>
                    </a>
                </div>'''

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace footer icons
    content = re.sub(
        r'<div class="flex gap-4">\s*<a href="#" class="text-gray-400 hover:text-terracotta transition-colors"><i data-lucide="instagram"[^>]*></i></a>\s*<a href="#" class="text-gray-400 hover:text-terracotta transition-colors"><i data-lucide="twitter"[^>]*></i></a>\s*<a href="#" class="text-gray-400 hover:text-terracotta transition-colors"><i data-lucide="linkedin"[^>]*></i></a>\s*</div>',
        new_social,
        content
    )
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print(f"Replaced footer social icons in {len(files)} files.")
