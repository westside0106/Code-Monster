# Python Advanced Tricks

## 🧠 List/Dict Comprehensions
Effiziente und lesbare Konstruktion:
```python
squares = [x**2 for x in range(10)]
word_lengths = {word: len(word) for word in ["hi", "hello"]}
```

## ⚙️ Generator Expressions & yield
Speicherschonende Iteration über große Datenmengen:
```python
def read_large_file(file_path):
    with open(file_path, encoding="utf-8") as f:
        for line in f:
            yield line.strip()
```

## 🧱 Kontext-Manager (`@contextlib`)
Elegantes Management von Ressourcen (z. B. Timer, Locks):
```python
import time
from contextlib import contextmanager

@contextmanager
def timer(label="Elapsed"):
    start = time.perf_counter()
    try:
        yield
    finally:
        duration = time.perf_counter() - start
        print(f"{label}: {duration:.4f}s")
```

## 🎯 Decorators (`@functools`)
Reuse von Logging, Caching, Validierung:
```python
from functools import wraps

def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[CALL] {func.__name__} args={args} kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper
```

## 🧾 Type Hints & Protocols (PEP 484, 544)
Verbessert Lesbarkeit und Tooling-Support:
```python
from typing import Protocol

class SupportsClose(Protocol):
    def close(self) -> None: ...

def close_all(things: list[SupportsClose]) -> None:
    for t in things:
        t.close()
```

## 🧬 Metaclasses
Ermöglicht Klass-Generierung, Validation, Registries:
```python
class AutoIDMeta(type):
    def __new__(mcs, name, bases, namespace):
        namespace['id'] = namespace.get('id', 0) + 1
        return super().__new__(mcs, name, bases, namespace)

class Base(metaclass=AutoIDMeta):
    pass

class Sub(Base):
    pass

print(Base.id, Sub.id)  # z. B. 1 2
```

## 🪄 Dynamisches Importieren
Plugins, Extensibilität, CLI Befehle:
```python
import importlib

def load_plugin(name: str):
    module = importlib.import_module(name)
    return getattr(module, 'main', None)
```

## 🧩 NamedTuples & Dataclasses
Kompakte Datenrepräsentation:
```python
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])

from dataclasses import dataclass

@dataclass(frozen=True)
class Car:
    brand: str
    hp: int
```

## 🔁 Unpacking / Multiple Assignment
Mehr Übersichtlichkeit und Pattern-Matching:
```python
a, b, *rest = range(5)
```

## 🛠️ Walrus-Operator (Python 3.8+)
Inline Zuweisung:
```python
if (n := len(my_list)) > 5:
    print(f"List has {n} items")
```

## 🔄 Pattern Matching (Python 3.10+)
Ersetzt komplexe `if-elif`-Chains:
```python
def http_status(code: int) -> str:
    match code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case _:
            return "Unknown"
```

## ⚡ Context Manager für Async (Python 3.11+)
```python
import asyncio
from contextlib import asynccontextmanager

@asynccontextmanager
async def notify_on_exit(msg: str):
    try:
        yield
    finally:
        print(msg)
```