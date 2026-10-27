"""Original Year 6 maths questions, topic weighting and exact SVG diagrams."""
from pathlib import Path
from fractions import Fraction
from collections import Counter
import json,math
ROOT=Path(__file__).resolve().parents[1]
ASSETS=ROOT/'dist/assets';ASSETS.mkdir(exist_ok=True)
T=['Nombor bulat dan operasi asas','Pecahan, perpuluhan dan peratus','Wang','Masa dan waktu','Ukuran dan sukatan','Ruang','Koordinat, nisbah dan kadaran','Pengurusan data dan kebolehjadian']
Q=[]
def field(id,label,answer,max,topic,model,**extra):
 return dict(id=id,type='math',kind=extra.pop('kind','number'),label=label,answer=answer,max=max,topic=T[topic],model=model,**extra)
def group(id,title,intro,fields,**extra):
 Q.append(dict(id=id,section=id[0].upper(),title=title,intro=intro,fields=fields,**extra))
def a(n,topic,prompt,answer,model,**extra):
 group(f'a{n}',f'Soalan {n}',prompt,[field(f'a{n}','Jawapan akhir',answer,2,topic,model,**extra)],topic=T[topic])
a(1,0,'Tukarkan 3/4 juta kepada nombor bulat.',750000,'3/4 × 1 000 000 = 750 000. Kaedah penukaran betul (1), jawapan 750 000 (1).',displayUnit='nombor bulat')
a(2,0,'Cari nilai anu dalam ayat matematik: (4 800 000 − □) ÷ 4 = 1 100 000.',400000,'1 100 000 × 4 = 4 400 000 (1). Anu = 4 800 000 − 4 400 000 = 400 000 (1).',displayUnit='nombor bulat')
a(3,1,'Hitung 2 1/4 ÷ 3/4.',3,'2 1/4 ÷ 3/4 = 9/4 × 4/3 (1) = 3 (1).')
a(4,1,'Hitung 6.72 ÷ 0.8.',8.4,'6.72 ÷ 0.8 = 67.2 ÷ 8 (1) = 8.4 (1).')
a(5,2,'Harga tanda sebuah beg ialah RM240. Diskaun 15% diberikan. Berapakah harga beg selepas diskaun?',204,'Diskaun = 15/100 × RM240 = RM36 (1). Harga selepas diskaun = RM240 − RM36 = RM204 (1).',displayUnit='RM',units=['RM','ringgit'])
a(6,2,'Aina menyimpan RM2 000. Kadar faedah mudah yang diberikan dalam soalan ini ialah 3% setahun. Hitung faedah untuk satu tahun.',60,'Faedah mudah setahun = 3/100 × RM2 000 (1) = RM60 (1). Kadar ini data rekaan untuk latihan.',displayUnit='RM',units=['RM','ringgit'])
a(7,3,'Bandar P menggunakan GMT+8 dan Bandar Q menggunakan GMT+2. Apabila waktu di P ialah 18:15, nyatakan waktu di Q pada hari yang sama dalam format 24 jam.','12:15','Perbezaan masa = 8 − 2 = 6 jam (1). Q lewat 6 jam: 18:15 − 6 jam = 12:15 (1).',kind='time',displayUnit='HH:MM (24 jam)')
group('a8','Soalan 8','Bandar P menggunakan GMT+8 dan Bandar R menggunakan GMT+10. Waktu di P ialah 23:30 pada 12 November 2026. Nyatakan waktu dan tarikh di R.',[
 field('a8a','(a) Waktu di R dalam format 24 jam.','01:30',1,3,'R awal 2 jam. 23:30 + 2 jam = 01:30 pada hari berikutnya (1).',kind='time',displayUnit='HH:MM (24 jam)'),
 field('a8b','(b) Tarikh di R.','13 November 2026',1,3,'13 November 2026 (1). Terima 13/11/2026 atau 13 Nov 2026.',kind='word',accepted=['13 November 2026','13 Nov 2026','13/11/2026','13-11-2026'],displayUnit='hh/bb/tttt')],topic=T[3])
