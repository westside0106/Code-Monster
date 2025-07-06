# 🧬 Data & Structure – data_handling_snippets.py + structure.txt

## 🔹 Quelle 1: data_handling_snippets.py

```python
import pandas as pd
import json
import csv
from typing import Any, Iterator, Dict, Union

# 📊 CSV → Pandas DataFrame mit Hygienefunktionen
def load_csv_to_df(
    path: str,
    encoding: str = 'utf-8',
    usecols: list[str] | None = None,
    dtype: dict[str, Any] | None = None,
    parse_dates: list[str] | None = None,
) -> pd.DataFrame:
    df = pd.read_csv(path, encoding=encoding, usecols=usecols, dtype=dtype, parse_dates=parse_dates)
    df.dropna(inplace=True)
    return df

# 💾 JSON → Python-Dict
def load_json(path: str, encoding: str = 'utf-8') -> Union[Dict, list]:
    with open(path, 'r', encoding=encoding) as f:
        return json.load(f)

# 🖨️ JSON-Dump mit Sortierung & Standardformat
def save_json(obj: Any, path: str, encoding: str = 'utf-8', indent: int = 2) -> None:
    with open(path, 'w', encoding=encoding) as f:
        json.dump(obj, f, ensure_ascii=False, indent=indent, sort_keys=True)

# 🔁 Zeilenweises CSV-Lesen großer Dateien
def iter_csv(path: str, encoding: str = 'utf-8') -> Iterator[Dict[str, str]]:
    with open(path, 'r', encoding=encoding) as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row

# 🎯 Flexible Daten-Ouput Funktion
def export_data(
    df: pd.DataFrame,
    target: str,
    format: str = 'csv',
    **kwargs
) -> None:
    match format.lower():
        case 'csv':
            df.to_csv(target, index=False, **kwargs)
        case 'json':
            save_json(df.to_dict(orient='records'), target, **kwargs)
        case 'excel':
            df.to_excel(target, index=False, **kwargs)
        case _:
            raise ValueError(f"Unsupported format: {format}")

# 🧼 Beispiel für Data-Cleaning Pipeline
def clean_df(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates()
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].str.strip().str.lower()
    return df

# 📦 Testbare Main-Funktion
def main():
    df = load_csv_to_df('data/input.csv', parse_dates=['timestamp'])
    df = clean_df(df)
    export_data(df, 'data/output.json', format='json')
    df_large = pd.DataFrame(iter_csv('data/huge.csv'))
    print("Rows loaded:", len(df_large))

if __name__ == "__main__":
    main()
```

---

## 🔹 Quelle 2: structure.txt

```
📁 my_project/
├── src/
│   └── my_project/
│       ├── __init__.py
│       ├── main.py           # Entry-Point (`python -m my_project`)
│       ├── config.py         # Config via `pydantic`/`toml`
│       ├── services.py       # Business-Logic
│       ├── models.py         # Data-Modelle (z. B. `@dataclass` oder Pydantic)
│       ├── utils.py          # Allgemeine Hilfsfunktionen
│       └── api/              # (Optional) API-Logik als Submodule
│           └── __init__.py
│
├── tests/                    # Unittests (pytest-konform)
│   ├── __init__.py
│   └── test_main.py
│
├── docs/                     # Projektdokumentation (z.B. Sphinx/ReStructuredText)
│
├── scripts/                  # CLI oder Hilfsskripte (z. B. Data-Migration)
│
├── pyproject.toml            # Tooling-Konfiguration (build, lint, test, format)
├── poetry.lock or requirements.txt  # Lock-Datei / Dependencies
├── tox.ini or .github/workflows/ci.yml  # CI/CD Pipeline-Definition
├── .gitignore
├── LICENSE
└── README.md
```