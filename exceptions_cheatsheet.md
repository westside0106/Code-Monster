
# Exceptions Cheat Sheet – Code‑Monster ⚠️

## 🎯 Zielsetzung
Best Practices für robustes Exception Handling: Verständlich, sicher und wartungsfreundlich – absolut produktionsreif.

---

## 🧠 Prinzipien & Patterns

### ✅ 1. Nur behandeln, was du kontrollieren kannst  
- Fange Exceptions nur, wenn du wirklich reagieren kannst

### ✅ 2. Spezifische Exceptions  
- Immer präzise fangen (z. B. `ValueError`, `FileNotFoundError`, nicht `Exception`)

### ✅ 3. Exceptions nicht verschlucken  
- Kein Leercatch, kein Hinwegwerfen ohne Logging

### ✅ 4. Chaining/Wrapping nutzen  
- Wrappe tiefere Exceptions in eigene – `raise X from Y`

### ✅ 5. Exceptions nur bei echten Ausnahmen  
- Kein Ersatz für normale Flusssteuerung

### ✅ 6. Ressourcen absichern  
- Nutze `finally`, `with` oder `try-with-resources` (Java)

---

## 📌 Sprachspezifische Beispiele

### 🐍 Python

```python
try:
    with open(path) as f:
        data = json.load(f)
except FileNotFoundError as e:
    log.error("File not found", path=path, error=e)
    raise CustomAppError("Load failed") from e
finally:
    cleanup()
```

---

### 🚀 JavaScript / Node.js

```js
try {
  const data = await fs.promises.readFile(path);
} catch (e) {
  logger.error("Failed to read file", { path, err: e });
  throw new AppError("Cannot load config", e);
}
```

---

### ☕ Java

```java
try (InputStream in = Files.newInputStream(path)) {
  ...
} catch (IOException e) {
  logger.error("Unable to open file {}", path, e);
  throw new MyCustomException("Config load failed", e);
}
```

---

## 🧩 Exception-Safety Levels  
- Basic: Zustand valide  
- Strong: Transaktionssicherheit  
- No-throw: garantiert keine Exceptions

---

## 🗂️ Common Anti-Patterns  

| Anti-Pattern             | Problem                              |
|--------------------------|--------------------------------------|
| Leeres catch             | Fehler wird verschluckt              |
| Rethrow ohne Kontext     | Verlust Root-Cause (`throw e.msg`)   |
| Fangen aller Exceptions  | Kontextverlust, unklarer Zustand     |

---

## 📋 Quick-Checkliste

- [x] Nur behandeln, wenn nötig  
- [x] Spezifisch fangen  
- [x] Fehler korrekt loggen  
- [x] Exceptions weiterreichen (`from e`)  
- [x] Ressourcen mit `finally`, `with`, `try-with-resources`  
- [x] Kein stilles Verschlucken  
- [x] Aussagekräftige Fehlertexte für User

---

## 🔚 Fazit
Volle Exception-Handling-Power – für robuste, wartbare und verständliche Software. Dieses Cheat Sheet ist sofort einsetzbar – 100 % Code‑Monster-ready.
