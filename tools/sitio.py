# Genera agdesign.agency (sitio principal de servicios). Uso: python3 tools/sitio.py  (escribe sitio/index.html y sitio/aviso-de-privacidad/)
import os, re, html
D = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(D)
E = html.escape
WA = 'https://wa.me/526635419838'
CAMP = 'https://web.agdesign.agency/'
# portafolio tomado de la campaña (mismas tarjetas)
camp = open(os.path.join(R, 'index.html'), encoding='utf-8').read()
i = camp.index('<div class="work">'); j = camp.index('\n  </div>\n</section>', i)
work = camp[i:j].replace('src="img/apps/', 'src="img/apps/')
SVC = [
  dict(k='web', t='Página web nueva', p='$3,990', pn='campaña, antes $9,990', d='Tu negocio en internet con dominio, hospedaje y 2 correos corporativos el primer año. Lista en 72 horas.',
       inc=['2 páginas y hasta 8 secciones', 'Dominio y hospedaje por 1 año', '2 correos con tu dominio', 'Hecha para celular y Google'],
       pay=CAMP, btn='Ver demos y apartar', tag='Más pedido'),
  dict(k='reno', t='Renovación de sitio', p='$4,000', pn='pago único', d='Si tu sitio es viejo o lento no lo parchamos: lo rehacemos desde cero con diseño actual y lo pasamos a nuestro hospedaje.',
       inc=['Diseño nuevo para celular', 'Migración de tu dominio', 'Textos y fotos acomodados', 'Velocidad y seguridad al día'],
       pay='https://buy.stripe.com/4gM5kC90y3Sj1Du6KxejK09', btn='Renovar mi sitio'),
  dict(k='app', t='Web apps a la medida', p='desde $8,999', pn='pago único', d='Sistemas que tu equipo abre desde el celular o la compu: CRM, reportes de ventas, control de personal y más.',
       inc=['CRM y seguimiento de clientes', 'Tableros de KPIs en tiempo real', 'Gestión de personal y ventas', 'Funciona en cualquier navegador'],
       pay='https://buy.stripe.com/4gMfZggt0ewX95W5GtejK0a', btn='Quiero mi app'),
  dict(k='marca', t='Creación de marca', p='$20,000', pn='pago único', d='Tu marca completa para que te vean profesional en todos lados: del logo a cómo usarlo en redes, papelería y tu local.',
       inc=['Logo y sus versiones', 'Paleta de colores y tipografías', 'Manual de uso de marca', 'Aplicaciones para redes y papelería'],
       pay='https://buy.stripe.com/3cI28q90yewX5TK1qdejK07', btn='Crear mi marca'),
  dict(k='impi', t='Registro de marca', p='$8,000', pn='por clase', d='Protegemos el nombre y logo de tu negocio ante el IMPI para que nadie más los use.',
       inc=['Búsqueda de marcas parecidas', 'Solicitud ante el IMPI', 'Derechos del IMPI incluidos', 'Seguimiento hasta el título'],
       pay='https://buy.stripe.com/bJebJ090ygF50zqfh3ejK08', btn='Registrar mi marca'),
]
ICON = {
 'web': '<rect x="6" y="9" width="36" height="26" rx="4" fill="none" stroke="currentColor" stroke-width="3"/><path d="M6 16h36M18 41h12M24 35v6" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><circle cx="11" cy="12.5" r="1.5" fill="currentColor"/>',
 'reno': '<path d="M38 20a14 14 0 10-1 9" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><path d="M39 10v10H29" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>',
 'app': '<rect x="14" y="5" width="20" height="38" rx="5" fill="none" stroke="currentColor" stroke-width="3"/><path d="M19 30v-5M24 30v-10M29 30v-7" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>',
 'marca': '<path d="M24 6l5 11 12 1-9 8 3 12-11-7-11 7 3-12-9-8 12-1z" fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/>',
 'impi': '<path d="M24 5l15 6v11c0 10-7 17-15 21-8-4-15-11-15-21V11z" fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><path d="M17 24l5 5 9-10" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>',
}
def card(s):
    inc = ''.join(f'<li>{E(x)}</li>' for x in s['inc'])
    tag = f'<span class="tag">{E(s["tag"])}</span>' if s.get('tag') else ''
    return f'''<article class="svc rv {'hot' if s.get('tag') else ''}">{tag}<div class="ic"><svg viewBox="0 0 48 48" aria-hidden="true">{ICON[s['k']]}</svg></div>
<h3>{E(s['t'])}</h3><p>{E(s['d'])}</p><ul>{inc}</ul><div class="pr"><b>{E(s['p'])}</b><span>{E(s['pn'])}</span></div>
<a class="btn" href="{s['pay']}">{E(s['btn'])} &rarr;</a><a class="mini" href="{WA}?text={E('Hola, tengo una duda sobre ' + s['t'].lower())}">Tengo una duda</a></article>'''
FAQ = [('¿Cómo pago?', 'En línea, con tarjeta, desde el botón de cada servicio. La página web de campaña también se puede pagar a 12 meses sin intereses.'),
       ('¿Qué pasa después de pagar?', 'En menos de 24 horas te escribimos por WhatsApp para pedirte lo que necesitamos y darte fechas.'),
       ('¿Dan factura?', 'Sí. Los precios son más IVA si necesitas factura. Después de pagar, pídela por WhatsApp con tus datos fiscales.'),
       ('¿El registro de marca incluye los derechos del IMPI?', 'Sí. Los $8,000 incluyen la búsqueda, la solicitud, los derechos del IMPI de una clase y el seguimiento hasta el título.'),
       ('¿Puedo combinar servicios?', 'Sí. Muchos clientes empiezan con su marca y después hacemos su página o su app con la misma identidad.')]
