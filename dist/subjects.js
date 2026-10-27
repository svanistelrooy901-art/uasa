'use strict';
const SUBJECTS={
 sains:{key:'sains',label:'Sains',heading:'Fahami sains.',eyebrow:'SEDIA UNTUK CABARAN SAINS?',store:'makmal-uasa-sains6-v1',filename:'Keputusan_UASA_Sains_T6.json',sections:[{count:10,max:10,title:'10 soalan objektif',desc:'Pilih satu jawapan'},{count:2,max:8,title:'2 soalan berstruktur',desc:'Pilihan & padanan'},{count:4,max:32,title:'4 soalan KPS & aplikasi',desc:'Jawapan bertulis & jadual'}]},
 sejarah:{key:'sejarah',label:'Sejarah',heading:'Kenali kisah negara.',eyebrow:'JEJAK SEJARAH, FAHAMI MALAYSIA',store:'makmal-uasa-sejarah6-v1',filename:'Keputusan_UASA_Sejarah_T6.json',sections:[{count:20,max:20,title:'20 soalan objektif',desc:'Pilih satu jawapan'},{count:4,max:20,title:'4 soalan berstruktur',desc:'Padanan & pilihan jawapan'},{count:2,max:10,title:'2 soalan respons terhad',desc:'Pendapat, kepentingan & huraian'}]},
 matematik:{key:'matematik',label:'Matematik',heading:'Kira dengan yakin.',eyebrow:'FAHAMI LANGKAH, TEMUI JAWAPAN',store:'makmal-uasa-matematik6-v1',filename:'Keputusan_UASA_Matematik_T6.json',sections:[{count:13,max:26,title:'13 soalan respons terhad',desc:'Pengiraan & aplikasi Tahun 6'},{count:2,max:24,title:'2 soalan penyelesaian masalah',desc:'Beberapa bahagian dengan jalan kerja'}]}
};
const BASE_EXAM=SUBJECTS[document.documentElement?.dataset.subject||'sains'];
const IS_MATH_SET2=BASE_EXAM.key==='matematik'&&document.documentElement?.dataset.set==='2';
const EXAM=IS_MATH_SET2?{...BASE_EXAM,setNumber:'02',store:'makmal-uasa-matematik6-set2-v1',filename:'Keputusan_UASA_Matematik_T6_Set2.json'}:{...BASE_EXAM,setNumber:'01'};
