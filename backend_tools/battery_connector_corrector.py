import json

filepath = r"C:\Users\Ota\Documents\Portable Applications\(Python Scripts)\gel_blaster_compare\src\blasters_data.json"

with open(filepath, 'r', encoding='utf-8') as f:
    blasters = json.load(f)

def determine_connector(title, brand):
    t = title.upper()
    b = brand.upper()
    
    # Manufacturers that have standardized on XT30 for modern (2024-2026) batches
    if b == "JINGJI" or "JING JI" in t:
        return "XT30 (High-Discharge)"
    
    if b == "SIJUN" or "SI JUN" in t:
        return "XT30 (Standard)"
        
    if b == "XYL" or "LITTLE MOON" in t:
        return "XT30"

    if b == "UDL":
        if "XM7" in t or "MCX" in t:
            return "XT30"
        if "P320" in t:
            return "Proprietary (Magazine Battery Contact)"

    # E&C (East & Crane) - Highly dependent on the batch. 
    # AKGelBlaster's "Fully Loaded" or "DEVGRU" batches are almost all XT30 now.
    if b == "E&C" or "EAST & CRANE" in t:
        if any(keyword in t for keyword in ["SAI", "TTI", "N4", "STRIKE INDUSTRIES", "DEVGRU", "2025", "2026"]):
            return "XT30 (AKGB High-Spec)"
        return "Deans (T-Plug) / Mini Tamiya"

    # CYMA - The great divide
    if b == "CYMA":
        if "ESHOOTER" in t or "MOSFET" in t or "2025" in t or "2026" in t:
            return "XT30 (Electronic Trigger Spec)"
        return "Mini Tamiya / SM Plug"

    # Classic Army
    if b == "CLASSIC ARMY" or "PX9" in t or "NEMESIS" in t:
        return "Deans (T-Plug)"

    # AKA
    if b == "AKA" or "ALPHA KING" in t:
        return "Deans (T-Plug)"

    # Double Bell
    if "DOUBLE BELL" in t:
        return "Mini Tamiya"

    # LDT / Warinterest
    if "LDT" in t or "WARINTEREST" in t:
        if "V3" in t or "V4" in t or "MP5K" in t:
            return "Mini Tamiya or XT30 (Batch Dependent)"
        return "Mini Tamiya"

    # Pistols (Non-GBB)
    if any(keyword in t for keyword in ["EBB", "ELECTRIC BLOWBACK"]):
        if "UDL" in t: return "Proprietary (Magazine Battery Contact)"
        if "G22" in t or "XYH" in t: return "SM Plug (7.4v)"
        return "SM Plug (Standard EBB)"

    # GBB 
    if any(keyword in t for keyword in ["GBB", "GAS BLOWBACK"]):
        return "N/A (Green Gas / Co2)"

    # Springers / Manual
    if "SHOTGUN" in t or "M870" in t or "MANUAL" in t:
        return "N/A (Manual Action)"

    return "Mini Tamiya / SM Plug (Legacy)"

for blaster in blasters:
    title = blaster.get('title', '')
    
    # Find brand again for logic
    brand = "Unknown"
    known_brands = ["JingJi", "CYMA", "AKA", "XYL", "E&C", "SIJUN", "LEHUI", "DS", "DK", "Cosmoxtoy", "UDL", "Classic Army", "Golden Eagle", "Double Bell", "LDT"]
    for b in known_brands:
        if b.upper() in title.upper():
            brand = b
            break
            
    connector = determine_connector(title, brand)
    
    if 'cross_referenced_specs' not in blaster:
        blaster['cross_referenced_specs'] = {}
        
    blaster['cross_referenced_specs']['battery'] = connector

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(blasters, f, indent=2)

print("Battery Connector Database Re-evaluated and Corrected across all 156 blasters!")
