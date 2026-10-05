import os
import glob
import re

files = glob.glob('*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    modified = False
    
    # We want to replace <div class="flex justify-center flex-wrap gap-4"> 
    # with <div class="flex flex-col sm:flex-row justify-center gap-4">
    if 'class="flex justify-center flex-wrap gap-4"' in content:
        content = content.replace('class="flex justify-center flex-wrap gap-4"', 'class="flex flex-col sm:flex-row justify-center gap-4"')
        modified = True
        
    # And we want to ensure the a tags inside these have: w-full sm:w-auto min-w-[240px] text-center
    # We can just look for the typical CTA classes and inject our new classes if they aren't there
    
    primary_cta = 'class="px-8 py-4 bg-terracotta text-white hover:bg-ivory hover:text-charcoal transition-colors uppercase tracking-wider text-sm font-medium"'
    new_primary_cta = 'class="w-full sm:w-auto min-w-[240px] text-center px-8 py-4 bg-terracotta text-white hover:bg-ivory hover:text-charcoal transition-colors uppercase tracking-wider text-sm font-medium"'
    
    if primary_cta in content:
        content = content.replace(primary_cta, new_primary_cta)
        modified = True

    secondary_cta = 'class="px-8 py-4 border border-ivory text-ivory hover:bg-ivory hover:text-charcoal transition-colors uppercase tracking-wider text-sm font-medium"'
    new_secondary_cta = 'class="w-full sm:w-auto min-w-[240px] text-center px-8 py-4 border border-ivory text-ivory hover:bg-ivory hover:text-charcoal transition-colors uppercase tracking-wider text-sm font-medium"'
    
    if secondary_cta in content:
        content = content.replace(secondary_cta, new_secondary_cta)
        modified = True
        
    # Also in community.html it's sometimes split across lines, let's use regex for safety
    # Wait, the string replace might miss it if there are newlines.
    
    if modified:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f'Updated exact matches in {f}')
