# Makmal UASA - Sains Tahun 6

Laman latihan UASA Sains Tahun 6 berdasarkan topik ulang kaji yang diberikan: **50 markah, 75 minit**.

## Ciri

- Bahagian A: 10 soalan objektif, 10 markah.
- Bahagian B: 2 soalan berstruktur, 8 markah.
- Bahagian C: 4 soalan KPS dan aplikasi, 32 markah.
- Pemasa, navigasi soalan, penanda semak kemudian dan simpan jawapan automatik pada pelayar.
- A/B ditanda tepat secara automatik.
- C menerima **cadangan kata kunci**, diikuti semakan dan pelarasan markah ibu bapa berdasarkan skema.
- Paparan markah, gred latihan, skema, eksport keputusan JSON dan cetak / PDF.

## Jalankan secara lokal

Aplikasi HTML/CSS/JavaScript tanpa kebergantungan runtime luaran. Serve direktori `dist/` melalui HTTP, contohnya:

```sh
python3 -m http.server 8080 --directory dist
```

Buka `http://localhost:8080`.

## Semakan

Gunakan Node.js 22 atau lebih baharu:

```sh
npm ci
npm run build
npm test
```

Fail aplikasi siap berada dalam `dist/`. Build menjalankan semakan sintaks dan ujian pemarkahan; tiada bundler diperlukan.

## Cloudflare Workers

Konfigurasi `wrangler.jsonc` menggunakan nama Worker berasingan `makmal-uasa-sains-t6` dan static assets daripada `dist/`.

Melalui Wrangler CLI pada akaun Cloudflare sendiri:

```sh
npx wrangler login
npx wrangler deploy
```

Untuk sambungan Git di Cloudflare, pilih repo ini dan branch `main`. Arahan build: `npm ci && npm run build`. Arahan deploy: `npx wrangler deploy`. Root projek ialah akar repo. Tiada environment variable, pangkalan data atau API key diperlukan oleh aplikasi ini.

## Had pemarkahan dan penyimpanan

- Ini **latihan kendiri**, bukan peperiksaan berpengawasan. Skema dimuatkan dalam pelayar.
- Pemarkahan bertulis menggunakan padanan kata kunci, bukan pemahaman AI. Ayat negatif, jawapan alternatif atau ejaan boleh dinilai tidak tepat. Markah C kekal cadangan sehingga disahkan ibu bapa.
- Mod ibu bapa tiada kata laluan. Pengesahan itu setempat, bukan pengesahan identiti ibu bapa.
- Gred latihan: A 80-100%, B 65-79%, C 50-64%, D 40-49%, E 0-39%. Bukan skala gred atau tahap penguasaan rasmi sekolah.
- Nama dan jawapan disimpan dalam localStorage pada peranti / pelayar ini sahaja. Tiada dashboard atau rekod pelajar berpusat. Muat turun keputusan untuk menyimpan salinan.
- Pemasa kekal selepas refresh. Apabila laman ditutup, tiada proses latar server; jika masa sudah tamat, jawapan dihantar apabila laman dibuka semula.
- Kertas latihan topik terpilih; bukan kertas rasmi KPM.

## Struktur

```text
dist/             Aplikasi siap untuk dihoskan
  index.html
  style.css
  questions.js    Kandungan soalan dan skema
  app.js          Aliran peperiksaan dan pemarkahan
tests.cjs         Ujian pemarkahan dan pemasa
wrangler.jsonc    Konfigurasi Cloudflare
```

Repo ini bebas daripada identiti projek Sites. Konfigurasi Cloudflare tidak menyasarkan AdvisorLink atau projek Mamu yang lain.
