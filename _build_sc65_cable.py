"""Baut die Landingpages SmartCharge 65 (/smartcharge-65/) und SmartCharge Cable 240 (/kabel-240/).
Design und CSS kommen 1:1 von der SmartCharge-140-Seite (gleiche Produktfamilie), plus ein paar Ergänzungen.
Danach: python3 _build_schema.py (JSON-LD)."""
import pathlib, re

R = pathlib.Path(__file__).parent
SRC = (R / "smartcharge-140/index.html").read_text(encoding="utf-8")
CSS = re.search(r"<style>\n(.*?)</style>", SRC, re.S).group(1)
CSS = re.sub(r'(\.stage\{position:relative;width:100%;aspect-ratio:1/1;overflow:hidden;border-radius:16px;)background:#fff url\("data:[^"]+"\) center/cover no-repeat\}',
             r"\1background:#fff}", CSS)
assert "data:image/jpeg" not in CSS.split(".stage::before")[0].split(".stage{")[1]
CSS = CSS.replace("/* Haut: hell, GREENMNKY-Grün als Akzent (Buttons, Labels), dunkles Grün für Text-Akzente. Das Smart Display ist das Herzstück: Anschlüsse belegen, sehen, was ankommt – live, auf dem Produkt. */",
                  "/* Gleiches Design wie SmartCharge 140 (Produktfamilie): hell, GREENMNKY-Grün als Akzent. */")
EXTRA = """
/* Ergänzungen SmartCharge 65 / Cable 240 */
.stage video.st{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:1}
.stage .real{position:absolute;left:12px;top:12px;background:rgba(14,17,20,.78);color:#fff;padding:6px 10px;border-radius:999px;font-family:var(--mono);font-size:11.5px;letter-spacing:.06em;text-transform:uppercase}
.pc .k{min-width:46px;text-align:center}
.xlink{color:var(--text);font-weight:600;text-decoration-color:var(--green);text-decoration-thickness:2px;text-underline-offset:3px}
"""

ARROW = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
ICON = {
    "bolt": '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
    "screen": '<rect x="3" y="4" width="18" height="16" rx="2.5"/><path d="M7 12h10M7 8h6M7 16h8"/>',
    "weight": '<rect x="4" y="3" width="16" height="18" rx="3"/><path d="M9 21v-4M15 21v-4"/>',
    "box": '<path d="M3 7l9-4 9 4v10l-9 4-9-4z"/><path d="M3 7l9 4 9-4M12 11v10"/>',
    "cable": '<path d="M4 20c4 0 4-8 8-8s4 8 8 8"/><rect x="2" y="4" width="5" height="6" rx="1.5"/><rect x="17" y="4" width="5" height="6" rx="1.5"/><path d="M4.5 10v4M19.5 10v4"/>',
}
def trust(items):
    li = "\n".join(f'      <li><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#5C636B" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON[i]}</svg>{t}</li>' for i, t in items)
    return f'  <div class="trust">\n    <ul>\n{li}\n    </ul>\n  </div>'

PAY = '<div class="pay" aria-label="Zahlungsarten"><span>PayPal</span><span>Apple Pay</span><span>Google Pay</span><span>Klarna</span><span>Kreditkarte</span></div>'
ASSURE = '<ul class="assure">\n            <li>Über 100.000 Bestellungen über greenmnky.de</li>\n            <li>14 Tage Widerruf, 2 Jahre Gewährleistung</li>\n          </ul>'

V65, V140, V240 = "62086485246220", "66075700363532", "66079483592972"

def page(**k):
    return f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{k['title']}</title>
<meta name="description" content="{k['desc']}">
<meta property="og:title" content="{k['og_title']}">
<meta property="og:description" content="{k['og_desc']}">
<meta property="og:type" content="product">
<meta property="og:url" content="https://eazygadgetz.de{k['path']}">
<meta property="og:image" content="https://eazygadgetz.de{k['path']}img/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="1200">
<meta property="og:locale" content="de_DE">
<meta property="og:site_name" content="eazygadgetz">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://eazygadgetz.de{k['path']}img/og.jpg">
<link rel="canonical" href="https://eazygadgetz.de{k['path']}">
<link rel="icon" href="/favicon.png" type="image/png" sizes="256x256">
<link rel="icon" href="/favicon-32.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#F6F7F5">
<link rel="preload" href="fonts/rubik.woff2" as="font" type="font/woff2" crossorigin>
{k['preload']}
<style>
{CSS}{EXTRA}</style>
</head>
<body>

<p class="bar mono">Versand mit DHL aus Deutschland<span class="bar-x"> · Ab 50 € versandkostenfrei</span> · 14 Tage Widerruf</p>

<header class="site">
  <div class="wrap">
    <div class="brand">
      <a class="home" href="/"><img src="/img/mark.png" width="512" height="512" alt="">eazygadgetz</a>
      <a class="logo" href="#top" aria-label="{k['name']}, nach oben"><i aria-hidden="true"></i>{k['logo']}<small>by GREENMNKY</small></a>
    </div>
    <span class="seller mono">Verkauf durch<br>GREENMNKY</span>
    <nav class="nav" aria-label="Seite">
{k['nav']}
    </nav>
    <a class="btn small" href="#kaufen">Kaufen · {k['price']}</a>
  </div>
</header>

<main id="top">
{k['main']}
</main>

<footer>
  <div class="wrap">
    <div>
      <h4>Verkauf und Versand</h4>
      <p>GREENMNKY GmbH · Lindigstraße 1 · 63801 Kleinostheim<br>Telefon +49 6021 43 76 84 0 · b2csupport@greenmnky.de</p>
      <p style="margin-top:10px">{k['footer_links']}</p>
    </div>
    <div>
      <h4>Rechtliches</h4>
      <ul>
        <li><a href="/impressum/">Impressum</a></li>
        <li><a href="/datenschutz/">Datenschutz</a></li>
        <li><a href="https://greenmnky.de/policies/terms-of-service">AGB</a></li>
        <li><a href="https://greenmnky.de/policies/refund-policy">Widerrufsrecht</a></li>
        <li><a href="https://greenmnky.de/policies/shipping-policy">Versand und Zahlung</a></li>
      </ul>
    </div>
    <div class="legal" id="produktsicherheit">
      <p><strong>Hinweise zur Produktsicherheit.</strong> Verantwortlicher Wirtschaftsakteur in der EU: GREENMNKY GmbH, Lindigstraße 1, 63801 Kleinostheim, Deutschland, <a href="mailto:b2csupport@greenmnky.de">b2csupport@greenmnky.de</a>. Weitere Angaben findest du auf dem Typenschild und der Verpackung.</p>
      <p>{k['safety']}</p>
      <p>{k['marks']}</p>
    </div>
  </div>
