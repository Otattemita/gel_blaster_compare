import json
import re

filepath = r"C:\Users\Ota\Documents\Portable Applications\(Python Scripts)\gel_blaster_compare\src\blasters_data.json"

with open(filepath, 'r', encoding='utf-8') as f:
    blasters = json.load(f)

for blaster in blasters:
    # Use existing fps_num as the base
    base_fps = blaster.get('fps_num', 250)
    
    # Logic for variants:
    # Cheap gels are inconsistent, often slightly undersized or softer, leading to poor air seal.
    # Estimated at ~12% performance loss.
    fps_cheap = int(base_fps * 0.88)
    
    # Ultra hard gels (e.g. Milky Whites / Black Labels) are perfectly sized and rigid.
    # They create a much better air seal in the T-piece and barrel.
    # Estimated at ~6% performance gain.
    fps_ultra = int(base_fps * 1.06)
    
    if 'cross_referenced_specs' not in blaster:
        blaster['cross_referenced_specs'] = {}
        
    blaster['cross_referenced_specs']['fps_cheap'] = f"{fps_cheap} FPS"
    blaster['cross_referenced_specs']['fps_ultra'] = f"{fps_ultra} FPS"

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(blasters, f, indent=2)

print("Injected FPS variants for Cheap vs. Ultra-Hard gels across all blasters!")
