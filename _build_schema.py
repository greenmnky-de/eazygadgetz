"""Schreibt die JSON-LD-Blöcke (schema.org) in Startseite, Ring II, PhotoTag und SmartCharge 140. Idempotent: ersetzt vorhandene Blöcke."""
import json, pathlib, re
B="https://eazygadgetz.de"
ORG={"@type":"Organization","@id":B+"/#org","name":"eazygadgetz","legalName":"GREENMNKY GmbH","url":B+"/","logo":B+"/img/logo.png",
     "email":"b2csupport@greenmnky.de","telephone":"+49 6021 4376840",
     "address":{"@type":"PostalAddress","streetAddress":"Lindigstraße 1","postalCode":"63801","addressLocality":"Kleinostheim","addressCountry":"DE"},
     "sameAs":["https://greenmnky.de"]}
SELLER={"@id":B+"/#org"}
SHIP={"@type":"OfferShippingDetails","shippingRate":{"@type":"MonetaryAmount","value":"3.30","currency":"EUR"},
      "shippingDestination":{"@type":"DefinedRegion","addressCountry":"DE"},
      "deliveryTime":{"@type":"ShippingDeliveryTime","handlingTime":{"@type":"QuantitativeValue","minValue":0,"maxValue":1,"unitCode":"DAY"},
                      "transitTime":{"@type":"QuantitativeValue","minValue":1,"maxValue":3,"unitCode":"DAY"}}}
RET={"@type":"MerchantReturnPolicy","applicableCountry":"DE","returnPolicyCategory":"https://schema.org/MerchantReturnFiniteReturnWindow",
     "merchantReturnDays":14,"returnMethod":"https://schema.org/ReturnByMail","returnFees":"https://schema.org/ReturnFeesCustomerResponsibility"}
def offer(url,price,avail="https://schema.org/InStock"):
    return {"@type":"Offer","url":url,"price":price,"priceCurrency":"EUR","availability":avail,
            "itemCondition":"https://schema.org/NewCondition","seller":SELLER,"shippingDetails":SHIP,"hasMerchantReturnPolicy":RET}