a(9,4,'Wayar seragam sepanjang 2.5 m mempunyai jisim 0.6 kg. Hitung jisim wayar yang sama jenis sepanjang 7.5 m.',1.8,'7.5 ÷ 2.5 = 3 (1). Jisim = 3 × 0.6 kg = 1.8 kg (1).',displayUnit='kg',units=['kg','kilogram'])
a(10,5,'Rajah menunjukkan bulatan berpusat O. Jejari OB ialah 4.5 cm. A, O dan B berada pada satu garis lurus. Berapakah panjang diameter AB?',9,'Diameter = 2 × jejari (1) = 2 × 4.5 cm = 9 cm (1).',displayUnit='cm',units=['cm','sentimeter'])
Q[-1]['image']='assets/math-circle.svg';Q[-1]['imageAlt']='Bulatan berpusat O, dengan A dan B di hujung diameter. Jejari OB 4.5 cm. Rajah tidak mengikut skala.'
a(11,5,'Sebuah heksagon sekata mempunyai jumlah sudut pedalaman 720°. Hitung satu sudut pedalamannya.',120,'Heksagon sekata mempunyai 6 sudut yang sama besar (1). Satu sudut = 720° ÷ 6 = 120° (1).',displayUnit='darjah (°)',units=['°','darjah'])
a(12,6,'Pada peta grid, P berada di (2, 3) dan Q di (7, 3). Skala mengufuk ialah 1 unit mewakili 2 km. Hitung jarak sebenar antara P dengan Q.',10,'Beza koordinat mengufuk = 7 − 2 = 5 unit (1). Jarak = 5 × 2 km = 10 km (1).',displayUnit='km',units=['km','kilometer'])
Q[-1]['image']='assets/math-grid.svg';Q[-1]['imageAlt']='Grid sukuan pertama: P (2,3), Q (7,3). Jarak antara kedua-duanya mengufuk; 1 unit mewakili 2 km.'
a(13,7,'Carta pai menunjukkan aktiviti pilihan 40 orang murid. Sektor Sukan ialah 180°, Seni 90° dan Muzik 90°. Berapakah bilangan murid yang memilih Seni?',10,'Bahagian Seni = 90°/360° = 1/4 (1). Bilangan murid = 1/4 × 40 = 10 orang (1).',displayUnit='orang',units=['orang','murid'])
Q[-1]['image']='assets/math-pie.svg';Q[-1]['imageAlt']='Carta pai: Sukan separuh bulatan (180°), Seni suku bulatan (90°), Muzik suku bulatan (90°). Jumlah 40 murid.'
group('b1','1. Jelajah ilmu dan jualan cenderamata','Jawab semua bahagian. Maklumat setiap bahagian adalah berasingan. Tunjukkan jalan kerja di ruang yang disediakan.',[
 field('b1a','(a) Pusat Sains menerima 1.2 juta pengunjung pada separuh pertama tahun dan 3/4 juta pada separuh kedua. Hitung jumlah pengunjung dalam nombor bulat.',1950000,2,0,'3/4 juta = 0.75 juta; jumlah = 1.2 + 0.75 = 1.95 juta (1) = 1 950 000 pengunjung (1).',displayUnit='orang',units=['orang','pengunjung']),
 field('b1b','(b) Sebuah muzium menerima 0.8 juta pengunjung pada tahun lalu. Tahun ini, bilangannya ialah 125% daripada tahun lalu. Hitung bilangan pengunjung tahun ini dalam nombor bulat.',1000000,3,1,'125% = 1.25 (1). 1.25 × 0.8 juta = 1 juta (1). Jawapan = 1 000 000 pengunjung (1).',displayUnit='orang',units=['orang','pengunjung']),
 field('b1c','(c) Kos sebuah cenderamata ialah RM12. Harga tandanya RM15.90. Selepas rebat RM0.90 diberikan, berapakah untung bagi satu cenderamata?',3,2,2,'Harga jual sebenar = RM15.90 − RM0.90 = RM15 (1). Untung = RM15 − RM12 = RM3 (1).',displayUnit='RM',units=['RM','ringgit']),
 field('b1d','(d) Sebuah penerbangan bertolak dari Bandar P (GMT+8) pada 09:00. Penerbangan mengambil masa 2 jam ke Bandar S (GMT+7). Nyatakan waktu ketibaan di S dalam format 24 jam.','10:00',2,3,'Tiba pada 11:00 mengikut waktu P (1). S lewat 1 jam, maka waktu tempatan ketibaan ialah 10:00 (1).',kind='time',displayUnit='HH:MM (24 jam)'),
 field('b1e','(e) Nisbah bilangan pengunjung dewasa kepada kanak-kanak ialah 2 : 3. Jumlah pengunjung ialah 250 orang. Hitung bilangan kanak-kanak.',150,3,6,'Jumlah bahagian = 2 + 3 = 5 (1). Satu bahagian = 250 ÷ 5 = 50 (1). Kanak-kanak = 3 × 50 = 150 orang (1).',displayUnit='orang',units=['orang','kanak-kanak'])])