</footer>

<div class="sticky" id="sticky" aria-hidden="true">
  <img src="{k['sticky_img']}" width="1400" height="1400" alt="">
  <div><b>{k['name']}</b><span id="stickySub">{k['sticky_sub']}</span></div>
  <a class="btn green" id="stickyBuy" href="{k['first_url']}" tabindex="-1">Bestellen</a>
</div>

<script>
(function(){{
  var $=function(id){{return document.getElementById(id)}};
  var eur=function(n){{return n.toFixed(2).replace(".",",")+" €"}};
  var UTM=(function(){{
    try{{var q=new URLSearchParams(location.search),o=new URLSearchParams(),has=false;
      ["utm_source","utm_medium","utm_campaign","utm_content","utm_term","ref","fbclid","ttclid","gclid"].forEach(function(k){{var v=q.get(k);if(v){{o.set(k,v);has=true;}}}});
      if(has)return o.toString();}}catch(e){{}}
    return "utm_source=eazygadgetz&utm_medium=landingpage&utm_campaign={k['campaign']}";
  }})();
  var OPTS={k['opts_js']};
  var opt="{k['opt_default']}";
  function update(){{
    var o=OPTS[opt];
    $("priceMain").textContent=eur(o.total);
    $("priceWas").textContent=o.was?eur(o.was):""; $("priceWas").style.display=o.was?"":"none";
    $("priceSub").textContent=o.sub;
    $("buyLabel").textContent="Jetzt bestellen · "+eur(o.total);
    $("shipLine").textContent=o.ship;
    var url="https://greenmnky.de/cart/"+o.items+"?"+UTM; $("buy").href=url; $("stickyBuy").href=url;
    $("stickySub").textContent=o.label+" · "+eur(o.total);
  }}
  document.querySelectorAll('input[name="opt"]').forEach(function(i){{i.addEventListener("change",function(){{opt=this.value;update()}})}});
  $("buyForm").addEventListener("submit",function(e){{e.preventDefault()}});
  document.querySelectorAll("[data-pick]").forEach(function(b){{b.addEventListener("click",function(){{var v=this.getAttribute("data-pick");var r=document.querySelector('input[name="opt"][value="'+v+'"]');if(r){{r.checked=true;opt=v;update();}}$("kaufen").scrollIntoView({{behavior:"smooth",block:"start"}});}})}});
  var reduce=window.matchMedia&&window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if(reduce){{document.querySelectorAll("video.loop").forEach(function(v){{v.removeAttribute("autoplay");v.pause();v.setAttribute("controls","");}})}}
  var sticky=$("sticky");
  if("IntersectionObserver" in window){{
    new IntersectionObserver(function(entries){{var e=entries[0];var past=!e.isIntersecting&&e.boundingClientRect.top<0;sticky.classList.toggle("show",past);sticky.setAttribute("aria-hidden",String(!past));$("stickyBuy").tabIndex=past?0:-1;}}).observe($("buy"));
  }}
  update();
}})();
</script>
</body>
</html>
"""

def buybox(name, opts, default_label, first_url, price, sub, ship):
    rows = []
    for o in opts:
        tag = f'<span class="tag{" best" if o.get("best") else ""}">{o["tag"]}</span>' if o.get("tag") else ""
        chk = " checked" if o.get("checked") else ""
        rows.append(f'            <div><input type="radio" name="opt" id="o{o["v"]}" value="{o["v"]}"{chk}><label for="o{o["v"]}"><span class="q"><b>{o["b"]}</b><small>{o["s"]}</small></span>{tag}<span class="sum">{o["sum"]}</span></label></div>')
    return f"""    <div class="hero-buy" id="kaufen">
      <form class="buybox" id="buyForm" aria-label="{name} bestellen">
        <p class="stock"><i aria-hidden="true"></i>Auf Lager · Versand mit DHL aus Deutschland</p>
        <div class="price">
          <strong id="priceMain">{price}</strong>
          <s id="priceWas" style="display:none"></s>
          <span class="was" id="priceSub">{sub}</span>
        </div>
        <fieldset>
          <legend>Auswahl</legend>
          <div class="qty">
{chr(10).join(rows)}
          </div>
        </fieldset>
        <div class="cta">
          <a class="btn green" id="buy" href="{first_url}">
            <span id="buyLabel">Jetzt bestellen · {price}</span>
            {ARROW}
          </a>
          <p class="fine" id="shipLine">{ship}</p>
          {PAY}
          {ASSURE}
        </div>
      </form>
    </div>"""

def faq(items):
    return "\n".join(f"      <details><summary>{q}</summary><p>{a}</p></details>" for q, a in items)

def specs(items):
    return "\n".join(f"        <div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in items)

# --------------------------------------------------------------------------------------------
#  SmartCharge 65
# --------------------------------------------------------------------------------------------
U65 = "utm_source=eazygadgetz&amp;utm_medium=landingpage&amp;utm_campaign=smartcharge65"
URL65 = f"https://greenmnky.de/cart/{V65}:1?{U65}"
OPTS65 = ('{"1":{items:"' + V65 + ':1",total:29.95,label:"Nur Ladegerät",sub:"inkl. MwSt., zzgl. 3,30 € Versand",ship:"Weiter zur sicheren Kasse von GREENMNKY. Ab 50 € versandkostenfrei."},'
          '"kabel":{items:"' + V65 + ':1,' + V240 + ':1",total:54.90,label:"Mit Display-Kabel",sub:"inkl. MwSt., versandkostenfrei",ship:"Weiter zur sicheren Kasse von GREENMNKY. Versand mit DHL aus Deutschland, kostenlos."}}')

main65 = f"""<section class="hero" aria-labelledby="h1">
  <div class="wrap">
    <div class="hero-copy">
      <p class="eyebrow mono"><span>65 W über USB-C</span><span>Live-Display</span><span>108 g</span></p>
      <h1 id="h1">Ein Ladegerät.<span class="g">Handy bis Laptop.</span></h1>
      <p class="lead">iPhone, iPad, MacBook Air oder Switch: Der SmartCharge 65 liefert bis zu <b>65 Watt über USB-C</b> und wiegt nur 108 g. Das Display zeigt dir direkt am Netzteil, <b>wie viel gerade ankommt.</b></p>
      <ul class="checks">
        <li>Ersetzt Handy-, Tablet- und Laptop-Netzteil</li>
        <li>Neues MacBook ohne Netzteil im Karton? Der hier lädt es</li>
        <li>Live-Anzeige der Ladeleistung statt Raten</li>
      </ul>
    </div>

    <div class="hero-stage">
      <div class="stage-card">
        <div class="stage">
          <img class="st on" src="img/hero.webp" width="1400" height="1400" fetchpriority="high" decoding="sync" alt="GREENMNKY SmartCharge 65 zweimal: vorn mit Smart Display, dahinter von der Seite mit USB-C-Anschluss und Eurostecker">
        </div>
      </div>
    </div>

