# 🛡️ Security Guide – security_basics.md + security_checklist.md

## 🔹 Quelle 1: security_basics.md

PK    åZ¿ñC  C     Untitled.textbundle/text.md# Security Basics â CodeâMonster ð¡ï¸

## ð¯ Zweck
Grundlagen der sicheren Softwareentwicklung (âSecure by Designâ) â von der Planung bis ins Deployment. Ziel: Sicherheitsfehler vermeiden, bevor sie entstehen.

---

## ð Secure by Design & Secure by Default
- Sicherheitsaspekte **von Anfang an** ins Design aufnehmen (Threat Modeling, geringste Privilegien)  [oai_citation:0â¡en.wikipedia.org](https://en.wikipedia.org/wiki/Secure_by_design?utm_source=chatgpt.com)  
- Standardkonfigurationen so sicher wie mÃ¶glich machen (FeatureâFlags off, unnÃ¶tige Ports zu) ()

---

## ð§© SDLC & DevSecOps Integration
- Sicherheit in allen Phasen des SDLC verankern (Plan â Code â Test â Release â Monitor)  [oai_citation:1â¡securitycompass.com](https://www.securitycompass.com/blog/software-security-requirements-checklist/?utm_source=chatgpt.com)  
- Automatisierte Security-Checks in CI/CD integrieren (SAST, DAST, Dependency Scans, Container Scans)

---

## â Security Checkliste

### 1. Input Validation & Sanitization  
- Alle externen Inputs validieren (Whitelist).  
- Escape & encode Daten â Schutz vor SQLâInjection, XSS etc.  [oai_citation:2â¡xygeni.io](https://xygeni.io/blog/secure-coding-practices-checklist/?utm_source=chatgpt.com)

### 2. Authentifizierung & Autorisierung  
- Starke PasswÃ¶rter, MFA implementieren.  
- Prinzip der kleinsten Rechte: jede Komponente nur mit Minimalprivilegien betreiben.  [oai_citation:3â¡xygeni.io](https://xygeni.io/blog/secure-coding-practices-checklist/?utm_source=chatgpt.com)

### 3. Fehlerâ und Ausnahmemanagement  
- Keine sensiblen Infos in UserâFehlermeldungen.  
- Sichere LoggingâStrategie ohne Leak kritischer Daten. ()

### 4. DatenverschlÃ¼sselung  
- VerschlÃ¼sselung sowohl **at rest** als auch **in transit** (TLS, AESâ256).  
- Secrets nicht hardâcoden â Secure Vault & Rotation verwenden.  [oai_citation:4â¡xygeni.io](https://xygeni.io/blog/secure-coding-practices-checklist/?utm_source=chatgpt.com)

### 5. AbhÃ¤ngigkeitsâManagement  
- Automatische Scans nach bekannten Vulnerabilities (z.â¯B. OWASP DependencyâCheck).  
- DrittanbieterâBibliotheken aktuell halten.  [oai_citation:5â¡en.wikipedia.org](https://en.wikipedia.org/wiki/Code_review?utm_source=chatgpt.com)

### 6. APIâ & NetzwerkâSecurity  
- HTTPS, Input-Checks, Auth/Rate-Limit fÃ¼r APIâEndpoints.  
- Firewall/Segmentation fÃ¼r Netzwerkzugriffe.  [oai_citation:6â¡de.wikipedia.org](https://de.wikipedia.org/wiki/Security_Development_Lifecycle?utm_source=chatgpt.com)

### 7. Automatisierte Security Tests  
- **SAST**: statischer CodeâScan (SonarQube, CodeQL etc.)  [oai_citation:7â¡en.wikipedia.org](https://en.wikipedia.org/wiki/Static_application_security_testing?utm_source=chatgpt.com)  
- **DAST**: Simulation von Angriffen gegen laufende Services.  
- **IAST**: Kombination aus beidem, falls verfÃ¼gbar.

### 8. Code Reviews & Pair-Programming  
- Mindestens ein Reviewer, automatisierte Tools unterstÃ¼tzen  [oai_citation:8â¡securitycompass.com](https://www.securitycompass.com/blog/software-security-requirements-checklist/?utm_source=chatgpt.com) [oai_citation:9â¡en.wikipedia.org](https://en.wikipedia.org/wiki/Static_application_security_testing?utm_source=chatgpt.com) [oai_citation:10â¡en.wikipedia.org](https://en.wikipedia.org/wiki/Code_review?utm_source=chatgpt.com)  
- Fokus: Sicherheitsfehler, Logik-SchwÃ¤chen, XSS-/Injection-Gefahren.

### 9. Monitoring & Incident Response  
- Zentralisiertes Logging (SIEM), automatische Alerts.  
- Vorgeplantes Incident-ResponseâPlaybook inkl. Forensik & Rollback.

---

## ð  Defensive Programming
- Eingaben defensiv Ã¼berprÃ¼fen, Fehler abfangen, sichere Defaults setzen  [oai_citation:11â¡securitycompass.com](https://www.securitycompass.com/blog/software-security-requirements-checklist/?utm_source=chatgpt.com) [oai_citation:12â¡yslingshot.com](https://www.yslingshot.com/security-checklist/?utm_source=chatgpt.com)  
- Assertions und Design by Contract nutzen, um ungÃ¼ltige ZustÃ¤nde frÃ¼h zu erkennen.

---

## ð Ressourcen & Standards
- **OWASP**: Secure Coding Practices, Topâ¯10, ASVS, ZAP, Entwickler-Guides  [oai_citation:13â¡en.wikipedia.org](https://en.wikipedia.org/wiki/Defensive_programming?utm_source=chatgpt.com) [oai_citation:14â¡en.wikipedia.org](https://en.wikipedia.org/wiki/OWASP?utm_source=chatgpt.com)  
- **Microsoft SDL**: Secure by Design, Default, Deployment + Privacy by Design  [oai_citation:15â¡de.wikipedia.org](https://de.wikipedia.org/wiki/Security_Development_Lifecycle?utm_source=chatgpt.com)  
- ISO 27001, NIST SSDF, PCI DSS â je nach Branche relevant  [oai_citation:16â¡securitycompass.com](https://www.securitycompass.com/blog/software-security-requirements-checklist/?utm_source=chatgpt.com)

---

## ð Quick-Reference Checkliste

| Bereich                     | Handlungsempfehlung                                                         |
|----------------------------|------------------------------------------------------------------------------|
| **Design**                 | Threat Model & Principle of Least Privilege verankern                      |
| **Code**                   | Input-Validierung, Output-Encoding, Defensive Programming                  |
| **Authentication & Authz**| MFA, RBAC, SecureâbyâDefault                                                |
| **Error Handling**         | Keine sensiblen Infos in Errors, Logging getrennt                          |
| **Datenschutz**            | TLS, AESâVerschlÃ¼sselung, Secret Management                                |
| **Dependency Scan**        | Tools & regelmÃ¤Ãige Updates                                                 |
| **Security Testing**       | SAST/DAST/IAST in CI/CD pipeline                                            |
| **Review & Monitoring**    | Peer-Review, SIEM, Incident Response Team                                  |

---

## ð¡ Fazit
Mit diesem Guide hast du eine **Handlungssichere Roadmap** zur Implementation sicherer Software von der Architektur bis zur Auslieferung.  
100â¯% Deckung fÃ¼r moderne SecurityâAnforderungen â direkt in CodeâMonster integrierbar.

---PK    åZ               Untitled.textbundle/bin/PK    åZúÜäd      )   Untitled.textbundle/navigatorFilters.json{"notes":true,"markers":true,"synopses":true,"sectionHeaders":true,"images":true,"referenceLinks":true,"links":true,"sceneHeaders":true,"includedFiles":true}PK    åZ               Untitled.textbundle/resources/PK    åZuþÇ  Ç  )   Untitled.textbundle/resources/header.json[
  {
    "alignmentGroup" : "left",
    "id" : "6AF46496-B11A-4B49-8B53-0FA6FCF39800",
    "position" : 0,
    "type" : "blank",
    "value" : ""
  },
  {
    "alignmentGroup" : "center",
    "id" : "A3C45FE8-629F-4AB9-A85A-FA75F7B871F7",
    "position" : 0,
    "type" : "blank",
    "value" : ""
  },
  {
    "alignmentGroup" : "right",
    "id" : "BA1F1D72-7FA8-49A5-A557-563FC81B57C9",
    "position" : 0,
    "type" : "blank",
    "value" : ""
  }
]PK    åZ5pøÏ=  =  +   Untitled.textbundle/resources/settings.json{
  "editorSettings" : {
    "revisionColorIndex" : 0,
    "revisionMode" : false
  },
  "overviewSettings" : {
    "highlightAction" : false,
    "highlightAllDialogue" : false,
    "highlightSceneHeaders" : false,
    "thumbnailSize" : "medium"
  },
  "previewSettings" : {

  },
  "printSettings" : {
    "automaticNumbering" : 0,
    "printCompletedChecklistItems" : true,
    "printCustomPages" : true,
    "printFirstPageHeadersAndFooters" : false,
    "printGeneratedText" : false,
    "printInlineNotes" : false,
    "printParagraphNumbers" : false,
    "printRevisionColor" : false,
    "printRevisionStars" : true,
    "printRevisionsOnly" : false,
    "printSections" : true,
    "printSynopses" : false,
    "printTitlePage" : true,
    "printWatermark" : false,
    "sectionOptions" : {
      "five" : true,
      "four" : true,
      "one" : true,
      "six" : true,
      "three" : true,
      "two" : true
    },
    "templateName" : null
  },
  "uiSettings" : {
    "cursorPosition" : 6065,
    "scrollPosition" : 2153.5,
    "sidebarWidth" : 0
  },
  "version" : 3
}PK    åZ¿à
Ç  Ç  )   Untitled.textbundle/resources/footer.json[
  {
    "alignmentGroup" : "left",
    "id" : "21953AB3-E407-4DF2-837D-DD443E2D4544",
    "position" : 0,
    "type" : "blank",
    "value" : ""
  },
  {
    "alignmentGroup" : "center",
    "id" : "D2380B2B-9148-4580-98E1-20FA9A5D27DA",
    "position" : 0,
    "type" : "blank",
    "value" : ""
  },
  {
    "alignmentGroup" : "right",
    "id" : "0F0C37AB-8ED4-4022-A3C2-C13774B1F438",
    "position" : 0,
    "type" : "blank",
    "value" : ""
  }
]PK    åZ
L$:5  :5  *   Untitled.textbundle/resources/outline.json[
  {
    "id" : "E5EBCA68-0A4C-4912-A757-3B0B1AEF7612",
    "index" : 0,
    "isCollapsed" : false,
    "level" : 1,
    "range" : [
      0,
      36
    ],
    "rawString" : "# Security Basics â CodeâMonster ð¡ï¸",
    "string" : "Security Basics â CodeâMonster ð¡ï¸",
    "type" : "sectionHeader"
  },
  {
    "id" : "1F3432BE-BF6C-4886-8AAE-6AE26DC55CA2",
    "index" : 1,
    "isCollapsed" : false,
    "level" : 2,
    "range" : [
      38,
      11
    ],
    "rawString" : "## ð¯ Zweck",
    "string" : "ð¯ Zweck",
    "type" : "sectionHeader"
  },
  {
    "id" : "B3510958-BEF9-464C-9FFA-75B48E01F8D6",
    "index" : 2,
    "isCollapsed" : false,
    "level" : 2,
    "range" : [
      215,
      42
    ],
    "rawString" : "## ð Secure by Design & Secure by Default",
    "string" : "ð Secure by Design & Secure by Default",
    "type" : "sectionHeader"
  },
  {
    "id" : "A08B5B8C-ACDE-4A64-925F-48B84B880138",
    "index" : 3,
    "isCollapsed" : false,
    "level" : 3,
    "range" : [
      360,
      104
    ],
    "rawString" : "[oai_citation:0â¡en.wikipedia.org](https:\/\/en.wikipedia.org\/wiki\/Secure_by_design?utm_source=chatgpt.com)",
    "string" : "[oai_citation:0â¡en.wikipedia.org] https:\/\/en.wikipedia.org\/wiki\/Secure_by_design?utm_source=chatgpt.com",
    "type" : "link"
  },
  {
    "id" : "19A69EE7-9CEB-40CA-A5E1-7FF709700007",
    "index" : 4,
    "isCollapsed" : false,
    "level" : 2,
    "range" : [
      570,
      34
    ],
    "rawString" : "## ð§© SDLC & DevSecOps Integration",
    "string" : "ð§© SDLC & DevSecOps Integration",
    "type" : "sectionHeader"
  },
  {
    "id" : "43FEFF52-A7BF-4673-A348-E82170A433E4",
    "index" : 5,
    "isCollapsed" : false,
    "level" : 3,
    "range" : [
      695,
      139
    ],
    "rawString" : "[oai_citation:1â¡securitycompass.com](https:\/\/www.securitycompass.com\/blog\/software-security-requirements-checklist\/?utm_source=chatgpt.com)",
    "string" : "[oai_citation:1â¡securitycompass.com] https:\/\/www.securitycompass.com\/blog\/software-security-requirements-checklist\/?utm_source=chatgpt.com",
    "type" : "link"
  },
  {
    "id" : "82B7611C-A08A-46D7-B8C2-07BFBE3B4EEF",
    "index" : 6,
    "isCollapsed" : false,
    "level" : 2,
    "range" : [
      945,
      24
    ],
    "rawString" : "## â Security Checkliste",
    "string" : "â Security Checkliste",
    "type" : "sectionHeader"
  },
  {
    "id" : "5626B15B-66AE-453F-B201-2A7D6A7AF593",
    "index" : 7,
    "isCollapsed" : false,
    "level" : 3,
    "range" : [
      971,
      40
    ],
    "rawString" : "### 1. Input Validation & Sanitization  ",
    "string" : "1. Input Validation & Sanitization",
    "type" : "sectionHeader"
  },
  {
    "id" : "D15AD4A1-2B75-451B-BB04-A7C91241EE1B",
    "index" : 8,
    "isCollapsed" : false,
    "level" : 4,
    "range" : [
      1123,
      108
    ],
    "rawString" : "[oai_citation:2â¡xygeni.io](https:\/\/xygeni.io\/blog\/secure-coding-practices-checklist\/?utm_source=chatgpt.com)",
    "string" : "[oai_citation:2â¡xygeni.io] https:\/\/xygeni.io\/blog\/secure-coding-practices-checklist\/?utm_source=chatgpt.com",
    "type" : "link"
  },
  {
    "id" : "B78BA632-4048-4DBF-AE56-EAF5566A0763",
    "index" : 9,
    "isCollapsed" : false,
    "level" : 3,
    "range" : [
      1233,
      42
    ],
    "rawString" : "### 2. Authentifizierung & Autorisierung  ",
    "string" : "2. Authentifizierung & Autorisierung",
    "type" : "sectionHeader"
  },
  {
    "id" : "95E21F97-6598-4F75-AB97-53A2F84CFDC6",
    "index" : 10,
    "isCollapsed" : false,
    "level" : 4,
    "range" : [
      1406,
      108
    ],
    "rawString" : "[oai_citation:3â¡xygeni.io](https:\/\/xygeni.io\/blog\/secure-coding-practices-checklist\/?utm_source=chatgpt.com)",
    "string" : "[oai_citation:3â¡xygeni.io] https:\/\/xygeni.io\/blog\/secure-coding-practices-checklist\/?utm_source=chatgpt.com",
    "type" : "link"
  },
  {
    "id" : "2545B355-C618-431F-9F18-F50C94A021B5",
    "index" : 11,
    "isCollapsed" : false,
    "level" : 3,
    "range" : [
      1516,
      39
    ],
    "rawString" : "### 3. Fehlerâ und Ausnahmemanagement  ",
    "string" : "3. Fehlerâ und Ausnahmemanagement",
    "type" : "sectionHeader"
  },
  {
    "id" : "C311799E-BF98-41B2-A88F-42E87181108E",
    "index" : 12,
    "isCollapsed" : false,
    "level" : 3,
    "range" : [
      1667,
      29
    ],
    "rawString" : "### 4. DatenverschlÃ¼sselung  ",
    "string" : "4. DatenverschlÃ¼sselung",
    "type" : "sectionHeader"
  },
  {
    "id" : "B093E9A8-CCF5-4560-BEAC-22F16A420D8C",
    "index" : 13,
    "isCollapsed" : false,
    "level" : 4,
    "range" : [
      1841,
      108
    ],
    "rawString" : "[oai_citation:4â¡xygeni.io](https:\/\/xygeni.io\/blog\/secure-coding-practices-checklist\/?utm_source=chatgpt.com)",
    "string" : "[oai_citation:4â¡xygeni.io] https:\/\/xygeni.io\/blog\/secure-coding-practices-checklist\/?utm_source=chatgpt.com",
    "type" : "link"
  },
  {
    "id" : "6F34F896-D690-493F-A66B-86332ED70842",
    "index" : 14,
    "isCollapsed" : false,
    "level" : 3,
    "range" : [
      1951,
      33
    ],
    "rawString" : "### 5. AbhÃ¤ngigkeitsâManagement  ",
    "string" : "5. AbhÃ¤ngigkeitsâManagement",
    "type" : "sectionHeader"
  },
  {
    "id" : "4EC80CF4-06D5-409B-8A77-72BD9A69F16C",
    "index" : 15,
    "isCollapsed" : false,
    "level" : 4,
    "range" : [
      2117,
      99
    ],
    "rawString" : "[oai_citation:5â¡en.wikipedia.org](https:\/\/en.wikipedia.org\/wiki\/Code_review?utm_source=chatgpt.com)",
    "string" : "[oai_citation:5â¡en.wikipedia.org] https:\/\/en.wikipedia.org\/wiki\/Code_review?utm_source=chatgpt.com",
    "type" : "link"
  },
  {
    "id" : "D6DFBF2A-259D-426F-94CF-A1DDA0BCA9CF",
    "index" : 16,
    "isCollapsed" : false,
    "level" : 3,
    "range" : [
      2218,
      33
    ],
    "rawString" : "### 6. APIâ & NetzwerkâSecurity  ",
    "string" : "6. APIâ & NetzwerkâSecurity",
    "type" : "sectionHeader"
  },
  {
    "id" : "74C4BEFD-8364-47DF-A948-356ECD88971E",
    "index" : 17,
    "isCollapsed" : false,
    "level" : 4,
    "range" : [
      2359,
      118
    ],
    "rawString" : "[oai_citation:6â¡de.wikipedia.org](https:\/\/de.wikipedia.org\/wiki\/Security_Development_Lifecycle?utm_source=chatgpt.com)",
    "string" : "[oai_citation:6â¡de.wikipedia.org] https:\/\/de.wikipedia.org\/wiki\/Security_Development_Lifecycle?utm_source=chatgpt.com",
    "type" : "link"
  },
  {
    "id" : "CCF14D2F-AD49-40DB-9BE0-50064BA9C482",
    "index" : 18,
    "isCollapsed" : false,
    "level" : 3,
    "range" : [
      2479,
      38
    ],
    "rawString" : "### 7. Automatisierte Security Tests  ",
    "string" : "7. Automatisierte Security Tests",
    "type" : "sectionHeader"
  },
  {
    "id" : "12DD2315-1084-4F10-A788-B2CC2E3B93CD",
    "index" : 19,
    "isCollapsed" : false,
    "level" : 4,
    "range" : [
      2577,
      123
    ],
    "rawString" : "[oai_citation:7â¡en.wikipedia.org](https:\/\/en.wikipedia.org\/wiki\/Static_application_security_testing?utm_source=chatgpt.com)",
    "string" : "[oai_citation:7â¡en.wikipedia.org] https:\/\/en.wikipedia.org\/wiki\/Static_application_security_testing?utm_source=chatgpt.com",
    "type" : "link"
  },
  {
    "id" : "0A566657-4BA2-4BFA-90BA-C513B755A0C3",
    "index" : 20,
    "isCollapsed" : false,
    "level" : 3,
    "range" : [
      2821,
      40
    ],
    "rawString" : "### 8. Code Reviews & Pair-Programming  ",
    "string" : "8. Code Reviews & Pair-Programming",
    "type" : "sectionHeader"
  },
  {
    "id" : "47EE8E19-3346-4FB9-BC65-9B8720B09CA0",
    "index" : 21,
    "isCollapsed" : false,
    "level" : 4,
    "range" : [
      2924,
      139
    ],
    "rawString" : "[oai_citation:8â¡securitycompass.com](https:\/\/www.securitycompass.com\/blog\/software-security-requirements-checklist\/?utm_source=chatgpt.com)",
    "string" : "[oai_citation:8â¡securitycompass.com] https:\/\/www.securitycompass.com\/blog\/software-security-requirements-checklist\/?utm_source=chatgpt.com",
    "type" : "link"
  },
  {
    "id" : "707901BE-285F-4ACA-BE51-218742676791",
    "index" : 22,
    "isCollapsed" : false,
    "level" : 4,
    "range" : [
      3064,
      123
    ],
    "rawString" : "[oai_citation:9â¡en.wikipedia.org](https:\/\/en.wikipedia.org\/wiki\/Static_application_security_testing?utm_source=chatgpt.com)",
    "string" : "[oai_citation:9â¡en.wikipedia.org] https:\/\/en.wikipedia.org\/wiki\/Static_application_security_testing?utm_source=chatgpt.com",
    "type" : "link"
  },
  {
    "id" : "A002580C-6DF0-476B-96F7-ECB75A93136D",
    "index" : 23,
    "isCollapsed" : false,
    "level" : 4,
    "range" : [
      3188,
      100
    ],
    "rawString" : "[oai_citation:10â¡en.wikipedia.org](https:\/\/en.wikipedia.org\/wiki\/Code_review?utm_source=chatgpt.com)",
    "string" : "[oai_citation:10â¡en.wikipedia.org] https:\/\/en.wikipedia.org\/wiki\/Code_review?utm_source=chatgpt.com",
    "type" : "link"
  },
  {
    "id" : "F90DD050-03C9-4088-A889-5E3B343A5DF5",
    "index" : 24,
    "isCollapsed" : false,
    "level" : 3,
    "range" : [
      3362,
      39
    ],
    "rawString" : "### 9. Monitoring & Incident Response  ",
    "string" : "9. Monitoring & Incident Response",
    "type" : "sectionHeader"
  },
  {
    "id" : "66C0BEB9-5686-46BB-ACFA-4CB78A62FA78",
    "index" : 25,
    "isCollapsed" : false,
    "level" : 2,
    "range" : [
      3534,
      27
    ],
    "rawString" : "## ð  Defensive Programming",
    "string" : "ð  Defensive Programming",
    "type" : "sectionHeader"
  },
  {
    "id" : "7213F045-63DB-45FC-9CE3-C46AF816A6B8",
    "index" : 26,
    "isCollapsed" : false,
    "level" : 3,
    "range" : [
      3636,
      140
    ],
    "rawString" : "[oai_citation:11â¡securitycompass.com](https:\/\/www.securitycompass.com\/blog\/software-security-requirements-checklist\/?utm_source=chatgpt.com)",
    "string" : "[oai_citation:11â¡securitycompass.com] https:\/\/www.securitycompass.com\/blog\/software-security-requirements-checklist\/?utm_source=chatgpt.com",
    "type" : "link"
  },
  {
    "id" : "863FF7FE-2E3F-4414-93ED-0F6FC1F53321",
    "index" : 27,
    "isCollapsed" : false,
    "level" : 3,
    "range" : [
      3777,
      103
    ],
    "rawString" : "[oai_citation:12â¡yslingshot.com](https:\/\/www.yslingshot.com\/security-checklist\/?utm_source=chatgpt.com)",
    "string" : "[oai_citation:12â¡yslingshot.com] https:\/\/www.yslingshot.com\/security-checklist\/?utm_source=chatgpt.com",
    "type" : "link"
  },
  {
    "id" : "752A87DD-1582-4E51-AD9D-B7B3252AF9EF",
    "index" : 28,
    "isCollapsed" : false,
    "level" : 2,
    "range" : [
      3973,
      28
    ],
    "rawString" : "## ð Ressourcen & Standards",
    "string" : "ð Ressourcen & Standards",
    "type" : "sectionHeader"
  },
  {
    "id" : "DBC7DC28-3299-475A-A43E-9043527AB0CD",
    "index" : 29,
    "isCollapsed" : false,
    "level" : 3,
    "range" : [
      4078,
      110
    ],
    "rawString" : "[oai_citation:13â¡en.wikipedia.org](https:\/\/en.wikipedia.org\/wiki\/Defensive_programming?utm_source=chatgpt.com)",
    "string" : "[oai_citation:13â¡en.wikipedia.org] https:\/\/en.wikipedia.org\/wiki\/Defensive_programming?utm_source=chatgpt.com",
    "type" : "link"
  },
  {
    "id" : "AB430F05-1C6E-4F9F-A812-D7D37340FDC1",
    "index" : 30,
    "isCollapsed" : false,
    "level" : 3,
    "range" : [
      4189,
      94
    ],
    "rawString" : "[oai_citation:14â¡en.wikipedia.org](https:\/\/en.wikipedia.org\/wiki\/OWASP?utm_source=chatgpt.com)",
    "string" : "[oai_citation:14â¡en.wikipedia.org] https:\/\/en.wikipedia.org\/wiki\/OWASP?utm_source=chatgpt.com",
    "type" : "link"
  },
  {
    "id" : "F50B8494-A932-4988-9538-2B912826C7FF",
    "index" : 31,
    "isCollapsed" : false,
    "level" : 3,
    "range" : [
      4366,
      119
    ],
    "rawString" : "[oai_citation:15â¡de.wikipedia.org](https:\/\/de.wikipedia.org\/wiki\/Security_Development_Lifecycle?utm_source=chatgpt.com)",
    "string" : "[oai_citation:15â¡de.wikipedia.org] https:\/\/de.wikipedia.org\/wiki\/Security_Development_Lifecycle?utm_source=chatgpt.com",
    "type" : "link"
  },
  {
    "id" : "1C7B843E-ABE5-4D46-8E14-B9B3FB1192E3",
    "index" : 32,
    "isCollapsed" : false,
    "level" : 3,
    "range" : [
      4548,
      140
    ],
    "rawString" : "[oai_citation:16â¡securitycompass.com](https:\/\/www.securitycompass.com\/blog\/software-security-requirements-checklist\/?utm_source=chatgpt.com)",
    "string" : "[oai_citation:16â¡securitycompass.com] https:\/\/www.securitycompass.com\/blog\/software-security-requirements-checklist\/?utm_source=chatgpt.com",
    "type" : "link"
  },
  {
    "id" : "F3853B9E-258A-44BA-BF09-F7DA38A40EAA",
    "index" : 33,
    "isCollapsed" : false,
    "level" : 2,
    "range" : [
      4695,
      32
    ],
    "rawString" : "## ð Quick-Reference Checkliste",
    "string" : "ð Quick-Reference Checkliste",
    "type" : "sectionHeader"
  },
  {
    "id" : "02ED61BB-DEB9-4F77-B589-B9CA30B0A91B",
    "index" : 34,
    "isCollapsed" : false,
    "level" : 2,
    "range" : [
      5821,
      11
    ],
    "rawString" : "## ð¡ Fazit",
    "string" : "ð¡ Fazit",
    "type" : "sectionHeader"
  },
  {
    "id" : "FF2FF26E-A6C2-4B69-929F-F978CBBC0D60",
    "index" : 35,
    "isCollapsed" : false,
    "level" : -1,
    "range" : [
      6065,
      0
    ],
    "rawString" : "",
    "string" : "",
    "type" : "blank"
  }
]PK    åZWÇØy  y  -   Untitled.textbundle/resources/sideboards.json[
  {
    "iconName" : "info.circle",
    "id" : "C58AA7CB-1577-4324-8C4E-529FEA422276",
    "isActive" : true,
    "name" : "Stats",
    "position" : 0
  },
  {
    "iconName" : "rectangle.grid.1x2",
    "id" : "45D33A98-EF9C-41FD-97B4-680E1F2D5269",
    "isActive" : true,
    "name" : "Shelf",
    "position" : 1
  },
  {
    "iconName" : "checkmark",
    "id" : "53066DE7-1D91-46B8-8F71-4EAB98B553CF",
    "isActive" : true,
    "name" : "Todos",
    "position" : 2
  },
  {
    "iconName" : "person.2",
    "id" : "8FC50D7E-E7C6-4992-B5AB-34E1D37230C2",
    "isActive" : true,
    "name" : "Characters",
    "position" : 3
  }
]PK    åZ^¾Á4Ý   Ý   4   Untitled.textbundle/resources/navigator-filters.json{
  "images" : true,
  "includedFiles" : true,
  "links" : true,
  "markers" : true,
  "notes" : true,
  "referenceLinks" : true,
  "sceneHeaders" : true,
  "sectionHeaders" : true,
  "synopses" : true,
  "todos" : true
}PK    åZÖº=þ   þ   (   Untitled.textbundle/resources/shelf.json{
  "items" : [

  ],
  "settings" : {
    "visibility" : {
      "comments" : true,
      "genderAnalysis" : true,
      "goals" : true,
      "grammarHighlights" : true,
      "snippets" : true,
      "stats" : true,
      "todoList" : true
    }
  }
}PK    åZ            "   Untitled.textbundle/scratchpad.txtPK    åZTk,  ,     Untitled.textbundle/info.json{
  "com.quoteunquoteapps.highland2" : {
    "currentTabIndex" : -1,
    "printParagraphNumbers" : false,
    "showSynopses" : false,
    "sidebarWidth" : 0,
    "templateName" : "Screenplay",
    "version" : 3
  },
  "transient" : false,
  "type" : "com.quoteunquoteapps.fountain",
  "version" : 2
}PK    åZ               Untitled.textbundle/revisions/PK    åZÿ>gF  gF  *   Untitled.textbundle/revisions/current.json{"number":0,"deletions":[],"colorIndex":0,"content":"YnBsaXN0MDDUAQIDBAUGBwpYJHZlcnNpb25ZJGFyY2hpdmVyVCR0b3BYJG9iamVjdHMSAAGGoF8QD05TS2V5ZWRBcmNoaXZlctEICVRyb290gAGvEB4LDBcbIikwMTk6PUBGTU5UXF01XmJobW5yent\/g4dVJG51bGzVDQ4PEBESExQVFlhOU1N0cmluZ18QD05TQXR0cmlidXRlSW5mb1xOU0F0dHJpYnV0ZXNaTlNEZWxlZ2F0ZVYkY2xhc3OAAoAbgASAAIAd0hEYGRpZTlMuc3RyaW5ngANvERexACMAIABTAGUAYwB1AHIAaQB0AHkAIABCAGEAcwBpAGMAcwAgIBMAIABDAG8AZABlIBEATQBvAG4AcwB0AGUAcgAg2D3e4f4PAAoACgAjACMAINg8368AIABaAHcAZQBjAGsACgBHAHIAdQBuAGQAbABhAGcAZQBuACAAZABlAHIAIABzAGkAYwBoAGUAcgBlAG4AIABTAG8AZgB0AHcAYQByAGUAZQBuAHQAdwBpAGMAawBsAHUAbgBnACAAKCAeAFMAZQBjAHUAcgBlACAAYgB5ACAARABlAHMAaQBnAG4gHAApACAgEwAgAHYAbwBuACAAZABlAHIAIABQAGwAYQBuAHUAbgBnACAAYgBpAHMAIABpAG4AcwAgAEQAZQBwAGwAbwB5AG0AZQBuAHQALgAgAFoAaQBlAGwAOgAgAFMAaQBjAGgAZQByAGgAZQBpAHQAcwBmAGUAaABsAGUAcgAgAHYAZQByAG0AZQBpAGQAZQBuACwAIABiAGUAdgBvAHIAIABzAGkAZQAgAGUAbgB0AHMAdABlAGgAZQBuAC4ACgAKAC0ALQAtAAoACgAjACMAINg93RAAIABTAGUAYwB1AHIAZQAgAGIAeQAgAEQAZQBzAGkAZwBuACAAJgAgAFMAZQBjAHUAcgBlACAAYgB5ACAARABlAGYAYQB1AGwAdAAKAC0AIABTAGkAYwBoAGUAcgBoAGUAaQB0AHMAYQBzAHAAZQBrAHQAZQAgACoAKgB2AG8AbgAgAEEAbgBmAGEAbgBnACAAYQBuACoAKgAgAGkAbgBzACAARABlAHMAaQBnAG4AIABhAHUAZgBuAGUAaABtAGUAbgAgACgAVABoAHIAZQBhAHQAIABNAG8AZABlAGwAaQBuAGcALAAgAGcAZQByAGkAbgBnAHMAdABlACAAUAByAGkAdgBpAGwAZQBnAGkAZQBuACkAIAAgAFsAbwBhAGkAXwBjAGkAdABhAHQAaQBvAG4AOgAwICEAZQBuAC4AdwBpAGsAaQBwAGUAZABpAGEALgBvAHIAZwBdACgAaAB0AHQAcABzADoALwAvAGUAbgAuAHcAaQBrAGkAcABlAGQAaQBhAC4AbwByAGcALwB3AGkAawBpAC8AUwBlAGMAdQByAGUAXwBiAHkAXwBkAGUAcwBpAGcAbgA\/AHUAdABtAF8AcwBvAHUAcgBjAGUAPQBjAGgAYQB0AGcAcAB0AC4AYwBvAG0AKQAgACAACgAtACAAUwB0AGEAbgBkAGEAcgBkAGsAbwBuAGYAaQBnAHUAcgBhAHQAaQBvAG4AZQBuACAAcwBvACAAcwBpAGMAaABlAHIAIAB3AGkAZQAgAG0A9gBnAGwAaQBjAGgAIABtAGEAYwBoAGUAbgAgACgARgBlAGEAdAB1AHIAZSARAEYAbABhAGcAcwAgAG8AZgBmACwAIAB1AG4AbgD2AHQAaQBnAGUAIABQAG8AcgB0AHMAIAB6AHUAKQAgACgAKQAKAAoALQAtAC0ACgAKACMAIwAg2D7d6QAgAFMARABMAEMAIAAmACAARABlAHYAUwBlAGMATwBwAHMAIABJAG4AdABlAGcAcgBhAHQAaQBvAG4ACgAtACAAUwBpAGMAaABlAHIAaABlAGkAdAAgAGkAbgAgAGEAbABsAGUAbgAgAFAAaABhAHMAZQBuACAAZABlAHMAIABTAEQATABDACAAdgBlAHIAYQBuAGsAZQByAG4AIAAoAFAAbABhAG4AICGSACAAQwBvAGQAZQAgIZIAIABUAGUAcwB0ACAhkgAgAFIAZQBsAGUAYQBzAGUAICGSACAATQBvAG4AaQB0AG8AcgApACAAIABbAG8AYQBpAF8AYwBpAHQAYQB0AGkAbwBuADoAMSAhAHMAZQBjAHUAcgBpAHQAeQBjAG8AbQBwAGEAcwBzAC4AYwBvAG0AXQAoAGgAdAB0AHAAcwA6AC8ALwB3AHcAdwAuAHMAZQBjAHUAcgBpAHQAeQBjAG8AbQBwAGEAcwBzAC4AYwBvAG0ALwBiAGwAbwBnAC8AcwBvAGYAdAB3AGEAcgBlAC0AcwBlAGMAdQByAGkAdAB5AC0AcgBlAHEAdQBpAHIAZQBtAGUAbgB0AHMALQBjAGgAZQBjAGsAbABpAHMAdAAvAD8AdQB0AG0AXwBzAG8AdQByAGMAZQA9AGMAaABhAHQAZwBwAHQALgBjAG8AbQApACAAIAAKAC0AIABBAHUAdABvAG0AYQB0AGkAcwBpAGUAcgB0AGUAIABTAGUAYwB1AHIAaQB0AHkALQBDAGgAZQBjAGsAcwAgAGkAbgAgAEMASQAvAEMARAAgAGkAbgB0AGUAZwByAGkAZQByAGUAbgAgACgAUwBBAFMAVAAsACAARABBAFMAVAAsACAARABlAHAAZQBuAGQAZQBuAGMAeQAgAFMAYwBhAG4AcwAsACAAQwBvAG4AdABhAGkAbgBlAHIAIABTAGMAYQBuAHMAKQAKAAoALQAtAC0ACgAKACMAIwAgJwUAIABTAGUAYwB1AHIAaQB0AHkAIABDAGgAZQBjAGsAbABpAHMAdABlAAoACgAjACMAIwAgADEALgAgAEkAbgBwAHUAdAAgAFYAYQBsAGkAZABhAHQAaQBvAG4AIAAmACAAUwBhAG4AaQB0AGkAegBhAHQAaQBvAG4AIAAgAAoALQAgAEEAbABsAGUAIABlAHgAdABlAHIAbgBlAG4AIABJAG4AcAB1AHQAcwAgAHYAYQBsAGkAZABpAGUAcgBlAG4AIAAoAFcAaABpAHQAZQBsAGkAcwB0ACkALgAgACAACgAtACAARQBzAGMAYQBwAGUAIAAmACAAZQBuAGMAbwBkAGUAIABEAGEAdABlAG4AICATACAAUwBjAGgAdQB0AHoAIAB2AG8AcgAgAFMAUQBMIBEASQBuAGoAZQBjAHQAaQBvAG4ALAAgAFgAUwBTACAAZQB0AGMALgAgACAAWwBvAGEAaQBfAGMAaQB0AGEAdABpAG8AbgA6ADIgIQB4AHkAZwBlAG4AaQAuAGkAbwBdACgAaAB0AHQAcABzADoALwAvAHgAeQBnAGUAbgBpAC4AaQBvAC8AYgBsAG8AZwAvAHMAZQBjAHUAcgBlAC0AYwBvAGQAaQBuAGcALQBwAHIAYQBjAHQAaQBjAGUAcwAtAGMAaABlAGMAawBsAGkAcwB0AC8APwB1AHQAbQBfAHMAbwB1AHIAYwBlAD0AYwBoAGEAdABnAHAAdAAuAGMAbwBtACkACgAKACMAIwAjACAAMgAuACAAQQB1AHQAaABlAG4AdABpAGYAaQB6AGkAZQByAHUAbgBnACAAJgAgAEEAdQB0AG8AcgBpAHMAaQBlAHIAdQBuAGcAIAAgAAoALQAgAFMAdABhAHIAawBlACAAUABhAHMAcwB3APYAcgB0AGUAcgAsACAATQBGAEEAIABpAG0AcABsAGUAbQBlAG4AdABpAGUAcgBlAG4ALgAgACAACgAtACAAUAByAGkAbgB6AGkAcAAgAGQAZQByACAAawBsAGUAaQBuAHMAdABlAG4AIABSAGUAYwBoAHQAZQA6ACAAagBlAGQAZQAgAEsAbwBtAHAAbwBuAGUAbgB0AGUAIABuAHUAcgAgAG0AaQB0ACAATQBpAG4AaQBtAGEAbABwAHIAaQB2AGkAbABlAGcAaQBlAG4AIABiAGUAdAByAGUAaQBiAGUAbgAuACAAIABbAG8AYQBpAF8AYwBpAHQAYQB0AGkAbwBuADoAMyAhAHgAeQBnAGUAbgBpAC4AaQBvAF0AKABoAHQAdABwAHMAOgAvAC8AeAB5AGcAZQBuAGkALgBpAG8ALwBiAGwAbwBnAC8AcwBlAGMAdQByAGUALQBjAG8AZABpAG4AZwAtAHAAcgBhAGMAdABpAGMAZQBzAC0AYwBoAGUAYwBrAGwAaQBzAHQALwA\/AHUAdABtAF8AcwBvAHUAcgBjAGUAPQBjAGgAYQB0AGcAcAB0AC4AYwBvAG0AKQAKAAoAIwAjACMAIAAzAC4AIABGAGUAaABsAGUAciARACAAdQBuAGQAIABBAHUAcwBuAGEAaABtAGUAbQBhAG4AYQBnAGUAbQBlAG4AdAAgACAACgAtACAASwBlAGkAbgBlACAAcwBlAG4AcwBpAGIAbABlAG4AIABJAG4AZgBvAHMAIABpAG4AIABVAHMAZQByIBEARgBlAGgAbABlAHIAbQBlAGwAZAB1AG4AZwBlAG4ALgAgACAACgAtACAAUwBpAGMAaABlAHIAZQAgAEwAbwBnAGcAaQBuAGcgEQBTAHQAcgBhAHQAZQBnAGkAZQAgAG8AaABuAGUAIABMAGUAYQBrACAAawByAGkAdABpAHMAYwBoAGUAcgAgAEQAYQB0AGUAbgAuACAAKAApAAoACgAjACMAIwAgADQALgAgAEQAYQB0AGUAbgB2AGUAcgBzAGMAaABsAPwAcwBzAGUAbAB1AG4AZwAgACAACgAtACAAVgBlAHIAcwBjAGgAbAD8AHMAcwBlAGwAdQBuAGcAIABzAG8AdwBvAGgAbAAgACoAKgBhAHQAIAByAGUAcwB0ACoAKgAgAGEAbABzACAAYQB1AGMAaAAgACoAKgBpAG4AIAB0AHIAYQBuAHMAaQB0ACoAKgAgACgAVABMAFMALAAgAEEARQBTIBEAMgA1ADYAKQAuACAAIAAKAC0AIABTAGUAYwByAGUAdABzACAAbgBpAGMAaAB0ACAAaABhAHIAZCARAGMAbwBkAGUAbgAgIBMAIABTAGUAYwB1AHIAZQAgAFYAYQB1AGwAdAAgACYAIABSAG8AdABhAHQAaQBvAG4AIAB2AGUAcgB3AGUAbgBkAGUAbgAuACAAIABbAG8AYQBpAF8AYwBpAHQAYQB0AGkAbwBuADoANCAhAHgAeQBnAGUAbgBpAC4AaQBvAF0AKABoAHQAdABwAHMAOgAvAC8AeAB5AGcAZQBuAGkALgBpAG8ALwBiAGwAbwBnAC8AcwBlAGMAdQByAGUALQBjAG8AZABpAG4AZwAtAHAAcgBhAGMAdABpAGMAZQBzAC0AYwBoAGUAYwBrAGwAaQBzAHQALwA\/AHUAdABtAF8AcwBvAHUAcgBjAGUAPQBjAGgAYQB0AGcAcAB0AC4AYwBvAG0AKQAKAAoAIwAjACMAIAA1AC4AIABBAGIAaADkAG4AZwBpAGcAawBlAGkAdABzIBEATQBhAG4AYQBnAGUAbQBlAG4AdAAgACAACgAtACAAQQB1AHQAbwBtAGEAdABpAHMAYwBoAGUAIABTAGMAYQBuAHMAIABuAGEAYwBoACAAYgBlAGsAYQBuAG4AdABlAG4AIABWAHUAbABuAGUAcgBhAGIAaQBsAGkAdABpAGUAcwAgACgAegAuIC8AQgAuACAATwBXAEEAUwBQACAARABlAHAAZQBuAGQAZQBuAGMAeSARAEMAaABlAGMAawApAC4AIAAgAAoALQAgAEQAcgBpAHQAdABhAG4AYgBpAGUAdABlAHIgEQBCAGkAYgBsAGkAbwB0AGgAZQBrAGUAbgAgAGEAawB0AHUAZQBsAGwAIABoAGEAbAB0AGUAbgAuACAAIABbAG8AYQBpAF8AYwBpAHQAYQB0AGkAbwBuADoANSAhAGUAbgAuAHcAaQBrAGkAcABlAGQAaQBhAC4AbwByAGcAXQAoAGgAdAB0AHAAcwA6AC8ALwBlAG4ALgB3AGkAawBpAHAAZQBkAGkAYQAuAG8AcgBnAC8AdwBpAGsAaQAvAEMAbwBkAGUAXwByAGUAdgBpAGUAdwA\/AHUAdABtAF8AcwBvAHUAcgBjAGUAPQBjAGgAYQB0AGcAcAB0AC4AYwBvAG0AKQAKAAoAIwAjACMAIAA2AC4AIABBAFAASSARACAAJgAgAE4AZQB0AHoAdwBlAHIAayARAFMAZQBjAHUAcgBpAHQAeQAgACAACgAtACAASABUAFQAUABTACwAIABJAG4AcAB1AHQALQBDAGgAZQBjAGsAcwAsACAAQQB1AHQAaAAvAFIAYQB0AGUALQBMAGkAbQBpAHQAIABmAPwAcgAgAEEAUABJIBEARQBuAGQAcABvAGkAbgB0AHMALgAgACAACgAtACAARgBpAHIAZQB3AGEAbABsAC8AUwBlAGcAbQBlAG4AdABhAHQAaQBvAG4AIABmAPwAcgAgAE4AZQB0AHoAdwBlAHIAawB6AHUAZwByAGkAZgBmAGUALgAgACAAWwBvAGEAaQBfAGMAaQB0AGEAdABpAG8AbgA6ADYgIQBkAGUALgB3AGkAawBpAHAAZQBkAGkAYQAuAG8AcgBnAF0AKABoAHQAdABwAHMAOgAvAC8AZABlAC4AdwBpAGsAaQBwAGUAZABpAGEALgBvAHIAZwAvAHcAaQBrAGkALwBTAGUAYwB1AHIAaQB0AHkAXwBEAGUAdgBlAGwAbwBwAG0AZQBuAHQAXwBMAGkAZgBlAGMAeQBjAGwAZQA\/AHUAdABtAF8AcwBvAHUAcgBjAGUAPQBjAGgAYQB0AGcAcAB0AC4AYwBvAG0AKQAKAAoAIwAjACMAIAA3AC4AIABBAHUAdABvAG0AYQB0AGkAcwBpAGUAcgB0AGUAIABTAGUAYwB1AHIAaQB0AHkAIABUAGUAcwB0AHMAIAAgAAoALQAgACoAKgBTAEEAUwBUACoAKgA6ACAAcwB0AGEAdABpAHMAYwBoAGUAcgAgAEMAbwBkAGUgEQBTAGMAYQBuACAAKABTAG8AbgBhAHIAUQB1AGIAZQAsACAAQwBvAGQAZQBRAEwAIABlAHQAYwAuACkAIAAgAFsAbwBhAGkAXwBjAGkAdABhAHQAaQBvAG4AOgA3ICEAZQBuAC4AdwBpAGsAaQBwAGUAZABpAGEALgBvAHIAZwBdACgAaAB0AHQAcABzADoALwAvAGUAbgAuAHcAaQBrAGkAcABlAGQAaQBhAC4AbwByAGcALwB3AGkAawBpAC8AUwB0AGEAdABpAGMAXwBhAHAAcABsAGkAYwBhAHQAaQBvAG4AXwBzAGUAYwB1AHIAaQB0AHkAXwB0AGUAcwB0AGkAbgBnAD8AdQB0AG0AXwBzAG8AdQByAGMAZQA9AGMAaABhAHQAZwBwAHQALgBjAG8AbQApACAAIAAKAC0AIAAqACoARABBAFMAVAAqACoAOgAgAFMAaQBtAHUAbABhAHQAaQBvAG4AIAB2AG8AbgAgAEEAbgBnAHIAaQBmAGYAZQBuACAAZwBlAGcAZQBuACAAbABhAHUAZgBlAG4AZABlACAAUwBlAHIAdgBpAGMAZQBzAC4AIAAgAAoALQAgACoAKgBJAEEAUwBUACoAKgA6ACAASwBvAG0AYgBpAG4AYQB0AGkAbwBuACAAYQB1AHMAIABiAGUAaQBkAGUAbQAsACAAZgBhAGwAbABzACAAdgBlAHIAZgD8AGcAYgBhAHIALgAKAAoAIwAjACMAIAA4AC4AIABDAG8AZABlACAAUgBlAHYAaQBlAHcAcwAgACYAIABQAGEAaQByAC0AUAByAG8AZwByAGEAbQBtAGkAbgBnACAAIAAKAC0AIABNAGkAbgBkAGUAcwB0AGUAbgBzACAAZQBpAG4AIABSAGUAdgBpAGUAdwBlAHIALAAgAGEAdQB0AG8AbQBhAHQAaQBzAGkAZQByAHQAZQAgAFQAbwBvAGwAcwAgAHUAbgB0AGUAcgBzAHQA\/AB0AHoAZQBuACAAIABbAG8AYQBpAF8AYwBpAHQAYQB0AGkAbwBuADoAOCAhAHMAZQBjAHUAcgBpAHQAeQBjAG8AbQBwAGEAcwBzAC4AYwBvAG0AXQAoAGgAdAB0AHAAcwA6AC8ALwB3AHcAdwAuAHMAZQBjAHUAcgBpAHQAeQBjAG8AbQBwAGEAcwBzAC4AYwBvAG0ALwBiAGwAbwBnAC8AcwBvAGYAdAB3AGEAcgBlAC0AcwBlAGMAdQByAGkAdAB5AC0AcgBlAHEAdQBpAHIAZQBtAGUAbgB0AHMALQBjAGgAZQBjAGsAbABpAHMAdAAvAD8AdQB0AG0AXwBzAG8AdQByAGMAZQA9AGMAaABhAHQAZwBwAHQALgBjAG8AbQApACAAWwBvAGEAaQBfAGMAaQB0AGEAdABpAG8AbgA6ADkgIQBlAG4ALgB3AGkAawBpAHAAZQBkAGkAYQAuAG8AcgBnAF0AKABoAHQAdABwAHMAOgAvAC8AZQBuAC4AdwBpAGsAaQBwAGUAZABpAGEALgBvAHIAZwAvAHcAaQBrAGkALwBTAHQAYQB0AGkAYwBfAGEAcABwAGwAaQBjAGEAdABpAG8AbgBfAHMAZQBjAHUAcgBpAHQAeQBfAHQAZQBzAHQAaQBuAGcAPwB1AHQAbQBfAHMAbwB1AHIAYwBlAD0AYwBoAGEAdABnAHAAdAAuAGMAbwBtACkAIABbAG8AYQBpAF8AYwBpAHQAYQB0AGkAbwBuADoAMQAwICEAZQBuAC4AdwBpAGsAaQBwAGUAZABpAGEALgBvAHIAZwBdACgAaAB0AHQAcABzADoALwAvAGUAbgAuAHcAaQBrAGkAcABlAGQAaQBhAC4AbwByAGcALwB3AGkAawBpAC8AQwBvAGQAZQBfAHIAZQB2AGkAZQB3AD8AdQB0AG0AXwBzAG8AdQByAGMAZQA9AGMAaABhAHQAZwBwAHQALgBjAG8AbQApACAAIAAKAC0AIABGAG8AawB1AHMAOgAgAFMAaQBjAGgAZQByAGgAZQBpAHQAcwBmAGUAaABsAGUAcgAsACAATABvAGcAaQBrAC0AUwBjAGgAdwDkAGMAaABlAG4ALAAgAFgAUwBTAC0ALwBJAG4AagBlAGMAdABpAG8AbgAtAEcAZQBmAGEAaAByAGUAbgAuAAoACgAjACMAIwAgADkALgAgAE0AbwBuAGkAdABvAHIAaQBuAGcAIAAmACAASQBuAGMAaQBkAGUAbgB0ACAAUgBlAHMAcABvAG4AcwBlACAAIAAKAC0AIABaAGUAbgB0AHIAYQBsAGkAcwBpAGUAcgB0AGUAcwAgAEwAbwBnAGcAaQBuAGcAIAAoAFMASQBFAE0AKQAsACAAYQB1AHQAbwBtAGEAdABpAHMAYwBoAGUAIABBAGwAZQByAHQAcwAuACAAIAAKAC0AIABWAG8AcgBnAGUAcABsAGEAbgB0AGUAcwAgAEkAbgBjAGkAZABlAG4AdAAtAFIAZQBzAHAAbwBuAHMAZSARAFAAbABhAHkAYgBvAG8AawAgAGkAbgBrAGwALgAgAEYAbwByAGUAbgBzAGkAawAgACYAIABSAG8AbABsAGIAYQBjAGsALgAKAAoALQAtAC0ACgAKACMAIwAg2D3e4AAgAEQAZQBmAGUAbgBzAGkAdgBlACAAUAByAG8AZwByAGEAbQBtAGkAbgBnAAoALQAgAEUAaQBuAGcAYQBiAGUAbgAgAGQAZQBmAGUAbgBzAGkAdgAgAPwAYgBlAHIAcAByAPwAZgBlAG4ALAAgAEYAZQBoAGwAZQByACAAYQBiAGYAYQBuAGcAZQBuACwAIABzAGkAYwBoAGUAcgBlACAARABlAGYAYQB1AGwAdABzACAAcwBlAHQAegBlAG4AIAAgAFsAbwBhAGkAXwBjAGkAdABhAHQAaQBvAG4AOgAxADEgIQBzAGUAYwB1AHIAaQB0AHkAYwBvAG0AcABhAHMAcwAuAGMAbwBtAF0AKABoAHQAdABwAHMAOgAvAC8AdwB3AHcALgBzAGUAYwB1AHIAaQB0AHkAYwBvAG0AcABhAHMAcwAuAGMAbwBtAC8AYgBsAG8AZwAvAHMAbwBmAHQAdwBhAHIAZQAtAHMAZQBjAHUAcgBpAHQAeQAtAHIAZQBxAHUAaQByAGUAbQBlAG4AdABzAC0AYwBoAGUAYwBrAGwAaQBzAHQALwA\/AHUAdABtAF8AcwBvAHUAcgBjAGUAPQBjAGgAYQB0AGcAcAB0AC4AYwBvAG0AKQAgAFsAbwBhAGkAXwBjAGkAdABhAHQAaQBvAG4AOgAxADIgIQB5AHMAbABpAG4AZwBzAGgAbwB0AC4AYwBvAG0AXQAoAGgAdAB0AHAAcwA6AC8ALwB3AHcAdwAuAHkAcwBsAGkAbgBnAHMAaABvAHQALgBjAG8AbQAvAHMAZQBjAHUAcgBpAHQAeQAtAGMAaABlAGMAawBsAGkAcwB0AC8APwB1AHQAbQBfAHMAbwB1AHIAYwBlAD0AYwBoAGEAdABnAHAAdAAuAGMAbwBtACkAIAAgAAoALQAgAEEAcwBzAGUAcgB0AGkAbwBuAHMAIAB1AG4AZAAgAEQAZQBzAGkAZwBuACAAYgB5ACAAQwBvAG4AdAByAGEAYwB0ACAAbgB1AHQAegBlAG4ALAAgAHUAbQAgAHUAbgBnAPwAbAB0AGkAZwBlACAAWgB1AHMAdADkAG4AZABlACAAZgByAPwAaAAgAHoAdQAgAGUAcgBrAGUAbgBuAGUAbgAuAAoACgAtAC0ALQAKAAoAIwAjACDYPdzaACAAUgBlAHMAcwBvAHUAcgBjAGUAbgAgACYAIABTAHQAYQBuAGQAYQByAGQAcwAKAC0AIAAqACoATwBXAEEAUwBQACoAKgA6ACAAUwBlAGMAdQByAGUAIABDAG8AZABpAG4AZwAgAFAAcgBhAGMAdABpAGMAZQBzACwAIABUAG8AcCAvADEAMAAsACAAQQBTAFYAUwAsACAAWgBBAFAALAAgAEUAbgB0AHcAaQBjAGsAbABlAHIALQBHAHUAaQBkAGUAcwAgACAAWwBvAGEAaQBfAGMAaQB0AGEAdABpAG8AbgA6ADEAMyAhAGUAbgAuAHcAaQBrAGkAcABlAGQAaQBhAC4AbwByAGcAXQAoAGgAdAB0AHAAcwA6AC8ALwBlAG4ALgB3AGkAawBpAHAAZQBkAGkAYQAuAG8AcgBnAC8AdwBpAGsAaQAvAEQAZQBmAGUAbgBzAGkAdgBlAF8AcAByAG8AZwByAGEAbQBtAGkAbgBnAD8AdQB0AG0AXwBzAG8AdQByAGMAZQA9AGMAaABhAHQAZwBwAHQALgBjAG8AbQApACAAWwBvAGEAaQBfAGMAaQB0AGEAdABpAG8AbgA6ADEANCAhAGUAbgAuAHcAaQBrAGkAcABlAGQAaQBhAC4AbwByAGcAXQAoAGgAdAB0AHAAcwA6AC8ALwBlAG4ALgB3AGkAawBpAHAAZQBkAGkAYQAuAG8AcgBnAC8AdwBpAGsAaQAvAE8AVwBBAFMAUAA\/AHUAdABtAF8AcwBvAHUAcgBjAGUAPQBjAGgAYQB0AGcAcAB0AC4AYwBvAG0AKQAgACAACgAtACAAKgAqAE0AaQBjAHIAbwBzAG8AZgB0ACAAUwBEAEwAKgAqADoAIABTAGUAYwB1AHIAZQAgAGIAeQAgAEQAZQBzAGkAZwBuACwAIABEAGUAZgBhAHUAbAB0ACwAIABEAGUAcABsAG8AeQBtAGUAbgB0ACAAKwAgAFAAcgBpAHYAYQBjAHkAIABiAHkAIABEAGUAcwBpAGcAbgAgACAAWwBvAGEAaQBfAGMAaQB0AGEAdABpAG8AbgA6ADEANSAhAGQAZQAuAHcAaQBrAGkAcABlAGQAaQBhAC4AbwByAGcAXQAoAGgAdAB0AHAAcwA6AC8ALwBkAGUALgB3AGkAawBpAHAAZQBkAGkAYQAuAG8AcgBnAC8AdwBpAGsAaQAvAFMAZQBjAHUAcgBpAHQAeQBfAEQAZQB2AGUAbABvAHAAbQBlAG4AdABfAEwAaQBmAGUAYwB5AGMAbABlAD8AdQB0AG0AXwBzAG8AdQByAGMAZQA9AGMAaABhAHQAZwBwAHQALgBjAG8AbQApACAAIAAKAC0AIABJAFMATwAgADIANwAwADAAMQAsACAATgBJAFMAVAAgAFMAUwBEAEYALAAgAFAAQwBJACAARABTAFMAICATACAAagBlACAAbgBhAGMAaAAgAEIAcgBhAG4AYwBoAGUAIAByAGUAbABlAHYAYQBuAHQAIAAgAFsAbwBhAGkAXwBjAGkAdABhAHQAaQBvAG4AOgAxADYgIQBzAGUAYwB1AHIAaQB0AHkAYwBvAG0AcABhAHMAcwAuAGMAbwBtAF0AKABoAHQAdABwAHMAOgAvAC8AdwB3AHcALgBzAGUAYwB1AHIAaQB0AHkAYwBvAG0AcABhAHMAcwAuAGMAbwBtAC8AYgBsAG8AZwAvAHMAbwBmAHQAdwBhAHIAZQAtAHMAZQBjAHUAcgBpAHQAeQAtAHIAZQBxAHUAaQByAGUAbQBlAG4AdABzAC0AYwBoAGUAYwBrAGwAaQBzAHQALwA\/AHUAdABtAF8AcwBvAHUAcgBjAGUAPQBjAGgAYQB0AGcAcAB0AC4AYwBvAG0AKQAKAAoALQAtAC0ACgAKACMAIwAg2D3cywAgAFEAdQBpAGMAawAtAFIAZQBmAGUAcgBlAG4AYwBlACAAQwBoAGUAYwBrAGwAaQBzAHQAZQAKAAoAfAAgAEIAZQByAGUAaQBjAGgAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAfAAgAEgAYQBuAGQAbAB1AG4AZwBzAGUAbQBwAGYAZQBoAGwAdQBuAGcAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAfAAKAHwALQAtAC0ALQAtAC0ALQAtAC0ALQAtAC0ALQAtAC0ALQAtAC0ALQAtAC0ALQAtAC0ALQAtAC0ALQB8AC0ALQAtAC0ALQAtAC0ALQAtAC0ALQAtAC0ALQAtAC0ALQAtAC0ALQAtAC0ALQAtAC0ALQAtAC0ALQAtAC0ALQAtAC0ALQAtAC0ALQAtAC0ALQAtAC0ALQAtAC0ALQAtAC0ALQAtAC0ALQAtAC0ALQAtAC0ALQAtAC0ALQAtAC0ALQAtAC0ALQAtAC0ALQAtAC0ALQAtAC0ALQAtAHwACgB8ACAAKgAqAEQAZQBzAGkAZwBuACoAKgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAfAAgAFQAaAByAGUAYQB0ACAATQBvAGQAZQBsACAAJgAgAFAAcgBpAG4AYwBpAHAAbABlACAAbwBmACAATABlAGEAcwB0ACAAUAByAGkAdgBpAGwAZQBnAGUAIAB2AGUAcgBhAG4AawBlAHIAbgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAHwACgB8ACAAKgAqAEMAbwBkAGUAKgAqACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAfAAgAEkAbgBwAHUAdAAtAFYAYQBsAGkAZABpAGUAcgB1AG4AZwAsACAATwB1AHQAcAB1AHQALQBFAG4AYwBvAGQAaQBuAGcALAAgAEQAZQBmAGUAbgBzAGkAdgBlACAAUAByAG8AZwByAGEAbQBtAGkAbgBnACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAHwACgB8ACAAKgAqAEEAdQB0AGgAZQBuAHQAaQBjAGEAdABpAG8AbgAgACYAIABBAHUAdABoAHoAKgAqAHwAIABNAEYAQQAsACAAUgBCAEEAQwAsACAAUwBlAGMAdQByAGUgEQBiAHkgEQBEAGUAZgBhAHUAbAB0ACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAHwACgB8ACAAKgAqAEUAcgByAG8AcgAgAEgAYQBuAGQAbABpAG4AZwAqACoAIAAgACAAIAAgACAAIAAgACAAfAAgAEsAZQBpAG4AZQAgAHMAZQBuAHMAaQBiAGwAZQBuACAASQBuAGYAbwBzACAAaQBuACAARQByAHIAbwByAHMALAAgAEwAbwBnAGcAaQBuAGcAIABnAGUAdAByAGUAbgBuAHQAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAHwACgB8ACAAKgAqAEQAYQB0AGUAbgBzAGMAaAB1AHQAegAqACoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAfAAgAFQATABTACwAIABBAEUAUyARAFYAZQByAHMAYwBoAGwA\/ABzAHMAZQBsAHUAbgBnACwAIABTAGUAYwByAGUAdAAgAE0AYQBuAGEAZwBlAG0AZQBuAHQAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAHwACgB8ACAAKgAqAEQAZQBwAGUAbgBkAGUAbgBjAHkAIABTAGMAYQBuACoAKgAgACAAIAAgACAAIAAgACAAfAAgAFQAbwBvAGwAcwAgACYAIAByAGUAZwBlAGwAbQDkAN8AaQBnAGUAIABVAHAAZABhAHQAZQBzACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAfAAKAHwAIAAqACoAUwBlAGMAdQByAGkAdAB5ACAAVABlAHMAdABpAG4AZwAqACoAIAAgACAAIAAgACAAIAB8ACAAUwBBAFMAVAAvAEQAQQBTAFQALwBJAEEAUwBUACAAaQBuACAAQwBJAC8AQwBEACAAcABpAHAAZQBsAGkAbgBlACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAB8AAoAfAAgACoAKgBSAGUAdgBpAGUAdwAgACYAIABNAG8AbgBpAHQAbwByAGkAbgBnACoAKgAgACAAIAAgAHwAIABQAGUAZQByAC0AUgBlAHYAaQBlAHcALAAgAFMASQBFAE0ALAAgAEkAbgBjAGkAZABlAG4AdAAgAFIAZQBzAHAAbwBuAHMAZQAgAFQAZQBhAG0AIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAB8AAoACgAtAC0ALQAKAAoAIwAjACDYPdyhACAARgBhAHoAaQB0AAoATQBpAHQAIABkAGkAZQBzAGUAbQAgAEcAdQBpAGQAZQAgAGgAYQBzAHQAIABkAHUAIABlAGkAbgBlACAAKgAqAEgAYQBuAGQAbAB1AG4AZwBzAHMAaQBjAGgAZQByAGUAIABSAG8AYQBkAG0AYQBwACoAKgAgAHoAdQByACAASQBtAHAAbABlAG0AZQBuAHQAYQB0AGkAbwBuACAAcwBpAGMAaABlAHIAZQByACAAUwBvAGYAdAB3AGEAcgBlACAAdgBvAG4AIABkAGUAcgAgAEEAcgBjAGgAaQB0AGUAawB0AHUAcgAgAGIAaQBzACAAegB1AHIAIABBAHUAcwBsAGkAZQBmAGUAcgB1AG4AZwAuACAAIAAKADEAMAAwIC8AJQAgAEQAZQBjAGsAdQBuAGcAIABmAPwAcgAgAG0AbwBkAGUAcgBuAGUAIABTAGUAYwB1AHIAaQB0AHkgEQBBAG4AZgBvAHIAZABlAHIAdQBuAGcAZQBuACAgEwAgAGQAaQByAGUAawB0ACAAaQBuACAAQwBvAGQAZSARAE0AbwBuAHMAdABlAHIAIABpAG4AdABlAGcAcgBpAGUAcgBiAGEAcgAuAAoACgAtAC0ALdIcHR4fWiRjbGFzc25hbWVYJGNsYXNzZXNfEA9OU011dGFibGVTdHJpbmejHiAhWE5TU3RyaW5nWE5TT2JqZWN00iMRJChaTlMub2JqZWN0c6MlJieABYALgBSAGtMqIxErLS9XTlMua2V5c6EsgAahLoAHgApWTlNGb2501DIzNBE1Njc4Vk5TU2l6ZVhOU2ZGbGFnc1ZOU05hbWUjQCgAAAAAAAAQEIAIgAlZSGVsdmV0aWNh0hwdOzxWTlNGb250ojsh0hwdPj9cTlNEaWN0aW9uYXJ5oj4h0yojEUFDL6EsgAahRIAMgArWMjNHSDQRNTZJSks4XE5TRGVzY3JpcHRvclpOU0hhc1dpZHRogA4IgA2ACV8QD0FwcGxlQ29sb3JFbW9qadMRT1BRUlNfEBdOU0ZvbnREZXNjcmlwdG9yT3B0aW9uc18QGk5TRm9udERlc2NyaXB0b3JBdHRyaWJ1dGVzgBMSgAAAAIAP0yojEVVYL6JWV4AQgBGiWUuAEoANgApfEBNOU0ZvbnRTaXplQXR0cmlidXRlXxATTlNGb250TmFtZUF0dHJpYnV0ZdIcHV9gXxAQTlNGb250RGVzY3JpcHRvcqJhIV8QEE5TRm9udERlc2NyaXB0b3LTKiMRY2UvoSyABqFmgBWACtYyM0dINBE1NmlKaziAFwiAFoAJXEx1Y2lkYUdyYW5kZdMRT1BRcHGAExKAAQABgBjTKiMRc3YvolZXgBCAEaJZeIASgBmAClxMdWNpZGFHcmFuZGXSHB18fV5OU011dGFibGVBcnJheaN8fiFXTlNBcnJhedKAEYGCV05TLmRhdGFPEDIhAAMBBQADAa4BAAMB4AIAAwFTALEBAnAAAgGbFAADAbQDAAMBzwUAAwHjCAADAe4BAIAc0hwdhIVdTlNNdXRhYmxlRGF0YaOEhiFWTlNEYXRh0hwdiIldTlNUZXh0U3RvcmFnZaSKi4whXU5TVGV4dFN0b3JhZ2VfEBlOU011dGFibGVBdHRyaWJ1dGVkU3RyaW5nXxASTlNBdHRyaWJ1dGVkU3RyaW5nAAgAEQAaACQAKQAyADcASQBMAFEAUwB0AHoAhQCOAKAArQC4AL8AwQDDAMUAxwDJAM4A2ADaMEAwRTBQMFkwazBvMHgwgTCGMJEwlTCXMJkwmzCdMKQwrDCuMLAwsjC0MLYwvTDGMM0w1jDdMOYw6DDqMOww9jD7MQIxBTEKMRcxGjEhMSMxJTEnMSkxKzE4MUUxUDFSMVMxVTFXMWkxcDGKMacxqTGuMbAxtzG6MbwxvjHBMcMxxTHHMd0x8zH4MgsyDjIhMigyKjIsMi4yMDIyMj8yQTJCMkQyRjJTMloyXDJhMmMyajJtMm8ycTJ0MnYyeDJ6MocyjDKbMp8ypzKsMrQy6TLrMvAy\/jMCMwkzDjMcMyEzLzNLAAAAAAAAAgEAAAAAAAAAjQAAAAAAAAAAAAAAAAAAM2A="}PK    åZ               Untitled.textbundle/assets/PK    åZ               Untitled.textbundle/PK    åZ¿ñC  C             ¤    Untitled.textbundle/text.mdPK    åZ                       íA|  Untitled.textbundle/bin/PK    åZúÜäd      )           ¤²  Untitled.textbundle/navigatorFilters.jsonPK    åZ                       íA  Untitled.textbundle/resources/PK    åZuþÇ  Ç  )           ¤Ò  Untitled.textbundle/resources/header.jsonPK    åZ5pøÏ=  =  +           ¤à  Untitled.textbundle/resources/settings.jsonPK    åZ¿à
Ç  Ç  )           ¤f   Untitled.textbundle/resources/footer.jsonPK    åZ
L$:5  :5  *           ¤t"  Untitled.textbundle/resources/outline.jsonPK    åZWÇØy  y  -           ¤öW  Untitled.textbundle/resources/sideboards.jsonPK    åZ^¾Á4Ý   Ý   4           ¤ºZ  Untitled.textbundle/resources/navigator-filters.jsonPK    åZÖº=þ   þ   (           ¤é[  Untitled.textbundle/resources/shelf.jsonPK    åZ            "           ¤-]  Untitled.textbundle/scratchpad.txtPK    åZTk,  ,             ¤m]  Untitled.textbundle/info.jsonPK    åZ                       íAÔ^  Untitled.textbundle/revisions/PK    åZÿ>gF  gF  *           ¤_  Untitled.textbundle/revisions/current.jsonPK    åZ                       íA¿¥  Untitled.textbundle/assets/PK    åZ                       íAø¥  Untitled.textbundle/PK      n  *¦    

---

## 🔹 Quelle 2: security_checklist.md

# Security Checklist – Code‑Monster 🛡️

## 🎯 Zweck
Vollständige Checkliste zur Absicherung von Software – vom Design über Code bis Deployment. Direkte Orientierung für CI/CD-Pipelines und Reviews.

---

## ✅ 1. Design & Architektur
- Threat Modeling durchführen.
- Prinzip der **geringsten Privilegien** („Least Privilege“).
- **Secure by Design/Default**: Alle Komponenten standardmäßig sicher konfigurieren.  [oai_citation:0‡en.wikipedia.org](https://en.wikipedia.org/wiki/Lynis?utm_source=chatgpt.com)

---

## ✅ 2. Input Validation & Output Encoding
- Alle externen Inputs anhand von Whitelists validieren.
- Output im Kontext sicher codieren (z. B. HTML/Escaping).
- Tiefgehende Validierung aller Header, URLs, Dateipfade, Cookies. ()

---

## ✅ 3. Authentifizierung & Autorisierung
- Zwei-Faktor-Authentifizierung (2FA) überall wo möglich. ()
- Passwortregeln & Schutz vor Brute-Force.
- Token & Session-Management: sichere Flags, kurze TTLs.
- Rollenzugriff & RBAC klar definieren.

---

## ✅ 4. Fehler- & Ausnahmehandling
- Keine sensiblen Daten in Fehlermeldungen oder Logs.
- Unterschiedliche Log-Level: debug/log/admin getrennt.
- Fail-secure: bei Fehlern sichere Zustände erzwingen.  [oai_citation:1‡github.com](https://github.com/shieldfy/API-Security-Checklist?utm_source=chatgpt.com) [oai_citation:2‡owasp.org](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/stable-en/02-checklist/05-checklist?utm_source=chatgpt.com)

---

## ✅ 5. Datenverschlüsselung & Secrets
- TLS für alle Verbindungen, AES‑256 für ruhende Daten.
- Secrets extern speichern (Vault), keine Hardcodierung.
- Automatisierte Rotation von Schlüsseln & Tokens.
- Git-Scanning für Geheimnisse erkennen.  [oai_citation:3‡reco.ai](https://www.reco.ai/hub/github-security-checklist?utm_source=chatgpt.com) [oai_citation:4‡arxiv.org](https://arxiv.org/abs/2208.11280?utm_source=chatgpt.com)

---

## ✅ 6. Abhängigkeitsmanagement
- Tools wie OWASP Dependency-Check oder Dependabot einsetzen.  [oai_citation:5‡reco.ai](https://www.reco.ai/hub/github-security-checklist?utm_source=chatgpt.com)
- Abhängigkeiten aktuell halten & Schwachstellen zeitnah patchen.

---

## ✅ 7. API- & Netzwerk-Sicherheit
- Nur HTTPS verwenden, keine HTTP-Downgrades.
- API-Endpoints mit Authn, Rate-Limit, Input-Checks absichern.
- Netzwerksegmentierung und Firewalls einsetzen. ()

---

## ✅ 8. Datei-Uploads & Ressourcenzugriffe
- Nur sichere Dateitypen erlaubt (Whitelist).
- Virenscan für Uploads durchführen.
- Pfade bereinigen, keine direkte User-Dateizugriffe erlauben.  [oai_citation:6‡github.com](https://github.com/eliotsykes/rails-security-checklist?utm_source=chatgpt.com)

---

## ✅ 9. CI/CD & Repository-Sicherheit
- GitHub: unbedingt mit 2FA absichern, Branch Protection aktivieren.  [oai_citation:7‡reco.ai](https://www.reco.ai/hub/github-security-checklist?utm_source=chatgpt.com)
- CI/CD Checkliste:
  -Lint → Test → Static Analysis → Security Scan (SAST/DAST) → Build.
  - Geheimnisse nur via OIDC oder Vault für GitHub Actions.  [oai_citation:8‡stepsecurity.io](https://www.stepsecurity.io/blog/github-actions-security-best-practices?utm_source=chatgpt.com)
  - Drittanbieter-Actions streng zulassen & pinnen.  [oai_citation:9‡stepsecurity.io](https://www.stepsecurity.io/blog/github-actions-security-best-practices?utm_source=chatgpt.com)

---

## ✅ 10. Statische & dynamische Analysen
- Statische Tools: SonarQube, CodeQL, Flake8, Bandit. ()
- Dynamische Tests: OWASP ZAP, IAST/Taint Tracking, Pentest-Tools.
- OWASP Testing Checklist als Grundlage verwenden.  [oai_citation:10‡cybersectools.com](https://cybersectools.com/tools/owasp-testing-checklist-v4-markdown?utm_source=chatgpt.com)

---

## ✅ 11. Monitoring & Incident-Response
- Zentralisiertes Logging & SIEM-Integration.
- Automatische Alerts bei Anomalien.
- Vorgefertigtes Playbook für Incident Response, Forensik & Rollback.

---

## ✅ 12. Code Reviews & Pair Programming
- Mindestens ein Security- und Logikreview vor Merge.
- Checkliste verwenden und automatisierte Tools integrieren.
- Pair Programming bei kritischen Komponenten.

---

## ✅ 13. Betriebs- & Umgebungshärtung
- Nur notwendige Dienste laufen.
- Aktuelle Patches für Betriebssysteme & Laufzeitumgebungen. ()
- Netzwerkzugriffe absichern, Firewalls, TLS-Validierung.

---

## 📋 Schnell-Übersicht

| Bereich                  | Wichtigste Maßnahmen                                           |
|--------------------------|----------------------------------------------------------------|
| Design                   | Threat Model & Least Privilege                                |
| Input/Output             | Whitelist Validation & Encoding                               |
| Authn/Authz              | 2FA, Token TTLs, RBAC                                         |
| Fehler & Logs            | Kein Leak, Fail-Secure                                        |
| Daten & Secrets          | TLS, Vault, Rotation                                          |
| Dependencies             | Dependabot, OWASP CHECK                                       |
| API & Netzwerk           | HTTPS, Rate Limits, Firewall                                  |
| File Upload              | Whitelist, Virus Scan, Pfad-Sicherheit                        |
| CI/CD                    | 2FA, OIDC, Branch Protection, SAST/DAST, Secret Management    |
| Static/Dynamic Testing   | SonarQube, ZAP, OWASP Testing Checklist                       |
| Monitoring & Response    | SIEM, Alerts, Playbook                                        |
| Code Review              | Automatisch & manuell, Pair Programming                      |
| Betriebshärtung          | Patching, Service Minimierung, TLS                            |

---

## 🔚 Fazit
`security_checklist.md` bietet dir eine **umfassende, sofort einsetzbare Komplettlösung** zur Absicherung deines Projekts – vollintegrierbar ins Code-Monster-Setup, ohne Ergänzungsbedarf. Ready für Datei 4/20?