group('b2','2. Karnival Matematik','Jawab semua bahagian. Setiap situasi diberi secara berasingan. Data dan kadar dalam soalan ialah rekaan untuk latihan.',[
 field('b2ai','(a)(i) Sebanyak 1.5 L minuman mempunyai jisim 1.2 kg. Pada kadar campuran yang sama, hitung jisim 7.5 L minuman itu.',6,2,4,'Faktor gandaan = 7.5 ÷ 1.5 = 5 (1). Jisim = 5 × 1.2 kg = 6 kg (1).',displayUnit='kg',units=['kg','kilogram']),
 field('b2aii','(a)(ii) Semua 7.5 L minuman itu diisi ke dalam botol 250 mL. Berapakah botol penuh yang diperoleh?',30,2,4,'7.5 L = 7 500 mL (1). Bilangan botol = 7 500 ÷ 250 = 30 botol (1).',displayUnit='botol',units=['botol']),
 field('b2b','(b) Hiasan berbentuk pentagon sekata mempunyai jumlah sudut pedalaman 540°. Hitung satu sudut pedalamannya.',108,2,5,'Pentagon sekata mempunyai 5 sudut sama besar (1). Satu sudut = 540° ÷ 5 = 108° (1).',displayUnit='darjah (°)',units=['°','darjah']),
 field('b2c','(c) Lima tiket berharga RM20. Pada kadar yang sama, berapakah harga lapan tiket?',32,2,6,'Harga satu tiket = RM20 ÷ 5 = RM4 (1). Harga 8 tiket = 8 × RM4 = RM32 (1).',displayUnit='RM',units=['RM','ringgit']),
 field('b2di','(d)(i) Daripada 60 pengunjung, 15 memilih gerai robotik. Hitung sudut sektor Robotik dalam carta pai bagi semua pengunjung.',90,2,7,'Bahagian Robotik = 15/60 = 1/4 (1). Sudut sektor = 1/4 × 360° = 90° (1).',displayUnit='darjah (°)',units=['°','darjah']),
 field('b2dii','(d)(ii) Sebuah kotak hanya mengandungi 5 bola merah dan 3 bola biru. Satu bola diambil tanpa melihat. Nyatakan kebolehjadian mendapat bola hijau. Gunakan istilah yang sesuai.','Mustahil',1,7,'Mustahil (1). Tiada bola hijau dalam kotak.',kind='word',accepted=['mustahil']),
 dict(id='b2diii',type='text',label='(d)(iii) Berikan sebab bagi jawapan (d)(ii).',max=1,topic=T[7],model='Tiada bola hijau dalam kotak / kotak hanya mengandungi bola merah dan biru (1). Terima alasan setara yang betul.',rules=[[['tiada','tidak ada','tidak mempunyai','tidak mengandungi'],['hijau']]],concepts=[['tiada bola hijau']])])
# Independent arithmetic checks for the key.
assert Fraction(9,4)/Fraction(3,4)==3
assert Fraction('6.72')/Fraction('0.8')==Fraction('8.4')
assert Fraction(240)*(1-Fraction(15,100))==204
assert Fraction(2000)*Fraction(3,100)==60
assert Fraction('7.5')/Fraction('2.5')*Fraction('0.6')==Fraction('1.8')
assert Fraction(90,360)*40==10
assert Fraction('1.2')*1000000+Fraction(3,4)*1000000==1950000
assert Fraction(125,100)*800000==1000000
assert Fraction('15.90')-Fraction('0.90')-12==3
assert Fraction(3,5)*250==150
assert Fraction('7.5')/Fraction('1.5')*Fraction('1.2')==6
assert Fraction('7.5')*1000/250==30
assert Fraction(540,5)==108
assert Fraction(20,5)*8==32
assert Fraction(15,60)*360==90
assert len(Q)==15
assert [sum(f['max'] for q in Q if q['section']==s for f in q['fields']) for s in 'AB']==[26,24]
weights=Counter()
for q in Q:
 for f in q['fields']: weights[f['topic']]+=f['max']
