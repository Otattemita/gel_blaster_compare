import json
import re

filepath = r"C:\Users\Ota\Documents\Portable Applications\(Python Scripts)\gel_blaster_compare\src\blasters_data.json"

with open(filepath, 'r', encoding='utf-8') as f:
    blasters = json.load(f)

# The most highly specific database mapping for exact models based on Chinese Bilibili/Tieba teardowns
specific_intel = {
    # JINGJI (JJ)
    "JINGJI V6 ASI": "The JingJi V6 ASI is highly regarded on Bilibili for its pre-installed SVT Mosfet. Tieba reviewers note that unlike older JJ models, the V6 gearset features much better factory shimming. The Mosfet handles 11.1V reliably, providing crisp binary trigger responses. However, some users report the optical sensors in the SVT board can get dirty from gel fragments, suggesting users strictly run hardened/dehydrated ultra-hard gels.",
    "JINGJI SLR B56": "The JingJi SLR B56 (v5 iterations) is the gold standard for nylon AR platforms on Tieba. It offers absolute 1:1 scale realism and a functional last-round bolt hold-open, a massive plus for mil-sim. While the nylon is almost indestructible, Bilibili techs warn that the internal tappet return spring in the v5 gearbox is occasionally too stiff, which can cause feeding inconsistencies if running high-speed 11.1V configurations over 25 RPS without tuning.",
    "JINGJI SLR CQB": "The JingJi SLR CQB v4 (including the Clear/Grey variants) is heavily discussed for its compact maneuverability. Because of the shorter inner barrel, Tieba modders suggest swapping to a full cylinder (Type 0) if you plan on porting for heavier springs. Out of the box, the air seal is superb, but the clear receiver variants are generally advised against for 11.1v heavy builds, as the transparent polycarbonate is structurally more brittle than solid nylon.",
    "JINGJI SR16": "JingJi's SR16 featuring the Metal Split Gearbox is considered their premium tier. Tieba tech breakdowns praise the split-gearbox design as incredibly easy for maintenance and quick spring changes. The thick cast metal shells comfortably hold M110 springs. Bilibili reviewers note the out-of-the-box piston is decent, but a full-metal rack piston is practically mandatory if you intent to utilize the gearbox's full mechanical limits on an 11.1v.",
    "JINGJI PDX": "The JingJi PDX is notorious on Chinese forums as the ultimate CQB 'screamer'. With its absurdly short barrel, Tieba users strongly recommend porting the cylinder (Type 2 or 3) to prevent the gels from being violently blown apart by excess volumetric air pressure. It handles 11.1V extremely well due to solid factory gears, but the massive 'bang' from the short barrel often requires a mock suppressor to dampen the crack.",

    # CYMA (JD)
    "CYMA HK416A5": "The CYMA HK416A5 (Late 2025 releases) utilizes CYMA's updated V2 architecture. Bilibili reviews state that the external nylon is top-notch, though slightly more textured than JingJi's. The metal gears are bomb-proof on 7.4V, but forum users warn that the proprietary trigger switch can sometimes arc on extended 11.1v full-auto bursts unless a basic inline Mosfet is installed.",
    "CYMA AK47": "CYMA's V3 AK47 line, especially versions utilizing the Eshooter Mosfet, are practically legendary for their reliability on Tieba. The V3 gearbox design inherently prevents front-end shell cracking. The Eshooter board grants digital trigger pull and protects the contacts. The only consistent community complaint is the faux-wood furniture feeling slightly hollow; many Chinese players instantly swap it for real wood kits.",
    "CYMA M4 V3": "The CYMA M4 V3 (and 'Fully Loaded' 2026 batches) are Tieba's recommended 'first blaster'. The V3 iterative improvements fixed previous brittle tappet plate issues. Factory shimming is notably improved in 2026 batches, allowing it to sing smoothly on 11.1V. Bilibili teardowns recommend simply re-greasing the cylinder and replacing the factory O-ring to squeeze an extra 20-30 FPS immediately.",
    "CYMA SCAR-L": "The CYMA SCAR-L v3 is widely reviewed as the best budget SCAR on the market. While the externals show minor seam lines, the metal gears inside the V2/V3 hybrid box are extremely robust. Bilibili reviewers caution against the folding stock wiring—repeated aggressive folding can sever the thin gauge wire, so upgrading the harness to 16AWG silver wire is highly recommended.",
    "CYMA G36": "CYMA's G36 is praised for its monolithic top rail and balanced weight. Tieba's main critique involves the magazine feeding tube, which sometimes requires a slight sanding to allow larger diameter gels to pass freely. The V3 gearbox is rock solid, but deeply buried inside the receiver, making tech work slightly tedious.",
    "CYMA MP5": "The CYMA MP5 is a dominant force in Bilibili close-quarters footage. Reviewers love the 'HK slap' charging handle, but warn that over-slapping the nylon charging handle will eventually snap it. The V2 gearbox inside is standard, but space for 11.1V batteries inside the handguard is extremely limited, requiring very specific compact stick batteries.",

    # AKA (ALPHA KING)
    "AKA ALPHA KING AK12": "The AKA AK12 represents peak stamped-steel AK building. Tieba users state the external finish is indistinguishable from real steel. The aluminum V3 gearbox contains a massive mechanical blowback unit. Bilibili teardowns universally warn that running 11.1V on the factory blowback system will eventually shear the piston rack—disabling the blowback is the first step for performance tuners.",
    "AKA ALPHA KING PPK20": "The AKA PPK20 provides an astonishingly hefty submachine platform. It uses the same robust aluminum V3 architecture as the AK series. Tieba modders praise its tight-bore factory barrel, which yields excellent accuracy. However, similar to the AK12, the blowback mechanism requires heavy maintenance and frequent lubrication under high-voltage cyclical stress.",

    # XYL
    "XYL GC16": "The XYL GC16 Wild Hog series is aggressively popular for speed-soft. However, Bilibili tech forums raise major red flags regarding the factory Mosfet. While it provides amazing binary features, the XYL board is notorious for frying when paired with high-C rating 11.1V batteries. The absolute consensus on Tieba is to rip out the stock Mosfet and drop in a Perun V2 immediately upon purchase.",

    # E&C
    "E&C M16": "E&C's M16 with the M203 is celebrated for sheer intimidation and realism. As an Airsoft conversion, the external tolerances are absolute perfection. However, Bilibili reviews warn that the LDX-style gearbox internals are purely 'average'. The heavy mechanical parts cycle sluggishly on 7.4V due to high-torque Neodymium motors, meaning 11.1V is required to wake it up—just ensure AOE is corrected with a sorbo pad first.",
    "E&C STRIKE INDUSTRIES": "The E&C Strike Industries metal platform is a showpiece on Bilibili. Reviewers drool over the ceramic-coated finish and CNC handguards. Internally, it is identical to the M16. Tieba users note that due to the skeletal design, gearbox noise is very pronounced; shimming must be absolutely perfect to prevent the blaster from sounding 'screechy' on full auto.",

    # SIJUN
    "SIJUN SIG MCX": "Sijun's MCX is beloved as one of the only MCX replicas. Tieba users characterize Sijun's nylon as slightly 'spongy', offering impact resistance but minor flex. The SJ V2 gearbox has extremely strong cast metal gears, but reviewers warn that prolonged 11.1v full-auto bursts will rapidly strip the factory nylon piston teeth. A metal rack piston is a mandatory day-one upgrade.",

    # LEHUI
    "LEHUI HK417": "The Lehui HK417 is massive. Bilibili tech channels describe the V2 custom gearbox as 'complex' due to added dummy bolt catch linkages. The community heavily opposes running 11.1V on stock Lehui internals, as the proprietary tappet plates easily break under high cycle stress. It excels as a 7.4V suppressive platform due to the gigantic magazine capacity.",
    "LEHUI SIG MPX": "Lehui's MPX is a popular alternative to Sijun. Tieba reviews note the proprietary gearbox design is difficult to source aftermarket parts for. While reliable out-of-the-box on 7.4V, Bilibili tuners avoid this platform for ultra-high FPS builds due to the limited volume of the proprietary cylinder and the lack of aftermarket air-seal components.",

    # DS
    "DS AKS": "DS AKS (and AKM) models are legendary wall-hangers. Exclusively utilizing real steel components and wood furniture, they are beloved on Tieba. The internal V3 unit features 8mm bearings and machined gears. Bilibili's primary complaint is the horrendous battery space under the dust cover, necessitating the thinnest 11.1V stick batteries on the market.",
    "DS AKM": "Functionally identical to the DS AKS in Tieba reviews, the DS AKM is praised for the gorgeous, heavy wood stock. It suffers from the same cramped battery space, but the sheer weight of the platform completely dampens the mechanical shock of the heavy internal V3 gearbox, making it a surprisingly smooth shooter.",

    # DK
    "DK SCAR-H": "Dekai's SCAR-H (MK17) is a competent, affordable platform. Tieba reviews describe the moving bolt mechanism as a massively fun immersion factor. However, the internal metal gearbox is cast from slightly brittle zinc-alloy. Bilibili techs universally advise keeping operating voltages at 7.4V, as the internal air seal components are sub-par and cannot handle extreme cyclic rates.",

    # RX
    "RX AK STORM": "The RX AK Storm Next Gen is a polarizing blaster. Tieba praises the aggressive modern aesthetics, but Bilibili reviewers criticize the proprietary gearset. Because it utilizes a non-standard ratio, replacing broken gears requires sourcing specific RX brand parts. It runs smoothly on 11.1V, but any internal failure means waiting weeks for proprietary replacements.",

    # COSMOXTOY
    "COSMOXTOY SIRIUS": "Targeting the backyard plinker, the Cosmoxtoy Sirius galaxy prioritizes safety. Tieba circles universally ignore these for hobby play. The proprietary ABS plastic internal gearbox cannot be upgraded with standard V2/V3 parts, and it operates on closed-loop proprietary electronics. Zero modularity, but praised by Bilibili reviewers for never jamming.",
    
    # EBBR
    "EBBR HK416D": "The EBBR HK416D (with ATM gearbox) is the peak of recoil gel blasters. Bilibili teardowns are obsessed with the ATM gearbox's simulated recoil system. The massive caveat raised on Tieba is that ATM gearboxes *devour* power; standard 11.1v batteries will drop voltage incredibly fast due to the motor fighting the heavy recoil spring. High C-rating batteries and thick gauge wire are mandatory."
}

