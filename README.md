# HyperBoostX V3 — Unified Full Edition (Interactive Prototype)

**Status: browser-only interactive design prototype. NOT a native Windows optimizer.**

Dibuat sebagai spesifikasi UI/UX V3 terbaru yang mempertahankan keterlacakan nama fitur HyperBoostX V1–V2, bukan sebagai klaim seluruh fungsi Windows telah selesai dibuat.

## Open & deploy

- **Offline langsung:** buka `index.html` lewat Chrome/Edge (double click). Semua file bersifat lokal, tanpa CDN.
- **GitHub Pages:** commit seluruh isi folder ini ke root branch `main` dari repo prototipe yang ingin digunakan. Aktifkan *Settings → Pages → Deploy from branch → main / root*. Jangan hanya upload `index.html` — folder `assets/` dan `data/` dibutuhkan.
- **Development server:** jalankan `python -m http.server 8080` di folder ini, buka `http://localhost:8080`.
- **Versi satu file:** gunakan `HyperBoostX-V3-Unified-Standalone.html` (diberikan terpisah) untuk pratinjau tanpa folder tambahan.

## Isi prototipe

- 73 modul V3 dikelompokkan dalam 14 kelompok navigasi.
- 73 nama menu V2 dari `docs/UI_ACTION_MAP_v2.10.0.md` dipetakan secara eksplisit ke modul V3 lewat `data/catalog.json`.
- Tombol fitur membuka penjelasan dan review simulasi, bukan perubahan PC.
- Katalog fitur dapat dicari dengan Ctrl+K / ⌘K; pencarian juga mengindeks nama menu V2.
- Dark/light mode, favorit, draft profil, daftar game demo, skenario contoh, catatan aksi simulasi, serta ekspor JSON.
- Dashboard & chart berlabel demo; tidak mengklaim membaca CPU/GPU nyata.
- Simulasi alur approve dan kriteria Safety Guard. AI Assistant menggunakan jawaban aturan sederhana lokal dan tidak terhubung ke model AI.
- Research Mode A/B/C/D mempertahankan skema penelitian satu PC, tanpa mengarang hasil.
- Responsif untuk desktop dan mobile; tidak memerlukan library online.

## Sumber historis

- Repo V1–V2: https://github.com/jxxzy/HyperBoostX
- Action Map V2: https://github.com/jxxzy/HyperBoostX/blob/main/docs/UI_ACTION_MAP_v2.10.0.md
- Feature Truth Matrix V2: https://github.com/jxxzy/HyperBoostX/blob/main/docs/FEATURE_TRUTH_MATRIX_v2.10.0.md
- Prototipe awal V3: https://github.com/NEXORAID-ID/hyperboostx-v3-prototype

Dokumentasi V2 menyebut **73 menu dan 606 aksi**. Keduanya adalah *source reference*, bukan hasil verifikasi runtime dari prototipe baru. `catalog.json` hanya memuat pemetaan tingkat menu, bukan 606 ActionId/endpoint historis. Untuk menjaga parity sesungguhnya, developer harus mengimpor, memetakan, mengimplementasikan, dan menguji tiap aksi V2, termasuk fungsi dari V1 yang tidak terwadahi pada V2 akhir.

## Langkah selanjutnya menuju aplikasi native

1. Jadikan `data/catalog.json` dan data dokumentasi action map V2 sebagai kandidat registry canonical.
2. Audit parity **per kemampuan** (bukan hanya kesamaan nama): input, hasil, preview, permission, mutasi, restore, dan evidence.
3. Implementasikan shell WPF/WinUI native dengan isi halaman sesuai prototype; jangan menggunakan preview browser untuk mengubah Windows.
4. Buat backend .NET/Python yang berkomunikasi melalui IPC dengan worker berhak akses minimum, allowlisted ActionIds, signed manifests, typed parameters, dan Safety Guard.
5. Tes pada Windows 10/11, admin/non-admin, offline/unsupported, hardware low-end/high-end, crash/reboot, clean install/uninstall, termasuk rollback nyata.
6. Rilis stable hanya setelah gate bukti native, installer, packaging, dan pemetaan fitur seluruhnya lulus. Jangan menandai fitur dummy/partial sebagai selesai.

## Struktur

- `index.html` — app shell HTML.
- `assets/styles.css` — design system, dark/light, desktop/mobile.
- `assets/app.js` — route engine, state, modal, command search, demo features.
- `data/catalog.json` — readable data modules dan crosswalk historis.
- `data/catalog.js` — bentuk inline/global katalog, agar dapat dibuka via `file://`.
- `data/build_data.py` — sumber katalog dan generator file data.
- `tests/validate.mjs` — uji integritas dasar katalog.

## Keamanan dan privasi

Teks demo dan daftar game/profil disimpan di localStorage browser. Jangan memasukkan password, API key, token webhook, atau informasi sensitif. JSON ekspor **selalu** mencantumkan `simulated: true` dan `realWindowsMeasurements: false`. Tidak ada API backend atau permintaan jaringan dari kode ini. Tombol `Simulasikan saja` hanya mencatat riwayat demo.
