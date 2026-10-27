const fs=require('fs'),vm=require('vm'),assert=require('node:assert/strict');
const saved=new Map([['makmal-uasa-matematik6-v1',JSON.stringify({version:1,status:'result',started:123,answers:{a1:'750000'}})]]);
const app=fs.readFileSync('dist/app.js','utf8').replace("setInterval(tick,1000);document.addEventListener('visibilitychange',()=>{if(!document.hidden)tick();});welcome();",'');
const ctx=vm.createContext({document:{documentElement:{dataset:{subject:'matematik',set:'2'}},querySelector:()=>null},localStorage:{getItem:k=>saved.get(k)||null,setItem:(k,v)=>saved.set(k,v)},Date,setTimeout,console});
const run=s=>vm.runInContext(s,ctx);run(fs.readFileSync('dist/subjects.js','utf8')+'\n'+fs.readFileSync('dist/questions-matematik-set2.js','utf8')+'\n'+app);
assert.equal(run('state'),null);assert.equal(run('STORE'),'makmal-uasa-matematik6-set2-v1');assert.equal(run('EXAM.setNumber'),'02');assert.equal(run('EXAM.filename'),'Keputusan_UASA_Matematik_T6_Set2.json');assert.equal(run('EXAM.key'),'matematik');
run("state={version:1,status:'exam',started:Date.now(),answers:{},workings:{},overrides:{},flags:[],index:0}");
assert.equal(run('QUESTIONS.length'),15);assert.equal(run('fields.length'),26);assert.equal(run('total()'),0);
assert.deepEqual(JSON.parse(run("JSON.stringify(sectionIds.map(s=>fields.filter(f=>f.section===s).reduce((n,f)=>n+f.max,0)))")),[26,24]);
const coverage=JSON.parse(fs.readFileSync('docs/math-set2-coverage.json','utf8'));assert.deepEqual(coverage.topics.map(t=>t.marks),[6,7,6,6,6,6,7,6]);for(const t of coverage.topics)assert.equal(run(`fields.filter(f=>f.topic===${JSON.stringify(t.topic)}).reduce((n,f)=>n+f.max,0)`),t.marks);
// Independent expected answers; do not obtain expected values from the question bank.
const expected={a1:'1600000',a2:'2250000',a3:'5 1/4',a4:'3.24',a5:'144',a6:'100',a7:'12:40',a8a:'21:20',a8b:'06/12/2026',a9:'3',a10:'6.4',a11:'135',a12:'18',a13:'8',b1a:'3600000',b1b:'900000',b1c:'5.50',b1d:'20:25',b1e:'200',b2ai:'7.2',b2aii:'24',b2b:'45',b2c:'45',b2di:'180',b2dii:'pasti',b2diii:'Semua bola di dalam beg berwarna kuning.'};
for(const [id,answer]of Object.entries(expected)){run(`state.answers[${JSON.stringify(id)}]=${JSON.stringify(answer)}`);assert.equal(run(`score(fields.find(f=>f.id===${JSON.stringify(id)}))`),run(`fields.find(f=>f.id===${JSON.stringify(id)}).max`),id);}
assert.equal(run('total()'),50);
for(const answer of ['5.25','21/4']){run(`state.answers.a3=${JSON.stringify(answer)}`);assert.equal(run("score(fields.find(f=>f.id==='a3'))"),2);}
run("state.answers.b2diii='Tiada bola warna lain.'");assert.equal(run("autoScore(fields.find(f=>f.id==='b2diii'))"),1);
run("state.answers.b2diii='Ada bola hijau.'");assert.equal(run("autoScore(fields.find(f=>f.id==='b2diii'))"),0);
run("state.answers.a10='12.8';state.workings.a10='12.8 ÷ 2 = 12.8';state.overrides.a10=1");assert.equal(run("score(fields.find(f=>f.id==='a10'))"),1);
const old=saved.get('makmal-uasa-matematik6-v1');run('persist()');assert.equal(saved.get('makmal-uasa-matematik6-v1'),old);assert.ok(saved.has('makmal-uasa-matematik6-set2-v1'));
const q1=JSON.parse(fs.readFileSync('dist/questions-matematik.js','utf8').replace('const QUESTIONS = ','').trim().replace(/;$/,''));const q2=JSON.parse(run('JSON.stringify(QUESTIONS)'));assert.ok(q2.every((q,i)=>q.intro!==q1[i].intro));for(const q of q2)if(q.image)assert.ok(fs.existsSync('dist/'+q.image));
const html=fs.readFileSync('dist/matematik-set2.html','utf8');assert.ok(html.includes('data-set="2"'));assert.ok(html.includes('questions-matematik-set2.js'));assert.ok(!html.includes('src="questions-matematik.js"'));assert.ok(fs.readFileSync('dist/index.html','utf8').includes('href="matematik-set2.html"'));
console.log('PASS: Set 2 independent answer key, all-new stems, 26/24 format, balanced topics, equivalent fractions/dates, new probability reason, separate attempts/exports, legacy Set 1 preservation, routes and diagrams.');
