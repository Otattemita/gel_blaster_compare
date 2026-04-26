import json
import re
from datetime import datetime

filepath = r"C:\Users\Ota\Documents\Portable Applications\(Python Scripts)\gel_blaster_compare\src\blasters_data.json"

with open(filepath, 'r', encoding='utf-8') as f:
    blasters = json.load(f)

# Approximate base years if no date is found in the title
known_release_dates = {
    "JINGJI SLR B56": "2023-01",
    "JINGJI SR16": "2024-01",
    "DK SCAR-H": "2023-08",
    "SIJUN SIG MCX": "2025-01",
    "E&C M16": "2023-11",
    "COSMOXTOY SIRIUS": "2024-02",
    "E&C STRIKE INDUSTRIES": "2024-05",
    "DS AKS": "2023-04",
    "DS AKM": "2023-04",
    "CYMA SCAR-L": "2024-06",
    "LEHUI HK417": "2022-09",
    "AKA ALPHA KING AK12": "2021-11",
    "AKA ALPHA KING PPK20": "2022-07",
    "RX AK STORM": "2022-05",
    "JINGJI PDX": "2022-11",
    "XYL GC16": "2025-09"
}

months_map = {
    "JAN": "01", "JANUARY": "01",
    "FEB": "02", "FEBRUARY": "02",
    "MAR": "03", "MARCH": "03",
    "APR": "04", "APRIL": "04",
    "MAY": "05",
    "JUN": "06", "JUNE": "06",
    "JUL": "07", "JULY": "07",
    "AUG": "08", "AUGUST": "08",
    "SEP": "09", "SEPTEMBER": "09",
    "OCT": "10", "OCTOBER": "10",
    "NOV": "11", "NOVEMBER": "11",
    "DEC": "12", "DECEMBER": "12",
}

for blaster in blasters:
    title = blaster.get('title', '').upper()
    
    found_year = None
    found_month = "01" # Default to January if only year found
    
    # 1. Regex to extract explicit dates from title (e.g. "Mar 2026", "December 2025", "2024", "Jan 2024")
    year_match = re.search(r'(20\d{2})', title)
    if year_match:
        found_year = year_match.group(1)
        
    for month_str, month_num in months_map.items():
        if re.search(r'\b' + month_str + r'\b', title):
            found_month = month_num
            break
            
    final_date_str = None
    
    if found_year:
        final_date_str = f"{found_year}-{found_month}"
    else:
        # 2. Match against knowledge base
        for model, date_val in known_release_dates.items():
            if model.upper() in title:
                final_date_str = date_val
                break
                
    # 3. Last fallback
    if not final_date_str:
        final_date_str = "2023-06" # Average default
        
    blaster['release_date'] = final_date_str
    
    # Create timestamp for sorting
    try:
        dt = datetime.strptime(final_date_str, "%Y-%m")
        blaster['release_timestamp'] = int(dt.timestamp())
    except:
        blaster['release_timestamp'] = 0

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(blasters, f, indent=2)

print("Injected release dates and timestamps into blasters_data.json")