assert [weights[t] for t in T]==[6,7,6,6,6,6,7,6],weights
(ROOT/'dist/questions-matematik.js').write_text('const QUESTIONS = '+json.dumps(Q,ensure_ascii=False)+';\n')
(ROOT/'docs/math-coverage.json').write_text(json.dumps(dict(total=50,topics=[dict(topic=t,marks=weights[t]) for t in T]),ensure_ascii=False,indent=2)+'\n')
# Exact repo-native diagrams, no generated factual imagery.
head='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 280" role="img">'
text=lambda x,y,s:f'<text x="{x}" y="{y}" font-family="sans-serif" font-size="15" fill="#183833">{s}</text>'
svg=head+'<rect width="520" height="280" rx="16" fill="#f3f7f1"/><circle cx="260" cy="132" r="95" fill="white" stroke="#115e59" stroke-width="2"/><line x1="165" y1="132" x2="355" y2="132" stroke="#779487" stroke-dasharray="5 4"/><line x1="260" y1="132" x2="355" y2="132" stroke="#115e59" stroke-width="3"/><circle cx="260" cy="132" r="4" fill="#115e59"/>'+text(145,139,'A')+text(366,139,'B')+text(250,155,'O')+text(278,117,'4.5 cm')+text(155,260,'Rajah tidak mengikut skala')+'</svg>'
(ASSETS/'math-circle.svg').write_text(svg)
svg=head+'<rect width="520" height="280" rx="16" fill="#f3f7f1"/>'
for x in range(9):
 xx=65+x*48;svg+=f'<line x1="{xx}" y1="25" x2="{xx}" y2="225" stroke="#d8e2dc"/>'+text(xx-5,247,str(x))
for y in range(5):
 yy=225-y*48;svg+=f'<line x1="65" y1="{yy}" x2="449" y2="{yy}" stroke="#d8e2dc"/>'+text(40,yy+5,str(y))
svg+='<path d="M65 25 V225 H460" fill="none" stroke="#183833" stroke-width="2"/>'+text(470,230,'x')+text(45,18,'y')
for x,label in [(2,'P (2,3)'),(7,'Q (7,3)')]:
 xx=65+x*48;yy=225-3*48;svg+=f'<circle cx="{xx}" cy="{yy}" r="6" fill="#115e59"/>'+text(xx-28,yy-17,label)
svg+='<line x1="161" y1="81" x2="401" y2="81" stroke="#d09a34" stroke-width="3" stroke-dasharray="5 4"/>'+text(145,274,'Skala: 1 unit mewakili 2 km')+'</svg>'
(ASSETS/'math-grid.svg').write_text(svg)
svg=head+'<rect width="520" height="280" rx="16" fill="#f3f7f1"/>'
start=-90
for angle,color in [(180,'#a9cdb9'),(90,'#efc572'),(90,'#aabfdc')]:
 end=start+angle;x1=155+100*math.cos(math.radians(start));y1=137+100*math.sin(math.radians(start));x2=155+100*math.cos(math.radians(end));y2=137+100*math.sin(math.radians(end));svg+=f'<path d="M155 137 L{x1:.4f} {y1:.4f} A100 100 0 0 1 {x2:.4f} {y2:.4f} Z" fill="{color}" stroke="white" stroke-width="2"/>';start=end
for y,label,c in [(65,'Sukan: 180°','#a9cdb9'),(112,'Seni: 90°','#efc572'),(159,'Muzik: 90°','#aabfdc')]:svg+=f'<rect x="290" y="{y-14}" width="17" height="17" rx="3" fill="{c}"/>'+text(320,y,label)
svg+=text(290,219,'Jumlah: 40 murid')+'</svg>';(ASSETS/'math-pie.svg').write_text(svg)
print('Matematik: A26 + B24; lapan topik:',dict(weights))
