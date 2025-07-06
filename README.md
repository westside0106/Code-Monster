# 🧠 Code-Monster

Willkommen beim **Code-Monster**, deinem smarten KI-Dev-Tool!  
Dieses Projekt bietet dir produktionsnahe GPT-Endpunkte für Refactoring, Fehlersuche, Testgenerierung & mehr – als API, lokal oder auf Fly.io/Render deploybar.

![Code-Monster Preview](assets/code-monster-preview.gif)

---

## 🚀 Features

| Endpoint               | Funktion                                      |
|------------------------|-----------------------------------------------|
| `/refactor`            | Automatisiertes Clean Code Refactoring        |
| `/explaintraceback`    | GPT-gestützte Fehleranalyse deiner Logs       |
| `/generate_tests`      | Unit-Test-Erzeugung aus deinem Code           |
| `/uml_from_code`       | Generiert UML-Diagramme aus deinem Quelltext  |

---

## ⚙️ Installation

```bash
git clone https://github.com/westside0106/Code-Monster.git
cd Code-Monster
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 📡 Nutzung (lokal)

```bash
uvicorn main:app --reload
```

Zugriff via:  
👉 `http://127.0.0.1:8000/docs` für Swagger UI  
👉 `http://127.0.0.1:8000/redoc` für Redoc-Dokumentation

---

## 🧪 Beispiel: Refactor Endpoint

**POST** `http://127.0.0.1:8000/refactor`

```json
{
  "code": "def add(a,b): return a+b"
}
```

**Antwort:**
```json
{
  "refactored_code": "def add(a: int, b: int) -> int:\n    return a + b"
}
```

---

## 🖼️ Screenshots & GIFs

| Vorschau | Beschreibung |
|---------|--------------|
| ![GIF](assets/code-monster-preview.gif) | Live-Demo: `/explaintraceback` in Aktion |
| ![GIF](assets/refactor-demo.gif) | Automatisches Refactoring erklärt von GPT |

---

## 📦 Deployment

Mit [Fly.io](https://fly.io/docs/launch/) oder [Render](https://render.com/docs) einfach deployen.

```bash
flyctl launch
```

oder

```toml
# fly.toml
[env]
  OPENAI_API_KEY="sk-..."
```

---

## 📄 Lizenz

MIT © Philipp / westside0106  
Du darfst alles nutzen, erweitern oder forken – einfach verlinken ✌️

---

## 📬 Kontakt

Du hast eine Idee oder willst das Monster füttern?  
📧 [code-monster@layzsshop.com](mailto:code-monster@layzsshop.com)
