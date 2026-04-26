import json
import re

filepath = r"C:\Users\Ota\Documents\Portable Applications\(Python Scripts)\gel_blaster_compare\src\blasters_data.json"

with open(filepath, 'r', encoding='utf-8') as f:
    blasters = json.load(f)

# We want a cleaner flow but still keep the warning trigger
prefixes = [
    r"🔍 \*\*Tieba Consensus\*\*:\s*",
    r"📸 \*\*Xiaohongshu Vibe\*\*:\s*",
    r"⚖️ \*\*Zhihu Context\*\*:\s*",
    r"📱 \*\*Douyin Hype\*\*:\s*",
    r"🛠️ SDG Forum \(.*?\):\s*",
    r"🛠️ SDG Forum:\s*",
    r"⚠️ \*\*Bilibili Tech Warning\*\*:\s*",
    r"🔍\s*",
    r"📸\s*",
    r"⚖️\s*",
    r"📱\s*",
    r"🛠️\s*",
    r"⚠️\s*"
]

for blaster in blasters:
    if 'cross_referenced_specs' in blaster and 'notes' in blaster['cross_referenced_specs']:
        notes = blaster['cross_referenced_specs']['notes']
        
        # Keep designation separate
        parts = notes.split('\n\n', 1)
        designation = parts[0]
        content = parts[1] if len(parts) > 1 else ""
        
        # Clean the content - BUT PRESERVE "TECH WARNING:"
        # Since combine_intel already converted Bilibili warnings to "TECH WARNING:"
        
        for p in prefixes:
            content = re.sub(p, "", content, flags=re.IGNORECASE)
        
        # Ensure only one space between combined sentences
        content = re.sub(r'\s+', ' ', content).strip()
        
        blaster['cross_referenced_specs']['notes'] = f"{designation}\n\n{content}"

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(blasters, f, indent=2)

print("Broad intelligence cleanup complete!")
