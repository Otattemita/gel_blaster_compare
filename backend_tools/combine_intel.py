import json
import re

filepath = r"C:\Users\Ota\Documents\Portable Applications\(Python Scripts)\gel_blaster_compare\src\blasters_data.json"

with open(filepath, 'r', encoding='utf-8') as f:
    blasters = json.load(f)

for blaster in blasters:
    if 'cross_referenced_specs' in blaster and 'notes' in blaster['cross_referenced_specs']:
        notes = blaster['cross_referenced_specs']['notes']
        lines = notes.split('\n')
        
        designation = ""
        combined_text = []
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            if line.startswith("📌 **Designation**:"):
                designation = line
            else:
                # Remove the emoji and bold tags prefix
                # Example: "🔍 **Tieba Consensus**: Text..."
                match = re.search(r'^.*? \*\*.*?\*\*: (.*)', line)
                if match:
                    content = match.group(1)
                    if "Bilibili Tech Warning" in line:
                        combined_text.append(f"TECH WARNING: {content}")
                    else:
                        combined_text.append(content)
                else:
                    combined_text.append(line)
        
        final_notes = designation + "\n\n" + " ".join(combined_text)
        blaster['cross_referenced_specs']['notes'] = final_notes

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(blasters, f, indent=2)

print("Combined intelligence successfully!")
