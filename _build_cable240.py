"""Baut die Landingpage SmartCharge Cable 240 (/kabel-240/).
Gemeinsame Bausteine (page, buybox, trust, faq, specs) und das Grund-Design kommen aus _build_sc65_cable.py.
Bilder: generiert mit den Hersteller-Renderings und einem Foto des leuchtenden Displays als Vorlage (img/k-*.webp).
Danach: python3 _build_schema.py (JSON-LD)."""
import re
from _build_sc65_cable import R, page, buybox, trust, faq, specs, ARROW, V65, V140, V240

UCB = "utm_source=eazygadgetz&amp;utm_medium=landingpage&amp;utm_campaign=cable240"
URLCB = f"https://greenmnky.de/cart/{V240}:1?{UCB}"
OPTSCB = ('{"1":{items:"' + V240 + ':1",total:24.95,label:"Nur das Kabel",sub:"inkl. MwSt., zzgl. 3,30 € Versand",ship:"Weiter zur sicheren Kasse von GREENMNKY. Ab 50 € versandkostenfrei."},'
          '"sc65":{items:"' + V65 + ':1,' + V240 + ':1",total:54.90,label:"Mit SmartCharge 65",sub:"inkl. MwSt., versandkostenfrei",ship:"Weiter zur sicheren Kasse von GREENMNKY. Versand mit DHL aus Deutschland, kostenlos."},'
          '"sc140":{items:"' + V140 + ':1,' + V240 + ':1",total:69.95,was:84.90,label:"Mit SmartCharge 140",sub:"inkl. MwSt., versandkostenfrei · du sparst 14,95 €",ship:"Weiter zur sicheren Kasse von GREENMNKY. Der Set-Rabatt wird dort automatisch abgezogen."}}')

CB_CSS = """
/* Cable 240: Fotos statt Freisteller */
.stage-card.photo{padding:0;background:#0B0D10;border-color:rgba(10,18,12,.16);overflow:hidden}
.stage-card.photo .stage{aspect-ratio:4/5;border-radius:0;background:#0B0D10}
.stage-card.photo .stage img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.chip{position:absolute;left:14px;bottom:14px;display:inline-flex;align-items:center;gap:8px;background:rgba(11,13,16,.72);-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px);color:#fff;padding:8px 12px;border-radius:999px;font-family:var(--mono);font-size:11.5px;letter-spacing:.06em;text-transform:uppercase}
.chip i{width:8px;height:8px;border-radius:50%;background:var(--green);box-shadow:0 0 10px var(--green)}
.wide-shot{margin:0;border-radius:var(--radius);overflow:hidden;background:#0B0D10;border:1px solid var(--line);box-shadow:0 30px 70px rgba(10,18,12,.12)}
.wide-shot img{width:100%;aspect-ratio:3/2;object-fit:cover}
.wva-grid{display:grid;grid-template-columns:1fr;gap:12px;margin-top:14px}
.wva{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:22px 22px 24px;display:grid;gap:8px;align-content:start}
.wva .u{font-family:var(--mono);font-size:30px;font-weight:500;line-height:1;color:var(--green-text)}
.wva h3{font-size:20px}
.wva p{color:var(--muted);font-size:15.5px}
.note{margin-top:14px;font-size:13px;color:var(--muted)}
.pain h3{font-size:21px;line-height:1.15}
.pain .ic{width:44px;height:44px;border-radius:12px;background:rgba(0,211,50,.14);display:grid;place-items:center}
.dtile img{aspect-ratio:4/5}
.scene-img.photo{aspect-ratio:auto;background:#0B0D10}
.scene-copy .checks{margin-top:6px}
.set-vis.photo{aspect-ratio:4/3;background:#0B0D10;overflow:hidden}
.set-vis.photo img{position:static;width:100%;height:100%;object-fit:cover}
.cmp{min-width:0}
@media (max-width:640px){ .cmp{font-size:13.5px} .cmp th,.cmp td{padding:12px 10px;-webkit-hyphens:auto;hyphens:auto} .cmp tbody th{width:36%} .cmp thead th{font-size:10.5px;letter-spacing:.04em;-webkit-hyphens:manual;hyphens:manual} }
@media (max-width:380px){ .cmp th,.cmp td{padding:11px 7px} .cmp{font-size:13px} }
@media (min-width:760px){ .wva-grid{grid-template-columns:repeat(3,1fr)} }
@media (min-width:960px){ .scene-img.photo{min-height:100%} .set-vis.photo{aspect-ratio:auto;align-self:stretch;min-height:340px} }
"""

