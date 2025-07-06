# 🧪 Testing Complete – pytest_guide.md + testing_strategies.md

## 🔹 Quelle 1: pytest_guide.md

# Pytest Guide – Code‑Monster 🧪

## 🎯 Zielsetzung
Umfassender Leitfaden zur Nutzung von **pytest** — vom Setup bis zu Testorganisation, Parametrisierung, Markern, Fixtures und CI‑Integration. Maximale Effizienz & Lesbarkeit.

---

## 1. Setup & Projektstruktur

```bash
python -m venv .venv
source .venv/bin/activate
pip install pytest pytest-cov pytest-xdist pytest-html pytest-mock
```

Vorgeschlagene Struktur:
```
project/
├── src/…             # Produktionscode
├── tests/
│   ├── test_module.py
│   └── conftest.py   # gemeinsame Fixtures
└── pytest.ini        # zentrales Config-File
```

---

## 2. Test Discovery & Konfiguration

Standard-Regeln:
- Dateien: `test_*.py` oder `*_test.py`
- Funktionen/Klassen: Prefix `test_`

Beispiel `pytest.ini`:
```ini
[pytest]
addopts = -v --cov=src --cov-report=xml
python_files = tests/test_*.py
markers =
    slow: mark slow tests
    integration: mark integration-level tests
```

---

## 3. Fixtures & Setup/Teardown

▶ Verwende `conftest.py` für globale Fixtures  
Beispiel:
```python
import pytest

@pytest.fixture(scope="session")
def db():
    conn = setup_db()
    yield conn
    conn.close()
```

---

## 4. Parameterisierung & Data-Driven Tests

```python
import pytest

@pytest.mark.parametrize("inp,expected", [(2,4),(3,9),(5,25)])
def test_square(inp, expected):
    assert square(inp) == expected
```

---

## 5. Marker: Gruppen, Priorität & Skips

```python
@pytest.mark.slow
def test_heavy():
    ...
```

---

## 6. Assertions & Reporting

Nutze native `assert`, bessere Reports mit `pytest-html`, `pytest-cov`, `pytest-xdist`.

---

## 7. Mocks & Monkeypatch

```python
def test_api_call(mocker):
    m = mocker.patch('app.requests.get')
    m.return_value.json.return_value = {"ok": True}
    assert fetch() is True
```

---

## 8. Klassen und Setup/Teardown im Test

Bevorzuge Fixtures über Testklassen.

---

## 9. Beste Praktiken

- AAA‑Pattern (Arrange – Act – Assert)
- Test‑Unabhängigkeit, keine Seiteneffekte

---

## 10. CI/CD-Integration

```bash
pytest --cov=src --junitxml=report.xml
```

Parallel mit:
```bash
pytest -n auto
```

---

## 11. Flaky Tests

```python
@pytest.mark.flaky(reruns=2)
def test_flaky():
    ...
```

---

## 12. Erweiterte Tipps

- HTML-Reports: `--html=report.html`  
- Benchmarking: `pytest-benchmark`  
- BDD: `pytest-bdd`

---

## 📕 Schnelle Übersicht

| Thema            | Empfehlung                            |
|------------------|----------------------------------------|
| Projektstruktur  | `src/`, `tests/`, `conftest.py`       |
| Config File      | `pytest.ini`                           |
| Fixtures         | `yield` für Teardown                   |
| Parameterisierung| `@pytest.mark.parametrize`            |
| Marker           | `slow`, `integration`                 |
| Mocks            | `pytest-mock`, `monkeypatch`          |
| CI Integration   | Coverage, Reports, Paralleltests      |

---

## 🔚 Fazit
Vollständig konfigurierter Pytest‑Guide für Code‑Monster – produktionsbereit.

---

## 🔹 Quelle 2: testing_strategies.md

# Testing Strategies – Code‑Monster 🧪

## 🎯 Zielsetzung
Definiert Strategien, um maximale Qualität effizient sicherzustellen. Fokus: Klarheit in Methoden, Priorisierung, Automatisierung & Feedback‑Loops.

---

