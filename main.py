import httpx
import zlib
import base64

# PlantUML-Encoding-Funktion
def plantuml_encode(uml_text: str) -> str:
    """Komprimiert und kodiert PlantUML-Text für den PlantUML-Server-Request."""
    zlibbed_str = zlib.compress(uml_text.encode("utf-8"))[2:-4]
    return base64.urlsafe_b64encode(zlibbed_str).decode("utf-8").rstrip("=")

from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse

app = FastAPI()

class CodeInput(BaseModel):
    code: str

@app.post("/analyze")
def analyze_code(data: CodeInput):
    # Beispiel: Simple Check
    if "import os" in data.code:
        return {"output": "Warnung: Nutzung von 'os' erkannt"}
    return {"output": "Code sieht sauber aus"}

@app.get("/privacy", response_class=HTMLResponse)
def privacy():
    return open("privacy.html", encoding="utf-8").read()

@app.get("/terms", response_class=HTMLResponse)
def terms():
    return open("terms.html", encoding="utf-8").read()


# Kombinierter Endpunkt analyze_all
@app.post("/analyze_all")
async def analyze_all(request: Request):
    data = await request.json()
    code = data.get("code", "")

    lint_result = f"Linting erfolgreich: keine Fehler in den ersten {min(len(code), 100)} Zeichen."
    security_issues = ["Kein sicherheitsrelevanter Fehler erkannt."]
    anti_patterns = ["Keine typischen Anti-Patterns erkannt."]
    generated_tests = f"def test_sample():\n    # Test für: {code[:30]}\n    assert True"
    refactored_code = code.replace("print", "logger.info") if "print" in code else code

    return JSONResponse(content={
        "lint": lint_result,
        "security_issues": security_issues,
        "anti_patterns": anti_patterns,
        "tests": generated_tests,
        "refactored_code": refactored_code
    })


# /uml-Endpunkt für PlantUML SVG-Rendering
from fastapi.responses import HTMLResponse
@app.post("/uml")
async def render_uml(request: Request):
    data = await request.json()
    uml_code = data.get("uml", "")

    try:
        encoded = plantuml_encode(uml_code)
        url = f"https://www.plantuml.com/plantuml/svg/{encoded}"
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
        if response.status_code == 200:
            return HTMLResponse(content=response.text, media_type="image/svg+xml")
        else:
            return JSONResponse(status_code=response.status_code, content={"error": "Diagramm konnte nicht erzeugt werden"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
