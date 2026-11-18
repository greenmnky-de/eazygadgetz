"""Erzeugt /impressum/index.html und /datenschutz/index.html im Look der Ring-II-Seite."""
import pathlib
R = pathlib.Path("/home/claude/eazygadgetz")
STAND = "17. November 2026"

BASE = """<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} – eazygadgetz</title>
<meta name="robots" content="noindex,follow">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<style>
@font-face{{font-family:"Rubik";src:url("/ring-ii/fonts/rubik.woff2") format("woff2");font-weight:300 900;font-display:swap}}
:root{{--bg:#0A0B0D;--card:#15181D;--line:rgba(255,255,255,.10);--text:#F2F3F0;--muted:#A2A7AE;--accent:#F2F3F0;color-scheme:dark}}
*{{box-sizing:border-box}}
html,body{{margin:0;background:var(--bg);color:var(--text);font-family:"Rubik",system-ui,-apple-system,"Segoe UI",Arial,sans-serif;line-height:1.55}}
a{{color:var(--text)}}
.wrap{{max-width:760px;margin:0 auto;padding:40px 22px 80px}}
header{{display:flex;align-items:center;justify-content:space-between;gap:16px;margin-bottom:40px}}
.logo{{font-weight:900;font-size:22px;letter-spacing:-.03em;text-decoration:none}}
.logo span{{color:var(--muted);font-weight:400}}
nav a{{color:var(--muted);text-decoration:none;font-size:14px;margin-left:16px}}
nav a:hover{{color:var(--text)}}
h1{{font-size:clamp(2rem,5vw,2.8rem);font-weight:900;letter-spacing:-.03em;line-height:1;margin:0 0 10px}}
.stand{{color:var(--muted);font-size:14px;margin-bottom:34px}}
h2{{font-size:1.15rem;margin:34px 0 10px;font-weight:700}}
p,li{{color:#D5D8DC;font-size:16px}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:20px 22px;margin:14px 0}}
.card p{{margin:4px 0}}
footer{{margin-top:60px;padding-top:20px;border-top:1px solid var(--line);color:var(--muted);font-size:13px;display:flex;flex-wrap:wrap;gap:14px}}
footer a{{color:var(--muted);text-decoration:none}}
footer a:hover{{color:var(--text)}}
</style>
</head>
<body>
<div class="wrap">
<header>
  <a class="logo" href="/">eazygadgetz <span>by GREENMNKY</span></a>
  <nav><a href="/ring-ii/">Ring II</a><a href="/phototag/">PhotoTag</a><a href="/impressum/">Impressum</a><a href="/datenschutz/">Datenschutz</a></nav>
</header>
<main>
<h1>{title}</h1>
<p class="stand">Stand: {stand}</p>
{body}
</main>
<footer>
  <span>© GREENMNKY GmbH</span>
  <a href="/impressum/">Impressum</a>
  <a href="/datenschutz/">Datenschutz</a>
  <a href="https://greenmnky.de/policies/terms-of-service" rel="noopener">AGB</a>
  <a href="https://greenmnky.de/policies/refund-policy" rel="noopener">Widerrufsrecht</a>
  <a href="https://greenmnky.de/policies/shipping-policy" rel="noopener">Versand und Zahlung</a>
</footer>
</div>
</body>
</html>
"""

IMPRESSUM = """
<p>Angaben gemäß § 5 DDG und § 18 Abs. 2 MStV.</p>
<div class="card">
<p><strong>GREENMNKY GmbH</strong></p>
<p>Lindigstraße 1<br>63801 Kleinostheim<br>Deutschland</p>
</div>
<div class="card">
<p><strong>Kontakt</strong></p>
<p>Telefon: <a href="tel:+4960214376840">+49 6021 43 76 84 - 0</a></p>
<p>E-Mail: <a href="mailto:b2csupport@greenmnky.de">b2csupport@greenmnky.de</a></p>
</div>
<div class="card">
<p><strong>Vertretungsberechtigter Geschäftsführer</strong><br>Ziya Orhan</p>
<p><strong>Registereintrag</strong><br>Amtsgericht Aschaffenburg, HRB 15500</p>
<p><strong>Umsatzsteuer-Identifikationsnummer</strong> gemäß § 27a UStG<br>DE328774522</p>
<p><strong>Verantwortlich für den Inhalt</strong> nach § 18 Abs. 2 MStV<br>Ziya Orhan, Anschrift wie oben</p>
</div>
<h2>Verbraucherstreitbeilegung</h2>
<p>Zur Teilnahme an einem Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle sind wir nicht verpflichtet und nicht bereit.</p>
<h2>Hinweis zu dieser Seite</h2>
<p>eazygadgetz.de ist ein Angebot der GREENMNKY GmbH. Bestellungen werden über unseren Online-Shop <a href="https://greenmnky.de" rel="noopener">greenmnky.de</a> abgewickelt. Dort gelten unsere <a href="https://greenmnky.de/policies/terms-of-service" rel="noopener">AGB</a>, die <a href="https://greenmnky.de/policies/refund-policy" rel="noopener">Widerrufsbelehrung</a> sowie die <a href="https://greenmnky.de/policies/shipping-policy" rel="noopener">Versand- und Zahlungsbedingungen</a>.</p>
<h2>Markenhinweise</h2>
<p>GoPro, HERO und MAX sind Marken der GoPro Inc. DJI und Osmo sind Marken von SZ DJI Technology Co., Ltd. Insta360 ist eine Marke der Arashi Vision Inc. Apple, iPhone und iOS sind Marken der Apple Inc. Android ist eine Marke der Google LLC. OnCtrl ist eine Marke ihres Inhabers. Die Nennung dient nur dem Hinweis auf die Kompatibilität.</p>
"""