{buybox("SmartCharge 65", [
    dict(v="1", b="Nur Ladegerät", s="SmartCharge 65", sum="29,95 €", checked=True),
    dict(v="kabel", b="Mit Display-Kabel", s="+ SmartCharge Cable 240, 1,5 m", tag="versandkostenfrei", best=True, sum="54,90 €"),
], "Nur Ladegerät", URL65, "29,95&nbsp;€", "inkl. MwSt., zzgl. 3,30 € Versand", "Weiter zur sicheren Kasse von GREENMNKY. Ab 50 € versandkostenfrei.")}
  </div>

{trust([("bolt", "65 W über USB-C"), ("screen", "Live-Anzeige der Ladeleistung"), ("weight", "108 g, 42,5 mm breit"), ("box", "Versand aus Deutschland")])}
</section>

<section id="warum" aria-labelledby="h-warum">
  <div class="wrap">
    <div class="sec-head">
      <p class="mono">Warum ein eigenes Ladegerät</p>
      <h2 id="h-warum">Netzteil?<br><span class="g">Nicht im Karton.</span></h2>
      <p>Neue iPhones kommen seit Jahren ohne Netzteil. Seit März 2026 liefert Apple auch neue MacBooks in der EU ohne aus. Das Kabel liegt bei, der Stecker fehlt.</p>
    </div>
    <div class="pains">
      <div class="pain"><p class="was-so">„Neues MacBook ausgepackt: Kabel da, Netzteil nicht. Das originale 70-W-Netzteil kostet bei Apple 65 €.“</p><p class="now"><b>SmartCharge 65:</b> 65 W für 29,95 €, mit Display.</p></div>
      <div class="pain"><p class="was-so">„Neues iPhone, nur ein USB-C-Kabel im Karton. Der alte Würfel aus der Schublade hat USB-A und lädt im Schneckentempo.“</p><p class="now"><b>USB-C mit 65 W:</b> Dein iPhone lädt so schnell, wie es kann.</p></div>
      <div class="pain"><p class="was-so">„In der Tasche: ein Netzteil fürs Handy, eins fürs Tablet, eins für den Laptop.“</p><p class="now"><b>108 g:</b> ein Ladegerät für alles mit USB-C.</p></div>
    </div>
  </div>
</section>

<section id="alltag" aria-labelledby="h-alltag" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head">
      <p class="mono">Im Alltag</p>
      <h2 id="h-alltag">Klein.<br><span class="g">Überall dabei.</span></h2>
    </div>
    <div class="scenes">
      <article class="scene">
        <div class="scene-img"><img src="img/scene-desk.webp" width="1400" height="1400" alt="SmartCharge 65 auf einem hellen Tisch neben Smartphone, Tablet, Kopfhörern und Laptop" loading="lazy"></div>
        <div class="scene-copy">
          <p class="mono">Schreibtisch</p>
          <h3>Erst das Handy.<br>Dann der Laptop.</h3>
          <p>Morgens das iPhone, mittags das iPad, abends das MacBook: Der SmartCharge 65 erkennt das angeschlossene Gerät und liefert genau die Leistung, die es annimmt.</p>
          <ul class="devs"><li>iPhone</li><li>iPad</li><li>MacBook Air</li><li>Kopfhörer</li></ul>
        </div>
      </article>
      <article class="scene flip">
        <div class="scene-img"><img src="img/scene-bag.webp" width="1400" height="1400" alt="SmartCharge 65 auf einem Tisch vor einer Laptoptasche, daneben Trinkflasche, Sonnenbrille und Smartphone" loading="lazy"></div>
        <div class="scene-copy">
          <p class="mono">Unterwegs</p>
          <h3>108 Gramm.<br>Passt in jede Tasche.</h3>
          <p>42,5 mm breit und stark genug für den Laptop. Ab in den Rucksack, ins Handgepäck oder ins Hotel – ein Ladegerät statt drei.</p>
          <ul class="devs"><li>Rucksack</li><li>Büro</li><li>Hotel</li></ul>
        </div>
      </article>
      <article class="scene">
        <div class="scene-img"><img src="img/scene-all.webp" width="1400" height="1400" alt="SmartCharge 65 vor Tablet, Smartphone und Spielkonsole" loading="lazy"></div>
        <div class="scene-copy">
          <p class="mono">Allrounder</p>
          <h3>Switch, Tablet,<br>Kopfhörer.</h3>
          <p>Alles mit USB-C lädt hier: Nintendo Switch, Galaxy-Tablet, Kopfhörer, Powerbank. iPhones mit Lightning lädst du mit einem USB-C-auf-Lightning-Kabel.</p>
          <ul class="devs"><li>Switch</li><li>Tablet</li><li>Powerbank</li></ul>
        </div>
      </article>
    </div>
    <div class="mid-cta">
      <p><b>29,95 €</b> · mit Display-Kabel <b>54,90 €</b> und versandkostenfrei</p>
      <a class="btn green" href="#kaufen">Jetzt bestellen {ARROW}</a>
    </div>
  </div>
</section>

