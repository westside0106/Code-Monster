# Refactoring Tips – Code‑Monster 🛠️

## 🎯 Zielsetzung
Refactoring ist die systematische **Umstrukturierung bestehenden Codes**, ohne das Verhalten zu ändern – für bessere Lesbarkeit, Wartbarkeit und weniger technischen Schulden  [oai_citation:0‡easyappointments.org](https://easyappointments.org/blog/best-practices-on-code-refactoring/?utm_source=chatgpt.com) [oai_citation:1‡medium.com](https://medium.com/swlh/the-ultimate-engineers-guide-to-code-refactoring-c38372632906?utm_source=chatgpt.com).

---

## 📌 1. Wann refaktorisieren?

- **Vor neuen Features**: verbesserte Codebasis als Fundament ()  
- **Bei drittem Duplikat**: nach der „Rule of Three“ abstrahieren  [oai_citation:2‡en.wikipedia.org](https://en.wikipedia.org/wiki/Rule_of_three_%28computer_programming%29?utm_source=chatgpt.com)  
- **Code-Review & Sprint-Ende**: nutzt letzte Chance vor Release ()

---

## 🔍 2. Typische Code Smells erkennen

- **Lange Methoden**, **unklare Namen**, **Duplikate**, **magische Zahlen**, **Data Clumps**, **Excessive Comments**  [oai_citation:3‡en.wikipedia.org](https://en.wikipedia.org/wiki/Code_smell?utm_source=chatgpt.com)  
- **Design-Smells** wie zu große Klassen, zyklische Abhängigkeiten etc.  [oai_citation:4‡en.wikipedia.org](https://en.wikipedia.org/wiki/Design_smell?utm_source=chatgpt.com)

---

## 🔧 3. Refactoring-Techniken

### Methoden & Variablen
- Extract/Inline Method, Extract Variable, Replace Temp with Query  [oai_citation:5‡refactoring.guru](https://refactoring.guru/refactoring/techniques?utm_source=chatgpt.com)  
- Rename Method/Variable für Klarheit, Remove Magic Numbers

### Struktur & Klassen
- Extract/Inline Class, Move Method/Field, Hide Delegate, Introduce Parameter Object  [oai_citation:6‡digma.ai](https://digma.ai/java-code-refactoring/?utm_source=chatgpt.com) [oai_citation:7‡refactoring.guru](https://refactoring.guru/refactoring/techniques?utm_source=chatgpt.com)

### Kontrollstrukturen
- Replace Nested Conditional with Guard Clauses, Consolidate Conditional, Introduce Null Object  [oai_citation:8‡refactoring.guru](https://refactoring.guru/refactoring/techniques?utm_source=chatgpt.com)

### Abstraktion
- Pull Up/Push Down Method, Replace Type Code with State/Strategy, etc.  [oai_citation:9‡refactoring.guru](https://refactoring.guru/refactoring/techniques?utm_source=chatgpt.com)

---

## 📈 4. Refactoring-Prozess

1. **Tests sichern**: Unit-Tests abdecken, damit Verhalten stabil bleibt ()  
2. **Kleine Schritte**: iterativ, Tests nach jedem Schritt laufen lassen  [oai_citation:10‡refactoring.guru](https://refactoring.guru/refactoring?utm_source=chatgpt.com)  
3. **Automatisierte Tools nutzen**: IDE-Refactorings (z. B. IntelliJ, PyCharm, Eclipse) ()  
4. **Code-Smells entfernen**, sauber dokumentieren

---

## 🧩 5. Best Practices & Mindset

- **Focus on Readability** – verständlicher Code ist das Ziel  [oai_citation:11‡refactoring.guru](https://refactoring.guru/refactoring?utm_source=chatgpt.com) [oai_citation:12‡easyappointments.org](https://easyappointments.org/blog/best-practices-on-code-refactoring/?utm_source=chatgpt.com)  
- **DRY-Prinzip** beibehalten – Duplikate beseitigen ()  
- **Planen, nicht perfektionieren** – Refactoring sprinten, nicht endlos dran bleiben  [oai_citation:13‡medium.com](https://medium.com/swlh/the-ultimate-engineers-guide-to-code-refactoring-c38372632906?utm_source=chatgpt.com)  
- **QA-Integration** – Qualitätsteam früh einbinden ()  
- **Toolunterstützung** – Linter, Static Analysis, IDE helfen Fehler vermeiden  [oai_citation:14‡easyappointments.org](https://easyappointments.org/blog/best-practices-on-code-refactoring/?utm_source=chatgpt.com)

---

## 🗃️ 6. Refactoring-Checkliste

| Schritt                   | Empfehlung                                                                 |
|---------------------------|----------------------------------------------------------------------------|
| Tests vorhanden           | ✅ Unit-Tests für Funktionen/Methoden                                      |
| Code smells erkannt       | ✅ Duplikate, lange Methoden, magische Werte etc.                          |
| Kleine, isolierte Schritte| ✅ Refactoring in kleinen Commits                                          |
| Automatisierte Tools      | ✅ IDE-Refactorings und Linters                                            |
| Klar benannte Änderungen  | ✅ PR mit Refactoring-Zweck + Checkliste                                   |
| QA involviert             | ✅ Review durch Team/QA                                                    |

---

## 🔚 Fazit

`refactoring_tips.md` liefert dir eine **vollständige, produktionsfähige Route** vom Erkennen von Smells über Techniken bis zur sauberen Umsetzung – Code‑Monster-Level.