const fs=require('fs'),vm=require('vm'),assert=require('node:assert/strict');
const config=fs.readFileSync('dist/subjects.js','utf8'),history=fs.readFileSync('dist/questions-sejarah.js','utf8');
const app=fs.readFileSync('dist/app.js','utf8').replace("setInterval(tick,1000);document.addEventListener('visibilitychange',()=>{if(!document.hidden)tick();});welcome();",'');
const saved=new Map();
const ctx=vm.createContext({document:{documentElement:{dataset:{subject:'sejarah'}},querySelector:()=>null},localStorage:{getItem:k=>saved.get(k)||null,setItem:(k,v)=>saved.set(k,v)},Date,setTimeout,console});
const run=s=>vm.runInContext(s,ctx);run(config+'\n'+history+'\n'+app);
run("state={answers:{},overrides:{},flags:[],status:'exam',version:1,started:Date.now()}");
assert.equal(run('QUESTIONS.length'),26);assert.equal(run('fields.length'),44);
assert.deepEqual(JSON.parse(run("JSON.stringify('ABC'.split('').map(s=>fields.filter(f=>f.section===s).reduce((n,f)=>n+f.max,0)))")),[20,20,10]);
assert.equal(run('total()'),0);assert.equal(run('STORE'),'makmal-uasa-sejarah6-v1');
run('persist()');assert.ok(saved.has('makmal-uasa-sejarah6-v1'));assert.ok(!saved.has('makmal-uasa-sains6-v1'));
run("fields.filter(isChoice).forEach(f=>state.answers[f.id]=f.answer)");assert.equal(run('total()'),40);
run("fields.filter(isChoice).forEach(f=>state.answers[f.id]=(f.answer+1)%f.options.length)");assert.equal(run('total()'),0);
run("state.answers.c1a='Mengeratkan perpaduan dan hubungan muhibah sesama kaum.'");assert.equal(run("autoScore(fields.find(f=>f.id==='c1a'))"),1);
run("state.answers.c1a='Mengeratkan perpaduan. Memupuk sikap hormat.'");assert.equal(run("autoScore(fields.find(f=>f.id==='c1a'))"),2);
run("state.answers.c1b='Mengadakan persembahan tarian. Murid pelbagai kaum bekerjasama. Ini mengeratkan hubungan.'");assert.equal(run("autoScore(fields.find(f=>f.id==='c1b'))"),3);
run("state.answers.c2a='Menarik pelancong dan meningkatkan pelancongan.'");assert.equal(run("autoScore(fields.find(f=>f.id==='c2a'))"),1);
run("state.answers.c2a='Menarik pelancong dan meningkatkan pendapatan peniaga.'");assert.equal(run("autoScore(fields.find(f=>f.id==='c2a'))"),2);
run("state.answers.c2b='Menghasilkan buku skrap. Berkongsi pencapaian atlet dengan rakan. Ini mendorong kami bersikap gigih.'");assert.equal(run("autoScore(fields.find(f=>f.id==='c2b'))"),3);
run("fields.filter(isChoice).forEach(f=>state.answers[f.id]=f.answer)");assert.equal(run('total()'),50);
run('state.overrides.c1a=0');assert.equal(run('total()'),48);
assert.equal(run('grade(total()*2)'),'A');assert.equal(run("copyAnswer(fields.find(f=>f.id==='b1a'))"),'27 Mei 1961');
for(const subject of ['sains','sejarah']){const html=fs.readFileSync('dist/'+subject+'.html','utf8');assert.ok(html.includes('data-subject="'+subject+'"'));assert.ok(html.includes('src="subjects.js"'));}
assert.ok(fs.readFileSync('dist/index.html','utf8').includes('href="sejarah.html"'));
for(const q of JSON.parse(run('JSON.stringify(QUESTIONS)'))){for(const f of q.fields){assert.ok(f.model&&f.max>0);if(f.type==='select'||f.type==='choice')assert.ok(f.answer>=0&&f.answer<f.options.length);}}
console.log('PASS: History 20/20/10 format; all 26 groups reachable; 50 marks; exact objective marking; duplicate concepts; open rubrics; parent override; isolated storage; subject routes.');