<section id="display" aria-labelledby="h-disp" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head">
      <p class="mono">Das Smart Display</p>
      <h2 id="h-disp">Du siehst,<br><span class="g">was ankommt.</span></h2>
      <p>Lädt dein Gerät gerade mit 18 Watt oder mit 60? Das Display zeigt die aktuelle Ladeleistung direkt am Netzteil.</p>
    </div>
    <div class="ports-sec">
      <div class="tile"><img src="img/display.webp" width="1400" height="1400" alt="SmartCharge 65 auf einem dunklen Sockel, das Display leuchtet" loading="lazy"></div>
      <div class="plist">
        <div class="pc"><span class="k">01</span><span><b>Schnell oder langsam?</b><span>Die Zahl zeigt sofort, ob gerade Schnellladen läuft.</span></span><span class="w"></span></div>
        <div class="pc"><span class="k">02</span><span><b>Kabel-Check</b><span>Bleibt die Leistung niedrig, bremst oft das Kabel. Tauschen, ablesen, fertig.</span></span><span class="w"></span></div>
        <div class="pc"><span class="k">03</span><span><b>Akku fast voll</b><span>Gegen Ende sinkt die Leistung. Das ist normal und schont den Akku.</span></span><span class="w"></span></div>
        <p class="fine">Abbildungen sind Produktbilder, der Display-Inhalt ist beispielhaft.</p>
      </div>
    </div>
  </div>
</section>

<section id="vergleich" aria-labelledby="h-cmp" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head">
      <p class="mono">Vergleich</p>
      <h2 id="h-cmp">Warum nicht<br><span class="g">das Original?</span></h2>
      <p>Apples 70-W-Netzteil hat 5 Watt mehr. Dafür kostet es mehr als das Doppelte und zeigt dir nicht, was ankommt.</p>
    </div>
    <div class="cmp-wrap">
      <table class="cmp">
        <thead><tr><th scope="col"><span class="sr">Merkmal</span></th><th scope="col" class="us">SmartCharge 65</th><th scope="col">Original-Netzteil 70 W<small>Apple</small></th></tr></thead>
        <tbody>
          <tr><th scope="row">Max. Leistung</th><td class="us">65 W</td><td>70 W</td></tr>
          <tr><th scope="row">Anschluss</th><td class="us">1× USB-C</td><td>1× USB-C</td></tr>
          <tr><th scope="row">Lädt iPhone, iPad, MacBook Air</th><td class="us"><i class="y">Ja</i></td><td><i class="y">Ja</i></td></tr>
          <tr><th scope="row">Live-Anzeige der Ladeleistung</th><td class="us"><i class="y">Ja</i></td><td><i class="n">Nein</i></td></tr>
          <tr><th scope="row">Preis</th><td class="us"><b>29,95 €</b></td><td>65 € im Apple Store</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section id="kabel" aria-labelledby="h-set" style="padding-top:0">
  <div class="wrap">
    <div class="setbox">
      <div class="set-vis" aria-hidden="true">
        <img class="set-charger" src="img/front.webp" width="1400" height="1400" alt="">
        <img class="set-cable" src="/kabel-240/img/cable-coil.webp" width="1400" height="1400" alt="">
        <span class="plus">+</span>
      </div>
      <div class="set-copy">
        <p class="mono">Passendes Kabel</p>
        <h2 id="h-set">Mit Display-Kabel.<br><span class="g">Versand gratis.</span></h2>
        <p>Für die vollen 65 W braucht es ein Kabel, das mehr als 3 A schafft – viele mitgelieferte Kabel hören bei 60 W auf. Das <b>SmartCharge Cable 240</b> lässt bis zu 240 W durch und zeigt im Stecker Watt, Volt und Ampere. Zusammen liegst du über 50 €, der Versand ist dann kostenlos.</p>
        <div class="set-compare">
          <div class="sc"><span class="mono">Nur Ladegerät</span><strong>29,95 €</strong><small>zzgl. 3,30 € Versand</small></div>
          <div class="sc best"><span class="mono">Mit Kabel</span><strong>54,90 €</strong><small>versandkostenfrei</small></div>
        </div>
        <button class="btn green" type="button" data-pick="kabel">Mit Kabel bestellen · 54,90 € {ARROW}</button>
        <p class="fine"><a class="xlink" href="/kabel-240/">Mehr zum SmartCharge Cable 240</a></p>
      </div>
    </div>
  </div>
</section>

<section aria-labelledby="h-size" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head">
      <p class="mono">Größe &amp; Lieferumfang</p>
      <h2 id="h-size">Klein.<br><span class="g">Trotzdem 65 W.</span></h2>
    </div>
    <div class="sizes">
      <div class="sz">
        <div class="tile"><img src="img/back.webp" width="1400" height="1400" alt="SmartCharge 65 von der Seite: USB-C-Anschluss mit Aufdruck PD 65W, GREENMNKY-Schriftzug und Eurostecker" loading="lazy"></div>
        <p>80 × 42,5 × 42,5 mm und 108 g. Der USB-C-Anschluss sitzt an der Seite, das Display vorn, der Eurostecker hinten.</p>
      </div>
      <div style="display:grid;gap:18px">
        <div class="inbox">
          <h3>Im Paket</h3>
          <ul>
            <li><b>1×</b>SmartCharge 65 mit Eurostecker (passt in Schuko-Steckdosen)</li>
          </ul>
          <p class="fine">Für die vollen 65 W: ein USB-C-Kabel mit 5 A, zum Beispiel das <a href="/kabel-240/">SmartCharge Cable 240</a>.</p>
        </div>
        <div class="inbox">
          <h3>Passt zu</h3>
          <ul class="plain"><li>MacBook Air, MacBook Neo und viele USB-C-Laptops (Power Delivery)</li><li>iPad, iPhone ab iPhone 15, iPhones mit Lightning per USB-C-auf-Lightning-Kabel</li><li>Samsung Galaxy S24 bis S26</li><li>Nintendo Switch, Kopfhörer, Powerbanks</li></ul>
        </div>
      </div>
    </div>
  </div>
</section>

