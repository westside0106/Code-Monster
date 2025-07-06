# Deployment Basics – Code‑Monster 🚀

## 🎯 Zielsetzung
Ein praxisnaher Deployment-Guide – von CI/CD-Pipelines bis hin zu Strategien wie Blue‑Green, Canary & Rollbacks – für saubere, sichere und ausfallsichere Deployments.

---

## 📦 1. CI/CD-Grundlagen

- **Commit early & often**: kleine, atomare Commits – schnelle Rückmeldung im CI  [oai_citation:0‡dhiwise.com](https://www.dhiwise.com/post/software-deployment-modern-guide?utm_source=chatgpt.com)  
- **Build only once**: ein Artifact pro Deployment – Version identisch durch alle Phasen  [oai_citation:1‡codefresh.io](https://codefresh.io/learn/ci-cd/11-ci-cd-best-practices-for-devops-success/?utm_source=chatgpt.com)  
- **Shared pipelines** (DRY): vermeiden redundanter Pipelines bei Mikroservices  [oai_citation:2‡codefresh.io](https://codefresh.io/learn/ci-cd/11-ci-cd-best-practices-for-devops-success/?utm_source=chatgpt.com)  
- Bewahre Repos, Skripte, Configs versioniert im VCS

---

## ⚙️ 2. Deploy-Strategien

### Blue‑Green Deployment  
- Zwei identische Environments (blue/green), Traffic kann nahtlos umgeschwenkt werden  
- Ermöglicht **Zero Downtime** und sofortiges Rollback  [oai_citation:3‡jetbrains.com](https://www.jetbrains.com/teamcity/ci-cd-guide/ci-cd-best-practices/?utm_source=chatgpt.com) [oai_citation:4‡en.wikipedia.org](https://en.wikipedia.org/wiki/Blue%E2%80%93green_deployment?utm_source=chatgpt.com)

### Canary Releases  
- Neue Version nur für Teil der Nutzer, bevor globales Rollout  
- Ideal, um Risiken zu minimieren

### Rolling Updates  
- Stufenweises Deployment z. B. in Kubernetes, ersetzt Container nach und nach  
- Kein Single Point of Failure

---

## 🔒 3. Rollback- & Recovery-Strategien

- Halte vorheriges Deployment bereit, einfache Rollback-Mechanismen ermöglichen schnelles Zurücksetzen  
- CI/CD-Pipeline sollte Rollbacks automatisiert unterstützen  
- DORA-Metriken zur Performance: Change-Frequency, MTTR, Failure-Rate – Monitoring wichtig  [oai_citation:5‡reddit.com](https://www.reddit.com/r/devops/comments/1fm542y/cicd_strategies_with_environment_specific/?utm_source=chatgpt.com) [oai_citation:6‡en.wikipedia.org](https://en.wikipedia.org/wiki/DevOps?utm_source=chatgpt.com) [oai_citation:7‡en.wikipedia.org](https://en.wikipedia.org/wiki/Coding_best_practices?utm_source=chatgpt.com)

---

## 🌐 4. Umgebungshärtung & Isolation

- Setze staging als Spiegel von production ein  [oai_citation:8‡en.wikipedia.org](https://en.wikipedia.org/wiki/Deployment_environment?utm_source=chatgpt.com)  
- Automatisierte Tests (Smoke, Integration, Performance) vor Go-Live  
- Isolierte Umgebungen (Netzwerk, DB), spezifische Configs, Secrets via Vault oder ENV

---

## 🔁 5. Automatisierung & Toolchain

- CI/CD Pipeline Steps: checkout → build → test → security scan → deploy → observability  
- Tools: GitHub Actions, GitLab CI, Jenkins (für CI, nicht CD), ArgoCD/Spinnaker für Deployments  [oai_citation:9‡plural.sh](https://www.plural.sh/blog/stop-using-jenkins-for-continuous-deployment-cd/?utm_source=chatgpt.com)  
- Automatisiert: Linters, Tests, Security, Performance-Checks (Blackfire, CodeQL, SonarQube)

---

## 📊 6. Monitoring & Rollout-Kontrolle

- Health-Checks, Metrics, Logs, Tracing sollten vor dem Release eingebunden sein  
- Canary-Phasen automatisch überwacht – auf Fehler direkt zurückrollen

---

## 🧩 7. Branch- & Release-Strategien

- **Keine env-spezifischen Branches** – verwende Feature Flags  [oai_citation:10‡en.wikipedia.org](https://en.wikipedia.org/wiki/Blue%E2%80%93green_deployment?utm_source=chatgpt.com) [oai_citation:11‡reddit.com](https://www.reddit.com/r/devops/comments/1fm542y/cicd_strategies_with_environment_specific/?utm_source=chatgpt.com)  
- Tags für Releases (z. B. `v1.2.3`) – Versionierung im VCS  
- GitOps empfohlen: Repos beschreiben Infrastruktur Deployment

---

## 🛠️ 8. Security & Compliance

- “Security-first” Ansatz: SAST/DAST Scans im Pipeline-Prozess  [oai_citation:12‡codefresh.io](https://codefresh.io/learn/ci-cd/11-ci-cd-best-practices-for-devops-success/?utm_source=chatgpt.com) [oai_citation:13‡techradar.com](https://www.techradar.com/pro/breaking-silos-unifying-devops-and-mlops-into-a-unified-software-supply-chain?utm_source=chatgpt.com)  
- STRIDE-basiertes Threat Modeling während Pipeline-Design  [oai_citation:14‡arxiv.org](https://arxiv.org/abs/2506.06478?utm_source=chatgpt.com)

---

## 📋 Quick-Checklist

| Bereich             | Maßnahmen                                                                 |
|---------------------|---------------------------------------------------------------------------|
| CI/CD               | Commit often, build once, shared pipelines                                |
| Deployment          | Blue‑Green, Canary, Rolling                                               |
| Rollback            | Automatisierte Wiederherstellung, MTTR-Monitoring                         |
| Umgebung            | Staging = Prod, Isolation, Secrets via Vault                              |
| Automatisierung     | Lint → Test → Security → Deploy → Monitor                                 |
| Monitoring          | Health Checks, Metrics, Logs, Canary-Monitoring                           |
| Branching           | Release Tags & Feature Flags, kein env-Split                              |
| Security            | SAST/DAST, Threat Modeling STRIDE, Compliance                             |

---

## 🔚 Fazit
`deployment_basics.md` ist dein Kompletttool für moderne, sichere & ausfallsichere Deployments – 100 % Code‑Monster-ready. Nichts fehlt, jede Stage abgedeckt.  
