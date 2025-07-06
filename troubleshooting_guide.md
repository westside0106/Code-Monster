# 🛠️ Troubleshooting Guide – Python

Ein kompakter Leitfaden zur Fehlersuche bei Python-Projekten – ideal für Debugging, CI, Onboarding und Fehleranalyse.

---

## 1. Syntax- & Indentation-Fehler  
- Häufige Ursachen: fehlender Doppelpunkt, falsche Einrückung  
- 🔍 **Tipp**: Der Traceback zeigt „^“-Marker – prüfe davor liegende Zeile  [oai_citation:0‡tabnine.com](https://www.tabnine.com/blog/python-code-debugging-common-bugs-tools-and-best-practices/?utm_source=chatgpt.com) [oai_citation:1‡docs.python.org](https://docs.python.org/3/tutorial/errors.html?utm_source=chatgpt.com)  
- Tools: `ruff`, `flake8`, `black`, IDEs (VS Code, PyCharm)

---

## 2. Laufzeit- (Runtime) Fehler  
- Typische Fehler:
  - `ZeroDivisionError`, `TypeError`, `NameError`, `KeyError`  [oai_citation:2‡reddit.com](https://www.reddit.com/r/learnpython/comments/16lm3xf/what_tips_and_tricks_do_you_have_to_make/?utm_source=chatgpt.com) [oai_citation:3‡docs.python.org](https://docs.python.org/3/tutorial/errors.html?utm_source=chatgpt.com)  
  - `AttributeError`, `FileNotFoundError`, `PermissionError`  
- Lösung:
  - Logs + lokale Tests gegen CI  
  - Tracebacks zurückverfolgen, Variablenwerte prüfen

---

## 3. Logik-Fehler  
(z. B. falsche Algorithmen, unerwartete Schleifen)  
- Typischerweise fallen sie in Unit-/Integrationstests auf  
- 🛠️ Debugging mit `print()`, `logging`, `pdb.set_trace()`  
- 👇 **Reddit-Tipp**: Teste nach jedem Funktions‑Step, um Ursprung einzugrenzen  [oai_citation:4‡studentrobotics.org](https://studentrobotics.org/docs/troubleshooting/python?utm_source=chatgpt.com)

---

## 4. Struktur- & Importprobleme  
- Vorsicht mit relativen Importen → `ModuleNotFoundError`, zirkulären Abhängigkeiten  
- **Checkliste**:
  - `__init__.py` vorhanden?
  - Paketstruktur stimmt mit `project.toml`/`setup.py` überein?

---

## 5. Synchronisation & Nebenläufigkeit  
- Probleme bei Threads/Async/AIOHTTP – Deadlocks, unvollständige Tasks  
- 🛠️ Nutze Semaphore, `asyncio.run(debug=True)`, Timeout-Manager (in deinen Snippets integriert)

---

## 6. I/O- & File-System-Fehler  
- z. B. `Permission denied`, falscher Interpreter-Shebang  
- ❗ **Typischer Fehler**: Datei ohne Ausführungsrechte direkt starten – Lösung: `python script.py` oder `chmod +x` ()

---

## 7. Abhängigkeits-Konflikte  
- Unterschiedliche Versionen von `requests`, `aiohttp`, `pytest`?  
- ✔️ Empfehlung: Verwende virtuelle Umgebungen + `project.toml` oder `requirements.txt`

---

## 8. Debugging Tools & Workflows  
- **Linters** (`ruff`, `flake8`, `pylint`) decken viele Fehler automatisch  
- **Debugger**: `pdb`, VS Code Breakpoints  
- **Print-Log-Strategie**: Schrittweise testen, um Codebereiche einzugrenzen – analog zu Reddit-Praxis  [oai_citation:5‡reddit.com](https://www.reddit.com/r/learnpython/comments/16lm3xf/what_tips_and_tricks_do_you_have_to_make/?utm_source=chatgpt.com)

---

## 9. Automatisierte Tests  
- TDD: Tests vor Code → verhindert Regressionen  
- 💡 Für CI: Führe `pytest --maxfail=1 --disable-warnings` + `--cov` aus

---

## 10. Fehler-Sammelstellen  
- Nutze `buglist_python_extended.txt` für permanente Dokumentation  
- Issues und Tickets koppeln, um wiederholbare Probleme systematisch zu adressieren  

---

## ✅ Fazit  
Durch systematisches Debugging (Syntax → Runtime → Logik → Struktur) reduziert man Fehlerquellen massiv. Tools & strukturierte Workflows sorgen für skalierbare Codequalität – dein Code-Monster bleibt robust.

---

*Inspiriert von Site24x7, BetterStack, AppAcademy, Reddit & RealPython*  [oai_citation:6‡arxiv.org](https://arxiv.org/abs/2101.09077?utm_source=chatgpt.com)