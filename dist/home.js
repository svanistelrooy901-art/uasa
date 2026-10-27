'use strict';
for(const [subject,key] of [['sains','makmal-uasa-sains6-v1'],['sejarah','makmal-uasa-sejarah6-v1'],['matematik','makmal-uasa-matematik6-v1']]){
 try{const value=JSON.parse(localStorage.getItem(key)||'null');const el=document.getElementById('saved-'+subject);if(value?.version===1&&['exam','result'].includes(value.status))el.textContent=value.status==='exam'?'Ada percubaan untuk disambung. Pemasa terus berjalan.':'Keputusan percubaan terakhir tersedia.';}catch{/* Browsing works even when local storage is unavailable. */}
}
