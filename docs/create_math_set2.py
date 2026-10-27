"""Original Mathematics Set 2; no modification of Set 1 data or assets."""
from pathlib import Path
from fractions import Fraction
from collections import Counter
import json,math
ROOT=Path(__file__).resolve().parents[1]
ASSETS=ROOT/'dist/assets';ASSETS.mkdir(exist_ok=True)
T=['Nombor bulat dan operasi asas','Pecahan, perpuluhan dan peratus','Wang','Masa dan waktu','Ukuran dan sukatan','Ruang','Koordinat, nisbah dan kadaran','Pengurusan data dan kebolehjadian']
Q=[]
def field(id,label,answer,max,topic,model,**extra):return dict(id=id,type='math',kind=extra.pop('kind','number'),label=label,answer=answer,max=max,topic=T[topic],model=model,**extra)
def group(id,title,intro,fields,**extra):Q.append(dict(id=id,section=id[0].upper(),title=title,intro=intro,fields=fields,**extra))
def a(n,topic,prompt,answer,model,**extra):group(f'a{n}',f'Soalan {n}',prompt,[field(f'a{n}','Jawapan akhir',answer,2,topic,model,**extra)],topic=T[topic])
a(1,0,'Tukarkan 1 3/5 juta kepada nombor bulat.',1600000,'1 3/5 juta = 8/5 × 1 000 000 (1) = 1 600 000 (1).',displayUnit='nombor bulat')
a(2,0,'Cari nilai anu dalam ayat matematik: (□ + 1 250 000) ÷ 5 = 700 000.',2250000,'700 000 × 5 = 3 500 000 (1). Anu = 3 500 000 − 1 250 000 = 2 250 000 (1).',displayUnit='nombor bulat')
a(3,1,'Hitung 3 1/2 ÷ 2/3. Berikan jawapan dalam pecahan atau perpuluhan.',5.25,'3 1/2 ÷ 2/3 = 7/2 × 3/2 (1) = 21/4 = 5 1/4 atau 5.25 (1).')
a(4,1,'Hitung 2.4 × 1.35.',3.24,'24 × 135 = 3 240; jumlah tempat perpuluhan ialah tiga (1). Jawapan = 3.240 = 3.24 (1).')
a(5,2,'Sepasang kasut berharga RM180 sebelum diskaun. Kedai memberikan diskaun 20%. Hitung harga kasut selepas diskaun.',144,'Diskaun = 20/100 × RM180 = RM36 (1). Harga selepas diskaun = RM180 − RM36 = RM144 (1).',displayUnit='RM',units=['RM','ringgit'])
a(6,2,'Sofia mempunyai pelaburan sebanyak RM2 500. Kadar dividen yang diberi dalam soalan ini ialah 4% bagi satu tahun. Hitung dividen yang diterimanya.',100,'Dividen = 4/100 × RM2 500 (1) = RM100 (1). Kadar ini data rekaan untuk latihan.',displayUnit='RM',units=['RM','ringgit'])
a(7,3,'Bandar X menggunakan GMT+9 dan Bandar Y menggunakan GMT+5. Waktu di X ialah 16:40. Nyatakan waktu di Y pada hari yang sama dalam format 24 jam.','12:40','Perbezaan masa = 9 − 5 = 4 jam (1). Waktu di Y = 16:40 − 4 jam = 12:40 (1).',kind='time',displayUnit='HH:MM (24 jam)')
group('a8','Soalan 8','Bandar X menggunakan GMT+8 dan Bandar Z menggunakan GMT+3. Waktu di X ialah 02:20 pada 7 Disember 2026. Nyatakan waktu dan tarikh di Z.',[
 field('a8a','(a) Waktu di Z dalam format 24 jam.','21:20',1,3,'Z lewat 5 jam. 02:20 − 5 jam = 21:20 pada hari sebelumnya (1).',kind='time',displayUnit='HH:MM (24 jam)'),
 field('a8b','(b) Tarikh di Z.','6 Disember 2026',1,3,'6 Disember 2026 (1). Terima 06/12/2026 atau 6 Dis 2026.',kind='word',accepted=['6 Disember 2026','06 Disember 2026','6 Dis 2026','06 Dis 2026','6/12/2026','06/12/2026','6-12-2026','06-12-2026'],displayUnit='hh/bb/tttt')],topic=T[3])
