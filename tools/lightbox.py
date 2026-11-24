# Lightbox para las capturas del portafolio (tocar la imagen la abre en grande).
import re,sys
LB='''<div id="lb" hidden onclick="this.hidden=true"><img alt=""><span>Toca para cerrar</span></div>
<style>#lb{position:fixed;inset:0;z-index:200;background:rgba(5,5,12,.92);display:flex;flex-direction:column;align-items:center;justify-content:center;padding:16px;gap:10px}#lb[hidden]{display:none}#lb img{max-width:100%;max-height:86vh;border-radius:12px;object-fit:contain}#lb span{color:#bbb;font-size:13px}a[data-lb]{cursor:zoom-in}</style>
<script>document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a[data-lb]');if(!a)return;e.preventDefault();var b=document.getElementById('lb');b.querySelector('img').src=a.getAttribute('href');b.hidden=false;});</script>
'''
def fix(s):
    s=re.sub(r'<div class="card rv (d\d)">(\s*<div class="shot"><img src="(img/apps/[^"]+)")',r'<a class="card rv \1" href="\3" data-lb>\2',s)
    # cerrar: el </div> de la tarjeta que sigue a su meta
    s=re.sub(r'(<a class="card rv d\d" href="img/apps/[^"]+" data-lb>.*?<div class="meta"><div><h3>[^<]*</h3><p>.*?</p></div></div>\s*)</div>',r'\1</a>',s,flags=re.S)
    if 'id="lb"' not in s: s=s.replace('</body>',LB+'</body>',1)
    return s
