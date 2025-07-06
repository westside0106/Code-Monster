
# Logging Strategies – Code‑Monster 🧠

## 🎯 Zielsetzung
Leitfaden zur Erstellung von **effektiven, sicheren und analysierbaren Logs** – von Design über Produktion bis Monitoring.

---

## 📌 1. Ziele & Planung
- Definiere klare Log-Ziele: Debugging, Auditing, Performance-Monitoring
- Review-Meeting zur Anpassung der Log-Level regelmäßig durchführen

---

## 🧭 2. Log-Level richtig anwenden
- DEBUG: Entwicklung & tiefgehende Diagnosen
- INFO: normale Betriebsinformationen
- WARN: unerwartete, aber nicht kritische Ereignisse
- ERROR/FATAL: kritische Fehler, die sofortiges Eingreifen brauchen
- In Produktion oft >= INFO, Debug nur lokal

---

## 🧱 3. Strukturierte Logs
- Nutze JSON oder key=value-Format statt unstrukturierter Texte
- Beispiel (Python mit structlog):

```python
import structlog
import logging

logging.basicConfig(format="%(message)s", level=logging.INFO)
log = structlog.get_logger()
log.info("User login", user_id="1234", ip="192.0.2.0")
```

---

## 🧰 4. Modulbasierte Logger
- Initialisiere Logger pro Modul: `logger = logging.getLogger(__name__)`
- In Libraries: NullHandler verwenden, damit Frameworks eigene Konfiguration erlauben

---

## ⏱️ 5. Zeitstempel & Kontext
- Nutze konsistentes ISO‑8601 Format mit Zeitzone
- Ergänze Logs um Kontext: module, user_id, request_id etc.

---

## 📝 6. Bedeutungvolle Log-Messages
- Schreibe klar, ausreichend, aber kurz
- Beispiel: `log.error("File not found: %s", filename)` statt `"error"`
- Paare Start/End-Logs ermöglichen Laufzeitmessung

---

## 🔐 7. Schutz & Datenschutz
- Verzichte auf persönliche Daten, Passwörter, Tokens
- Logs verschlüsseln und Zugriff strikt beschränken

---

## 🔄 8. Rotations- & Retention-Strategie
- Log‑Rotation basierend auf Größe/Zeit – z. B. `RotatingFileHandler`
- Klar definierte Aufbewahrungszeiten

---

## 🗃️ 9. Zentralisierung & Aggregation
- Log-Stapel: Fluentd, Fluent Bit, Logstash, CloudWatch, Datadog
- Zentrale Speicherung ermöglicht gute Suche & Dashboards

---

## 🖥️ 10. Performance & Sampling
- Achte auf Overhead durch Logging, besonders DEBUG in Prod
- Nutze Sampling bei hoher Log-Dichte

---

## 🛠️ 11. Automatismus & CI/CD Integration
- Log-Config automatisch laden (z. B. via YAML/JSON)
- CI-Check auf Logging-Standards integrieren (z. B. via CodeQL)
- Deployment: dynamisch Log-Level via ENV-Variablen

---

## 📚 12. Beobachtungen & Checkliste

| Bereich        | Maßnahmen                                                                 |
|----------------|----------------------------------------------------------------------------|
| Log-Level      | DEBUG nur lokal, INFO+ in Produktion                                      |
| Struktur       | JSON/kv, Modul-Kontext, Zeitstempel ISO-8601                              |
| Inhalte        | Start/End, Kontextfelder, klare Messages                                  |
| Datenschutz    | Keine sensiblen Daten, Verschlüsselung, Zugriffskontrolle                 |
| Rotation       | RotatingHandler, Retention pro Level                                      |
| Zentralisierung| Fluentd/Logstash/CloudWatch/Splunk zentral                               |
| Performance    | Sampling, Rate-Limit, asynchron, Format minimal                           |
| Automatisierung| CI/CD‑Checks, ENV‑Config, Deployment-Anpassung                            |

---

## 💡 Sprachbeispiele

### 🚀 JavaScript / Node.js (Winston + JSON)
```js
const { createLogger, transports, format } = require('winston');
const logger = createLogger({
  level: process.env.LOG_LEVEL || 'info',
  format: format.json(),
  defaultMeta: { service: 'user-service' },
  transports: [
    new transports.Console(),
    new transports.File({ filename: 'app.log', level: 'error' })
  ]
});
logger.info('Data processed', { userId: 123, durationMs: 34 });
```

---

## 🆕 13. Fazit
`logging_strategies.md` ist dein umfassender Guide für robuste, kontextreiche Logging-Infrastruktur – inklusive Struktur, Performance, Sicherheit und vollständigem CI/CD. Alles drin, nichts fehlt – dein 100 % Code‑Monster-Modul.
