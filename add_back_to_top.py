import glob
import re

files = glob.glob('*.html')

new_bottom_footer = '''        <div class="max-w-7xl mx-auto px-6 border-t border-graphite pt-8 flex flex-col md:flex-row justify-between items-center text-xs text-gray-500 uppercase tracking-wider relative">
            <p>&copy; 2026 Sartoria Knowledge Network.</p>
            <div class="flex items-center gap-6 mt-4 md:mt-0">
                <a href="#" class="hover:text-white transition-colors">Privacy Policy</a>
                <a href="#" class="hover:text-white transition-colors">Terms of Service</a>
                <button onclick="window.scrollTo({top: 0, behavior: 'smooth'})" class="ml-4 w-8 h-8 rounded-full bg-graphite flex items-center justify-center text-white hover:bg-terracotta transition-all duration-300" aria-label="Back to top">
                    <svg class="w-4 h-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5M5 12l7-7 7 7"/></svg>
                </button>
            </div>
        </div>'''

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We replace the bottom footer block
    # Note: original block starts with <div class="max-w-7xl mx-auto px-6 border-t border-graphite pt-8 flex flex-col md:flex-row justify-between items-center text-xs text-gray-500 uppercase tracking-wider">
    
    pattern = r'<div\s+class="max-w-7xl mx-auto px-6 border-t border-graphite pt-8 flex flex-col md:flex-row justify-between items-center text-xs text-gray-500 uppercase tracking-wider">\s*<p>&copy; 2026 Sartoria Knowledge Network\.</p>\s*<div class="flex gap-6 mt-4 md:mt-0">\s*<a href="#" class="hover:text-white transition-colors">Privacy Policy</a>\s*<a href="#" class="hover:text-white transition-colors">Terms of Service</a>\s*</div>\s*</div>'
    
    content = re.sub(pattern, new_bottom_footer, content)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print(f"Added back to top button in {len(files)} files.")