<section id="technik" aria-labelledby="h-specs" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head">
      <p class="mono">Technik</p>
      <h2 id="h-specs">Alle Daten.</h2>
    </div>
    <div class="specs">
      <dl class="spec-list">
{specs([
    ("Leistung", "65 W max. (GaN)"),
    ("USB-C", "5 V⎓3 A · 9 V⎓3 A · 15 V⎓3 A · 20 V⎓3,25 A (USB Power Delivery)"),
    ("Eingang", "110–240 V ~ 50/60 Hz, 1,5 A"),
    ("Display", "Smart Display, zeigt die aktuelle Ladeleistung"),
    ("Anschluss", "1× USB-C"),
    ("Stecker", "Eurostecker"),
    ("Gehäuse", "Flammhemmendes ABS + PC, Laser-Gravur"),
    ("Maße", "80 × 42,5 × 42,5 mm"),
    ("Gewicht", "108 g"),
    ("Artikel", "CHA.GWT.C65 · EAN 4251772541826"),
])}
      </dl>
      <div class="box">
        <h3>Prüfzeichen</h3>
        <ul><li>CE, RoHS</li><li>Gehäuse aus flammhemmendem Material</li></ul>
        <h3 style="margin-top:12px">Sicher kaufen</h3>
        <ul><li>Verkauf und Versand durch die GREENMNKY GmbH, Deutschland</li><li>14 Tage Widerrufsrecht, 2 Jahre Gewährleistung</li><li>Fragen: <a href="mailto:b2csupport@greenmnky.de">b2csupport@greenmnky.de</a></li></ul>
      </div>
    </div>
  </div>
</section>

<section id="faq" aria-labelledby="h-faq" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head">
      <p class="mono">Fragen</p>
      <h2 id="h-faq">Häufige Fragen.</h2>
    </div>
    <div class="faq">
{faq([
    ("Reicht der SmartCharge 65 für mein MacBook?", 'Für MacBook Air und MacBook Neo ja. Ein MacBook Pro lädt auch, unter voller Last aber langsamer als mit einem stärkeren Netzteil. Für das MacBook Pro 16" oder mehrere Geräte gleichzeitig nimm den <a href="/smartcharge-140/">SmartCharge 140</a>.'),
    ("Lädt er mein iPhone schnell?", "Ja. iPhones ab iPhone 15 laden über USB-C mit der Schnellladeleistung, die sie annehmen. Ältere iPhones mit Lightning brauchen ein USB-C-auf-Lightning-Kabel."),
    ("Kann ich zwei Geräte gleichzeitig laden?", 'Nein, er hat einen USB-C-Anschluss. Für mehrere Geräte auf einmal gibt es den <a href="/smartcharge-140/">SmartCharge 140</a> mit vier Anschlüssen.'),
    ("Was zeigt das Display?", "Die aktuelle Ladeleistung, direkt am Netzteil. Daran siehst du, ob gerade schnell geladen wird, ob ein Kabel bremst oder ob der Akku fast voll ist."),
    ("Welches Kabel brauche ich für die vollen 65 W?", 'Ein USB-C-Kabel, das mehr als 3 A kann (5-A-Kabel, oft als 100 W oder 240 W bezeichnet). Mit einem üblichen 3-A-Kabel sind es bis zu 60 W. Das <a href="/kabel-240/">SmartCharge Cable 240</a> schafft 5 A und zeigt die Werte gleich mit an.'),
    ("Wird er warm?", "Beim Laden mit voller Leistung wird er warm, das ist normal. GaN arbeitet effizienter als klassische Netzteile. Nicht abdecken und nicht in der Tasche betreiben."),
    ("Passt der Stecker in jede Steckdose?", "Es ist ein Eurostecker: Er passt in Schuko-Steckdosen in Deutschland, Österreich und den meisten EU-Ländern. Für UK, USA oder die Schweiz brauchst du einen Reiseadapter."),
    ("Wie schnell kommt meine Bestellung und was kostet der Versand?", "Wir versenden mit DHL aus Deutschland. Unter 50 € kostet der Versand 3,30 €, ab 50 € nichts – mit dem Display-Kabel zusammen bist du drüber. Du hast 14 Tage Widerrufsrecht."),
])}
    </div>
  </div>
</section>

<section class="final" aria-labelledby="h-final">
  <div class="wrap">
    <h2 id="h-final">Ein Ladegerät.<br><span class="g">Alles mit USB-C.</span></h2>
    <p>29,95 €. Mit dem 240-W-Display-Kabel 54,90 € und versandkostenfrei aus Deutschland.</p>
    <a class="btn green" href="#kaufen">Jetzt bestellen
      {ARROW}
    </a>
    <p class="fine">14 Tage Widerruf · 2 Jahre Gewährleistung · Kasse von GREENMNKY, kein Kundenkonto nötig</p>
  </div>
