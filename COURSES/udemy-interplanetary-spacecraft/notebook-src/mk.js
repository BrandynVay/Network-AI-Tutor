const { chromium } = require('playwright'); const path=require('path');
(async()=>{const b=await chromium.launch(); const p=await b.newPage(); await p.goto('file://'+path.resolve(process.argv[2])); await p.waitForTimeout(500);
await p.pdf({path:process.argv[3],format:'Letter',landscape:true,printBackground:true,margin:{top:0,bottom:0,left:0,right:0}}); await b.close();})();
