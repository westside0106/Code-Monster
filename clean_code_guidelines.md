
# Clean Code Guidelines – Code‑Monster 🚀

## 🎯 Zielsetzung
Leitfaden für **klare, wartbare und erweiterbare** Codebasis – für dich und dein Team. Fokus auf Lesbarkeit, Modularität, SOLID-Prinzipien & Best Practices in realen Projekten.

---

## 🧠 Prinzipien & Patterns

### 1. KISS – Keep It Simple, Stupid
- Logik minimal halten, Komplexität vermeiden.  
- „Simplicity is prerequisite for reliability.“ – Dijkstra

### 2. DRY – Don’t Repeat Yourself
- Vermeide Duplikate – zentrale Verantwortlichkeit.  
- **Python Beispiel:**
```python
# ❌ Duplizierter Code
def greet_john(): print("Hello John")
def greet_sarah(): print("Hello Sarah")

# ✅ DRY
def greet(name):
    print(f"Hello {name}")
```
- **JavaScript Beispiel:**
```js
function greet({ name }) {
  console.log(`Hello ${name}`);
}
greet({ name: 'John' });
greet({ name: 'Sarah' });
```

### 3. SOLID-Prinzipien
- **S** RP, OCP, LSP, ISP, DIP – klare, wartbare Struktur  
- **Python SRP Beispiel:**
```python
class FileReader:
    def read(self): ...
class FileWriter:
    def write(self): ...
```

### 4. Boy Scout Rule
- Immer Code sauberer hinterlassen, als man ihn fand.

### 5. POLA – Principle of Least Astonishment
- Kein überraschendes Verhalten – konsistente Names & Struktur.

---

## ✍️ Namensgebung & Konsistenz
- **Sprechende Namen** statt kryptische Kürzel (z. B. `totalAmount` vs. `x`)  
- Einheitlicher Stil (z. B. CamelCase in JS, snake_case in Python)  
- Großschreibung für Konstanten (z. B. `const MAX_ITEMS = 100`)

---

## 🎯 Funktionen & Modularisierung
- **Single Responsibility**: jede Funktion hat genau einen Zweck  
- Kurz (< 20 Zeilen), gut testbar, klare Parametrierung  
- Viele Parameter? Packe sie in ein Objekt oder dataklasse

---

## 🧹 Formatierung & Tools
- Einheitliche Einrückung, Zeilenbreite 80–120 Zeichen  
- Tools:
  - **Python**: Black, Pylint, Flake8, MyPy
  - **JS/TS**: Prettier, ESLint, TypeScript-Linter
  - **Allgemein**: SonarQube, CodeQL für statische Analysen

---

## 🗣⚠️ Kommentare & Dokumentation
- Nur bei komplexem „Warum“, nicht das „Was“ erklären  
- Kopfzeilen und Public APIs kurz dokumentieren  
- Und: lieber Code verbessern statt zu kommentieren

---

## 🔄 Refactoring-Strategien
- Regelmäßiges Refactoring nach Codeänderungen  
- Muster: Extract Method/Class, Rename, Inline  
- Trennung von Zuständigkeiten & Redundanzen reduzieren

---

## 🧪 Tests & TDD
- **Test-first (TDD)**: Tests vor der eigentlichen Implementation  
- Jeder Test nur **ein Assert**, schnell und isoliert  
- **Python (pytest):**
```python
def test_greet():
    assert greet("Alice") == "Hello Alice"
```
- **JS (Jest):**
```js
test('greet', () => {
  expect(greet('Bob')).toBe('Hello Bob');
});
```

---

## 🛠 Tools & Automatisierung
- Automatische Checks via CI/CD-Pipeline:
  - **Lint → Format → Test → Static Analysis → Build**  
- Tools:
  - Code Coverage: coverage.py, Istanbul
  - Security Scanner: Bandit (Python), npm audit (JS)

---

## 💡 Sprachspezifische Erweiterungen

### 🐍 Python
- Befolge **PEP 8** & „Zen of Python“ (`import this`)  
- Typannotationen (z. B. `def foo(x: int) -> str:`)  
- Verwende Context Manager:
```python
from pathlib import Path
import json

def read_json(path: Path) -> dict:
    with path.open() as f:
        return json.load(f)
```

### 🚀 JavaScript / TypeScript
- `const` statt `var`, sprechende Namen
```js
const currentDate = new Date();
```
- Funktionale Programmierung & unveränderliche Strukturen:
```js
const addProp = (obj, key, value) => ({ ...obj, [key]: value });
```
- Destructuring & Encapsulation:
```js
function sum({ a, b }) {
  return a + b;
}
```

---

## 📕 Quick-Reference Cheat Sheet

| Prinzip / Pattern              | Beschreibung                                        |
|-------------------------------|-----------------------------------------------------|
| **KISS**                      | Einfachheit vor Komplexität                        |
| **DRY**                       | Vermeidung von Duplikaten                          |
| **SOLID**                     | Struktur & Wartbarkeit durch OOP                   |
| **Boy Scout Rule**           | Code sauberer hinterlassen                         |
| **POLA**                      | Kein überraschendes Verhalten                      |
| **Sprechende Namen**         | Klarheit in Variablen- und Funktionsnamen          |
| **Kurze Funktionen**         | Eine Verantwortung pro Funktion                    |
| **Formatter/Linter**         | Automatische Durchsetzung des Stils               |
| **TDD**                      | Qualität von Anfang an sichern                     |
| **Reine Funktionen**         | Eingabe → Ausgabe ohne Nebeneffekte                |
| **Typen & Sicherheit**       | Type Hints (Python), Typensicherheit (TS/JS)       |

---

## 🔚 Fazit
Diese Datei liefert **umfassende Clean-Code-Standards mit konkreten Beispielen**, sofort anwendbar und nach Code-Monster-Anspruch komplett – nichts fehlt, du bist voll ausgestattet.