a(9,4,'Kain seragam sepanjang 2.4 m mempunyai jisim 0.75 kg. Hitung jisim kain yang sama jenis sepanjang 9.6 m.',3,'9.6 ÷ 2.4 = 4 (1). Jisim = 4 × 0.75 kg = 3 kg (1).',displayUnit='kg',units=['kg','kilogram'])
a(10,5,'Rajah menunjukkan bulatan berpusat O. Panjang diameter CD ialah 12.8 cm. Berapakah panjang jejari OD?',6.4,'Jejari = diameter ÷ 2 (1) = 12.8 cm ÷ 2 = 6.4 cm (1).',displayUnit='cm',units=['cm','sentimeter'])
Q[-1].update(image='assets/math2-circle.svg',imageAlt='Bulatan berpusat O. C dan D ialah hujung diameter sepanjang 12.8 cm. OD ialah jejari. Rajah tidak mengikut skala.')
a(11,5,'Sebuah oktagon sekata mempunyai jumlah sudut pedalaman 1 080°. Hitung satu sudut pedalamannya.',135,'Oktagon sekata mempunyai 8 sudut sama besar (1). Satu sudut = 1 080° ÷ 8 = 135° (1).',displayUnit='darjah (°)',units=['°','darjah'])
a(12,6,'Pada peta grid, P berada di (4, 1) dan Q di (4, 7). Skala mencancang ialah 1 unit mewakili 3 km. Hitung jarak sebenar antara P dengan Q.',18,'Beza koordinat mencancang = 7 − 1 = 6 unit (1). Jarak = 6 × 3 km = 18 km (1).',displayUnit='km',units=['km','kilometer'])
Q[-1].update(image='assets/math2-grid.svg',imageAlt='Grid sukuan pertama: P (4,1), Q (4,7). Jarak antara kedua-duanya mencancang; 1 unit mewakili 3 km.')
a(13,7,'Carta pai menunjukkan hobi 64 orang murid. Sektor Membaca ialah 180°, Melukis 90°, Catur 45° dan Berkebun 45°. Berapakah bilangan murid yang memilih Catur?',8,'Bahagian Catur = 45°/360° = 1/8 (1). Bilangan murid = 1/8 × 64 = 8 orang (1).',displayUnit='orang',units=['orang','murid'])
Q[-1].update(image='assets/math2-pie.svg',imageAlt='Carta pai hobi 64 murid: Membaca 180°, Melukis 90°, Catur 45° dan Berkebun 45°. Jumlah sudut 360°.')
group('b1','1. Projek buku dan pameran','Jawab semua bahagian. Setiap situasi adalah berasingan. Tunjukkan jalan kerja di ruang yang disediakan.',[
 field('b1a','(a) Sebuah penerbit mencetak 2.35 juta buku latihan pada tahun pertama dan 1 1/4 juta pada tahun kedua. Hitung jumlah buku yang dicetak dalam nombor bulat.',3600000,2,0,'1 1/4 juta = 1.25 juta; jumlah = 2.35 + 1.25 = 3.6 juta (1) = 3 600 000 buah buku (1).',displayUnit='buah',units=['buah','buku']),
 field('b1b','(b) Sebuah pusat pameran menerima 0.6 juta pengunjung tahun lalu. Bilangan pengunjung tahun ini ialah 150% daripada tahun lalu. Hitung bilangan pengunjung tahun ini dalam nombor bulat.',900000,3,1,'150% = 1.5 (1). 1.5 × 0.6 juta = 0.9 juta (1). Bilangan pengunjung = 900 000 orang (1).',displayUnit='orang',units=['orang','pengunjung']),
 field('b1c','(c) Kos sebuah buku cenderamata ialah RM18. Harga tandanya RM25. Pembeli diberi rebat RM1.50. Hitung untung bagi sebuah buku.',5.5,2,2,'Harga jual sebenar = RM25 − RM1.50 = RM23.50 (1). Untung = RM23.50 − RM18 = RM5.50 (1).',displayUnit='RM',units=['RM','ringgit']),
 field('b1d','(d) Penerbangan bertolak dari Bandar A (GMT+2) pada 14:25. Tempoh penerbangan ke Bandar B (GMT+5) ialah 3 jam. Nyatakan waktu tempatan ketibaan di B dalam format 24 jam.','20:25',2,3,'Tiba pada 17:25 mengikut waktu A (1). B awal 3 jam: 17:25 + 3 jam = 20:25 (1).',kind='time',displayUnit='HH:MM (24 jam)'),
 field('b1e','(e) Nisbah lencana merah kepada lencana biru ialah 3 : 5. Terdapat 320 lencana semuanya. Hitung bilangan lencana biru.',200,3,6,'Jumlah bahagian = 3 + 5 = 8 (1). Satu bahagian = 320 ÷ 8 = 40 (1). Lencana biru = 5 × 40 = 200 (1).',displayUnit='lencana',units=['lencana'])])
