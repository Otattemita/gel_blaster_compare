import json

filepath = r"C:\Users\Ota\Documents\Portable Applications\(Python Scripts)\gel_blaster_compare\src\blasters_data.json"

with open(filepath, 'r', encoding='utf-8') as f:
    blasters = json.load(f)

for blaster in blasters:
    # Ensure fps_num exists
    if 'fps_num' not in blaster:
        blaster['fps_num'] = int(''.join(filter(str.isdigit, str(blaster.get('fps', '250')))) or 250)
    
    # Let's derive 7.4v and 11.1v RPS numbers based on the previously assigned rps_num
    base_rps = blaster.get('rps_num', 15)
    
    title = blaster.get('title', '').upper()
    specs = json.dumps(blaster).upper()
    
    # Determine if the base_rps was meant as an 11.1v stat or 7.4v stat originally
    if "11.1" in specs or "MOSFET" in specs or any(k in title for k in ["E&C", "XYL", "JINGJI", "DS"]):
        # It was an 11.1v RPS natively. Calculate 7.4v downside.
        blaster['rps_11v'] = base_rps
        blaster['rps_7v'] = max(int(base_rps / 1.4), 10)
    else:
        # It was a 7.4v RPS natively. Calculate 11.1v upside.
        blaster['rps_7v'] = base_rps
        blaster['rps_11v'] = min(int(base_rps * 1.4), 25)
        
    blaster['rps'] = f"7.4v: {blaster['rps_7v']} | 11.1v: {blaster['rps_11v']}"

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(blasters, f, indent=2)

print("Battery profiles appended successfully.")
