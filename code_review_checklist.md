# Code Review Checklist – Code‑Monster ✅

## 🎯 Zweck
Strukturierte Checkliste für effektive Code-Reviews – Qualität, Konsistenz, Sicherheit, Wartbarkeit und Team-Kultur im Fokus.

---

## 📏 1. Umfang & Review-Dauer
- [ ] PR enthält **≤400 LOC**  
- [ ] Review-Dauer **≤60 Min** pro Sitzung

## 📝 2. PR-Titel & Beschreibung
- [ ] Klarer Titel
- [ ] PR erklärt **Was** & **Warum**

## 🌐 3. Kontext & lokale Reproduktion
- [ ] Reviewer kann Branch ziehen und das Feature/Problem lokal nachvollziehen

## 📏 4. Lesbarkeit & Stil
- [ ] Einrückung & Format korrekt
- [ ] Aussagekräftige Namen, keine Magic Numbers/Strings
- [ ] Kommentare nur bei notwendiger Erklärung

## 🧠 5. Logik & Funktionalität
- [ ] Funktion erfüllt Ziel komplett & korrekt
- [ ] Edge-Cases abgedeckt
- [ ] Fehlerhandling & Logging robust

## 🔄 6. Architektur & Struktur
- [ ] Methoden kurz (<20 Zeilen), Module klar strukturiert
- [ ] Keine Duplikate gemäß DRY
- [ ] SOLID-Prinzipien & passende Patterns

## ⚙️ 7. Tests & Coverage
- [ ] Unit-Tests vorhanden & schnell
- [ ] Randfälle + Fehler getestet
- [ ] Coverage ≥ 80 %
- [ ] Testcode lesbar & modular

## 🔒 8. Sicherheit & Datenvalidierung
- [ ] Input validiert & escaped
- [ ] Keine sensiblen Daten in Logs/Errors
- [ ] Abhängigkeiten prüfen

## 📈 9. Performance & Ressourcen
- [ ] Keine ineffizienten Loops/Algorithmen
- [ ] Ressourcen korrekt freigegeben
- [ ] Logging nicht übertrieben

## 🧪 10. CI/CD & Deployment
- [ ] Lint → Tests → Security → Build in Pipeline
- [ ] Keine Debug-/Testdaten im Prod-Code
- [ ] Feature Flags oder Deploy-Strategien berücksichtigt

## 📦 11. Branching & Versionierung
- [ ] Feature Flags statt env-Branches
- [ ] Release-Tags (`vX.Y.Z`) genutzt
- [ ] GitOps/IPR-Strategien falls vorhanden

## 🎉 12. Positives Feedback
- [ ] Gute Aspekte im PR herausstellen (Mentoring, Team-Stärkung)

## 🔚 Fazit
Diese Checkliste kombiniert alle wichtigen Review-Kriterien – ergänzt um PR-Größe, Review-Dauer, Kontext und positives Feedback. Damit hast du ein 360°‑Review-Tool im Code‑Monster‑Stil.

---