def ic(path):
    return f'<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#00B82C" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{path}</svg>'

IC_BOLT = ic('<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>')
IC_PLUG = ic('<path d="M9 2v6M15 2v6M7 8h10v4a5 5 0 0 1-10 0z"/><path d="M12 17v5"/>')
IC_DESK = ic('<path d="M3 21h18M5 21V7l7-4 7 4v14M9 21v-4h6v4"/>')

main = f"""<section class="hero" aria-labelledby="h1">
  <div class="wrap">
    <div class="hero-copy">
      <p class="eyebrow mono"><span>240 W · USB PD 3.1</span><span>Display im Stecker</span><span>1,5 m Nylon</span></p>
      <h1 id="h1">240 Watt.<span class="g">Live im Blick.</span></h1>
      <p class="lead">Das USB-C-Kabel mit Display im Stecker zeigt dir in Echtzeit <b>Watt, Volt und Ampere</b>. So siehst du sofort, ob dein Laptop, Handy oder Tablet <b>wirklich schnell lädt</b> – oder ob das Netzteil bremst.</p>
      <ul class="checks">
        <li>Bis 240 W: genug für jeden USB-C-Laptop und alles darunter</li>
        <li>Schwaches Netzteil? Erkennst du auf einen Blick</li>
        <li>1,5 m, 48-fach Nylongeflecht, Stecker aus Aluminium</li>
        <li>Für MacBook, iPhone 15 bis 17, iPad, Galaxy und alles mit USB-C</li>
      </ul>
    </div>

    <div class="hero-stage">
      <div class="stage-card photo">
        <div class="stage">
          <img src="img/k-hero-1200.webp" srcset="img/k-hero-720.webp 720w, img/k-hero-1200.webp 1200w" sizes="(min-width:960px) 560px, calc(100vw - 40px)" width="1200" height="1490" alt="SmartCharge Cable 240 steckt seitlich in einem Laptop, das Display im Stecker zeigt 96 W, 20 V und 4,8 A" fetchpriority="high">
          <span class="chip"><i aria-hidden="true"></i>Live: Watt · Volt · Ampere</span>
        </div>
      </div>
    </div>

{buybox("SmartCharge Cable 240", [
    dict(v="1", b="Nur das Kabel", s="SmartCharge Cable 240, 1,5 m", sum="24,95 €", checked=True),
    dict(v="sc65", b="Mit SmartCharge 65", s="+ 65-W-Ladegerät mit Display", tag="versandkostenfrei", sum="54,90 €"),
    dict(v="sc140", b="Mit SmartCharge 140", s="+ 140-W-Ladegerät, 4 Anschlüsse", tag="Kabel nur 10 €", best=True, sum="69,95 €"),
], "Nur das Kabel", URLCB, "24,95&nbsp;€", "inkl. MwSt., zzgl. 3,30 € Versand", "Weiter zur sicheren Kasse von GREENMNKY. Ab 50 € versandkostenfrei.")}
  </div>

{trust([("bolt", "240&nbsp;W · 48&nbsp;V / 5&nbsp;A"), ("screen", "Watt, Volt, Ampere live"), ("cable", "1,5 m Nylongeflecht"), ("box", "Versand aus Deutschland")])}
</section>

<section id="display" aria-labelledby="h-disp">
  <div class="wrap">
    <div class="sec-head">
      <p class="mono">Das Display im Stecker</p>
      <h2 id="h-disp">Drei Zahlen.<br><span class="g">Kein Rätselraten.</span></h2>
      <p>Einstecken und ablesen, was wirklich ankommt – direkt am Gerät, ohne App und ohne Messgerät.</p>
    </div>
    <figure class="wide-shot">
      <img src="img/k-display.webp" srcset="img/k-display-900.webp 900w, img/k-display.webp 1600w" sizes="(min-width:1240px) 1160px, calc(100vw - 40px)" width="1600" height="1073" alt="Nahaufnahme: Das Display im Stecker zeigt 65 W, 20 V und 3,2 A" loading="lazy">
    </figure>
    <div class="wva-grid">
      <div class="wva"><span class="u">W</span><h3>Watt: was ankommt</h3><p>Die Ladeleistung in diesem Moment. Daran siehst du, wie schnell gerade geladen wird.</p></div>
      <div class="wva"><span class="u">V</span><h3>Volt: was ausgehandelt ist</h3><p>Die Spannung, auf die sich Netzteil und Gerät geeinigt haben: meist 5, 9, 15 oder 20 V, bei 240-W-Laptops bis 48 V.</p></div>
      <div class="wva"><span class="u">A</span><h3>Ampere: wie viel fließt</h3><p>Der Strom, bis 5 A. Volt mal Ampere ergibt die Watt.</p></div>
    </div>
    <p class="note">Abbildungen beispielhaft. Welche Werte du siehst, hängt von Netzteil und Gerät ab.</p>
  </div>
</section>

<section id="check" aria-labelledby="h-check" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head">
      <p class="mono">Kabel-Check</p>
      <h2 id="h-check">Lädt langsam?<br><span class="g">Jetzt weißt du, warum.</span></h2>
    </div>
    <div class="pains">
      <div class="pain"><span class="ic">{IC_BOLT}</span><h3>Der Laptop lädt nicht richtig?</h3><p class="now">Zeigt das Display nur 20 oder 30 W, ist das Netzteil zu schwach für deinen Laptop.</p></div>
      <div class="pain"><span class="ic">{IC_PLUG}</span><h3>Welches Netzteil ist das schnelle?</h3><p class="now">Einstecken, ablesen: In Sekunden siehst du, welches Netzteil wie viel liefert.</p></div>
      <div class="pain"><span class="ic">{IC_DESK}</span><h3>Im Büro dauert es ewig?</h3><p class="now">Das Display zeigt, welcher Anschluss wie viel hergibt – zu Hause, im Büro, im Zug.</p></div>
    </div>
  </div>
</section>

<section id="einsatz" aria-labelledby="h-use" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head">
      <p class="mono">Passt zu</p>
      <h2 id="h-use">Ein Kabel.<br><span class="g">Für alles mit USB-C.</span></h2>
    </div>
    <div class="dtiles">
      <figure class="dtile"><img src="img/k-laptop.webp" width="800" height="993" alt="Laptop auf einem Holzschreibtisch lädt über das SmartCharge Cable 240, das Display zeigt 100 W, 20 V und 5 A" loading="lazy"><figcaption><b>Laptop</b><span>MacBook Air, MacBook Pro und USB-C-Laptops, bis 240 W – auch Gaming-Laptops mit USB-C-Ladebuchse.</span></figcaption></figure>
      <figure class="dtile"><img src="img/k-phone.webp" width="800" height="993" alt="Smartphone auf einem Nachttisch lädt über das SmartCharge Cable 240, das Display zeigt 27 W, 9 V und 3 A" loading="lazy"><figcaption><b>Handy</b><span>iPhone 15 bis 17, Samsung Galaxy und jedes andere Handy mit USB-C.</span></figcaption></figure>
      <figure class="dtile"><img src="img/k-tablet.webp" width="800" height="993" alt="Tablet auf dem Sofa lädt über das SmartCharge Cable 240, das Display zeigt 30 W, 15 V und 2 A" loading="lazy"><figcaption><b>Tablet</b><span>iPad mit USB-C, Galaxy Tab und Co. Schnellladen, wenn Netzteil und Tablet es können.</span></figcaption></figure>
      <figure class="dtile"><img src="img/k-travel.webp" width="800" height="993" alt="Aufgerolltes SmartCharge Cable 240 neben Reisetasche, Powerbank und Kopfhörern" loading="lazy"><figcaption><b>Unterwegs</b><span>Powerbank, Kopfhörer, Switch: 1,5 m lang, aufgerollt passt es in jede Tasche.</span></figcaption></figure>
    </div>
    <p class="note">Wie viel tatsächlich fließt, entscheiden Netzteil und Gerät. Das Kabel lässt bis zu 240 W durch.</p>
  </div>
</section>

<section id="material" aria-labelledby="h-mat" style="padding-top:0">
  <div class="wrap">
    <article class="scene">
      <div class="scene-img photo"><img src="img/k-material.webp" width="1400" height="1045" alt="Nahaufnahme: Aluminiumstecker mit GREENMNKY-Schriftzug, dahinter das schwarze Nylongeflecht" loading="lazy"></div>
      <div class="scene-copy">
        <p class="mono">Verarbeitung</p>
        <h3 id="h-mat">Gebaut für<br>jeden Tag.</h3>
        <ul class="checks">
          <li>48-fach Nylongeflecht, flammhemmend</li>
          <li>Steckergehäuse aus Aluminium an beiden Enden</li>
          <li>Laut Hersteller reiß- und abriebfest</li>
          <li>Überwacht laut Hersteller Spannung und Strom</li>
          <li>CE, UKCA und FCC</li>
        </ul>
      </div>
    </article>
  </div>
</section>

<section id="vergleich" aria-labelledby="h-cmp" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head">
      <p class="mono">Vergleich</p>
      <h2 id="h-cmp">Kabel ist nicht<br><span class="g">gleich Kabel.</span></h2>
    </div>
    <div class="cmp-wrap">
      <table class="cmp">
        <thead><tr><th scope="col"><span class="sr">Merkmal</span></th><th scope="col">Übliches USB-C-Kabel</th><th scope="col" class="us">SmartCharge Cable 240</th></tr></thead>
        <tbody>
          <tr><th scope="row">Zeigt Watt, Volt, Ampere</th><td><i class="n">Nein</i></td><td class="us"><i class="y">Live, im Stecker</i></td></tr>
          <tr><th scope="row">Ladeleistung</th><td>oft nur 60 W</td><td class="us"><i class="y">bis 240 W (USB PD 3.1)</i></td></tr>
          <tr><th scope="row">Schwaches Netzteil erkennen</th><td><i class="n">Raten</i></td><td class="us"><i class="y">Auf einen Blick</i></td></tr>
          <tr><th scope="row">Mantel und Stecker</th><td>oft Kunststoff</td><td class="us"><i class="y">Nylon&shy;geflecht, Aluminium</i></td></tr>
        </tbody>
      </table>
    </div>
    <div class="mid-cta">
      <p><b>24,95 €</b> · Versand mit DHL aus Deutschland · 14 Tage Widerruf</p>
      <a class="btn green" href="#kaufen">Jetzt bestellen {ARROW}</a>
    </div>
  </div>
</section>

<section id="set" aria-labelledby="h-set" style="padding-top:0">
  <div class="wrap">
    <div class="setbox">
      <div class="set-vis photo"><img src="img/k-set.webp" width="1400" height="1045" alt="SmartCharge 140 Ladegerät, daran angeschlossen das SmartCharge Cable 240" loading="lazy"></div>
      <div class="set-copy">
        <p class="mono">Spar-Set</p>
        <h2 id="h-set">Mit SmartCharge 140:<br><span class="g">Kabel für 10 €.</span></h2>
        <p>Leg den <b>SmartCharge 140</b> dazu, dann kostet das Kabel nur 10 € statt 24,95 €. Zwei Displays: Das Netzteil zeigt, was es abgibt, das Kabel, was am Gerät ankommt. Lieber kompakt? Mit dem <a class="xlink" href="/smartcharge-65/">SmartCharge 65</a> sind es 54,90 €, versandkostenfrei.</p>
        <div class="set-compare">
          <div class="sc"><span class="mono">Nur Kabel</span><strong>24,95 €</strong><small>zzgl. 3,30 € Versand</small></div>
          <div class="sc best"><span class="mono">Mit SmartCharge 140</span><strong>69,95 €</strong><small><s>84,90 €</s> · Kabel für 10 €</small></div>
        </div>
        <button class="btn green" type="button" data-pick="sc140">Set wählen · 69,95 € {ARROW}</button>
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
    ("Im Paket", "1× SmartCharge Cable 240"),
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
    ("Lädt mein iPhone damit schneller?", "Das Kabel bremst nicht: Es schafft bis zu 240 W. Wie schnell dein iPhone lädt, entscheiden Netzteil und iPhone. Das Display zeigt dir, was tatsächlich ankommt."),
    ("Passt es an ein iPhone mit Lightning?", "Nein, beide Enden sind USB-C. Es passt an iPhones ab iPhone 15 und an alles andere mit USB-C-Buchse."),
    ("Kann ich damit Daten übertragen?", "Es ist fürs Laden gebaut, auf der Verpackung steht als Funktion „Charging“. Für schnelle Datenübertragung, etwa zu externen SSDs oder Monitoren, nimm ein USB-C-Datenkabel."),
    ("Wo sitzt das Display?", "Im Stecker auf der Geräteseite. Du liest die Werte direkt am Laptop oder Handy ab."),
    ("Wie funktioniert „Kabel für 10&nbsp;€“?", 'Automatisch: Liegen <a href="/smartcharge-140/">SmartCharge 140</a> und Cable 240 zusammen im Warenkorb, zieht die Kasse 14,95 € ab. Kein Code nötig.'),
    ("Wie robust ist das Kabel?", "48-fach Nylongeflecht und Steckergehäuse aus Aluminium an beiden Enden, laut Hersteller flammhemmend, reiß- und abriebfest."),
    ("Wie schnell kommt meine Bestellung und was kostet der Versand?", "Wir versenden mit DHL aus Deutschland. Unter 50 € kostet der Versand 3,30 €, ab 50 € nichts – mit einem SmartCharge-Netzteil zusammen bist du drüber. Du hast 14 Tage Widerrufsrecht."),
])}
    </div>
  </div>
</section>

<section class="final" aria-labelledby="h-final">
  <div class="wrap">
    <h2 id="h-final">Laden mit<br><span class="g">Durchblick.</span></h2>
    <p>24,95 €. Mit dem SmartCharge 140 kostet das Kabel nur 10 €.</p>
    <a class="btn green" href="#kaufen">Jetzt bestellen
      {ARROW}
    </a>
    <p class="fine">14 Tage Widerruf · 2 Jahre Gewährleistung · Kasse von GREENMNKY, kein Kundenkonto nötig</p>
  </div>
</section>"""

