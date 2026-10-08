(function(){
var d=document,h=d.documentElement,c=window.CORTEX||{demoPronta:false,urlDemo:"/demo/resultado/"},on=c.demoPronta===true,rm=h.classList.contains('rm'),
sc=d.currentScript,base=sc?new URL('../../',sc.src).href:'/',IO='IntersectionObserver' in window,
$=function(s,r){return[].slice.call((r||d).querySelectorAll(s))};
function f(v,n){return v.toLocaleString('pt-BR',{minimumFractionDigits:n,maximumFractionDigits:n})}
$('[data-demo]').forEach(function(el){el.hidden=(el.getAttribute('data-demo')==='on')!==on});
$('[data-imagem]').forEach(function(el){el.hidden=(el.getAttribute('data-imagem')==='on')!==(c.demoImagem===true)});
if(c.demoImagem===true)$('img[data-demo-img]').forEach(function(i){i.src=base+'assets/img/demo-hero.png'});
$('details.menu a').forEach(function(a){a.addEventListener('click',function(){a.closest('details').removeAttribute('open')})});
var hd=$('header.top')[0],pg=d.createElement('div'),tk=false;pg.id='prog';pg.setAttribute('aria-hidden','true');hd.appendChild(pg);
function onS(){if(tk)return;tk=true;requestAnimationFrame(function(){var y=scrollY,m=h.scrollHeight-innerHeight;hd.classList.toggle('sc',y>4);if(!rm)pg.style.transform='scaleX('+(m>0?Math.min(y/m,1):0)+')';tk=false})}
addEventListener('scroll',onS,{passive:true});onS();
var links=$('nav.main a'),secs=$('main section[id]');
if(IO&&secs.length){var so=new IntersectionObserver(function(es){es.forEach(function(e){if(!e.isIntersecting)return;var k='#'+e.target.id;links.forEach(function(a){var u=a.getAttribute('href');if(u.slice(-k.length)===k)a.setAttribute('aria-current','true');else a.removeAttribute('aria-current')})})},{rootMargin:'-40% 0px -55% 0px'});secs.forEach(function(s){so.observe(s)})}
function count(el,dur,to,n){var t0=null;function s(t){if(t0===null)t0=t;var p=Math.min((t-t0)/dur,1);el.textContent=f(to*(1-Math.pow(1-p,3)),n);if(p<1)requestAnimationFrame(s)}requestAnimationFrame(s)}
if(IO&&!rm){var co=new IntersectionObserver(function(es){es.forEach(function(e){if(!e.isIntersecting)return;co.unobserve(e.target);count(e.target,800,+e.target.getAttribute('data-count'),0)})},{threshold:.6});
$('[data-count]').forEach(function(el){el.textContent='0';co.observe(el)})}
if(IO&&!rm){var ro=new IntersectionObserver(function(es){es.forEach(function(e){if(!e.isIntersecting)return;var el=e.target;ro.unobserve(el);el.classList.add('in','seen');var dl=parseFloat(el.style.transitionDelay)||0;setTimeout(function(){el.classList.remove('rv','in');el.style.transitionDelay=''},600+dl)})},{threshold:.12,rootMargin:'0px 0px -6% 0px'});
$('main .sec-h,main .card,main .steps li,main .flow li,main .strip li,main .sec-box,main .closer,main details.q,main .who>*,main .prev').forEach(function(el){var p=el.parentNode;p._n=p._n||0;el.style.transitionDelay=Math.min(p._n++,6)*70+'ms';el.classList.add('rv');ro.observe(el)});
var fo=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('go');fo.unobserve(e.target)}})},{threshold:.3});$('.dflow').forEach(function(el){fo.observe(el)})}
if(!rm)$('details.q').forEach(function(q){var s=q.firstElementChild;if(q.open)q.classList.add('show');
s.addEventListener('click',function(e){e.preventDefault();if(q.open&&q.classList.contains('show')){q.classList.remove('show');setTimeout(function(){q.open=false},360)}else{q.open=true;requestAnimationFrame(function(){requestAnimationFrame(function(){q.classList.add('show')})})}})});
})();
