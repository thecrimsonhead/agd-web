# Zoom de imágenes: cualquier foto que no sea liga se abre en grande al tocarla (24 nov, Alan).
ZOOM = '''<div id="zm" hidden><img alt=""><span>Toca para cerrar</span></div>
<style>#zm{position:fixed;inset:0;z-index:9999;background:rgba(5,5,12,.93);display:flex;flex-direction:column;align-items:center;justify-content:center;padding:16px;gap:10px;cursor:zoom-out}#zm[hidden]{display:none}#zm img{max-width:100%;max-height:86vh;border-radius:12px;object-fit:contain}#zm span{color:#bbb;font:13px sans-serif}img.zz{cursor:zoom-in}</style>
<script>(function(){var z=document.getElementById('zm'),zi=z.querySelector('img');
function ok(i){return !i.closest('a,button,nav,#zm')&&!/\\.svg(\\?|$)/i.test(i.src)&&(i.width>=120||i.height>=120);}
function marca(){document.querySelectorAll('img').forEach(function(i){if(ok(i))i.classList.add('zz');});}
marca();window.addEventListener('load',marca);
document.addEventListener('click',function(e){var i=e.target.closest&&e.target.closest('img.zz');
if(!i){var s=e.target.closest&&e.target.closest('.shot,.ph,figure');i=s&&!s.closest('a')&&s.querySelector('img.zz');}
if(!i)return;e.preventDefault();zi.src=(i.currentSrc||i.src).replace(/([?&]w=)\\d+/,'$11600');z.hidden=false;});
z.addEventListener('click',function(){z.hidden=true;});
document.addEventListener('keydown',function(e){if(e.key==='Escape')z.hidden=true;});})();</script>
'''
def poner(s, lang='es'):
    z = ZOOM if lang == 'es' else ZOOM.replace('Toca para cerrar', 'Tap to close')
    return s if 'id="zm"' in s else s.replace('</body>', z + '</body>', 1)

if __name__ == '__main__':
    import sys
    for p in sys.argv[1:]:
        t = open(p, encoding='utf-8').read(); n = poner(t)
        if n != t: open(p, 'w', encoding='utf-8').write(n); print('ok', p)