faq = ''.join(f'<details class="rv"><summary>{E(q)}</summary><p>{E(a)}</p></details>' for q, a in FAQ)
work_css = '''.work{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}@media(max-width:900px){.work{grid-template-columns:1fr 1fr}}@media(max-width:560px){.work{grid-template-columns:1fr}}
.card{display:block;border-radius:13px;overflow:hidden;border:1px solid var(--line);background:var(--card);text-decoration:none;color:#fff;transition:transform .35s,border-color .35s}.card:hover{transform:translateY(-6px);border-color:rgba(204,34,68,.6)}
.card .shot{aspect-ratio:16/10;position:relative;overflow:hidden}.card .shot svg{width:100%;height:100%}.card .meta{display:flex;justify-content:space-between;align-items:center;padding:16px 18px;gap:12px}.card h3{font-size:19px;margin:0}.card p{color:var(--mute);font-size:14px;margin:4px 0 0}
.card .go{flex:none;width:36px;height:36px;border-radius:50%;border:1.5px solid var(--line);display:flex;align-items:center;justify-content:center}.card .go svg{width:16px;height:16px}'''

_ix = camp
_a = _ix.index('<div class="dgrid">') + len('<div class="dgrid">')
_b = _ix.index('</div>\n', _ix.index('</a>', _ix.rindex('class="dcard', _a)))
DEMOS_CARDS = re.sub(r'href="demo/([a-z]+)/"', r'href="https://web.agdesign.agency/demo/\1/" target="_blank" rel="noopener"', _ix[_a:_b])
DEMOS_CSS = open(os.path.join(R, 'tools', 'demos.css'), encoding='utf-8').read()
DEMOS_HTML = '<section id="demos" style="padding-top:20px"><div class="wrap"><div class="cen"><span class="label">Demos por giro</span><h2 class="rv">Mira cómo se vería <span class="g">la página de tu negocio</span></h2><p class="sub rv">12 demos reales, listas para celular. La tuya lleva tu nombre, tus fotos y tus servicios.</p></div><div class="dgrid">' + DEMOS_CARDS + '</div></div></section>\n'
page = f'''<!doctype html>
<html lang="es-MX"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>AGDesign | Diseño y tecnología para negocios en México</title>
<meta name="description" content="Páginas web, renovación de sitios, web apps a la medida, creación y registro de marca. Precios claros y pago en línea.">
<meta property="og:title" content="AGDesign | Diseño y tecnología para negocios"><meta property="og:url" content="https://agdesign.agency/"><meta name="theme-color" content="#080810">
<link rel="icon" href="img/agd-logo.svg"><link rel="canonical" href="https://agdesign.agency/">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700;800&display=swap" rel="stylesheet">
<style>
:root{{--bg:#080810;--card:#12121C;--line:rgba(255,255,255,.09);--mute:#A7A6AD;--rojo:#FF4D6A;--mor:#A575E0;--btn:linear-gradient(135deg,#4F2474,#CC2244);--grad:linear-gradient(90deg,#FF4D6A,#A575E0)}}
*{{box-sizing:border-box}}html{{scroll-behavior:smooth}}body{{margin:0;background:var(--bg);color:#fff;font:400 16px/26px Outfit,system-ui,sans-serif;-webkit-font-smoothing:antialiased;overflow-x:hidden}}
a{{color:inherit}}.wrap{{max-width:1160px;margin:0 auto;padding:0 18px}}
header{{position:sticky;top:0;z-index:30;background:rgba(8,8,16,.78);backdrop-filter:blur(14px);border-bottom:1px solid var(--line)}}header .wrap{{display:flex;align-items:center;justify-content:space-between;height:70px}}
.logo img{{height:40px;width:auto;display:block}}nav{{display:flex;gap:24px;align-items:center;font-weight:600;font-size:15px}}nav a{{text-decoration:none;color:var(--mute)}}nav a:hover{{color:#fff}}@media(max-width:760px){{nav a.l{{display:none}}}}
.btn{{display:inline-flex;align-items:center;justify-content:center;gap:8px;text-decoration:none;font-weight:600;font-size:16px;border-radius:50px;padding:14px 24px;background:var(--btn);color:#fff;box-shadow:0 12px 30px -10px rgba(204,34,68,.6);transition:transform .2s}}.btn:hover{{transform:translateY(-2px)}}
.btn.sm{{padding:10px 18px;font-size:14px}}.btn.gh{{background:transparent;border:1px solid rgba(255,255,255,.22);box-shadow:none}}
.label{{font-size:12px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--mor)}}.g{{background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}}
.hero{{position:relative;padding:70px 0 50px;overflow:hidden}}.hero .wrap{{display:grid;grid-template-columns:1.1fr .9fr;gap:30px;align-items:center}}@media(max-width:860px){{.hero .wrap{{grid-template-columns:1fr}}}}
.hero h1{{font-size:clamp(40px,6.4vw,64px);line-height:1.02;font-weight:800;margin:14px 0 18px;letter-spacing:-.02em}}.hero p{{font-size:18px;line-height:28px;font-weight:300;color:#d9d8de;max-width:560px}}
.ctas{{display:flex;gap:12px;flex-wrap:wrap;margin-top:26px}}.blob{{position:absolute;border-radius:50%;filter:blur(70px);opacity:.35;z-index:-1}}.b1{{width:460px;height:460px;background:#CC2244;right:-120px;top:-80px;animation:mv 14s ease-in-out infinite alternate}}.b2{{width:420px;height:420px;background:#4F2474;left:-140px;bottom:-160px;animation:mv 18s ease-in-out infinite alternate-reverse}}
@keyframes mv{{to{{transform:translate(-60px,50px) scale(1.1)}}}}
.orb{{position:relative;aspect-ratio:1;max-width:440px;margin:0 auto;width:100%}}.orb .core{{position:absolute;inset:30%;border-radius:50%;background:var(--card);border:1px solid var(--line);display:grid;place-items:center;box-shadow:0 0 80px -10px rgba(204,34,68,.5)}}.orb .core img{{width:62%}}
.orb .ring{{position:absolute;inset:4%;border-radius:50%;border:1px dashed rgba(255,255,255,.14);animation:sp 40s linear infinite}}.orb .ring.r2{{inset:16%;animation-duration:28s;animation-direction:reverse}}
.orb .it{{position:absolute;width:64px;height:64px;margin:-32px;border-radius:18px;background:var(--card);border:1px solid var(--line);display:grid;place-items:center;color:var(--rojo);animation:fl 5s ease-in-out infinite}}.orb .it svg{{width:30px;height:30px}}.orb .it span{{position:absolute;top:70px;font-size:12px;color:var(--mute);white-space:nowrap;font-weight:600}}
@keyframes sp{{to{{transform:rotate(360deg)}}}}@keyframes fl{{50%{{transform:translateY(-10px)}}}}
section{{padding:70px 0}}h2{{font-size:clamp(28px,4.4vw,40px);line-height:1.1;font-weight:700;margin:10px 0 14px;letter-spacing:-.01em}}.sub{{color:var(--mute);max-width:640px;font-size:17px}}.cen{{text-align:center}}.cen .sub{{margin:0 auto}}
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:36px}}@media(max-width:980px){{.grid{{grid-template-columns:1fr 1fr}}}}@media(max-width:620px){{.grid{{grid-template-columns:1fr}}}}
.svc{{position:relative;background:var(--card);border:1px solid var(--line);border-radius:13px;padding:26px;display:flex;flex-direction:column;transition:transform .3s,border-color .3s}}.svc:hover{{transform:translateY(-5px);border-color:rgba(204,34,68,.5)}}.svc.hot{{border-color:rgba(204,34,68,.6);background:linear-gradient(180deg,rgba(204,34,68,.10),var(--card) 50%)}}
.svc .tag{{position:absolute;top:18px;right:18px;font-size:12px;font-weight:700;padding:4px 10px;border-radius:50px;background:var(--btn)}}.svc .ic{{width:54px;height:54px;border-radius:14px;background:rgba(204,34,68,.12);color:var(--rojo);display:grid;place-items:center;margin-bottom:16px}}.svc .ic svg{{width:28px;height:28px}}
.svc h3{{font-size:21px;margin:0 0 8px}}.svc p{{color:var(--mute);font-size:15px;line-height:24px;margin:0 0 14px}}.svc ul{{list-style:none;padding:0;margin:0 0 18px;display:grid;gap:8px;font-size:15px}}.svc li{{display:flex;gap:10px}}.svc li:before{{content:"";flex:none;width:18px;height:18px;margin-top:3px;border-radius:50%;background:var(--btn)}}
.svc .pr{{margin-top:auto;display:flex;align-items:baseline;gap:8px;margin-bottom:16px}}.svc .pr b{{font-size:30px;font-weight:800}}.svc .pr span{{color:var(--mute);font-size:14px}}.svc .mini{{text-align:center;font-size:14px;color:var(--mute);margin-top:12px}}
.steps{{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:36px;counter-reset:s}}@media(max-width:760px){{.steps{{grid-template-columns:1fr}}}}.steps div{{background:var(--card);border:1px solid var(--line);border-radius:13px;padding:24px;counter-increment:s}}.steps div:before{{content:"0" counter(s);display:block;font-size:40px;font-weight:800;line-height:1;margin-bottom:12px}}.steps div:nth-child(1):before{{color:#FF4D6A}}.steps div:nth-child(2):before{{color:#D45AA0}}.steps div:nth-child(3):before{{color:#A575E0}}
.steps b{{font-size:19px;display:block;margin-bottom:6px}}.steps p{{color:var(--mute);margin:0;font-size:15px}}
.why{{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:30px}}@media(max-width:900px){{.why{{grid-template-columns:1fr 1fr}}}}.why div{{border-top:2px solid;border-image:var(--grad) 1;padding-top:14px}}.why b{{display:block;font-size:18px;margin-bottom:4px}}.why span{{color:var(--mute);font-size:15px}}
{work_css}
.faq{{max-width:780px;margin:30px auto 0}}.faq details{{background:var(--card);border:1px solid var(--line);border-radius:13px;padding:18px 20px;margin-bottom:10px}}.faq summary{{font-weight:600;font-size:17px;cursor:pointer;list-style:none;display:flex;justify-content:space-between;gap:12px}}.faq summary:after{{content:"+";color:var(--rojo);font-size:22px}}.faq details[open] summary:after{{content:"–"}}.faq p{{color:var(--mute);margin:10px 0 0}}
.final{{text-align:center;border-radius:20px;padding:50px 24px;background:linear-gradient(135deg,rgba(79,36,116,.55),rgba(204,34,68,.45));border:1px solid var(--line)}}.final h2{{margin-top:0}}
footer{{padding:40px 0 60px;color:var(--mute);font-size:14px}}footer .wrap{{display:flex;justify-content:space-between;align-items:center;gap:16px;flex-wrap:wrap}}footer img{{height:34px}}
.rv{{opacity:0;transform:translateY(22px);transition:opacity .7s,transform .7s}}.rv.in{{opacity:1;transform:none}}
.wa{{position:fixed;right:18px;bottom:18px;width:58px;height:58px;border-radius:50%;background:#25D366;display:grid;place-items:center;z-index:40;box-shadow:0 10px 24px -6px rgba(37,211,102,.7)}}
@media(prefers-reduced-motion:reduce){{*{{animation:none!important;transition:none!important}}.rv{{opacity:1;transform:none}}}}
{DEMOS_CSS}</style></head><body>
<header><div class="wrap"><a class="logo" href="#"><img src="img/agd-logo.svg" alt="AGDesign"></a><nav><a class="l" href="#servicios">Servicios</a><a class="l" href="#proyectos">Proyectos</a><a class="l" href="#demos">Demos</a><a class="l" href="#como">Cómo trabajamos</a><a class="btn sm" href="{WA}">WhatsApp</a></nav></div></header>
<div class="hero"><div class="blob b1"></div><div class="blob b2"></div><div class="wrap"><div>
<span class="label rv">Estudio de diseño y tecnología</span><h1 class="rv">Hacemos que tu negocio <span class="g">se vea y venda</span> mejor.</h1>
<p class="rv">Páginas web, sistemas a la medida y marcas para negocios en México. Precios claros, pago en línea y un equipo que te acompaña de principio a fin.</p>
<div class="ctas rv"><a class="btn" href="#servicios">Ver servicios &rarr;</a><a class="btn gh" href="{CAMP}">Página web en 72 h por $3,990</a></div></div>
<div class="orb rv" aria-hidden="true"><div class="ring"></div><div class="ring r2"></div><div class="core"><img src="img/agd-logo.svg" alt=""></div>
''' + ''.join(f'<div class="it" style="left:{x}%;top:{y}%;animation-delay:-{k}s"><svg viewBox="0 0 48 48">{ICON[s["k"]]}</svg><span>{E(s["t"].split(" de ")[0] if s["k"]!="web" else "Páginas web")}</span></div>' for k, (s, (x, y)) in enumerate(zip(SVC, [(50, 6), (93, 38), (78, 88), (22, 88), (7, 38)]))) + f'''</div></div></div>
<section id="servicios"><div class="wrap"><div class="cen"><span class="label">Servicios</span><h2 class="rv">Todo lo que tu negocio necesita, <span class="g">con precio claro</span></h2><p class="sub rv">Eliges, pagas en línea y en menos de 24 horas te escribimos para arrancar. Precios más IVA si necesitas factura.</p></div>
<div class="grid">{''.join(card(s) for s in SVC)}<article class="svc rv" style="justify-content:center;text-align:center"><div class="ic" style="margin:0 auto 16px"><svg viewBox="0 0 48 48"><path d="M10 12h28a4 4 0 014 4v14a4 4 0 01-4 4H22l-8 7v-7h-4a4 4 0 01-4-4V16a4 4 0 014-4z" fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/></svg></div><h3>¿Necesitas otra cosa?</h3><p>Tiendas en línea, automatizaciones, presentaciones o algo a la medida. Platícanos y te decimos cómo lo resolvemos.</p><a class="btn gh" href="{WA}">Escríbenos por WhatsApp</a></article></div></div></section>
<section id="proyectos" style="padding-top:20px"><div class="wrap"><div class="cen"><span class="label">Proyectos</span><h2 class="rv">Lo que hemos construido</h2><p class="sub rv">Páginas, sistemas y marcas para negocios reales.</p></div><div style="margin-top:36px">{work}</div></div></section>
{DEMOS_HTML}<section id="como"><div class="wrap"><div class="cen"><span class="label">Cómo trabajamos</span><h2 class="rv">Sin vueltas, <span class="g">sin juntas eternas</span></h2></div>
<div class="steps"><div class="rv"><b>Eliges y pagas en línea</b><p>Cada servicio tiene su precio y su botón. Sin cotizaciones que tardan semanas.</p></div><div class="rv"><b>Nos cuentas por WhatsApp</b><p>En menos de 24 horas te escribimos para pedirte lo que necesitamos.</p></div><div class="rv"><b>Entregamos y te acompañamos</b><p>Revisas, pides cambios y lo dejamos funcionando. Seguimos contigo después.</p></div></div>
<div class="why"><div class="rv"><b>Socios, no proveedores</b><span>Nos importa que te funcione, no solo entregar.</span></div><div class="rv"><b>Rápido</b><span>Tu página en 72 horas; lo demás, con fechas claras.</span></div><div class="rv"><b>Para celular</b><span>Todo lo diseñamos primero para el teléfono.</span></div><div class="rv"><b>Precios claros</b><span>Lo que ves es lo que pagas.</span></div></div></div></section>
<section style="padding-top:10px"><div class="wrap"><div class="cen"><span class="label">Preguntas frecuentes</span><h2 class="rv">Resolvemos tus dudas</h2></div><div class="faq">{faq}</div></div></section>
<section style="padding-top:10px"><div class="wrap"><div class="final rv"><h2>¿Arrancamos?</h2><p class="sub" style="margin:0 auto 22px;color:#ECEAF2">Escríbenos y te decimos qué te conviene. Si ya sabes qué quieres, elige tu servicio y págalo en línea.</p><a class="btn" href="{WA}">Escríbenos por WhatsApp</a></div></div></section>
<footer><div class="wrap"><img src="img/agd-logo.svg" alt="AGDesign"><span>&copy; 2026 AGDesign. Creado con amor por AGDesign.</span><a href="aviso-de-privacidad/">Aviso de privacidad</a></div></footer>
<a class="wa" href="{WA}" aria-label="WhatsApp"><svg width="30" height="30" viewBox="0 0 24 24" fill="#fff"><path d="M12 2a10 10 0 00-8.6 15.1L2 22l5-1.3A10 10 0 1012 2zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.3-.7-2.8-1.1-4.5-4-4.7-4.2-.1-.2-1.1-1.5-1.1-2.9s.7-2 1-2.3c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.9 2.1c.1.2.1.3 0 .5l-.3.5-.4.4c-.1.2-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.2 1 2.1 1.3 2.4 1.5.3.1.5.1.6-.1l.9-1.1c.2-.3.4-.2.6-.1l2 1c.3.1.5.2.5.3.1.2.1.7-.1 1.4z"/></svg></a>
<script>(function(){{var io=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target)}}}})}},{{threshold:.06}});document.querySelectorAll('.rv').forEach(function(el){{io.observe(el)}});}})();</script>
</body></html>'''
import lightbox
page = lightbox.fix(page)
open(os.path.join(R, 'sitio', 'index.html'), 'w', encoding='utf-8').write(page)
aviso = f'''<!doctype html><html lang="es-MX"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Aviso de privacidad | AGDesign</title>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap" rel="stylesheet"><style>body{{margin:0;background:#080810;color:#ECEAF2;font:300 17px/28px Outfit,sans-serif}}.w{{max-width:760px;margin:0 auto;padding:40px 20px 80px}}h1{{font-weight:700;color:#fff}}h2{{font-weight:600;color:#fff;font-size:20px;margin-top:28px}}a{{color:#FF4D6A}}</style></head><body><div class="w">
<a href="../"><img src="../img/agd-logo.svg" alt="AGDesign" height="40"></a><h1>Aviso de privacidad</h1>
<p>AGDesign, con domicilio en la Ciudad de México, es responsable del tratamiento de los datos personales que nos compartes.</p>
<h2>Qué datos usamos</h2><p>Nombre, nombre de tu negocio, teléfono o WhatsApp, correo electrónico y, si pides factura, tus datos fiscales.</p>
<h2>Para qué los usamos</h2><p>Para hacer el trabajo que contrataste, contactarte por WhatsApp o correo sobre ese trabajo, cobrar y, si lo pides, facturar. No vendemos ni rentamos tus datos.</p>
<h2>Pagos</h2><p>Los pagos los procesan Mercado Pago o Stripe. Nosotros no vemos ni guardamos los datos de tu tarjeta.</p>
<h2>Tus derechos</h2><p>Puedes pedir acceso, corrección, cancelación u oposición al uso de tus datos escribiéndonos por <a href="{WA}">WhatsApp</a>. Te respondemos en un máximo de 20 días hábiles.</p>
<h2>Cambios</h2><p>Si cambiamos este aviso lo publicaremos en esta misma página. Última actualización: noviembre de 2026.</p></div></body></html>'''
os.makedirs(os.path.join(R, 'sitio', 'aviso-de-privacidad'), exist_ok=True)
open(os.path.join(R, 'sitio', 'aviso-de-privacidad', 'index.html'), 'w', encoding='utf-8').write(aviso)
print('ok')