# Preis und €-Zeichen nie trennen
main = re.sub(r"(\d) €", r"\1&nbsp;€", main)

html = page(
    title="SmartCharge Cable 240 – 240W USB-C Ladekabel mit Display, 1,5 m | eazygadgetz",
    desc="USB-C-auf-USB-C-Ladekabel mit 240 W (USB PD 3.1) und Display im Stecker, das Watt, Volt und Ampere live zeigt. 1,5 m, Nylongeflecht, Aluminiumstecker. 24,95 €, mit SmartCharge 140 nur 10 €.",
    og_title="SmartCharge Cable 240: 240 Watt, live im Blick.",
    og_desc="USB-C-Kabel mit Display im Stecker: zeigt Watt, Volt und Ampere live. 1,5 m, Nylongeflecht. 24,95 €, mit SmartCharge 140 nur 10 €.",
    path="/kabel-240/",
    preload='<link rel="preload" as="image" href="img/k-hero-1200.webp" imagesrcset="img/k-hero-720.webp 720w, img/k-hero-1200.webp 1200w" imagesizes="(min-width:960px) 560px, calc(100vw - 40px)" fetchpriority="high">',
    name="SmartCharge Cable 240", logo="Cable 240", price="24,95 €",
    nav='      <a href="/">Alle Gadgets</a>\n      <a href="#display">Display</a>\n      <a href="#einsatz">Passt zu</a>\n      <a href="#set">Spar-Set</a>\n      <a href="#technik">Technik</a>\n      <a href="#faq">Fragen</a>',
    main=main,
    footer_links='<a href="/">Alle Gadgets bei eazygadgetz</a> · <a href="/smartcharge-140/">SmartCharge 140</a> · <a href="/smartcharge-65/">SmartCharge 65</a> · <a href="/ring-ii/">OnCtrl Ring II</a> · <a href="/phototag/">PhotoTag</a> · <a href="/magnethalter/">Magnethalter</a>',
    safety="Nicht knicken, nicht an beschädigten Kabeln weiterladen. Elektrogeräte gehören nicht in den Hausmüll, sondern zu einer Sammelstelle.",
    marks="Apple, MacBook, iPad und iPhone sind Marken der Apple Inc. Samsung Galaxy ist eine Marke der Samsung Electronics Co., Ltd. Nintendo Switch ist eine Marke von Nintendo. Die Nennung dient nur dem Hinweis auf die Kompatibilität. Produktabbildungen beispielhaft.",
    sticky_img="img/k-thumb.webp", sticky_sub="Nur das Kabel · 24,95 €", first_url=URLCB,
    campaign="cable240", opts_js=OPTSCB, opt_default="1",
    css_extra=CB_CSS,
)
# neues Teilen-Bild (neuer Dateiname, damit Social-Caches es neu laden)
assert html.count("img/og.jpg") == 2
html = html.replace("img/og.jpg", "img/og2.jpg")

if __name__ == "__main__":
    out = R / "kabel-240/index.html"
    out.write_text(html, encoding="utf-8")
    css = "".join(re.findall(r"<style[^>]*>(.*?)</style>", html, re.S))
    print("kabel-240/index.html", len(html) // 1024, "KB, CSS-Regeln:", css.count("}"))