def crumbs(name,path):
    return {"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"eazygadgetz","item":B+"/"},{"@type":"ListItem","position":2,"name":name,"item":B+path}]}

pt=B+"/phototag/"
pt_desc="Bluetooth-Tracker mit Farb-E-Ink-Display: zeigt dein eigenes Foto und auf Knopfdruck deine Kontaktkarte. Wiederfinden über Apple „Wo ist?“ (ab iOS 14) oder Google Find Hub (ab Android 11), Signalton bis 90 dB, Knopfzelle CR2032 bis zu 10 Monate, Aluminium, IP65, 15 g."
VAR=[("Schwarz","WA.PT.B","6980145640009","var-black.webp"),("Rosé","WA.PT.RG","6980145640955","var-rose.webp"),("Orange","WA.PT.O","6980145640993","var-orange.webp")]
PG={"@context":"https://schema.org","@graph":[ORG,
  {"@type":"ProductGroup","@id":pt+"#product","name":"PhotoTag – Tracker mit Foto-Display für iPhone & Android","description":pt_desc,"url":pt,
   "brand":{"@type":"Brand","name":"PhotoTag"},"productGroupID":"WA.PT","variesBy":["https://schema.org/color"],
   "image":[pt+"img/var-black.webp",pt+"img/koffer.webp",pt+"img/foto-eink.webp",pt+"img/tag-cord-cat.webp"],
   "hasVariant":[{"@type":"Product","name":f"PhotoTag {n}","description":f"PhotoTag in {n}. "+pt_desc,"sku":sku,"gtin13":ean,"color":n,"image":pt+"img/"+img,"offers":offer(pt,"29.99")} for n,sku,ean,img in VAR]},
  crumbs("PhotoTag","/phototag/")]}
r=B+"/ring-ii/"
r_desc="Bluetooth-Fernbedienung als Ring für GoPro, DJI und Insta360 sowie Smartphone: Foto auslösen, Video starten, Musik steuern, Kurzvideos wischen. Drei Modi, ca. 8 h Akku, magnetisches Laden, Silikonringe in S, M und L im Lieferumfang."
RG={"@context":"https://schema.org","@graph":[ORG,
  {"@type":"Product","@id":r+"#product","name":"OnCtrl Ring II – Fernbedienungs-Ring für Action Cam & Smartphone","description":r_desc,"url":r,
   "brand":{"@type":"Brand","name":"OnCtrl"},"sku":"WA.BRCR200","color":"Schwarz",
   "image":[r+"img/ring-blue.webp",r+"img/og.jpg",r+"img/modi.webp"],"offers":offer(r,"29.95")},
  crumbs("OnCtrl Ring II","/ring-ii/")]}
sc=B+"/smartcharge-140/"
SHIP0=dict(SHIP,shippingRate={"@type":"MonetaryAmount","value":"0.00","currency":"EUR"})
def offer_free(url,price):
    o=offer(url,price); o["shippingDetails"]=SHIP0; return o
sc_desc="140-W-GaN-Ladegerät mit 3× USB-C (PD 3.1, bis 140 W an C1) und 1× USB-A (30 W). Smart Display zeigt live die Gesamtleistung und die Leistung pro Anschluss, Taste wechselt die Ansicht. Klappbarer Eurostecker, 82,5 × 71,5 × 36 mm, 260 g. Lädt MacBook Pro, iPad, iPhone und Kopfhörer gleichzeitig."
cb_desc="USB-C-auf-USB-C-Ladekabel mit 240 W (USB PD 3.1 EPR), 1,5 m, Nylongeflecht, Aluminiumstecker und Display im Stecker, das Watt, Volt und Ampere live zeigt."
SC={"@context":"https://schema.org","@graph":[ORG,
  {"@type":"Product","@id":sc+"#product","name":"GREENMNKY SmartCharge 140 – 140W GaN USB-C Ladegerät mit Smart Display","description":sc_desc,"url":sc,
   "brand":{"@type":"Brand","name":"GREENMNKY"},"sku":"CHA.GWT.C140","gtin13":"4251772541970","mpn":"RCE-14005ACCCLEU","color":"Graphit",
   "image":[sc+"img/hero-ring.webp",sc+"img/angle.webp",sc+"img/ports.webp",sc+"img/back.webp"],"offers":offer_free(sc,"59.95"),
   "isRelatedTo":{"@id":sc+"#cable"}},
  {"@type":"Product","@id":sc+"#cable","name":"GREENMNKY SmartCharge Cable 240 – 240W USB-C Ladekabel mit Display, 1,5 m","description":cb_desc,"url":sc+"#kaufen",
   "brand":{"@type":"Brand","name":"GREENMNKY"},"sku":"CHA.GWT.CC240","gtin13":"4251772542038","color":"Schwarz",
   "image":[sc+"img/cable-plugs.webp",sc+"img/cable-coil.webp"],"offers":offer(sc+"#kaufen","24.95")},
  crumbs("SmartCharge 140","/smartcharge-140/")]}
HG={"@context":"https://schema.org","@graph":[ORG,{"@type":"WebSite","@id":B+"/#website","url":B+"/","name":"eazygadgetz","inLanguage":"de","publisher":SELLER}]}

def inject(path,data,marker):
    f=pathlib.Path(path); s=f.read_text()
    s=re.sub(r'<script type="application/ld\+json">.*?</script>\n','',s,flags=re.S)
    block='<script type="application/ld+json">\n'+json.dumps(data,ensure_ascii=False,separators=(",",":"))+'\n</script>\n'
    assert s.count(marker)==1,(path,marker)
    f.write_text(s.replace(marker,block+marker,1)); print(path,"ok")
R=pathlib.Path(__file__).parent
inject(R/"phototag/index.html",PG,'<link rel="preload" href="fonts/archivo.woff2"')
inject(R/"ring-ii/index.html",RG,'<link rel="preload" href="fonts/rubik.woff2"')
inject(R/"index.html",HG,'<link rel="preload" href="/ring-ii/fonts/rubik.woff2"')
inject(R/"smartcharge-140/index.html",SC,'<link rel="preload" href="fonts/rubik.woff2"')
