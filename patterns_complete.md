# 🧱 Patterns Complete – patterns_factory.py + design_patterns_overview.md

## 🔹 Quelle 1: patterns_factory.py

```python
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Callable, TypeVar, Dict

# 🏭 Factory Pattern mit Registrierung via Decorator

T = TypeVar("T", bound="Product")

class Product(ABC):
    @abstractmethod
    def use(self) -> None:
        ...

# Registry für Produkterstellung
_registry: Dict[str, Callable[[], Product]] = {}

def register(name: str) -> Callable[[Callable[[], T]], Callable[[], T]]:
    def decorator(factory: Callable[[], T]) -> Callable[[], T]:
        _registry[name] = factory
        return factory
    return decorator

def create(name: str) -> Product:
    if name not in _registry:
        raise ValueError(f"Unknown product: {name}")
    return _registry[name]()

# Beispielprodukte
@register("widget")
class Widget(Product):
    def use(self) -> None:
        print("Using a widget")

@register("gadget")
class Gadget(Product):
    def use(self) -> None:
        print("Using a gadget")

# 🔄 Funktionärer Zugriff auf gesamte Registry
def list_products() -> list[str]:
    return list(_registry.keys())

# 🔧 Beispielanwendung
def main():
    print("Available:", list_products())
    for name in list_products():
        product = create(name)
        product.use()

if __name__ == "__main__":
    main()
```

---

## 🔹 Quelle 2: design_patterns_overview.md

# Design Patterns Overview – Code‑Monster 🧩

## 🎯 Zielsetzung
Präsentiert bewährte **Design Patterns** als wiederverwendbare, sprachunabhängige Lösungsansätze für häufige Software­design-Probleme – mit klarem Fokus auf Lesbarkeit, Wartbarkeit & Skalierbarkeit.

---

## 🧠 Was sind Design Patterns?
Design Patterns sind **generische, wiederverwendbare Lösungen** für typische Designprobleme – keine fertigen Codes, sondern Blaupausen, die an spezifische Kontexte angepasst werden.

> „Patterns are proven templates that solve recurring design problems and provide a shared vocabulary im Team.“ – Refactoring Guru

---

## 📂 Kategorien

### 1. Creational (Erzeugungsmuster)
Steuern Objektinstanzen-Erzeugung – vermeidet zu enge Kopplung:
- **Singleton**, **Factory Method**, **Abstract Factory**, **Builder**, **Prototype**

### 2. Structural (Strukturmuster)
Verwalten Objektkomposition – strukturierte Systeme:
- **Adapter**, **Bridge**, **Composite**, **Decorator**, **Facade**, **Flyweight**, **Proxy**

### 3. Behavioral (Verhaltensmuster)
Regeln Kommunikation zwischen Objekten:
- **Chain of Responsibility**, **Command**, **Observer**, **Iterator**, **Strategy**, **Template Method**, **Visitor**, **State**, **Mediator**, **Memento**

---

## 🎯 Warum Patterns nutzen?
- Steigern **Wiederverwendbarkeit** und **Lesbarkeit**
- Fördern gemeinsame **Architekturkommunikation** im Team
- Schützen vor Suboptimalität/Over-Engineering durch Standardlösungen

---

## ⚠️ Vorsicht bei Overuse!
Patterns sind mächtig – aber **nur bei Bedarf einsetzen**. Übermäßiger Gebrauch kann zu unnötiger Komplexität führen.

---

## 🧩 Beispiele

### Creational – Factory Method (Python)
```python
class Creator:
    def factory_method(self):
        raise NotImplementedError
    def create(self):
        product = self.factory_method()
        return product.do_something()

class ConcreteCreator(Creator):
    def factory_method(self):
        return ConcreteProduct()

class ConcreteProduct:
    def do_something(self):
        return "Produkt"
```

### Structural – Decorator (JavaScript)
```js
function logger(component) {
  return function(...args) {
    console.log("Calling", component.name, args);
    return component(...args);
  }
}
function sum(a,b) { return a+b; }
const loggedSum = logger(sum);
```

### Behavioral – Strategy (TypeScript)
```ts
interface Strategy { execute(a:number,b:number):number; }
class Add implements Strategy { execute(a,b){ return a+b } }
class Multiply implements Strategy { execute(a,b){ return a*b } }
function operate(a:number,b:number, s:Strategy){ return s.execute(a,b); }
```

---

## 🛠 Tools & Ressourcen
- **Refactoring.Guru** (über 22 klassische GoF Patterns)
- **DigitalOcean Tutorial**
- **Books**: „Head First Design Patterns“, „Design Patterns: Elements of Reusable Object‑Oriented Software“ (GoF)

---

## 📋 Quick-Reference Tabelle

| Kategorie   | Muster | Zweck |
|------------|--------|--------|
| Creational | Factory, Builder, Singleton | Erzeugung flexibler Instances |
| Structural | Adapter, Decorator, Proxy | Objektkomposition vereinfachen |
| Behavioral | Strategy, Observer, Command | Interaktion & Kontrollfluss strukturieren |

---

## 🔚 Fazit
Diese **Design Patterns Overview** liefert dir alle essentiellen Konzepte, Kategorien und praxisnahen Code­beispiele – ideal für sofortige Umsetzung im Code‑Monster‑Stil.