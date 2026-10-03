import re
import glob
import os

ids = [
    "1483985988355-763728e1935b", "1515886657613-9f3515b0c78f", "1445205170230-053b83016050", 
    "1528360983277-13d401cdc186", "1485230895920-c4387cc6df0f", "1487222411035-a5d4090b82b0", 
    "1462392246754-28c71e294156", "1492707892479-7bc8d5a4ee93", "1496747611176-843222e1e57c", 
    "1509631179647-0b704c600122", "1512436991641-6745cdb1723f", "1515347619152-446415ce6242", 
    "1516762689619-0f2c0cb3543d", "1529139574466-a30ac222237e", "1532453288672-3a27e9be2030", 
    "1539109136881-3be0616acf4b", "1550614000-4b95f1917f8a", "1551232864319-158a18fa8f81", 
    "1552374196-1ab2a1c593e8", "1558769132-cb1aea458c5e", "1579783902614-a3fb3927b6a5", 
    "1581044777550-4cfa60707c03", "1583091157849-43615e44cb89", "1598532163257-ae3c6b2524b6", 
    "1586026214152-6a4a4b41315b", "1620799140408-edc6dcb6d633", "1520006403909-838d6b92c22e", 
    "1494790108377-be9c29b29330", "1599566150163-29194dcaad36", "1490481651871-ab68de25d43d"
]

files = glob.glob('*.html')
id_idx = 0

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    def replacer(match):
        global id_idx
        w = match.group(2)
        unsplash_url = f"https://images.unsplash.com/photo-{ids[id_idx % len(ids)]}?auto=format&fit=crop&q=80&w={w}"
        id_idx += 1
        return unsplash_url

    # Match pollinations.ai URLs
    # format: https://image.pollinations.ai/prompt/xyz?width=W&height=H&nologo=true&seed=S
    new_content = re.sub(r'https://image\.pollinations\.ai/prompt/[a-zA-Z_]+\?width=([0-9]+)&height=[0-9]+&nologo=true&seed=[0-9]+', replacer, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
print("Replaced images in", len(files), "files")
