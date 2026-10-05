import os
import glob
files = glob.glob('*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Update social media icons in footer and contact page
    # Look for the transition-all duration-300
    
    # footer icons are text-gray-400
    old_classes_footer = "text-gray-400 hover:text-terracotta hover:border-terracotta transition-all duration-300"
    new_classes_footer = "text-gray-400 hover:bg-terracotta hover:text-white hover:border-terracotta hover:-translate-y-1 transition-all duration-300"
    
    # contact page icons are text-charcoal dark:text-ivory hover:text-terracotta
    old_classes_contact = "transition-all duration-300 hover:border-terracotta text-charcoal dark:text-ivory hover:text-terracotta"
    new_classes_contact = "transition-all duration-300 hover:bg-terracotta hover:border-terracotta hover:text-white dark:hover:text-white hover:-translate-y-1 text-charcoal dark:text-ivory"
    
    if old_classes_footer in content or old_classes_contact in content:
        content = content.replace(old_classes_footer, new_classes_footer)
        content = content.replace(old_classes_contact, new_classes_contact)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f'Updated {f}')
