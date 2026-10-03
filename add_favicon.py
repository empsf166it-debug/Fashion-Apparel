import glob
import re

files = glob.glob('*.html')

favicon_tag = '''    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23059669' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><circle cx='6' cy='6' r='3'></circle><circle cx='6' cy='18' r='3'></circle><line x1='20' y1='4' x2='8.12' y2='15.88'></line><line x1='14.47' y1='14.48' x2='20' y2='20'></line><line x1='8.12' y1='8.12' x2='12' y2='12'></line></svg>">
'''

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Check if a favicon already exists and remove it if it's there
    content = re.sub(r'<link\s+rel="icon"[^>]*>\n?', '', content)
    content = re.sub(r'<link\s+rel="shortcut icon"[^>]*>\n?', '', content)

    # Insert before </head>
    content = content.replace('</head>', f'{favicon_tag}</head>')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print(f"Added favicon to {len(files)} files.")
