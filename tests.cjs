const fs=require('fs'),vm=require('vm'),assert=require('node:assert/strict');
let code=fs.readFileSync('dist/subjects.js','utf8')+'\n'+fs.readFileSync('dist/questions.js','utf8')+'\n'+fs.readFileSync('dist/app.js','utf8');
// Run data and marking functions without browser initialization.
code=code.replace("setInterval(tick,1000);document.addEventListener('visibilitychange',()=>{if(!document.hidden)tick();});welcome();",'');
const ctx=vm.createContext({document:{querySelector:()=>null},localStorage:{getItem:()=>null},Date,console,setTimeout});vm.runInContext(code,ctx);
function run(s){return vm.runInContext(s,ctx);}
run("state={answers:{},overrides:{},status:'exam',started:Date.now()}");
assert.equal(run('fields.reduce((n,f)=>n+f.max,0)'),50);
assert.deepEqual(JSON.parse(run("JSON.stringify(['A','B','C'].map(s=>fields.filter(f=>f.section===s).reduce((n,f)=>n+f.max,0)))")),[10,8,32]);
assert.equal(run('total()'),0);
run("fields.filter(f=>f.type==='choice').forEach(f=>state.answers[f.id]=f.answer)");assert.equal(run("total('A')+total('B')"),18);
run("fields.filter(f=>f.type==='choice').forEach(f=>state.answers[f.id]=(f.answer+1)%f.options.length)");assert.equal(run("total('A')+total('B')"),0);
run("state.answers.c1b=['Ketinggian dari aras laut (m)','Tekanan udara (kPa)','0','100','2 000','80']");assert.equal(run("autoScore(fields.find(f=>f.id==='c1b'))"),2);
run("state.answers.c1b=['Ketinggian (m)','Tekanan (kPa)','2000','80','0','100']");assert.equal(run("autoScore(fields.find(f=>f.id==='c1b'))"),2);
run("state.answers.c1b=['ketinggian','tekanan','0','100','2000','90']");assert.equal(run("autoScore(fields.find(f=>f.id==='c1b'))"),0);
run("state.answers.c3c='Pusat penetasan telur penyu.'");assert.equal(run("autoScore(fields.find(f=>f.id==='c3c'))"),1);
run("state.answers.c3c='Pusat penetasan dan mengawal lampu pantai.'");assert.equal(run("autoScore(fields.find(f=>f.id==='c3c'))"),2);
run("state.answers.c4a='Saya suka sains' ");assert.equal(run("autoScore(fields.find(f=>f.id==='c4a'))"),0);
run("state.answers.c4a='Jambatan Q.'");assert.equal(run("autoScore(fields.find(f=>f.id==='c4a'))"),1);
run("state.overrides.c1a=2");assert.equal(run("score(fields.find(f=>f.id==='c1a'))"),2);
run("state.overrides.c1a=50");assert.equal(run("score(fields.find(f=>f.id==='c1a'))"),0);
assert.equal(run("esc('<img src=x onerror=alert(1)>')"),'&lt;img src=x onerror=alert(1)&gt;');
for(const [p,g] of [[100,'A'],[80,'A'],[79,'B'],[65,'B'],[64,'C'],[50,'C'],[49,'D'],[40,'D'],[39,'E'],[0,'E']])assert.equal(run(`grade(${p})`),g);
let expired=false;ctx.markExpired=()=>expired=true;run("submit=()=>markExpired();state.started=Date.now()-DURATION-1;tick()");assert.ok(expired);
console.log('PASS: 50-mark totals; exact choice marking; blank answers; table marking; distinct written criteria; parent overrides; grade boundaries; HTML escaping; timer expiry.');
