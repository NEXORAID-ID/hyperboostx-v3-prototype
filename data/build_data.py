import json, pathlib, re
root=pathlib.Path(__file__).parent
catalog=r'''COMMAND CENTER|Dashboard|Ringkasan kesehatan perangkat, beban sistem, dan aktivitas optimasi|scan|CPU load;GPU load;Memory pressure;Storage health
COMMAND CENTER|Smart Scan|Diagnosis perangkat dan pemeriksaan kesiapan Windows|scan|Quick scan;Deep scan;Gaming scan;Hardware scan;Privacy scan;Driver scan
COMMAND CENTER|One Click Boost|Rancang optimasi yang kompatibel sebelum disetujui|apply|Safe Boost;Gaming Boost;Low-End Boost;Creator Boost;Custom Boost
COMMAND CENTER|HyperBoost Score|Pahami skor kesiapan serta asal setiap pengukuran|scan|CPU readiness;RAM readiness;GPU readiness;Storage readiness;Network readiness;Reliability
COMMAND CENTER|Activity & Notifications|Riwayat tindakan, notifikasi, serta status pemulihan|read|Action history;Alerts;Pending restart;System notices
AI INTELLIGENCE|AI Assistant|Rekomendasi AI sadar-perangkat dengan persetujuan manual|ai|System diagnosis;Game recommendations;Hardware upgrades;Explain results
AI INTELLIGENCE|AI Provider Center|Atur provider lokal atau BYOK melalui penyimpanan aman|settings|Offline rules;NVIDIA BYOK;Model discovery;Managed gateway
AI INTELLIGENCE|GPU AI Assistant|Analisis beban grafis serta saran konfigurasi GPU|ai|Vendor detection;Driver health;VRAM pressure;Graphics recommendations
OPTIMIZATION|Performance Profiles|Profil daya dan performa dengan histori perubahan|profile|Balanced Safe;Maximum Safe;Gaming;Streaming;Creator;Office;Low-End PC;High-End PC;Laptop Battery;Expert Custom
OPTIMIZATION|Safe Tweak Library|Katalog perubahan terverifikasi berbasis risiko dan kompatibilitas|apply|CPU tweaks;Memory tweaks;Graphics tweaks;Power;Windows;Network;Privacy;Storage;Repair
OPTIMIZATION|Advanced Tweaks|Pemeriksaan nilai konfigurasi serta konsekuensi teknis|apply|Current values;Compatibility;Conflicts;Backups
OPTIMIZATION|CPU Optimization|Pantau topologi CPU serta kebijakan proses yang aman|scan|CPU topology;Background usage;Priority;Affinity;Power policies
OPTIMIZATION|CPU Turbo Diagnostics|Pemeriksaan clock, daya, dan batas termal tanpa overclock|scan|Clock telemetry;Power policy;Thermal limits;Turbo indicators
OPTIMIZATION|Smart Memory Guard|Lindungi aplikasi penting saat memori sedang tertekan|settings|Thresholds;Process exclusions;Commit charge;Notifications;Cooldown
OPTIMIZATION|Power Optimization|Lihat dan pratinjau konfigurasi daya Windows AC/DC|apply|Current plan;Plan inventory;Processor policy;Sleep;Restore
OPTIMIZATION|Hardware Tuner|Kontrol kebijakan OS yang benar-benar didukung perangkat|scan|CPU policy;GPU preference;Device power;Thermal awareness
GAMING|Game Boost Engine|Gabungkan kesiapan game, profil, dan pemulihan sesi|apply|CPU pressure;VRAM;Network;Overlay;Background apps;Session restore
GAMING|Game Library|Kelola game terpasang dan path eksekusi yang dipilih sendiri|profile|GTA V Legacy;GTA V Enhanced;FiveM;Roblox;Steam;Epic games;Manual game
GAMING|Per-Game Profiles|Kelola profil per-game yang dapat dikembalikan|profile|Auto apply;Auto restore;Profile editor;Import;Export;History
GAMING|Auto Gaming Mode|Jadwalkan profil aman berdasarkan lifecycle game|settings|Game detection;Profile conflict;Session exclusions;Recovery
GAMING|FPS & Frame Time|Catat data frame jika API pengukuran tersedia|scan|Average FPS;Frame time;1% low;0.1% low;Session history
GAMING|Stutter Analyzer|Korelasikan spike frame-time terhadap beban perangkat|scan|Frame-time spikes;GPU correlation;CPU load;Disk I/O;Thermal data
GAMING|Overlay Conflict Detector|Identifikasi overlay dan potensi konflik resource|scan|Discord;Steam;NVIDIA;AMD;RTSS;Xbox Game Bar
HARDWARE|Hardware Inventory|Inventarisasi komponen dengan sumber data yang jelas|scan|Processor;GPU;Motherboard;RAM;Storage;BIOS read-only
HARDWARE|GPU Center|Deteksi grafis multi-vendor dan kondisi driver|scan|NVIDIA;AMD;Intel;Hybrid graphics;Driver;VRAM
HARDWARE|Hardware Vendor Center|Pusat kompatibilitas utilitas OEM yang terdeteksi|scan|NVIDIA;AMD;Intel;MSI;ASUS;Other vendors
HARDWARE|Driver Health|Tinjau perangkat bermasalah dan sumber driver OEM|scan|Graphics;Chipset;Audio;LAN;Wi-Fi;Bluetooth;USB
HARDWARE|Device Manager|Temukan perangkat serta status kesalahan hardware|scan|Device inventory;Device errors;USB;Bluetooth;Display;Audio
HARDWARE|RGB Software Detector|Identifikasi aplikasi RGB dan overhead latar belakang|scan|SignalRGB;Mystic Light;OpenRGB;iCUE;Armoury Crate
HARDWARE|MSI Safe Optimizer|Periksa MSI Center tanpa mengganggu cooling service|scan|MSI Center;Mystic Light;Service dependencies;Exclusions
HARDWARE|Laptop & Battery|Analisis kapasitas baterai dan kebijakan AC/DC|scan|Battery capacity;Charge;Power source;Health;Energy profile
WINDOWS|Windows Optimization|Pusat preferensi Windows dan efek visual|apply|Visual effects;Notifications;Explorer;Storage Sense;Search indexing
WINDOWS|Startup Manager|Inventaris entri startup dan perubahan yang dapat dipulihkan|apply|Startup folder;Registry entries;App startup;Restore
WINDOWS|Boot Optimizer|Analisis event waktu boot dan dampak startup|scan|Boot events;Startup impact;Service dependencies;Boot history
WINDOWS|App Load Optimizer|Ukur waktu peluncuran aplikasi secara konsisten|scan|App inventory;Launch timing;Background load;History
WINDOWS|Process & Task Manager|Analisis proses, dependensi, dan daftar perlindungan|scan|CPU usage;Memory usage;Process tree;Priority;Protected processes
WINDOWS|Windows Services|Inspeksi layanan, dependensi, dan kontrol yang diizinkan|apply|Service inventory;Startup types;Dependencies;Protection;Restore
WINDOWS|Scheduled Tasks|Tinjau tugas terjadwal dan opsi pemulihan|scan|Task inventory;Triggers;Last result;Backup;Restore
WINDOWS|Debloat Center|Kelola aplikasi dengan pengecualian dan konfirmasi|apply|Win32 apps;Store packages;Dependencies;Exclusions;Uninstall preview
WINDOWS|Windows Update|Pantau update, reboot pending, dan troubleshooting|scan|Installed updates;Pending updates;Restart status;Troubleshooting
WINDOWS|Repair & Troubleshooting|Alur perbaikan Windows dengan gate hak akses|apply|SFC;DISM;Disk diagnostics;Update diagnostics;Event logs
STORAGE|Storage Center|Tinjau tipe drive, volume, kesehatan, dan TRIM|scan|HDD;SATA SSD;NVMe;Volumes;SMART;TRIM
STORAGE|Cleanup Center|Pratinjau penghapusan berkas temporer yang aman|apply|Temp files;Caches;Recycle Bin;Crash dumps;Shader cache
STORAGE|Duplicate & Large Files|Analisis file duplikat tanpa penghapusan otomatis|scan|Folder selection;Duplicate groups;Large files;Exclusions
STORAGE|Drive Optimization|Tentukan tindakan drive berdasarkan jenis media|apply|Media type;TRIM;Optimize drives;Schedule;Health
NETWORK|Network Center|Diagnostik adaptor, konfigurasi, dan traffic|scan|Adapters;IP configuration;Link speed;Wi-Fi;Traffic
NETWORK|DNS & Latency|Ukur latensi dan kualitas resolver tanpa klaim palsu|scan|Ping;Jitter;Loss;DNS response;Resolver selection
NETWORK|Network Profiles|Profil jaringan dengan preview dan rollback|apply|Balanced;Gaming diagnostics;DNS policy;Restore
CREATOR|Streaming Center|Kesiapan OBS, encoding, dan konflik streaming|scan|OBS;Streamlabs;NVENC;AMF;Quick Sync;CPU encoder
CREATOR|Audio & DJ Performance|Diagnostik DJ dan mikrofon, preservasi mixer V1–V2|scan|Rekordbox;Ableton;FL Studio;Serato;Advanced Mic Mixer;Voicemeeter;USB audio
CREATOR|Webcam Diagnostics|Pemeriksaan webcam serta camera tracking lama|scan|Webcam inventory;Microphones;Driver status;Permissions;Camera tracking
PRIVACY & SECURITY|Privacy Center|Privasi lokal dan persetujuan data|settings|Telemetry preferences;App permissions;Data export;Data deletion
PRIVACY & SECURITY|Security Health|Pemeriksaan Defender, firewall, dan proteksi sistem|scan|Defender;Firewall;UAC;Secure Boot;Update health;Defender Scan Guard
PRIVACY & SECURITY|LCD Performance Guard|Lindungi servis display, fan, dan pompa pendingin|settings|Monitor only;Gaming guard;Thresholds;Fan and pump exclusions
PRIVACY & SECURITY|Trust Center|Audit komponen, akses, System Reality Guard, dan pengecualian|scan|Permissions;Signed components;Integrations;Data sharing;System Reality Guard;Protected Apps
AUTOMATION|Scheduled Automation|Pratinjau otomasi lokal tanpa eksekusi sistem|settings|Scheduled scans;Cleanup;Reminders;Pause;Emergency stop
AUTOMATION|Task & Rule System|Rancang rule berbasis trigger dengan cooldown|settings|Triggers;Conditions;Approved actions;Cooldown;History
BACKUP & RECOVERY|Backup Snapshot Center|Rencana snapshot sebelum perubahan Windows|profile|Registry;Services;Power plan;Startup;Network;Restore point
BACKUP & RECOVERY|Restore & Rollback|Inspeksi histori serta strategi undo yang kompatibel|apply|Last action;Snapshot;Profile rollback;Conflict;History
BACKUP & RECOVERY|Emergency Recovery|Rencana pemulihan saat transaksi atau proses gagal|read|Pending transaction;Safe startup;Disable automation;Export diagnostics
REPORTS & TESTS|Benchmark Center|Templat benchmark yang membutuhkan pengukuran nyata|scan|CPU;Storage;Memory;Boot;FPS;Network
REPORTS & TESTS|Before / After Report|Perbandingan berbasis sumber dan kondisi pengujian|read|CPU idle;RAM idle;Boot;FPS;Frame time;Reclaimed space
REPORTS & TESTS|Research Mode|Protokol A/B/C/D pada satu PC untuk validasi penelitian|profile|A Windows default;B HyperBoostX;C SSD upgrade;D RAM upgrade;Run history
REPORTS & TESTS|Reports Center|Laporan terstruktur dan bukti lokal|read|System scan;Hardware;Gaming;Network;Benchmark;Action history
REPORTS & TESTS|Test Center|Periksa kontrak, navigasi, permission, dan gate|scan|UI binding;Backend;Database;Permissions;Backup;Runtime;AI;Webhook
REPORTS & TESTS|Application Health|Pemeriksaan readiness aplikasi serta sumber error|scan|Runtime;Worker status;Database;File integrity;Recovery
TOOLS & SETTINGS|Plugin Manager|Audit izin dan kompatibilitas plugin tepercaya|settings|Plugin inventory;Compatibility;Permissions;Activity
TOOLS & SETTINGS|Discord Webhook|Periksa integrasi webhook dengan consent dan redaksi|settings|Connection;Payload preview;Rate limit;Categories;Local fallback
TOOLS & SETTINGS|License Center|Status lisensi lokal serta ketentuan pihak ketiga|settings|Edition;Third-party licenses;Local state;Privacy
TOOLS & SETTINGS|Update Center|Sumber update, integrity, dan histori rilis|scan|Current version;Trusted source;Integrity;Update history
TOOLS & SETTINGS|Knowledge Base|Panduan, batasan, keamanan, dan recovery|read|Getting started;Optimizing safely;Troubleshooting;Recovery
TOOLS & SETTINGS|Settings|Preferensi aplikasi, tema, dan mode pengguna|settings|Theme;Language;User mode;Monitoring;Privacy
TOOLS & SETTINGS|About HyperBoostX|Informasi produk, kontributor, dan atribusi|read|HyperBoostX V3;NEXORAID;MR.4NONY;Third-party acknowledgements'''
mods=[]
for line in catalog.splitlines():
  g,n,d,k,f=line.split('|');mods.append({'id':re.sub(r'[^a-z0-9]+','-',n.lower()).strip('-'),'group':g,'name':n,'description':d,'kind':k,'features':f.split(';')})
