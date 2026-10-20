// 恋よみ 共通診断エンジン
function initQuiz(cfg){
  var root=document.getElementById(cfg.id);
  var qs=cfg.questions, i=0, total=0, answers=[];
  var html='<div class="bar"><i></i></div>';
  qs.forEach(function(q,idx){
    html+='<div class="q" data-i="'+idx+'"><div class="qnum">Q'+(idx+1)+' / '+qs.length+'</div><div class="qtext">'+q.t+'</div><div class="opts">';
    q.o.forEach(function(o,oi){html+='<button type="button" class="opt" data-p="'+o[1]+'" data-oi="'+oi+'">'+o[0]+'</button>';});
    html+='</div></div>';
  });
  html+='<div class="result"></div>';
  root.innerHTML=html;
  var bar=root.querySelector('.bar i');
  function show(){
    root.querySelectorAll('.q').forEach(function(el){el.classList.remove('active');});
    var el=root.querySelector('.q[data-i="'+i+'"]');
    if(el){el.classList.add('active');bar.style.width=(i/qs.length*100)+'%';}
  }
  root.addEventListener('click',function(e){
    var b=e.target.closest('.opt'); if(!b) return;
    total+=parseInt(b.getAttribute('data-p'),10); answers.push(parseInt(b.getAttribute('data-oi'),10));
    i++;
    if(i<qs.length){show();window.scrollTo({top:root.offsetTop-20,behavior:'smooth'});}
    else finish();
  });
  function finish(){
    bar.style.width='100%';
    root.querySelectorAll('.q').forEach(function(el){el.classList.remove('active');});
    var r=cfg.result(total,answers);
    var cl=document.querySelector('link[rel="canonical"]');
    var url=(cl&&cl.href)?cl.href:location.href.split('#')[0].split('?')[0];
    var text=cfg.shareText(r);
    var x='https://twitter.com/intent/tweet?text='+encodeURIComponent(text+' '+cfg.siteName)+'&url='+encodeURIComponent(url);
    var th='https://www.threads.net/intent/post?text='+encodeURIComponent(text+' '+cfg.siteName+' '+url);
    var line='https://social-plugins.line.me/lineit/share?url='+encodeURIComponent(url)+'&text='+encodeURIComponent(text);
    var res=root.querySelector('.result');
    res.innerHTML=(cfg.scoreLabel?'<div class="score-label">'+cfg.scoreLabel+'</div>':'')+'<div class="score">'+r.score+'</div><div class="rank">'+r.title+'</div>'+r.body+
      '<div class="share"><a href="'+x+'" target="_blank" rel="noopener">Xで結果をシェア</a><a href="'+th+'" target="_blank" rel="noopener">Threadsでシェア</a><a href="'+line+'" target="_blank" rel="noopener">LINEで送る</a><button type="button" class="retry">もう一度診断する</button></div>';
    res.classList.add('active');
    res.querySelector('.retry').addEventListener('click',function(){i=0;total=0;answers=[];res.classList.remove('active');show();});
    window.scrollTo({top:root.offsetTop-20,behavior:'smooth'});
    if(typeof gtag==='function') gtag('event','quiz_result',{quiz:location.pathname, result:r.title});
  }
  show();
}
