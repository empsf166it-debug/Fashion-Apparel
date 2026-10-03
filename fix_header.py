import glob

files = glob.glob('*.html')

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Change sticky header to fixed
    content = content.replace('header class="sticky top-0', 'header class="fixed top-0 w-full')
    
    # Add pt-20 to body to offset the fixed header
    if 'body class="' in content:
        content = content.replace('body class="', 'body class="pt-20 ')
        
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print(f"Fixed header to fixed top-0 with pt-20 body in {len(files)} files.")
