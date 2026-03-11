import asyncio
import httpx
from fastmcp import FastMCP
import os
import json

# Habilitar el parser experimental de OpenAPI de FastMCP
os.environ["FASTMCP_EXPERIMENTAL_ENABLE_NEW_OPENAPI_PARSER"] = "true"

# URL de Frigate (Ajustar según necesidad)
# Por defecto apunta a la IP local del proyecto
FRIGATE_URL = os.environ.get("FRIGATE_URL", "http://192.168.5.65:5000")

mcp = FastMCP("Frigate")

@mcp.tool()
async def get_raw_config() -> str:
    """Obtiene la configuración raw (YAML) de Frigate."""
    async with httpx.AsyncClient(timeout=30.0) as client:
        resp = await client.get(f"{FRIGATE_URL}/api/config/raw")
        data = resp.text.strip()
        # Manejar si viene entre comillas (JSON string)
        if data.startswith('"') and data.endswith('"'):
            return json.loads(data)
        return data

@mcp.tool()
async def save_config(yaml_content: str) -> str:
    """Guarda una nueva configuración en Frigate."""
    async with httpx.AsyncClient(timeout=30.0) as client:
        resp = await client.post(
            f"{FRIGATE_URL}/api/config/save?save_option=save",
            content=yaml_content,
            headers={"Content-Type": "text/plain"}
        )
        if resp.status_code == 200:
            return "Configuración guardada exitosamente."
        return f"Error al guardar: {resp.status_code} - {resp.text}"

@mcp.tool()
async def get_stats() -> str:
    """Obtiene las estadísticas de rendimiento de Frigate."""
    async with httpx.AsyncClient(timeout=30.0) as client:
        resp = await client.get(f"{FRIGATE_URL}/api/stats")
        return resp.text

@mcp.tool()
async def restart_frigate() -> str:
    """Reinicia el servicio de Frigate."""
    async with httpx.AsyncClient(timeout=30.0) as client:
        resp = await client.post(f"{FRIGATE_URL}/api/restart")
        return f"Reinicio enviado: {resp.status_code}"

if __name__ == "__main__":
    mcp.run()
