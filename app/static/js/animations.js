(function(){
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduce) return;

  // Count-up numbers on dashboard stat boxes
  document.querySelectorAll('.stats b').forEach(function(el){
    var target = parseInt(el.textContent.trim(), 10);
    if (isNaN(target) || target <= 0) return;
    var start = null, dur = 900;
    el.textContent = '0';
    function tick(t){
      if (start === null) start = t;
      var p = Math.min((t - start) / dur, 1);
      el.textContent = Math.round(target * (1 - Math.pow(1 - p, 3)));
      if (p < 1) requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  });

  // Reveal panels as they scroll into view
  if (!('IntersectionObserver' in window)) return;
  var io = new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      if (e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); }
    });
  }, {threshold: 0.12});
  document.querySelectorAll('.panel, .verify').forEach(function(el){
    el.classList.add('js-reveal'); io.observe(el);
  });
})();