</section>"""

sc65 = page(
    title="SmartCharge 65 – 65W GaN USB-C Ladegerät mit Smart Display | eazygadgetz",
    desc="GREENMNKY SmartCharge 65: 65-W-GaN-Ladegerät mit USB-C (Power Delivery) und Smart Display, das die aktuelle Ladeleistung zeigt. Lädt iPhone, iPad, MacBook Air und viele USB-C-Laptops. 108 g, 29,95 €, Versand aus Deutschland.",
    og_title="SmartCharge 65: Ein Ladegerät. Handy bis Laptop.",
    og_desc="65 W über USB-C, Smart Display, nur 108 g. 29,95 €, Versand mit DHL aus Deutschland. Mit 240-W-Display-Kabel 54,90 € und versandkostenfrei.",
    path="/smartcharge-65/",
    preload='<link rel="preload" href="img/hero.webp" as="image" fetchpriority="high">',
    name="SmartCharge 65", logo="SmartCharge 65", price="29,95 €",
    nav='      <a href="/">Alle Gadgets</a>\n      <a href="#alltag">Alltag</a>\n      <a href="#display">Display</a>\n      <a href="#vergleich">Vergleich</a>\n      <a href="#technik">Technik</a>\n      <a href="#faq">Fragen</a>',
    main=main65,
    footer_links='<a href="/">Alle Gadgets bei eazygadgetz</a> · <a href="/smartcharge-140/">SmartCharge 140</a> · <a href="/kabel-240/">SmartCharge Cable 240</a> · <a href="/ring-ii/">OnCtrl Ring II</a> · <a href="/phototag/">PhotoTag</a>',
    safety="Nur für den Betrieb in trockenen Innenräumen. Nicht abdecken, nicht öffnen, nicht mit beschädigtem Gehäuse verwenden. Elektrogeräte gehören nicht in den Hausmüll, sondern zu einer Sammelstelle.",
    marks="Apple, MacBook, iPad und iPhone sind Marken der Apple Inc. Samsung Galaxy ist eine Marke der Samsung Electronics Co., Ltd. Nintendo Switch ist eine Marke von Nintendo. Die Nennung dient nur dem Hinweis auf die Kompatibilität. Preisangabe zum Apple-Netzteil: Apple Store Deutschland, Stand November 2026.",
    sticky_img="img/front.webp", sticky_sub="Nur Ladegerät · 29,95 €", first_url=URL65,
    campaign="smartcharge65", opts_js=OPTS65, opt_default="1",
)

# --------------------------------------------------------------------------------------------
#  SmartCharge Cable 240
# --------------------------------------------------------------------------------------------
UCB = "utm_source=eazygadgetz&amp;utm_medium=landingpage&amp;utm_campaign=cable240"
URLCB = f"https://greenmnky.de/cart/{V240}:1?{UCB}"
OPTSCB = ('{"1":{items:"' + V240 + ':1",total:24.95,label:"Nur das Kabel",sub:"inkl. MwSt., zzgl. 3,30 € Versand",ship:"Weiter zur sicheren Kasse von GREENMNKY. Ab 50 € versandkostenfrei."},'
          '"sc65":{items:"' + V65 + ':1,' + V240 + ':1",total:54.90,label:"Mit SmartCharge 65",sub:"inkl. MwSt., versandkostenfrei",ship:"Weiter zur sicheren Kasse von GREENMNKY. Versand mit DHL aus Deutschland, kostenlos."},'
          '"sc140":{items:"' + V140 + ':1,' + V240 + ':1",total:69.95,was:84.90,label:"Mit SmartCharge 140",sub:"inkl. MwSt., versandkostenfrei · du sparst 14,95 €",ship:"Weiter zur sicheren Kasse von GREENMNKY. Der Set-Rabatt wird dort automatisch abgezogen."}}')

maincb = f"""<section class="hero" aria-labelledby="h1">
  <div class="wrap">
    <div class="hero-copy">
      <p class="eyebrow mono"><span>240 W · USB PD 3.1</span><span>Watt, Volt, Ampere live</span><span>1,5 m</span></p>
      <h1 id="h1">Ein Kabel,<span class="g">das mitmisst.</span></h1>
      <p class="lead">Das Display im Stecker zeigt dir live <b>Watt, Volt und Ampere</b>. Du siehst sofort, ob dein Laptop wirklich schnell lädt – <b>oder ob Netzteil oder Anschluss bremsen.</b></p>
      <ul class="checks">
        <li>Bis 240 W: genug für jeden USB-C-Laptop und alles darunter</li>
        <li>1,5 m, 48-fach Nylongeflecht, Stecker aus Aluminium</li>
        <li>USB-C auf USB-C: MacBook, iPad, iPhone 15 bis 17, Galaxy, Switch</li>
      </ul>
    </div>

    <div class="hero-stage">
      <div class="stage-card">
        <div class="stage">
          <video class="st loop" autoplay muted loop playsinline preload="auto" poster="img/loop-cable.webp" width="720" height="720" aria-label="Video: Das Kabel steckt in einem iPhone, das Display im Stecker zeigt die Ladeleistung, sie steigt von 36 auf 44 Watt bei 14 Volt"><source src="img/loop-cable.mp4" type="video/mp4"></video>
          <span class="real">Echte Aufnahme</span>
        </div>
      </div>
    </div>

{buybox("SmartCharge Cable 240", [
    dict(v="1", b="Nur das Kabel", s="SmartCharge Cable 240, 1,5 m", sum="24,95 €", checked=True),
    dict(v="sc65", b="Mit SmartCharge 65", s="+ 65-W-Ladegerät mit Display", tag="versandkostenfrei", sum="54,90 €"),
    dict(v="sc140", b="Mit SmartCharge 140", s="+ 140-W-Ladegerät, 4 Anschlüsse", tag="Kabel für 10 €", best=True, sum="69,95 €"),
], "Nur das Kabel", URLCB, "24,95&nbsp;€", "inkl. MwSt., zzgl. 3,30 € Versand", "Weiter zur sicheren Kasse von GREENMNKY. Ab 50 € versandkostenfrei.")}
  </div>

{trust([("bolt", "240 W · 48 V / 5 A"), ("screen", "Watt, Volt, Ampere live"), ("cable", "1,5 m Nylongeflecht"), ("box", "Versand aus Deutschland")])}
</section>

<section id="display" aria-labelledby="h-disp">
  <div class="wrap">
    <div class="sec-head">
      <p class="mono">Das Display im Stecker</p>
      <h2 id="h-disp">Du siehst,<br><span class="g">was ankommt.</span></h2>
      <p>Drei Zahlen, direkt am Gerät. Beide Fotos sind echt, mit dem Handy aufgenommen.</p>
    </div>
    <div class="scenes">
      <article class="scene">
        <div class="scene-img"><img src="img/real-cable-iphone.webp" width="1400" height="1400" alt="SmartCharge Cable 240 steckt in einem iPhone, das Display im Stecker zeigt 44 W, 14 V und 2,9 A" loading="lazy"></div>
        <div class="scene-copy">
          <p class="mono">Echt · am iPhone</p>
          <h3>44 Watt.<br>Läuft schnell.</h3>
          <p>Oben die Leistung, darunter Spannung und Strom: 14 Volt, 2,9 Ampere. Das iPhone lädt gerade schnell.</p>
          <ul class="devs"><li>44 W</li><li>14 V</li><li>2,9 A</li></ul>
        </div>
      </article>
      <article class="scene flip">
        <div class="scene-img"><img src="img/real-cable-mac.webp" width="1400" height="1400" alt="SmartCharge Cable 240 steckt in einem MacBook, das Display zeigt 8,8 W, 20 V und 0,4 A" loading="lazy"></div>
        <div class="scene-copy">
          <p class="mono">Echt · am MacBook</p>
          <h3>8,8 Watt.<br>Fast voll.</h3>
          <p>20 Volt liegen an, aber nur 0,4 Ampere fließen: Das MacBook nimmt gerade wenig, etwa weil der Akku fast voll ist. Bleibt der Wert schon bei leerem Akku so niedrig, liegt es am Netzteil.</p>
          <ul class="devs"><li>8,8 W</li><li>20 V</li><li>0,4 A</li></ul>
        </div>
      </article>
    </div>
    <div class="plist" style="margin-top:18px">
      <div class="pc"><span class="k">W</span><span><b>Watt</b><span>Wie viel Leistung gerade ankommt. Die Zahl, auf die es ankommt.</span></span><span class="w"></span></div>
      <div class="pc"><span class="k">V</span><span><b>Volt</b><span>Die Spannung, die Netzteil und Gerät ausgehandelt haben: meist 5, 9, 15 oder 20 V, je nach Gerät auch dazwischen. 240-W-Laptops gehen bis 48 V.</span></span><span class="w"></span></div>
      <div class="pc"><span class="k">A</span><span><b>Ampere</b><span>Wie viel Strom fließt, bis 5 A. Volt mal Ampere ergibt die Watt.</span></span><span class="w"></span></div>
    </div>
  </div>