DATENSCHUTZ = """
<p>Diese Datenschutzerklärung gilt für die Website <strong>eazygadgetz.de</strong>. Wir halten sie bewusst kurz, weil diese Seite nur sehr wenige Daten verarbeitet: keine Cookies, kein Tracking, keine Kontoanlage.</p>

<h2>1. Verantwortlicher</h2>
<div class="card">
<p>GREENMNKY GmbH<br>Lindigstraße 1<br>63801 Kleinostheim<br>Deutschland</p>
<p>Telefon: +49 6021 43 76 84 - 0<br>E-Mail: <a href="mailto:b2csupport@greenmnky.de">b2csupport@greenmnky.de</a></p>
</div>

<h2>2. Hosting und Server-Logfiles</h2>
<p>Diese Website wird als statische Seite über den Dienst <strong>Render</strong> (Render Services, Inc., 525 Brannan Street, Suite 300, San Francisco, CA 94107, USA) ausgeliefert. Beim Aufruf einer Seite verarbeitet der Server technisch notwendig folgende Daten: IP-Adresse, Datum und Uhrzeit, aufgerufene Datei, übertragene Datenmenge, Referrer-URL sowie Browser- und Betriebssystemkennung. Diese Zugriffsdaten dienen ausschließlich der Auslieferung, Sicherheit und Fehleranalyse der Seite und werden nicht mit anderen Daten zusammengeführt.</p>
<p>Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO (berechtigtes Interesse an einem sicheren und stabilen Betrieb). Die Verarbeitung erfolgt im Rahmen einer Auftragsverarbeitung nach Art. 28 DSGVO. Soweit dabei Daten in die USA übermittelt werden, geschieht dies auf Grundlage der Standardvertragsklauseln der EU-Kommission (Art. 46 Abs. 2 lit. c DSGVO). Server-Logfiles werden nach kurzer Zeit automatisch gelöscht.</p>

<h2>3. Keine Cookies, kein Tracking</h2>
<p>eazygadgetz.de setzt keine Cookies und verwendet keine Analyse-, Werbe- oder Social-Media-Tools. Schriftarten und Bilder werden von unserem eigenen Server geladen; es werden keine Inhalte von Drittanbietern nachgeladen. Ein Consent-Banner ist deshalb nicht erforderlich.</p>
<p>Links, über die du auf diese Seite gelangst (z. B. aus Instagram oder TikTok), können Kampagnen-Parameter in der Adresse enthalten (sogenannte UTM-Parameter). Diese Parameter enthalten keine personenbezogenen Daten; sie werden auf dieser Seite nicht gespeichert, sondern lediglich an den Link zu unserem Shop angehängt, damit wir erkennen, über welchen Kanal eine Bestellung zustande kam.</p>

<h2>4. Bestellung über greenmnky.de</h2>
<p>Wenn du auf „Jetzt bestellen“ klickst, wirst du zu unserem Online-Shop <a href="https://greenmnky.de" rel="noopener">greenmnky.de</a> weitergeleitet, der auf der Plattform Shopify betrieben wird. Erst dort gibst du Daten für deine Bestellung ein. Für die Verarbeitung im Shop und im Bestellprozess gilt die <a href="https://greenmnky.de/policies/privacy-policy" rel="noopener">Datenschutzerklärung von greenmnky.de</a>.</p>

<h2>5. Kontaktaufnahme</h2>
<p>Wenn du uns per E-Mail oder Telefon kontaktierst, verarbeiten wir deine Angaben zur Bearbeitung der Anfrage (Art. 6 Abs. 1 lit. b DSGVO bzw. lit. f DSGVO). Die Daten werden gelöscht, sobald sie für die Bearbeitung nicht mehr erforderlich sind und keine gesetzlichen Aufbewahrungspflichten entgegenstehen.</p>

<h2>6. Externe Links</h2>
<p>Diese Seite verlinkt auf unsere Profile bei Instagram und TikTok sowie auf unseren Shop. Für die Inhalte und die Datenverarbeitung der verlinkten Seiten sind deren Betreiber verantwortlich. Es sind keine Plugins dieser Dienste eingebunden; Daten werden erst übertragen, wenn du einen Link anklickst.</p>

<h2>7. Deine Rechte</h2>
<p>Du hast gegenüber uns das Recht auf Auskunft (Art. 15 DSGVO), Berichtigung (Art. 16), Löschung (Art. 17), Einschränkung der Verarbeitung (Art. 18), Datenübertragbarkeit (Art. 20) sowie Widerspruch gegen Verarbeitungen auf Grundlage von Art. 6 Abs. 1 lit. f DSGVO (Art. 21). Wende dich dafür an <a href="mailto:b2csupport@greenmnky.de">b2csupport@greenmnky.de</a>.</p>
<p>Außerdem kannst du dich bei einer Datenschutz-Aufsichtsbehörde beschweren. Für uns zuständig ist das Bayerische Landesamt für Datenschutzaufsicht (BayLDA), Promenade 18, 91522 Ansbach, <a href="https://www.lda.bayern.de" rel="noopener">www.lda.bayern.de</a>.</p>

<h2>8. Änderungen</h2>
<p>Wir passen diese Erklärung an, wenn sich die Website oder die Rechtslage ändert. Es gilt jeweils die hier veröffentlichte Fassung.</p>
"""

for slug, title, body in [("impressum", "Impressum", IMPRESSUM), ("datenschutz", "Datenschutz", DATENSCHUTZ)]:
    d = R / slug; d.mkdir(exist_ok=True)
    (d / "index.html").write_text(BASE.format(title=title, stand=STAND, body=body))
    print("wrote", d / "index.html")
