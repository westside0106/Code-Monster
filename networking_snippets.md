# 🕸️ Networking Snippets – Kombinierte Py-Files als Markdown

### 🔹 Quelle: `async_concurrency.py`
```python
import asyncio
from typing import Any, Callable, List
import aiohttp
import time
from contextlib import asynccontextmanager

# 🚀 Modernes Timeout-Context-Manager für async
@asynccontextmanager
async def timeout_manager(seconds: float):
    task = asyncio.current_task()
    try:
        yield
    except asyncio.CancelledError:
        raise
    finally:
        await asyncio.sleep(seconds)

# 🔧 Semaphore für Rate-Limits / Concurrency-Kontrolle
MAX_CONCURRENT = 10

sem = asyncio.Semaphore(MAX_CONCURRENT)

async def fetch(session: aiohttp.ClientSession, url: str) -> str:
    async with sem:
        async with session.get(url, timeout=10) as resp:
            return await resp.text()

async def bound_fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        return await fetch(session, url)

async def gather_with_concurrency(urls: List[str]) -> List[str]:
    tasks = [asyncio.create_task(bound_fetch(u)) for u in urls]
    return await asyncio.gather(*tasks)

def cpu_bound(n: int) -> int:
    return sum(i * i for i in range(n))

async def run_cpu_bound(loop: asyncio.AbstractEventLoop):
    return await loop.run_in_executor(None, cpu_bound, 10_000_000)

async def main(urls: List[str]):
    start = time.time()
    pages = await gather_with_concurrency(urls)
    print(f"Fetched {len(pages)} pages in {time.time() - start:.2f}s")

    loop = asyncio.get_running_loop()
    result = await run_cpu_bound(loop)
    print("CPU-bound result:", result)

if __name__ == "__main__":
    urls = [f"https://example.com/page/{i}" for i in range(20)]
    asyncio.run(main(urls), debug=True)
```

---

### 🔹 Quelle: `snippets_api_calls.py`
```python
import aiohttp
import asyncio
from typing import Any, Dict
from dataclasses import dataclass

@dataclass
class ApiResponse:
    status: int
    data: Any
    headers: Dict[str, str]

class ApiClient:
    def __init__(self, base_url: str, timeout: int = 10, retries: int = 3):
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.retries = retries

    async def fetch(self, session: aiohttp.ClientSession, endpoint: str, params: Dict[str, Any] = None) -> ApiResponse:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        last_exc = None
        for attempt in range(1, self.retries + 1):
            try:
                async with session.get(url, params=params, timeout=self.timeout) as resp:
                    data = await resp.json()
                    return ApiResponse(status=resp.status, data=data, headers=dict(resp.headers))
            except (aiohttp.ClientError, asyncio.TimeoutError) as exc:
                last_exc = exc
                await asyncio.sleep(2 ** attempt)
        raise RuntimeError(f"Failed to fetch {url} after {self.retries} retries") from last_exc

    async def post(self, session: aiohttp.ClientSession, endpoint: str, json_payload: Dict[str, Any]) -> ApiResponse:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        async with session.post(url, json=json_payload, timeout=self.timeout) as resp:
            data = await resp.json()
            return ApiResponse(status=resp.status, data=data, headers=dict(resp.headers))

async def main():
    client = ApiClient("https://api.example.com", timeout=5, retries=2)
    async with aiohttp.ClientSession() as session:
        resp = await client.fetch(session, "/items", params={"limit": 10})
        print(resp)
        resp_post = await client.post(session, "/items", json_payload={"name": "test"})
        print(resp_post)

if __name__ == "__main__":
    asyncio.run(main(), debug=True)
```