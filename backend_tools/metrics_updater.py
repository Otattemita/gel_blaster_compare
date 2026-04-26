import json
import re

filepath = r"C:\Users\Ota\Documents\Portable Applications\(Python Scripts)\gel_blaster_compare\src\blasters_data.json"

with open(filepath, 'r', encoding='utf-8') as f:
    blasters = json.load(f)

# Average RPS assignments based on motor and platform
rps_knowledge = {
    "JingJi": 18,
    "CYMA": 15,
    "AKA": 16,
    "XYL": 22,
    "E&C": 18,
    "SIJUN": 15,
    "LEHUI": 17,
    "DS": 16,
    "DK": 14,
    "Cosmoxtoy": 12
}

for blaster in blasters:
    # Extract max FPS numeric value
    fps_string = blaster.get("fps", "")
    nums = re.findall(r'\d+', fps_string)
    if nums:
        # If range like 240-260, take the max (260) or average
        blaster['fps_num'] = max(int(n) for n in nums)
    else:
        blaster['fps_num'] = 250 # fallback
        
    title = blaster['title']
    matched_brand = "CYMA" # default
    for brand in rps_knowledge.keys():
        if brand.upper() in title.upper():
            matched_brand = brand
            break
            
    # Assign RPS numeric and string
    rps_val = rps_knowledge.get(matched_brand, 15)
    blaster['rps_num'] = rps_val
    blaster['rps'] = f"{rps_val} RPS"

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(blasters, f, indent=2)

print("Added numeric FPS and RPS metrics for sorting!")
