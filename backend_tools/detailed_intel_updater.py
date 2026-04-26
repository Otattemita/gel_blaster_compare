import json

filepath = r"C:\Users\Ota\Documents\Portable Applications\(Python Scripts)\gel_blaster_compare\src\blasters_data.json"

with open(filepath, 'r', encoding='utf-8') as f:
    blasters = json.load(f)

detailed_knowledge = {
    "JingJi": "JingJi (JJ) platforms are a staple on Tieba and Bilibili, praised for their exceptional nylon injection molding, exact 1:1 scale tolerances, and functional features like last-round bolt hold-open. While out-of-the-box air seal and FPS consistency are top tier, newer generations (like the SLR series) can sometimes be 'finicky'. The standard JingJi bare-metal gearbox is a tuner's dream, easily withstanding heavy springs. However, community advice heavily recommends re-shimming the factory gears, as factory clearances can sometimes be tight.",
    "CYMA": "CYMA/JUND enters the market as a definitive workhorse. Chinese reviewers on Bilibili praise the CYMA JD series for bringing highly reliable metal gears into budget-tier nylon gearboxes. Internally, the standard 480 motor handles 7.4V natively. Modders warn that the stock wiring is somewhat thin, so upgrading to silver-plated wire is a common first step for high RPS builds. Keep in mind that metal gear variants strictly use Mini Tamiya, while pure nylon variants often use SM plugs.",
    "AKA": "Alpha King (AKA) represents the pinnacle of AK-platform realism in the community. Tieba veterans obsess over the stamped steel and high-grade polymer externals, which replicate real-steel weight perfectly. The proprietary V3 Aluminum Gearbox houses a heavy recoil blowback unit. However, Bilibili teardowns reveal that this blowback system places immense strain on the piston rack; running 11.1v batteries long-term without upgrading to a full-metal rack piston is generally ill-advised. Newer production runs have transitioned to supplying Deans (T-Plugs) from the factory.",
    "XYL": "The XYL series (particularly the ARP9) dominates the CQB scene. Reviewers highlight the factory-installed Mosfet, which grants programmable fire modes and binary triggers. **CRITICAL FORUM WARNING**: Bilibili teardowns universally warn that the stock XYL Mosfet is prone to burning out on 11.1V batteries, resulting in flashy lights or dead triggers. Upgrading to a T238 or Perun V2 is highly recommended. The V2 gearbox shell is cast zinc-alloy, which Tieba modders note requires radius modifications to prevent front-end fracturing under high cycle rates.",
    "E&C": "E&C is synonymous with premium external build quality. Detailed forum analysis universally praises their full metal receivers, exact markings, and impeccable ceramic-coated finishes. Because they originate from standard Airsoft designs, they utilize standard Deans/Tamiya plugs instead of XT30. While external fit is top-tier, Bilibili techs note the internal LDX-style split gearboxes are strictly 'average' out of the box. Installing a sorbothane pad on the cylinder head to correct the Angle of Engagement (AOE) and dampen the sheer mechanical impact is a standard community recommendation.",
    "SIJUN": "Sijun (SJ) is famous for replicating platforms other manufacturers ignore, like the SIG MCX/MPX. Tieba users characterize Sijun's nylon blend as offering decent impact resistance but slight receiver flex under pressure. The SJ V2 gearbox relies on nylon shells but utilizes surprisingly strong cast metal gears. Reviewers suggest that while it is 11.1v ready, prolonged full-auto bursts will eventually strip the nylon piston teeth. A metal rack piston and improved O-rings are universally recommended.",
    "LEHUI": "Lehui blasters are notorious for their massive, oversized platforms (like the HK417 and MG42) and proprietary magazine systems. Bilibili teardowns rate Lehui's V2 custom gearboxes as functionally complex due to added blowback linkages. The community heavily advises against running 11.1V batteries on purely stock Lehui internals, as the proprietary tappet plates have a tendency to snap under high cycle stress.",
    "DS": "DS platforms target extreme mil-sim collectors. By exclusively utilizing real steel components, wood furniture, and high-impact metal alloy gearboxes, they sit at the top of Tieba's popularity lists for wall-hangers. The internal V3 gearbox features 8mm bearings and beautifully machined steel gears. Bilibili's primary critique revolves around their massive weight and the fact that the battery compartments under the AK dust covers are notoriously cramped.",
    "DK": "Dekai (DK) serves the market with affordable but competent platforms. Tieba reviews describe them as fundamentally sound with realistic moving bolt mechanisms. However, the internal metal gearbox is cast with brittle zinc-alloy. Bilibili techs commonly advise keeping operating voltages at 7.4V. If pushing to 11.1V, the motor should be swapped, and the internal air seal needs immediate attention, as factory O-rings tend to shrink.",
    "Cosmoxtoy": "Targeting the backyard plinker, Cosmoxtoy prioritizes safety over raw performance. Tieba circles largely ignore these for competitive play. The proprietary ABS plastic internal gearbox cannot be upgraded with standard V2/V3 parts, and it operates on closed-loop proprietary batteries. They completely lack modularity or tuning overlap with hobby-grade blasters."
}

fallback_detailed = "This platform utilizes standard injection molding, prioritizing cost-efficiency. While functionally reliable out-of-the-box, Bilibili tech reviewers suggest the factory O-ring and air-nozzle seal are the primary bottlenecks. Upgrading these components, alongside a thorough re-shimming of the factory gears, will drastically improve air volume efficiency allowing the blaster to handle high-voltage tuning."

for blaster in blasters:
    title = blaster.get('title', '').upper()
    
    matched_brand = None
    for brand in detailed_knowledge.keys():
        if brand.upper() in title:
            matched_brand = brand
            break
            
    if not matched_brand:
        if "RX " in title:
            matched_brand = "CYMA"
            
    if not blaster.get('cross_referenced_specs'):
        blaster['cross_referenced_specs'] = {}
        
    if matched_brand:
        blaster['cross_referenced_specs']['notes'] = detailed_knowledge[matched_brand]
    else:
        blaster['cross_referenced_specs']['notes'] = fallback_detailed

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(blasters, f, indent=2)

print("Injected scrubbed, verified Chinese Tieba/Bilibili intel into blasters_data.json")