group('b2','2. Hari Kelab Sekolah','Jawab semua bahagian. Setiap situasi adalah berasingan. Data dan kadar dalam soalan ialah rekaan untuk latihan.',[
 field('b2ai','(a)(i) Sebanyak 2 L jus mempunyai jisim 1.6 kg. Pada kadar campuran yang sama, hitung jisim 9 L jus.',7.2,2,4,'Faktor gandaan = 9 ÷ 2 = 4.5 (1). Jisim = 4.5 × 1.6 kg = 7.2 kg (1).',displayUnit='kg',units=['kg','kilogram']),
 field('b2aii','(a)(ii) Semua 9 L jus itu diisi ke dalam botol 375 mL. Berapakah botol penuh yang diperoleh?',24,2,4,'9 L = 9 000 mL (1). Bilangan botol = 9 000 ÷ 375 = 24 botol (1).',displayUnit='botol',units=['botol']),
 field('b2b','(b) Sebuah bulatan hiasan dibahagikan kepada 8 sektor sama besar. Hitung sudut pada pusat bagi satu sektor.',45,2,5,'Satu putaran lengkap = 360° (1). Sudut bagi satu sektor = 360° ÷ 8 = 45° (1).',displayUnit='darjah (°)',units=['°','darjah']),
 field('b2c','(c) Empat buku nota berharga RM18. Pada kadar yang sama, hitung harga 10 buku nota.',45,2,6,'Harga satu buku nota = RM18 ÷ 4 = RM4.50 (1). Harga 10 buku nota = 10 × RM4.50 = RM45 (1).',displayUnit='RM',units=['RM','ringgit']),
 field('b2di','(d)(i) Daripada 96 orang murid, 48 memilih aktiviti kraftangan. Hitung sudut sektor Kraftangan dalam carta pai bagi semua murid.',180,2,7,'Bahagian Kraftangan = 48/96 = 1/2 (1). Sudut sektor = 1/2 × 360° = 180° (1).',displayUnit='darjah (°)',units=['°','darjah']),
 field('b2dii','(d)(ii) Sebuah beg hanya mengandungi 6 bola kuning. Sebiji bola diambil tanpa melihat. Nyatakan kebolehjadian mendapat bola kuning menggunakan istilah yang sesuai.','Pasti',1,7,'Pasti (1), kerana semua bola di dalam beg berwarna kuning.',kind='word',accepted=['pasti']),
 dict(id='b2diii',type='text',label='(d)(iii) Berikan sebab bagi jawapan (d)(ii).',max=1,topic=T[7],model='Semua bola di dalam beg berwarna kuning / beg hanya mengandungi bola kuning / tiada bola warna lain (1). Terima alasan setara yang betul.',reasonAlternatives=[[['semua','hanya','kesemua'],['kuning']],[['tiada','tidak ada'],['warna lain']]])])
# Independent exact arithmetic checks, not keyword-based answer generation.
checks=[(Fraction(8,5)*1000000,1600000),(700000*5-1250000,2250000),(Fraction(7,2)/Fraction(2,3),Fraction('5.25')),(Fraction('2.4')*Fraction('1.35'),Fraction('3.24')),(180*(1-Fraction(20,100)),144),(2500*Fraction(4,100),100),(Fraction('9.6')/Fraction('2.4')*Fraction('0.75'),3),(Fraction('12.8')/2,Fraction('6.4')),(1080/8,135),((7-1)*3,18),(Fraction(45,360)*64,8),((Fraction('2.35')+Fraction(5,4))*1000000,3600000),(Fraction(150,100)*600000,900000),(25-Fraction('1.50')-18,Fraction('5.5')),(Fraction(5,8)*320,200),(Fraction(9,2)*Fraction('1.6'),Fraction('7.2')),(9000/375,24),(360/8,45),(Fraction(18,4)*10,45),(Fraction(48,96)*360,180)]
for actual,expected in checks:assert actual==expected
assert len(Q)==15
assert [sum(f['max'] for q in Q if q['section']==s for f in q['fields']) for s in 'AB']==[26,24]
weights=Counter()
for q in Q:
 for f in q['fields']:weights[f['topic']]+=f['max']