</section>

<section id="check" aria-labelledby="h-check" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head">
      <p class="mono">Kabel-Check</p>
      <h2 id="h-check">Lädt langsam?<br><span class="g">Jetzt weißt du, warum.</span></h2>
    </div>
    <div class="pains">
      <div class="pain"><p class="was-so">„Der Laptop hängt am Netzteil und der Akku wird trotzdem leerer.“</p><p class="now"><b>Display ablesen:</b> Kommen nur 20 oder 30 W an, ist das Netzteil zu schwach für den Laptop.</p></div>
      <div class="pain"><p class="was-so">„Drei weiße Netzteile in der Schublade. Welches war das schnelle?“</p><p class="now"><b>Einstecken, ablesen:</b> In Sekunden siehst du, welches Netzteil wie viel liefert.</p></div>
      <div class="pain"><p class="was-so">„Zu Hause lädt das Handy schnell, im Büro dauert es ewig.“</p><p class="now"><b>Das Display zeigt's:</b> welcher Anschluss wie viel hergibt – zu Hause, im Büro, im Zug.</p></div>
    </div>
  </div>
</section>

<section id="einsatz" aria-labelledby="h-use" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head">
      <p class="mono">Passt zu</p>
      <h2 id="h-use">Ein Kabel.<br><span class="g">Für fast alles.</span></h2>
    </div>
    <div class="ports-sec">
      <div class="tile"><img src="img/cable-coil.webp" width="1400" height="1400" alt="SmartCharge Cable 240 aufgerollt: schwarzes Nylongeflecht, zwei USB-C-Stecker aus Aluminium, einer mit Display" loading="lazy"></div>
      <div class="plist">
        <div class="pc"><span class="k">LAPTOP</span><span><b>MacBook Air, MacBook Pro, USB-C-Laptops</b><span>Auch Gaming-Laptops mit 240-W-USB-C-Ladebuchse.</span></span><span class="w">bis 240 W</span></div>
        <div class="pc"><span class="k">HANDY</span><span><b>iPhone 15 bis 17, Samsung Galaxy S24 bis S26</b><span>Und jedes andere Handy mit USB-C.</span></span><span class="w"></span></div>
        <div class="pc"><span class="k">TABLET</span><span><b>iPad mit USB-C, Galaxy Tab</b><span>Schnellladen, wenn Netzteil und Tablet es können.</span></span><span class="w"></span></div>
        <div class="pc"><span class="k">MEHR</span><span><b>Nintendo Switch, Powerbanks, Kopfhörer</b><span>Alles mit USB-C-Buchse.</span></span><span class="w"></span></div>
        <p class="fine">Wie viel tatsächlich fließt, entscheiden Netzteil und Gerät. Das Kabel lässt bis zu 240 W durch.</p>
      </div>
    </div>
  </div>
</section>

<section id="set" aria-labelledby="h-set" style="padding-top:0">
  <div class="wrap">
    <div class="setbox">
      <div class="set-vis" aria-hidden="true">
        <img class="set-charger" src="/smartcharge-140/img/angle.webp" width="1400" height="1400" alt="">
        <img class="set-cable" src="img/cable-coil.webp" width="1400" height="1400" alt="">
        <span class="plus">+</span>
      </div>
      <div class="set-copy">
        <p class="mono">Mit Netzteil</p>
        <h2 id="h-set">Mit SmartCharge 140:<br><span class="g">Kabel für 10 €.</span></h2>
        <p>Liegen der <b>SmartCharge 140</b> und das Cable 240 zusammen im Warenkorb, kostet das Kabel 10 € statt 24,95 €. Zwei Displays: Das Netzteil zeigt, was es abgibt, das Kabel, was am Gerät ankommt. Lieber klein? Mit dem <a class="xlink" href="/smartcharge-65/">SmartCharge 65</a> sind es 54,90 €, versandkostenfrei.</p>
        <div class="set-compare">
          <div class="sc"><span class="mono">Nur Kabel</span><strong>24,95 €</strong><small>zzgl. 3,30 € Versand</small></div>
          <div class="sc best"><span class="mono">Mit SmartCharge 140</span><strong>69,95 €</strong><small><s>84,90 €</s> · Kabel für 10 €</small></div>
        </div>
        <button class="btn green" type="button" data-pick="sc140">Set bestellen · 69,95 € {ARROW}</button>
        <p class="fine">Der Rabatt wird an der Kasse automatisch abgezogen, kein Code nötig. <a class="xlink" href="/smartcharge-140/">Mehr zum SmartCharge 140</a></p>
      </div>
    </div>
  </div>
</section>

