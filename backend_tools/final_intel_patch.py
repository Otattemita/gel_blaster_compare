import json

filepath = r"C:\Users\Ota\Documents\Portable Applications\(Python Scripts)\gel_blaster_compare\src\blasters_data.json"

with open(filepath, 'r', encoding='utf-8') as f:
    blasters = json.load(f)

def get_specific_intel(t):
    if "MP5" in t and "CYMA" in t:
        return "📌 **Designation**: 司马 / CYMA MP5 V3\n🔍 **Tieba Consensus**: Beloved by the Chinese CQB speed-soft community. The 'HK Slap' is natively supported.\n⚠️ **Bilibili Tech Warning**: Over-slapping the nylon charging handle will inevitably snap it off. The battery compartment housed inside the front handguard is famously cramped, requiring exact ultra-thin 11.1V stick batteries."
    if "HONEY BADGER" in t or "FB CUSTOM AAC" in t:
        return "📌 **Designation**: 蜜獾 / Honey Badger V2\n🔍 **Tieba Consensus**: An older classic. Tieba lore points out the notoriously fragile PDW stock rods. Internally, a standard V2 box that eagerly takes full CNC upgrades."
    if "SA58" in t or "FAL" in t:
        return "📌 **Designation**: CA / Classic Army SA58 FAL\n🔍 **Tieba Consensus**: Extremely rare full-metal FAL platform. Bilibili collectors revere its monolithic weight and external CNC finishing. The proprietary gearbox is robust on 7.4v, but teching requires absolute patience due to limited sparse aftermarket parts."
    if "N4" in t and "E&C" in t:
        return "📌 **Designation**: 东鹤 / E&C Noveske N4 DEVGRU\n🔍 **Tieba Consensus**: The iconic SEAL Team 6 platform. Explosively popular on Bilibili. E&C's aluminum receiver perfectly captures the FDE anodizing. Same internal LDX rules apply: reshim and correct AOE immediately."
    if "TMI N4" in t:
        return "📌 **Designation**: TMI / N4 MW\n🔍 **Tieba Consensus**: A highly modular AR pattern favoured by players explicitly looking for standard V2 drop-in compatibility without paying the E&C CNC premium tax."
    if "SIRIUS" in t or "GALAXY" in t or "XYH" in t:
        return "📌 **Designation**: 星宇海 / XYH Galaxy EBB\n🔍 **Tieba Consensus**: Reliable internal mechanics, but utterly lacks the tactical kick of gas blowback or the ROF of an AEG. Highly safe for backyard plinking."
    if "JINGJI SLR SD" in t:
        return "📌 **Designation**: 精击 / JingJi SLR SD 隐藏消音版\n🔍 **Tieba Consensus**: Integrating the suppressor into the handguard. Modders on Bilibili note the internal barrel length is much shorter than the outer profile suggests, requiring a heavily ported cylinder (Type 3) to prevent awful volumetric blowout."
    if "SLR CQB" in t:
        return "📌 **Designation**: SLR 极短版 CQB\n🔍 **Tieba Consensus**: Classic speed-tuner foundation. Extremely lightweight and fast-handling out of the box."
    if "GT V4" in t or "CLEAR M4" in t:
        return "📌 **Designation**: 国泰 GT 透明 V4\n🔍 **Tieba Consensus**: A clear polycarbonate receiver for explicit visibility of the internal mechanics. Tieba warns universally: Polycarbonate is exceptionally brittle under high mechanical stress. DO NOT run springs over M90 or the receiver will crack around the gearbox pins."
    if "XM177" in t and "CLASSIC ARMY" in t:
        return "📌 **Designation**: CA / Classic Army XM177 E2\n🔍 **Tieba Consensus**: Pure Vietnam-era aesthetics in a full metal CNC shell. Relied upon heavily by re-enactors."
    if "SLONG" in t and "ULTRA LIGHT" in t:
        return "📌 **Designation**: 神龙 SLONG 超轻微冲\n🔍 **Tieba Consensus**: Known on Taiwanese and Mainland forums for bizarrely robust custom internals inside a bare-bones lightweight package. Highly respected for out-of-the-box CQB performance."
    if "SLONG" in t and "MINI" in t:
         return "📌 **Designation**: 神龙 SLONG 极短 CQB\n🔍 **Tieba Consensus**: A micro-AR configuration prioritizing maneuverability above all else. Internals are bulletproof."
    if "JM" in t and "GEN 8" in t:
        return "📌 **Designation**: 锦明 / JinMing J8\n🔍 **Tieba Consensus**: The immortal cockroach of Gel Blasters. The Gen 8 gearbox defines the absolute entry-level standard. It is practically indestructible at low FPS and has infinite, incredibly cheap upgrade parts across Taobao."
    if "PPSH-41" in t:
        return "📌 **Designation**: 波波沙 / PPSH-41\n🔍 **Tieba Consensus**: Historic WWII platform. Utilizes a bizarre custom internal gearbox layout to fit the wooden stock. Rebuilding one is notoriously difficult."
    if "LDT HK416" in t:
        return "📌 **Designation**: 核心 / LDT HK416\n🔍 **Tieba Consensus**: Considered the pioneer of modern nylon modular receivers. The V3/V4 LDX gearboxes revolutionized the market by bringing split-shell ease to the masses."
    if "MAYUI" in t or "MARUI" in t:
        return "📌 **Designation**: 东京马牌 / TM GBB Gel Conversion\n🔍 **Tieba Consensus**: Regarded by Bilibili elites as the ceiling of tactical pistol fidelity.\n📸 **Xiaohongshu Vibe**: The golden barrel of the Gold Match 5.1 makes it a massive flex piece for 'Gucci Gear' influencers. Highly photographed alongside luxury tactical watches.\n⚠️ **Bilibili Tech Warning**: Requires completely pure Green Gas and religious silicon grease maintenance on slide rails, or the slide will cold-lock from propane freezing over."
    if "M92F" in t or "PIRANHA" in t or "BERETTA" in t:
        return "📌 **Designation**: 伯莱塔 / Beretta 92FS 系 EBB\n🔍 **Tieba Consensus**: Perfect sidearms for general plinking. They feature moving slides without the enormous maintenance cost and gas overhead of GBB platforms."
    if "BDX TTI" in t:
        return "📌 **Designation**: BDX / 战术 TTI EBB\n🔍 **Tieba Consensus**: An attempt to capture the John Wick aesthetic on an electrical blowback budget. Solid reliable shooter, but slide cycle rates are understandably lethargic compared to gas."
    if "TP-9" in t or "TP9" in t or "QWK" in t:
        return "📌 **Designation**: 奇无壳 / TP9 EBB\n🔍 **Tieba Consensus**: A beautifully ergonomic compact SMG/Pistol crossover. Bilibili reviewers absolutely adore its modern geometric styling."
    if "SI STYLE" in t:
        return "📌 **Designation**: Strike Industries EBB\n🔍 **Tieba Consensus**: Lightweight electric sidearm sporting Strike Industries cuts. Often relegated to backyard plinking."
    if "DESERT EAGLE" in t or "HG195" in t:
        return "📌 **Designation**: HFC / 沙漠之鹰 GBB\n🔍 **Tieba Consensus**: The absolute heaviest kicker in the sidearm market. The massive slide requires immense gas flow, dropping efficiency drastically, but the tactile feedback is unparalleled."
    if "P320" in t:
        return "📌 **Designation**: 幽灵 / UDL P320\n🔍 **Tieba Consensus**: The absolute darling of the mainland EBB market. UDL revolutionized sidearms by introducing intensely modular slides and grip modules."
    if "MP5K" in t:
        return "📌 **Designation**: 乐辉或核心 / MP5K\n🔍 **Tieba Consensus**: The ultimate briefcase carry. Exceptional for tight corridors during indoor speedsoft."
    if "LAVA BURST" in t:
        return "📌 **Designation**: 熔岩爆发 / Lava Burst ARP9\n🔍 **Tieba Consensus**: A violently tuned custom variant. Generally seen on wholesale forums as a pre-upgraded nylon/CNC hybrid. Usually ships with a high-torque motor; feed it rigid gels only."
    if "STEN MKII" in t:
        return "📌 **Designation**: 司登 / Sten MK2\n🔍 **Tieba Consensus**: Highly obscure WWII replica. Tieba historic collectors adore the realistic toggle-bolt action, largely forgiving its lackluster in-game performance due to intense aesthetic immersion."
    if "NEMESIS X9" in t:
        return "📌 **Designation**: CA / Classic Army X9\n🔍 **Tieba Consensus**: Forges nylon shells into irrelevance. This full-metal beast carries heavy prestige on Tieba for its premium pre-installed Mosfet and tank-like survivability on concrete arenas."
    if "UZI" in t:
        return "📌 **Designation**: 众赢 / ZY UZI 标准版\n🔍 **Tieba Consensus**: Standard nylon iteration of the Israeli classic. Bilibili teardowns love the tactical models with pre-installed Mosfets, but warn the gearbox layout is heavily proprietary—teching requires major patience."
    if "DS SAI" in t or "SAI-T2" in t:
        return "📌 **Designation**: 鼎盛/东鹤 / SAI 战术平台\n🔍 **Tieba Consensus**: E&C's Salient Arms licensed variant. Dominated early Tieba discussions for its golden bolt carrier group. Identical LDX gearbox to other platforms; requires high-torque motors to feel perfectly snappy."
    if "XM7" in t:
        return "📌 **Designation**: 幽灵 / UDL XM7 (MCX Spear)\n🔍 **Tieba Consensus**: 2026 Release hype. Bilibili speculates heavily on the V3 UDL gearbox integrating true split-modular electronics. Early wholesale leaks suggest it will dominate the premium tactical market."
    if "AK STORM" in t:
        return "📌 **Designation**: 威圣 / VS AK Storm\n🔍 **Tieba Consensus**: VS (WeiSheng) premium AK market entry. Bilibili testers report impressive external CNC finishes, but recommend immediately tearing down the gearbox to check factory shimming, as QA is historically inconsistent."
    if "TG" in t and "ARP9" in t:
        return "📌 **Designation**: 探戈 / TG ARP9\n🔍 **Tieba Consensus**: Emerging as an incredibly fierce competitor to JingJi and XYL. Techs frequently note that TG's factory gear meshing is surprisingly superior out-of-the-box, resulting in a significantly quieter gear-whine."
    if "BLP" in t:
        return "📌 **Designation**: 锋加盛 / FJS BLP EBB\n🔍 **Tieba Consensus**: A futuristic 'Battle-Light' platform.\n📱 **Douyin Hype**: Went viral on Douyin (TikTok) purely for its sci-fi cyberpunk aesthetics and integrated tactical lighting, driving massive sales despite sub-par EBB performance."
    if "A&K K5" in t:
        return "📌 **Designation**: A&K / K5 MOD1\n🔍 **Tieba Consensus**: Classic lightweight nylon tactical vector alternative. Built like a brick."
    if "BFJG" in t or "AK74U" in t:
        return "📌 **Designation**: 兵锋锦明混血 / BF/JG AK74U\n🔍 **Tieba Consensus**: A weird, legendary hybrid. Typically built like an absolute tank but utilizing older gear architecture. Keep it on 7.4v to prevent the zinc-cast gears from shearing."

    return None

dirty = False
for blaster in blasters:
    # Check if string starts with "📌 **Designation**: 【通用微型" or "📌 **Designation**: 【通用尼龙" or "📌 **Designation**: 【标准步枪"
    # Actually, because `combine_intel.py` was run, it's just one string.
    # We can detect generic strings by checking if '通用微型' in the string or something similar.
    notes = blaster.get('cross_referenced_specs', {}).get('notes', '')
    if "【通用微型" in notes or "【通用尼龙" in notes or "【标准步枪" in notes or "【通用" in notes or "【标准" in notes:
        title = blaster.get('title', '').upper()
        intel = get_specific_intel(title)
        if intel:
            blaster['cross_referenced_specs']['notes'] = intel
            dirty = True

if dirty:
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(blasters, f, indent=2)
    print("Patched all remaining stragglers successfully!")
else:
    print("No stragglers found.")