assert len(mods)==73, f'Expected 73, got {len(mods)}'
assert len(set(x['id'] for x in mods))==73
legacy_names='''Dashboard|Smart Scan|HyperBoost Score|AI Performance Advisor|AI Center|NVIDIA Copilot|One Click Boost|Auto Gaming Mode|Performance Boost|CPU/RAM Optimizer|HyperBalance|Process Analyzer|Background Apps|Startup Manager|Cleanup|Storage|Network Tools|Network Booster|DNS & Latency Tools|Network Optimization|GPU Center|Hardware Vendor Center|Driver Recommendation|Driver & Update Center|Overlay Conflict Detector|RGB Software Detector|Game Library|Game Profiles|Gaming Booster|Gaming Essentials|Streaming Center|Creator Mode|Advanced Mic Mixer|Webcam Studio|Camera Tracking|Privacy Center|Security & Health|System Reality Guard|LCD Performance Guard|Defender Scan Guard|CPU Turbo Diagnostic|MSI Safe Optimizer|Security Reality Audit|Protected Apps|Apps Manager|App Uninstaller|Tweaks Center|Advanced Tweaks|Windows Features|Windows Services|Update Control|Repair Tools|Power Optimization|Visual Effects|Restore & Backup|Restore Point Manager|Reports|Performance History|Performance Report|Scheduled Automation|Task & Rule System|Utilities Tools|Feature Audit|Master Test Engine|Feature Audit Matrix|Plugin Marketplace|Cloud Sync & License Boundary|Release Readiness|Benchmark Lab|Knowledge Base|App Settings|About App|Default Fallback'''.split('|')
target_names='''Dashboard|Smart Scan|HyperBoost Score|AI Assistant|AI Assistant|AI Provider Center|One Click Boost|Auto Gaming Mode|Performance Profiles|CPU Optimization|Smart Memory Guard|Process & Task Manager|Process & Task Manager|Startup Manager|Cleanup Center|Storage Center|Network Center|Network Profiles|DNS & Latency|Network Profiles|GPU Center|Hardware Vendor Center|Driver Health|Driver Health|Overlay Conflict Detector|RGB Software Detector|Game Library|Per-Game Profiles|Game Boost Engine|Game Boost Engine|Streaming Center|Streaming Center|Audio & DJ Performance|Webcam Diagnostics|Webcam Diagnostics|Privacy Center|Security Health|Trust Center|LCD Performance Guard|Security Health|CPU Turbo Diagnostics|MSI Safe Optimizer|Security Health|Trust Center|Debloat Center|Debloat Center|Safe Tweak Library|Advanced Tweaks|Windows Optimization|Windows Services|Windows Update|Repair & Troubleshooting|Power Optimization|Windows Optimization|Backup Snapshot Center|Backup Snapshot Center|Reports Center|Before / After Report|Before / After Report|Scheduled Automation|Task & Rule System|Device Manager|Test Center|Test Center|Test Center|Plugin Manager|License Center|Application Health|Benchmark Center|Knowledge Base|Settings|About HyperBoostX|Application Health'''.split('|')
assert len(legacy_names)==73 and len(target_names)==73
name_to_id={m['name']:m['id'] for m in mods}
legacy=[]
review_list={'NVIDIA Copilot','Advanced Mic Mixer','Camera Tracking','System Reality Guard','Defender Scan Guard','Security Reality Audit','Protected Apps','Apps Manager','App Uninstaller','Cloud Sync & License Boundary','Plugin Marketplace','Creator Mode','HyperBalance','Performance Boost','Restore Point Manager'}
for name,target in zip(legacy_names,target_names):
  assert target in name_to_id,target
  legacy.append({'source':name,'target':target,'moduleId':name_to_id[target],'review':name in review_list})
obj={'version':'3.0.0-unified-prototype','sourceBaseline':'jxxzy/HyperBoostX v2.10.0','sourceDocumentedActions':606,'demoOnly':True,'modules':mods,'legacy':legacy}
(root/'catalog.json').write_text(json.dumps(obj,indent=2,ensure_ascii=False),encoding='utf-8')
(root/'catalog.js').write_text('window.HBX_DATA = '+json.dumps(obj,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
print('Modules',len(mods),'Historical',len(legacy),'Groups',len(set(m['group'] for m in mods)))