## 1. Test Strategy vs. Test Plan
- **Test Strategy**: Übergeordnete Ausrichtung – Ziele, Umfang, Methoden, Tools  [oai_citation:0‡amazon.com](https://www.amazon.com/Software-Testing-Strategies-testing-guide/dp/1837638020?utm_source=chatgpt.com) [oai_citation:1‡en.wikipedia.org](https://en.wikipedia.org/wiki/Continuous_testing?utm_source=chatgpt.com)  
- **Test Plan**: Projekt-spezifische Umsetzung – Testfälle, Rollen, Zeitplan.

---

## 2. Start Early & Shift-Left
- Testen möglichst im frühen SDLC – spart Zeit & Kosten  [oai_citation:2‡ranorex.com](https://www.ranorex.com/blog/software-testing-strategies/?utm_source=chatgpt.com)  
- Unit Tests beim Entwickeln, Integrations-/Systemtests bereits im Sprint.

---

## 3. Kombiniere Manuell + Automatisiert
- Manuelles Exploratory Testing + automatisierte Regression für Effizienz  [oai_citation:3‡de.wikipedia.org](https://de.wikipedia.org/wiki/Agiles_Testen?utm_source=chatgpt.com) [oai_citation:4‡ranorex.com](https://www.ranorex.com/blog/software-testing-strategies/?utm_source=chatgpt.com)  
- Teams kombinieren beides – menschliche Einsicht + Skalierbarkeit.

---

## 4. Risiko-basierte Strategie (Risk‑Based Testing)
- Priorisiere Tests nach Risiko (Likelihood & Impact)  [oai_citation:5‡bugbug.io](https://bugbug.io/blog/test-automation/software-testing-best-practices/?utm_source=chatgpt.com) [oai_citation:6‡en.wikipedia.org](https://en.wikipedia.org/wiki/Risk-based_testing?utm_source=chatgpt.com)  
- Fokussiert Testaufwand auf kritische Teile – Bessere Effizienz & Qualität.

---

## 5. Data‑Driven & Parametrisierung
- Trenne Testlogik von Testdaten  [oai_citation:7‡realpython.com](https://realpython.com/pytest-python-testing/?utm_source=chatgpt.com) [oai_citation:8‡en.wikipedia.org](https://en.wikipedia.org/wiki/Data-driven_testing?utm_source=chatgpt.com)  
- Ideal in pytest/JUnit: mehrere Inputs, gleiche Logik.

---

## 6. Continuous Testing (CI/CD)
- Automatisierte Tests bei jedem Commit – schnelles Feedback  [oai_citation:9‡en.wikipedia.org](https://en.wikipedia.org/wiki/Continuous_integration?utm_source=chatgpt.com) [oai_citation:10‡de.wikipedia.org](https://de.wikipedia.org/wiki/Agiles_Testen?utm_source=chatgpt.com)  
- Ergänze Static Analysis, Security Tests, Deployment Checks.

---

## 7. Testtypen & Ebenen
- **Unit Tests**: Methoden, Klassen (isoliert)  
- **Integration Tests**: Schnittstellen, Datenbanken  
- **System / E2E Tests**: Gesamtfluss  
- **Exploratory Tests**: menschliche Qualitätssicherung  
- **Performance / Load Tests** – messen Skalierungslimits

---

## 8. Pytest Best Practices
- Fixtures & parametrische Tests reduzieren Boilerplate  [oai_citation:11‡en.wikipedia.org](https://en.wikipedia.org/wiki/Continuous_testing?utm_source=chatgpt.com) [oai_citation:12‡medium.com](https://medium.com/tomtalkspython/mastering-pytest-a-comprehensive-guide-for-python-developers-99eb39998d81?utm_source=chatgpt.com) [oai_citation:13‡blog.mergify.com](https://blog.mergify.com/pytest-in-python/?utm_source=chatgpt.com)  
- Structuring tests: `<module>/tests/`, `conftest.py`, `pytest.ini`  [oai_citation:14‡reddit.com](https://www.reddit.com/r/Python/comments/o2pcj1/what_are_best_practices_with_pytest/?utm_source=chatgpt.com)  
- Keep tests independent, klare Benennung, Edge‑Cases abdecken  [oai_citation:15‡medium.com](https://medium.com/tomtalkspython/mastering-pytest-a-comprehensive-guide-for-python-developers-99eb39998d81?utm_source=chatgpt.com)

---

## 9. JavaScript / Jest
- `describe()` + `test()` sauber strukturieren  
- Mocking/Stubbing für isolierte Tests

---

## 10. BDD & Acceptance
- Akzeptanztests per BDD (Cucumber, SpecFlow)  [oai_citation:16‡betterstack.com](https://betterstack.com/community/guides/testing/pytest-guide/?utm_source=chatgpt.com) [oai_citation:17‡de.wikipedia.org](https://de.wikipedia.org/wiki/Agiles_Testen?utm_source=chatgpt.com)  
- Menschlich lesbar → Anforderungen <-> Tests spiegeln sich.

---

## 11. Metriken & Qualität
- Messen: Test Coverage, Testdauer, Defect Density, Flaky Test Rate  
- Continuous Feedback im Dev Board → immer nachbessern  [oai_citation:18‡de.wikipedia.org](https://de.wikipedia.org/wiki/Agiles_Testen?utm_source=chatgpt.com) [oai_citation:19‡bugbug.io](https://bugbug.io/blog/test-automation/software-testing-best-practices/?utm_source=chatgpt.com)

---

## 12. Tools & Automatisierung

| Bereich                 | Tools                                  |
|-------------------------|----------------------------------------|
| Unit Tests              | pytest, JUnit, Jest                    |
| Integration Tests       | pytest, Mocha, Selenium, Supertest     |
| Test Data Management    | Fixtures, Factories, Testcontainers    |
| Coverage                | coverage.py, Istanbul/NYC              |
| CI Integration          | Jenkins, GitHub/Lab Actions, CircleCI  |
| Performance             | JMeter, k6, Locust                     |
| Security Testing        | OWASP ZAP, Bandit, npm audit           |

---

## 13. Prozess & Teams
- **Frühe Einbindung**: Tester + Dev im Sprint-Plan  
- **Pair Testing** für komplexe Features  
- **Review Mechanismen**: Test-Cases + Code-Review Hand in Hand

---

## 14. Checkliste – auf einen Blick

- [ ] Strategy dokumentiert: Ziele, Tools, Scope  
- [ ] Frühe Tests & Shift-Left umgesetzt  
- [ ] Risk-Analyse initiiert + priorisiert  
- [ ] Testdaten strukturiert & parametrisiert  
- [ ] CI/Continuous Testing konfiguriert  
- [ ] Test Suites: Unit → Integration → E2E  
- [ ] BDD- bzw. Akzeptanz-Tests definiert  
- [ ] Metriken etabliert & ausgewertet  
- [ ] Automation + manuelles Testing kombiniert  
- [ ] Code- & Test-Reviews im Workflow integriert  

---

## 🔚 Fazit
Diese **Testing Strategy-Datei** stellt sicher, dass dein Projekt max. Qualität bei effizientem Aufwand erzielt – vollständig integriert in dein Code‑Monster‑Setup.