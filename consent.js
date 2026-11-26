/* eazygadgetz – Cookie-Einwilligung + Meta-Pixel
   Der Pixel wird erst geladen, wenn jemand auf „Akzeptieren“ klickt.
   Ohne Ja: kein Cookie, keine Anfrage an Meta.
   Einstellungen ändern: Link „Cookie-Einstellungen“ im Footer oder ein Element mit [data-consent-open]. */
(function () {
  "use strict";
  var PIXEL_ID = "1353639428321006";          /* GREENMNKY Pixel, derselbe wie im Shop */
  var KEY = "ez_consent";                       /* gespeichert im Browser (localStorage) */
  var VERSION = 1;                              /* erhöhen, wenn sich der Banner-Inhalt ändert -> neu fragen */
  var MAX_AGE = 365 * 24 * 3600 * 1000;         /* nach 12 Monaten neu fragen */
  var loaded = false;

  function read() {
    try {
      var c = JSON.parse(localStorage.getItem(KEY) || "null");
      if (c && c.v === VERSION && Date.now() - c.t < MAX_AGE) return c;
    } catch (e) {}
    return null;
  }
  function save(meta) {
    try { localStorage.setItem(KEY, JSON.stringify({ v: VERSION, meta: !!meta, t: Date.now() })); } catch (e) {}
  }

  /* ---------- Meta-Pixel ---------- */
  function num(t) {
    var m = String(t || "").replace(/\s| /g, "").match(/(\d{1,3}(?:\.\d{3})*|\d+)(?:,(\d{1,2}))?/);
    return m ? parseFloat(m[1].replace(/\./g, "") + "." + (m[2] || "0")) : 0;
  }
  function cartItems(href) {
    var m = String(href || "").match(/greenmnky\.de\/cart\/([0-9:,]+)/);
    if (!m) return [];
    return m[1].split(",").map(function (p) { var a = p.split(":"); return { id: a[0], quantity: parseInt(a[1] || "1", 10) || 1 }; })
      .filter(function (x) { return x.id; });
  }
  function product() {
    var out = null;
    [].forEach.call(document.querySelectorAll('script[type="application/ld+json"]'), function (s) {
      if (out) return;
      try {
        var d = JSON.parse(s.textContent), g = d["@graph"] || [d];
        g.forEach(function (n) {
          if (out) return;
          if (n["@type"] === "ProductGroup" && n.hasVariant && n.hasVariant[0]) out = { name: n.name, price: n.hasVariant[0].offers && n.hasVariant[0].offers.price };
          else if (n["@type"] === "Product" && n.offers) out = { name: n.name, price: n.offers.price };
        });
      } catch (e) {}
    });
    return out;
  }
  function loadPixel() {
    if (loaded) { window.fbq && window.fbq("consent", "grant"); return; }
    loaded = true;
    /* offizieller Meta-Basiscode */
    !function (f, b, e, v, n, t, s) { if (f.fbq) return; n = f.fbq = function () { n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments) }; if (!f._fbq) f._fbq = n; n.push = n; n.loaded = !0; n.version = "2.0"; n.queue = []; t = b.createElement(e); t.async = !0; t.src = v; s = b.getElementsByTagName(e)[0]; s.parentNode.insertBefore(t, s) }(window, document, "script", "https://connect.facebook.net/en_US/fbevents.js");
    fbq("init", PIXEL_ID);
    fbq("track", "PageView");
    var p = product(), buy = document.getElementById("buy"), items = cartItems(buy && buy.href);
    if (p) {
      var vc = { content_name: p.name, content_type: "product", currency: "EUR", value: parseFloat(p.price) || 0 };
      if (items.length) vc.content_ids = [items[0].id];
      fbq("track", "ViewContent", vc);
    }
  }
  function stopPixel() {
    if (window.fbq) { try { window.fbq("consent", "revoke"); } catch (e) {} }
    /* Meta-Cookies dieser Seite löschen */
    var host = location.hostname, doms = ["", host, "." + host, "." + host.replace(/^www\./, "")];
    ["_fbp", "_fbc"].forEach(function (n) {
      doms.forEach(function (d) { document.cookie = n + "=; Max-Age=0; path=/" + (d ? "; domain=" + d : ""); });
    });
  }

  /* Klick auf „Bestellen“ = In den Warenkorb (danach geht es direkt in die Shop-Kasse) */
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest('a[href*="greenmnky.de/cart/"]');
    var c = read();
    if (!a || !c || !c.meta || !window.fbq) return;
    var items = cartItems(a.href);
    if (!items.length) return;
    var pm = document.getElementById("priceMain");
    fbq("track", "AddToCart", {
      content_ids: items.map(function (x) { return x.id; }),
      contents: items,
      content_type: "product",
      num_items: items.reduce(function (s, x) { return s + x.quantity; }, 0),
      currency: "EUR",
      value: pm ? num(pm.textContent) : 0
    });
    /* normaler Linksklick: kurz warten, damit die Meldung noch rausgeht */
    if (e.button === 0 && !e.metaKey && !e.ctrlKey && !e.shiftKey && !e.altKey && a.target !== "_blank") {
      e.preventDefault();
      var href = a.href;
      setTimeout(function () { location.href = href; }, 300);
    }
  }, true);

  /* ---------- Banner ---------- */
  var CSS =
    "#ez-cc{position:fixed;left:12px;right:12px;bottom:12px;z-index:2147483000;max-width:560px;margin:0 auto;" +
    "background:#15161A;color:#F2F3F0;border:1px solid rgba(255,255,255,.14);border-radius:18px;padding:18px 18px 16px;" +
    "box-shadow:0 18px 50px rgba(0,0,0,.35);font-family:inherit;font-size:15px;line-height:1.5;text-align:left;-webkit-font-smoothing:antialiased}" +
    "#ez-cc[hidden]{display:none}" +
    "#ez-cc h2{margin:0 0 6px;font-size:16px;font-weight:700;line-height:1.3;color:#F2F3F0;letter-spacing:0}" +
    "#ez-cc p{margin:0;font-size:14px;line-height:1.5;color:#C9CCD1}" +
    "#ez-cc a{color:#F2F3F0;text-decoration:underline}" +
    "#ez-cc .ez-cc-b{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:14px}" +
    "#ez-cc button{appearance:none;cursor:pointer;font:inherit;font-size:15px;font-weight:700;padding:12px 10px;border-radius:12px;" +
    "border:2px solid #F2F3F0;background:#F2F3F0;color:#15161A;min-height:46px}" +
    "#ez-cc button:hover{background:#fff}" +
    "#ez-cc button:focus-visible{outline:3px solid #F0C233;outline-offset:2px}" +
    ".ez-cc-link{background:none;border:0;padding:0;margin:0;font:inherit;color:inherit;text-decoration:inherit;cursor:pointer}" +
    ".ez-cc-link:hover{text-decoration:underline}";
  var box = null, styled = false;
  function style() {
    if (styled) return; styled = true;
    var st = document.createElement("style"); st.textContent = CSS; document.head.appendChild(st);
  }
  function build() {
    if (box) return box;
    style();
    box = document.createElement("div");
    box.id = "ez-cc"; box.setAttribute("role", "dialog"); box.setAttribute("aria-labelledby", "ez-cc-t"); box.setAttribute("aria-describedby", "ez-cc-d");
    box.hidden = true;
    box.innerHTML =
      '<h2 id="ez-cc-t">Cookies und Meta-Pixel</h2>' +
      '<p id="ez-cc-d">Dürfen wir den Meta-Pixel nutzen? Damit sehen wir, ob unsere Werbung auf Instagram und Facebook ankommt, und Meta kann sie passender ausspielen. ' +
      'Dafür werden Cookies gesetzt und Meta erhält Daten zu deinem Besuch, auch in den USA. Ohne dein Ja passiert das nicht. ' +
      'Du kannst es jederzeit unter „Cookie-Einstellungen“ unten auf der Seite ändern. <a href="/datenschutz/#meta-pixel">Mehr in der Datenschutzerklärung</a></p>' +
      '<div class="ez-cc-b"><button type="button" data-ez="0">Ablehnen</button><button type="button" data-ez="1">Akzeptieren</button></div>';
    box.addEventListener("click", function (e) {
      var b = e.target.closest && e.target.closest("button[data-ez]");
      if (!b) return;
      var yes = b.getAttribute("data-ez") === "1";
      save(yes);
      box.hidden = true;
      if (yes) loadPixel(); else stopPixel();
    });
    document.body.appendChild(box);
    return box;
  }
  function open() { build().hidden = false; }

  /* Link „Cookie-Einstellungen“ neben „Datenschutz“ im Footer */
  function footerLink() {
    var ds = document.querySelector('footer a[href="/datenschutz/"]');
    if (!ds || document.querySelector(".ez-cc-link")) return;
    var btn = document.createElement("button");
    btn.type = "button"; btn.className = "ez-cc-link"; btn.textContent = "Cookie-Einstellungen";
    btn.addEventListener("click", open);
    /* sieht aus wie der Link „Datenschutz“ daneben */
    var cs = getComputedStyle(ds);
    ["color", "fontSize", "fontFamily", "fontWeight", "letterSpacing", "lineHeight", "textDecorationLine", "textUnderlineOffset", "textTransform"].forEach(function (k) { btn.style[k] = cs[k]; });
    var li = ds.parentNode;
    if (li && li.tagName === "LI") { var nl = document.createElement("li"); nl.appendChild(btn); li.parentNode.insertBefore(nl, li.nextSibling); }
    else ds.parentNode.insertBefore(btn, ds.nextSibling);
  }

  function init() {
    style();
    footerLink();
    document.addEventListener("click", function (e) {
      var o = e.target.closest && e.target.closest("[data-consent-open]");
      if (o) { e.preventDefault(); open(); }
    });
    var c = read();
    if (c && c.meta) loadPixel();
    else if (!c) open();
  }
  window.ezConsent = { open: open };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init); else init();
})();
