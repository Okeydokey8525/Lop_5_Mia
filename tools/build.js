// Keep browser rendering outside Microsoft Store Python's filesystem redirection.
const {spawnSync}=require('node:child_process'),path=require('node:path');
const ROOT=path.resolve(__dirname,'..'),args=process.argv.slice(2);
const python=process.env.MIA_PYTHON||(process.platform==='win32'?'python':'python3');
for(const [command,argv] of [[python,['-X','utf8',path.join(__dirname,'build.py'),...args]],
  ...args.includes('--standalone')?[]:[[process.execPath,[path.join(__dirname,'render_overviews.js')]]]]){
  const result=spawnSync(command,argv,{cwd:ROOT,stdio:'inherit'});
  if(result.error){console.error(result.error.message);process.exit(1);}
  if(result.status!==0)process.exit(result.status||1);
}
