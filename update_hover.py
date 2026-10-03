import glob
import re

files = glob.glob('*.html')

new_footer_social = '''                <div class="flex gap-4">
                    <a href="#" class="w-10 h-10 rounded-full border border-graphite flex items-center justify-center text-gray-400 hover:text-terracotta hover:border-terracotta transition-all duration-300">
                        <svg class="w-4 h-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
                    </a>
                    <a href="#" class="w-10 h-10 rounded-full border border-graphite flex items-center justify-center text-gray-400 hover:text-terracotta hover:border-terracotta transition-all duration-300">
                        <svg class="w-4 h-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33z"></path><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon></svg>
                    </a>
                    <a href="#" class="w-10 h-10 rounded-full border border-graphite flex items-center justify-center text-gray-400 hover:text-terracotta hover:border-terracotta transition-all duration-300">
                        <svg class="w-4 h-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
                    </a>
                    <a href="#" class="w-10 h-10 rounded-full border border-graphite flex items-center justify-center text-gray-400 hover:text-terracotta hover:border-terracotta transition-all duration-300">
                        <svg class="w-4 h-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg>
                    </a>
                </div>'''

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace footer icons block completely
    # First we match the div block that has the footer icons
    content = re.sub(
        r'<div class="flex gap-4">\s*<a href="#" class="w-10 h-10 rounded-full border border-graphite flex items-center justify-center text-gray-400 hover:text-white hover:bg-terracotta hover:border-terracotta transition-all duration-300 group">[\s\S]*?</div>',
        new_footer_social,
        content
    )
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
