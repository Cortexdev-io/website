(function(){
if(document.documentElement.classList.contains('rm'))return;
var IO='IntersectionObserver' in window;
[].forEach.call(document.querySelectorAll('.flow-fig'),function(fig){
var fx=fig.querySelector('.fx'),ctl=fig.querySelector('.fl-ctl'),bp=ctl.querySelector('[data-a=pause]'),br=ctl.querySelector('[data-a=replay]'),
cs=[].map.call(fx.querySelectorAll('[data-v]'),function(e){return{e:e,v:+e.dataset.v,d:+e.dataset.d,s:+e.dataset.s,p:e.dataset.p||''}}),
el=0,last=0,run=false,raf=0,T=6900;
function fmt(v,d){return v.toLocaleString('pt-BR',{minimumFractionDigits:d,maximumFractionDigits:d})}
function paint(t){cs.forEach(function(c){var p=Math.max(0,Math.min((t-c.s)/600,1));c.e.textContent=c.p+fmt(c.v*(1-Math.pow(1-p,3)),c.d)})}
function tick(ts){if(!run)return;el+=ts-last;last=ts;if(el>=T){paint(1e5);run=false;return}paint(el);raf=requestAnimationFrame(tick)}
function go(){run=true;last=performance.now();cancelAnimationFrame(raf);raf=requestAnimationFrame(tick)}
function play(){fx.classList.remove('is-playing','is-paused');void fx.offsetWidth;el=0;bp.textContent='Pausar';paint(0);fx.classList.add('is-playing');go()}
function toggle(){if(fx.classList.contains('is-paused')){fx.classList.remove('is-paused');bp.textContent='Pausar';if(el<T)go()}else{fx.classList.add('is-paused');bp.textContent='Retomar';run=false;cancelAnimationFrame(raf)}}
bp.addEventListener('click',toggle);br.addEventListener('click',play);
ctl.hidden=false;fx.classList.add('armed');paint(0);
if(!IO){play();return}
var o=new IntersectionObserver(function(es){if(es[0].isIntersecting){o.disconnect();play()}},{threshold:.4});o.observe(fx)});
})();