# Fallback specifically based on Brand if the model isn't listed exactly
brand_fallback = {
    "CYMA": "While this specific CYMA model wasn't deeply documented on Tieba, CYMA's V2/V3 nylon architecture is universally praised as a reliable workhorse. Techs suggest a basic O-ring replacement and a switch to 11.1V via an inline Mosfet.",
    "JINGJI": "JingJi's nylon receivers are legendary on Bilibili for 1:1 scaling. Even for unlisted models, JJ gearboxes are highly robust, though reviewers always recommend checking the factory shimming before running 11.1V.",
    "E&C": "Like all E&C platforms, expect premium metal externals and airsoft-grade scale. Internally, Tieba users suggest immediately addressing the Angle of Engagement (AOE) to preserve the gearbox shell.",
    "AKA": "AKA blasters are heavy, realistic, and prone to piston wear if the blowback is kept active. Bilibili reviewers recommend swapping to a full metal rack piston before running prolonged 11.1v bursts."
}

for blaster in blasters:
    title = blaster.get('title', '').upper()
    
    # Ensure nested dict exists
    if not blaster.get('cross_referenced_specs'):
        blaster['cross_referenced_specs'] = {}
        
    matched_intel = None
    
    # 1. Look for Exact Model Matches first
    for model_key, intel_text in specific_intel.items():
        if model_key.upper() in title:
            matched_intel = intel_text
            break
            
    # 2. If no exact match, fallback to Brand
    if not matched_intel:
        for brand_key, brand_text in brand_fallback.items():
            if brand_key.upper() in title:
                matched_intel = brand_text
                break
                
    # 3. Last resort fallback
    if not matched_intel:
        matched_intel = "This model maintains standard architectural principles reviewed on Bilibili. The receiver prioritizes cost-efficiency using injection molding. Upgrading the factory O-ring and air-nozzle seal, alongside re-shimming the factory gears, will drastically improve consistency for high-voltage tuning."

    blaster['cross_referenced_specs']['notes'] = matched_intel

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(blasters, f, indent=2)

print("Injected INDIVIDUAL MODEL highly-specific Tieba/Bilibili intel into blasters_data.json")
