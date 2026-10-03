import glob

files = glob.glob('*.html')

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Add overflow-x-hidden to html tag
    if 'class="light"' in content:
        content = content.replace('class="light"', 'class="light overflow-x-hidden"')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print(f"Added overflow-x-hidden to HTML tag in {len(files)} files.")