assert [weights[t] for t in T]==[6,7,6,6,6,6,7,6]
old=json.loads((ROOT/'dist/questions-matematik.js').read_text().removeprefix('const QUESTIONS = ').strip().removesuffix(';'))
assert all(new['intro']!=prior['intro'] for new,prior in zip(Q,old))
oldfields={f['id']:f for q in old for f in q['fields']}
assert all(f['label']!=oldfields[f['id']]['label'] for q in Q if q['section']=='B' for f in q['fields'] if f['id']!='b2diii')
(ROOT/'dist/questions-matematik-set2.js').write_text('const QUESTIONS = '+json.dumps(Q,ensure_ascii=False)+';\n')
(ROOT/'docs/math-set2-coverage.json').write_text(json.dumps(dict(set=2,total=50,topics=[dict(topic=t,marks=weights[t]) for t in T]),ensure_ascii=False,indent=2)+'\n')
head='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 320" role="img">'
def tx(x,y,s):return f'<text x="{x}" y="{y}" font-family="sans-serif" font-size="15" fill="#183833">{s}</text>'
svg=head+'<rect width="520" height="320" rx="16" fill="#f3f7f1"/><circle cx="260" cy="145" r="100" fill="white" stroke="#115e59" stroke-width="2"/><line x1="160" y1="145" x2="360" y2="145" stroke="#115e59" stroke-width="3"/><circle cx="260" cy="145" r="4" fill="#115e59"/>'+tx(140,150,'C')+tx(370,150,'D')+tx(250,169,'O')+tx(230,130,'12.8 cm')+tx(155,290,'Rajah tidak mengikut skala')+'</svg>'
(ASSETS/'math2-circle.svg').write_text(svg)
svg=head+'<rect width="520" height="320" rx="16" fill="#f3f7f1"/>'
for x in range(7):
 xx=120+x*28;svg+=f'<line x1="{xx}" y1="22" x2="{xx}" y2="260" stroke="#d8e2dc"/>'+tx(xx-5,281,str(x))
for y in range(9):
 yy=260-y*28;svg+=f'<line x1="120" y1="{yy}" x2="288" y2="{yy}" stroke="#d8e2dc"/>'+tx(95,yy+5,str(y))
svg+='<path d="M120 22 V260 H306" fill="none" stroke="#183833" stroke-width="2"/>'+tx(316,265,'x')+tx(100,18,'y')
svg+='<line x1="232" y1="232" x2="232" y2="64" stroke="#d09a34" stroke-width="3" stroke-dasharray="5 4"/>'
for y,label in [(1,'P (4,1)'),(7,'Q (4,7)')]:
 yy=260-y*28;svg+=f'<circle cx="232" cy="{yy}" r="6" fill="#115e59"/>'+tx(252,yy+5,label)
svg+=tx(140,311,'Skala: 1 unit mewakili 3 km')+'</svg>';(ASSETS/'math2-grid.svg').write_text(svg)
svg=head+'<rect width="520" height="320" rx="16" fill="#f3f7f1"/>';start=-90
for angle,color in [(180,'#a9cdb9'),(90,'#efc572'),(45,'#aabfdc'),(45,'#d4b8d8')]:
 end=start+angle;x1=150+100*math.cos(math.radians(start));y1=150+100*math.sin(math.radians(start));x2=150+100*math.cos(math.radians(end));y2=150+100*math.sin(math.radians(end));svg+=f'<path d="M150 150 L{x1:.4f} {y1:.4f} A100 100 0 0 1 {x2:.4f} {y2:.4f} Z" fill="{color}" stroke="white" stroke-width="2"/>';start=end
for y,label,c in [(65,'Membaca: 180°','#a9cdb9'),(110,'Melukis: 90°','#efc572'),(155,'Catur: 45°','#aabfdc'),(200,'Berkebun: 45°','#d4b8d8')]:svg+=f'<rect x="278" y="{y-14}" width="17" height="17" rx="3" fill="{c}"/>'+tx(308,y,label)
svg+=tx(278,265,'Jumlah: 64 murid')+'</svg>';(ASSETS/'math2-pie.svg').write_text(svg)
print('Set 2: 15 soalan utama, 26 ruang jawapan, 50 markah; semua soalan baharu.')
