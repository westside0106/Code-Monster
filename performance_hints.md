# Performance Hints – Code‑Monster ⚡️

## 🎯 Zielsetzung
Maßnahmen und Techniken zur **Identifikation, Analyse und Optimierung** von Performance-Engpässen – zügig und zielgerichtet im echten Projektumfeld.

---

## 📊 1. Benchmark & Messen zuerst
- Messen statt raten: Profiler wie `cProfile`/`pyinstrument`, Chrome DevTools, `perf` verwenden .
- Realistische Workloads: Test-Umgebung simuliert Produktionslast.

---

## ⏱️ 2. Hotspots identifizieren
- CPU‑ vs. I/O‑Bound unterscheiden  
- Profiling für Flaschenhälse, nicht für Geschwindigkeitsvergleiche

---

## 🎯 3. Algorithmus vor Struktur
- O(n) besser als O(n²) – komplexitätskritische Teile priorisieren  
- Datenstrukturen: `dict`/`set` statt `list` bei Suche

---

## 🛰️ 4. Asynchronität & Parallele Leitung
- Python: `asyncio`, `concurrent.futures`  
- JS: `async/await`, Web Workers  
- Caching vs. Threads – Wahl bewusst treffen

---

## 🧠 5. Caching & Memoization
- `functools.lru_cache` (Python) oder `memoize` Module  
- Datenbank/HTTP Ergebnisse lokal zwischenspeichern  
- Invalidation definieren, statt ewige Caches

---

## 🧩 6. Lazy Loading & Ressourcen Management
- Module, Daten structure erst laden, wenn nötig  
- Verbindungspools für Datenbank, HTTP, Redis

---

## 📦 7. Batch-Prozesse & Bulk-Operationen
- Statt Einzeloperationen: Batches – Datenbank, API, Dateien  
- Extraktion optimiert: CSV/Feather/Parquet statt JSON bei großen Daten

---

## 🔗 8. Netzwerk & Datenübertragung
- GZIP/HTTP2, Proxy & CDN, Keep-Alive aktiv  
- Payload minimal halten, Pagination nutzen

---

## 🖥️ 9. Frontend-Spezifika
- JS: Minify, Code Splitting, Lazy Component Loading  
- Web: Brotli/GZIP, Caching via Service Worker

---

## 🛠️ 10. Tools & CI/CD Integration
- Python: **pytest-benchmark**, `timeit`  
- JS: **Lighthouse**, **WebPageTest**  
- System: **JMeter**, **k6**, **Locust**  
- Performance-Messung Bestandteil in CI-Pipeline 

---

## 📋 Quick-Checklist

| Bereich                 | Empfehlung                                             |
|-------------------------|--------------------------------------------------------|
| Messen                  | Profiling statt Vermutung                              |
| Hotspots                | CPU vs. I/O klar identifizieren                        |
| Algorithmen             | Data-Strukturen & O‑Notation priorisieren              |
| Parallelität            | Async, Threads, Caching gezielt nutzen                 |
| Batch & Ressourcen      | Bulk statt Einzeloperationen                           |
| Netzwerkoptimierung     | Kompression, Caching, minimaler Payload                |
| Tools                   | Regelmäßige Performance-Tests in CI                    |

---

## 🔚 Fazit
Mit `performance_hints.md` bist du bestens ausgestattet: Messen, optimieren und integrieren von Performance-Instrumenten ist jetzt Teil des Code-Monster Fahrplans. Kein Platz für Ratespiel – nur datengetriebene, effektive Optimierung.