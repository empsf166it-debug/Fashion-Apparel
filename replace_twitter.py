import glob
import re

files = glob.glob('*.html')

youtube_svg_w5 = '<svg class="w-5 h-5 text-charcoal dark:text-ivory group-hover:text-white" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33z"></path><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon></svg>'

youtube_svg_w4 = '<svg class="w-4 h-4 group-hover:text-white" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33z"></path><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon></svg>'

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace Twitter w-5 in contact.html
    twitter_w5_pattern = r'<svg class="w-5 h-5 text-charcoal dark:text-ivory group-hover:text-white" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 4s-\.7 2\.1-2 3\.4c1\.6 10-9\.4 17\.3-18 11\.6 2\.2\.1 4\.4-\.6 6-2C3 15\.5\.5 9\.6 3 5c2\.2 2\.6 5\.6 4\.1 9 4-\.9-4\.2 4-6\.6 7-3\.8 1\.1 0 3-1\.2 3-1\.2z"></path></svg>'
    content = re.sub(twitter_w5_pattern, youtube_svg_w5, content)

    # Replace Twitter w-4 in footer
    twitter_w4_pattern = r'<svg class="w-4 h-4 group-hover:text-white" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 4s-\.7 2\.1-2 3\.4c1\.6 10-9\.4 17\.3-18 11\.6 2\.2\.1 4\.4-\.6 6-2C3 15\.5\.5 9\.6 3 5c2\.2 2\.6 5\.6 4\.1 9 4-\.9-4\.2 4-6\.6 7-3\.8 1\.1 0 3-1\.2 3-1\.2z"></path></svg>'
    content = re.sub(twitter_w4_pattern, youtube_svg_w4, content)

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print(f"Replaced Twitter with YouTube in {len(files)} files.")
