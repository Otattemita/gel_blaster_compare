import urllib.request
import json
import re
from bs4 import BeautifulSoup
import os

import urllib.request
import json
import re
from bs4 import BeautifulSoup
import os

collections = [
    {"url": "https://akgelblaster.com/collections/full-metal-gel-blaster/products.json", "category": "Rifle"},
    {"url": "https://akgelblaster.com/collections/pistols-and-smg-gel-blaster/products.json", "category": "Pistol"},
    {"url": "https://akgelblaster.com/collections/smg/products.json", "category": "SMG"},
    {"url": "https://akgelblaster.com/collections/gel-blasters/products.json", "category": "Rifle"} # General catch-all
]

products = []
seen_ids = set()

for coll in collections:
    page = 1
    while True:
        url = f"{coll['url']}?limit=250&page={page}"
        try:
            response = urllib.request.urlopen(url)
            data = json.loads(response.read())
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            break
            
        if not data.get('products'):
            break
            
        for p in data['products']:
            if p['id'] in seen_ids:
                continue
                
            in_stock = any(v['available'] for v in p['variants'])
            
            title = p['title']
            handle = p['handle']
            
            # Determine category based on title overrides
            category = coll["category"]
            if "PISTOL" in title.upper() or "GLOCK" in title.upper() or "HI-CAPA" in title.upper() or "1911" in title.upper() or "GBB" in title.upper():
                category = "Pistol"
            elif "SMG" in title.upper() or "MP5" in title.upper() or "ARP9" in title.upper() or "VECTOR" in title.upper() or "UZI" in title.upper() or "MP7" in title.upper() or "P90" in title.upper() or "10" in title.upper() and ("MAC" in title.upper() or "M10" in title.upper()):
                category = "SMG"
                
            html = p.get('body_html', '')
            soup = BeautifulSoup(html, 'html.parser')
            text = soup.get_text(separator=' ')
            
            price = min([float(v['price']) for v in p['variants']])
            
            fps_match = re.search(r'(\d+)\s*(?:-|to)?\s*(\d+)?\s*fps', text, re.IGNORECASE)
            fps = fps_match.group(0) if fps_match else "Unknown"
            
            gears_match = re.search(r'([A-Za-z0-9\-]+)\s*gearbox', text, re.IGNORECASE)
            gearbox = gears_match.group(0) if gears_match else "Standard Gearbox"
            
            img = p['images'][0]['src'] if p.get('images') else ''
                
            products.append({
                'id': p['id'],
                'title': title,
                'url': f"https://akgelblaster.com/products/{handle}",
                'price': price,
                'image': img,
                'fps': fps,
                'gearbox': gearbox,
                'category': category,
                'in_stock': in_stock,
                'specs': text[:200] + "..."
            })
            seen_ids.add(p['id'])
            
        page += 1

print(f"Total parsed across all categories: {len(products)}")

dest_path = r"C:\Users\Ota\Documents\Portable Applications\(Python Scripts)\gel_blaster_compare\src\blasters_data.json"
with open(dest_path, 'w', encoding='utf-8') as f:
    json.dump(products, f, indent=2)

print(f"Saved to {dest_path}")