<section id="technik" aria-labelledby="h-specs" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head">
      <p class="mono">Technik</p>
      <h2 id="h-specs">Alle Daten.</h2>
    </div>
    <div class="specs">
      <dl class="spec-list">
{specs([
    ("Anschluss", "USB-C auf USB-C"),
    ("Leistung", "bis 240 W (USB Power Delivery 3.1, bis 48 V⎓5 A)"),
    ("Display", "Watt, Volt und Ampere live, im Stecker auf Geräteseite"),
    ("Länge", "1,5 m"),
    ("Kabel", "48-fach Nylongeflecht, flammhemmend"),
    ("Stecker", "Gehäuse aus Aluminium an beiden Enden"),
    ("Funktion", "Laden"),
    ("Artikel", "CHA.GWT.CC240 · EAN 4251772542038"),
])}
      </dl>
      <div class="box">
        <h3>Prüfzeichen</h3>
        <ul><li>CE, UKCA, FCC</li><li>Überwacht laut Hersteller Spannung und Strom</li></ul>
        <h3 style="margin-top:12px">Sicher kaufen</h3>
        <ul><li>Verkauf und Versand durch die GREENMNKY GmbH, Deutschland</li><li>14 Tage Widerrufsrecht, 2 Jahre Gewährleistung</li><li>Fragen: <a href="mailto:b2csupport@greenmnky.de">b2csupport@greenmnky.de</a></li></ul>
      </div>
    </div>
  </div>
</section>

<section id="faq" aria-labelledby="h-faq" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head">
      <p class="mono">Fragen</p>
      <h2 id="h-faq">Häufige Fragen.</h2>
    </div>
    <div class="faq">
{faq([
    ("Brauche ich ein 240-W-Netzteil?", "Nein. Das Kabel lässt bis zu 240 W durch, mehr nicht. Wie viel tatsächlich fließt, entscheiden Netzteil und Gerät: Mit einem 65-W-Netzteil sind es höchstens 65 W – und das Display zeigt dir den echten Wert."),
    ("Lädt mein iPhone damit schneller?", "Das Kabel bremst nicht. Wie schnell dein iPhone lädt, hängt vom Netzteil und vom iPhone ab. In unserer Aufnahme lädt ein iPhone mit 44 W."),
    ("Passt es an ein iPhone mit Lightning?", "Nein, beide Enden sind USB-C. Es passt an iPhones ab iPhone 15 und an alles andere mit USB-C-Buchse."),
    ("Kann ich damit Daten übertragen?", "Es ist fürs Laden gebaut, auf der Verpackung steht als Funktion „Charging“. Für schnelle Datenübertragung, etwa zu externen SSDs oder Monitoren, nimm ein USB-C-Datenkabel."),
    ("Wo sitzt das Display?", "Im Stecker auf der Geräteseite. Du liest die Werte direkt am Laptop oder Handy ab."),
    ("Wie funktioniert „Kabel für 10 €“?", 'Automatisch: Liegen <a href="/smartcharge-140/">SmartCharge 140</a> und Cable 240 zusammen im Warenkorb, zieht die Kasse 14,95 € ab. Kein Code nötig.'),
    ("Wie robust ist das Kabel?", "48-fach Nylongeflecht und Steckergehäuse aus Aluminium an beiden Enden, laut Hersteller flammhemmend, reiß- und abriebfest."),
    ("Wie schnell kommt meine Bestellung und was kostet der Versand?", "Wir versenden mit DHL aus Deutschland. Unter 50 € kostet der Versand 3,30 €, ab 50 € nichts – mit einem SmartCharge-Netzteil zusammen bist du drüber. Du hast 14 Tage Widerrufsrecht."),
])}
    </div>
  </div>
</section>

<section class="final" aria-labelledby="h-final">
  <div class="wrap">
    <h2 id="h-final">Ein Kabel.<br><span class="g">Drei Zahlen.</span></h2>
    <p>24,95 €. Mit dem SmartCharge 140 kostet es nur 10 €.</p>
    <a class="btn green" href="#kaufen">Jetzt bestellen
      {ARROW}
    </a>
    <p class="fine">14 Tage Widerruf · 2 Jahre Gewährleistung · Kasse von GREENMNKY, kein Kundenkonto nötig</p>
  </div>
</section>"""

cable = page(
    title="SmartCharge Cable 240 – 240W USB-C Ladekabel mit Display, 1,5 m | eazygadgetz",
    desc="USB-C-auf-USB-C-Ladekabel mit 240 W (USB PD 3.1) und Display im Stecker, das Watt, Volt und Ampere live zeigt. 1,5 m, Nylongeflecht, Aluminiumstecker. 24,95 €, mit SmartCharge 140 nur 10 €.",
    og_title="SmartCharge Cable 240: Ein Kabel, das mitmisst.",
    og_desc="240 W, Display im Stecker zeigt Watt, Volt und Ampere live. 1,5 m, Nylongeflecht. 24,95 €, mit SmartCharge 140 nur 10 €.",
    path="/kabel-240/",
    preload='<link rel="preload" href="img/loop-cable.webp" as="image" fetchpriority="high">',
    name="SmartCharge Cable 240", logo="Cable 240", price="24,95 €",
    nav='      <a href="/">Alle Gadgets</a>\n      <a href="#display">Display</a>\n      <a href="#einsatz">Passt zu</a>\n      <a href="#set">Mit Netzteil</a>\n      <a href="#technik">Technik</a>\n      <a href="#faq">Fragen</a>',
    main=maincb,
    footer_links='<a href="/">Alle Gadgets bei eazygadgetz</a> · <a href="/smartcharge-140/">SmartCharge 140</a> · <a href="/smartcharge-65/">SmartCharge 65</a> · <a href="/ring-ii/">OnCtrl Ring II</a> · <a href="/phototag/">PhotoTag</a>',
    safety="Nicht knicken, nicht an beschädigten Kabeln weiterladen. Elektrogeräte gehören nicht in den Hausmüll, sondern zu einer Sammelstelle.",
    marks="Apple, MacBook, iPad und iPhone sind Marken der Apple Inc. Samsung Galaxy ist eine Marke der Samsung Electronics Co., Ltd. Nintendo Switch ist eine Marke von Nintendo. Die Nennung dient nur dem Hinweis auf die Kompatibilität.",
    sticky_img="img/cable-coil.webp", sticky_sub="Nur das Kabel · 24,95 €", first_url=URLCB,
    campaign="cable240", opts_js=OPTSCB, opt_default="1",
)

(R / "smartcharge-65/index.html").write_text(sc65, encoding="utf-8")
(R / "kabel-240/index.html").write_text(cable, encoding="utf-8")
for p in ["smartcharge-65/index.html", "kabel-240/index.html"]:
    s = (R / p).read_text(encoding="utf-8")
    css = "".join(re.findall(r"<style[^>]*>(.*?)</style>", s, re.S))
    print(p, len(s) // 1024, "KB, CSS-Regeln:", css.count("}"))
