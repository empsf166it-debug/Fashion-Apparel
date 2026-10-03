import glob
import re

files = glob.glob('*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace the desktop CTA
    content = re.sub(
        r'<a href="resources\.html"[^>]*class="px-5 py-2\.5 bg-charcoal text-ivory[^>]*>Explore\s*Resources</a>',
        '<a href="contact.html" class="px-5 py-2.5 bg-charcoal text-ivory dark:bg-ivory dark:text-charcoal text-xs tracking-wider uppercase hover:bg-terracotta dark:hover:bg-terracotta transition-colors">Contact Us</a>',
        content,
        flags=re.IGNORECASE | re.DOTALL
    )

    # Replace the mobile CTA
    content = re.sub(
        r'<a href="resources\.html"[^>]*class="mt-2 px-5 py-2\.5 bg-terracotta text-white[^>]*>Explore\s*Resources</a>',
        '<a href="contact.html" class="mt-2 px-5 py-2.5 bg-terracotta text-white text-center text-sm font-medium uppercase tracking-widest">Contact Us</a>',
        content,
        flags=re.IGNORECASE | re.DOTALL
    )

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print(f"Replaced CTA in {len(files)} files.")
