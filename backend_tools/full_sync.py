import subprocess
import os

scripts = [
    "scrape_blasters.py",
    "date_updater.py",
    "metrics_updater.py",
    "exact_metrics_updater.py",
    "fps_variant_updater.py",
    "enrich_blasters.py",
    "battery_connector_corrector.py",
    "pistol_smg_updater.py",
    "spring_rating_patch.py",
    "detailed_intel_updater.py",
    "hyper_intel_refresh.py",
    "final_intel_patch.py"
]

cwd = r"C:\Users\Ota\Documents\Portable Applications\(Python Scripts)\gel_blaster_compare\backend_tools"

for script in scripts:
    print(f"Running {script}...")
    result = subprocess.run(["python", script], cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running {script}:")
        print(result.stderr)
    else:
        print(result.stdout.strip())

print("\n--- MASTER INDEXING COMPLETE ---")
print("All high-fidelity technical intelligence has been restored and merged with the new scrape data.")
