import json

filepath = r"C:\Users\Ota\Documents\Portable Applications\(Python Scripts)\gel_blaster_compare\src\blasters_data.json"

with open(filepath, 'r', encoding='utf-8') as f:
    blasters = json.load(f)

for blaster in blasters:
    title = blaster.get('title', '').upper()
    notes = blaster.get('cross_referenced_specs', {}).get('notes', '')
    
    if "UDL P320" in title or "UDL SIG SAUER P320" in title:
        intel = ""
        if "SMC" in title:
             intel = "📌 **Designation**: 幽灵 / UDL P320 SMC 冲锋套件\n🔍 **Tieba Consensus**: Uses the P320 FCU (Fire Control Unit) dropped into a full tactical carbine chassis. Massively popular for CQB as it provides shoulder-stock stability while retaining lightweight handgun internals.\n⚠️ **Bilibili Tech Warning**: The folding stock hinge is plastic; do not drop it while deployed or the locking lug will shear off."
        elif "X5" in title:
             intel = "📌 **Designation**: 幽灵 / UDL P320 X5 Legion\n🔍 **Tieba Consensus**: The premium competition and target shooting variant. Features heavy tungsten-infused grips in the real-steel version, which UDL attempts to replicate with dense alloy plating.\n📸 **Xiaohongshu Vibe**: Loved by 3-Gun competitors and heavily featured in high-speed shooting drills on Douyin."
        elif "M18" in title:
             intel = "📌 **Designation**: 幽灵 / UDL P320 M18 (Compact)\n🔍 **Tieba Consensus**: The US Military compact carry choice. Bilibili reviewers note the shorter slide results in a marginally faster EBB cyclic rate compared to the full-size M17 due to reduced reciprocating mass.\n⚠️ **Bilibili Tech Warning**: Ensure the metal slide rails are heavily greased; dry cycling the metal slide version will immediately grind the nylon frame grooves."
        elif "M17" in title:
             intel = "📌 **Designation**: 幽灵 / UDL P320 M17 标准版\n🔍 **Tieba Consensus**: The flagship military standard sidearm that started UDL's dominance in the EBB market. Revolutionary for its magazine-housed battery system which deleted archaic external wiring."
             if "LITE" in title:
                 intel += "\n⚠️ **Bilibili Tech Warning**: The 'Lite' (简配版) versions utilize entirely nylon slides rather than metal. While they cycle faster, they completely lack the satisfying tactile clack of the premium metal batches."
        else:
             continue
             
        if intel:
             blaster['cross_referenced_specs']['notes'] = intel

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(blasters, f, indent=2)

print("UDL form factors patched successfully!")
