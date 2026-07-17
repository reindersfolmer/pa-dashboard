#!/usr/bin/env python3
"""Versleutel een dashboard-HTML tot een zelfstandige, wachtwoordbeveiligde pagina.

Gebruik:
    python3 build_page.py dashboard.html "wachtwoord" index.html

Vereist: pip install cryptography --break-system-packages
"""
import base64
import os
import sys

try:
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    from cryptography.hazmat.primitives import hashes
except ImportError:
    sys.exit("Pakket 'cryptography' ontbreekt. Draai eerst: pip install cryptography --break-system-packages")

ITERATIONS = 310_000

LOCKER = """<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#101418">
<meta name="apple-mobile-web-app-capable" content="yes">
<title>PA Dashboard</title>
<style>
  :root { color-scheme: light dark; }
  body { margin:0; min-height:100vh; display:flex; align-items:center; justify-content:center;
         font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
         background:#101418; color:#e8eaed; }
  .card { width:min(340px,88vw); padding:2rem 1.6rem; border-radius:16px; background:#1a2027;
          box-shadow:0 8px 32px rgba(0,0,0,.4); text-align:center; }
  h1 { font-size:1.15rem; margin:0 0 .3rem; font-weight:600; }
  p  { margin:.2rem 0 1.2rem; font-size:.85rem; color:#9aa4af; }
  input[type=password] { width:100%; box-sizing:border-box; padding:.7rem .8rem; font-size:1rem;
          border-radius:10px; border:1px solid #333c46; background:#0d1116; color:inherit; }
  label { display:flex; gap:.45rem; align-items:center; justify-content:center;
          font-size:.8rem; color:#9aa4af; margin:.8rem 0; }
  button { width:100%; padding:.7rem; font-size:1rem; font-weight:600; border:0; border-radius:10px;
          background:#3b82f6; color:#fff; cursor:pointer; }
  button:active { transform:scale(.98); }
  #err { color:#f87171; font-size:.85rem; min-height:1.2em; margin-top:.7rem; }
</style>
</head>
<body>
<div class="card">
  <h1>PA Dashboard</h1>
  <p>Voer je wachtwoord in om te openen</p>
  <form id="f">
    <input type="password" id="pw" autocomplete="current-password" autofocus>
    <label><input type="checkbox" id="rem" checked> onthoud op dit apparaat</label>
    <button type="submit">Openen</button>
  </form>
  <div id="err"></div>
</div>
<script>
/* PA-ENC v1 */
const PAYLOAD = "__PAYLOAD__";
const ITER = __ITER__;
const b = Uint8Array.from(atob(PAYLOAD), c => c.charCodeAt(0));
const salt = b.slice(0,16), iv = b.slice(16,28), ct = b.slice(28);
async function unlock(pw){
  const km = await crypto.subtle.importKey("raw", new TextEncoder().encode(pw), "PBKDF2", false, ["deriveKey"]);
  const key = await crypto.subtle.deriveKey({name:"PBKDF2", salt, iterations:ITER, hash:"SHA-256"},
      km, {name:"AES-GCM", length:256}, false, ["decrypt"]);
  const plain = await crypto.subtle.decrypt({name:"AES-GCM", iv}, key, ct);
  return new TextDecoder().decode(plain);
}
async function go(pw, remember){
  try{
    const html = await unlock(pw);
    if(remember){ try{ localStorage.setItem("pa_pw", pw); }catch(e){} }
    document.open(); document.write(html); document.close();
  }catch(e){
    try{ localStorage.removeItem("pa_pw"); }catch(_){}
    const el = document.getElementById("err");
    if(el) el.textContent = "Wachtwoord onjuist.";
  }
}
document.getElementById("f").addEventListener("submit", ev => {
  ev.preventDefault();
  go(document.getElementById("pw").value, document.getElementById("rem").checked);
});
try{
  const saved = localStorage.getItem("pa_pw");
  if(saved) go(saved, false);
}catch(e){}
</script>
</body>
</html>
"""


def build(src: str, password: str, dst: str) -> None:
    plain = open(src, "rb").read()
    salt = os.urandom(16)
    nonce = os.urandom(12)
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=ITERATIONS)
    key = kdf.derive(password.encode())
    ct = AESGCM(key).encrypt(nonce, plain, None)
    payload = base64.b64encode(salt + nonce + ct).decode()
    html = LOCKER.replace("__PAYLOAD__", payload).replace("__ITER__", str(ITERATIONS))
    open(dst, "w").write(html)
    print(f"OK: {dst} ({len(html)//1024} KB, versleuteld met AES-256-GCM)")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    build(sys.argv[1], sys.argv[2], sys.argv[3])
