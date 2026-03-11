import asyncio
import httpx
from fastmcp import FastMCP
import os
import json
import logging

# Configuración de Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mcp-frigate")

# Habilitar el parser experimental de OpenAPI de FastMCP
os.environ["FASTMCP_EXPERIMENTAL_ENABLE_NEW_OPENAPI_PARSER"] = "true"

# URL de Frigate (Configurable vía variable de entorno)
FRIGATE_URL = os.environ.get("FRIGATE_URL", "http://localhost:5000").rstrip("/")

mcp = FastMCP(
    "Frigate-Optimizer",
    title="Frigate NVR MCP Server",
    description="Protocolo de contexto para gestionar y optimizar instancias de Frigate NVR"
)

@mcp.tool()
async def get_config() -> str:
    """Obtiene la configuración actual (YAML) de la instancia de Frigate."""
    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            resp = await client.get(f"{FRIGATE_URL}/api/config/raw")
            resp.raise_for_status()
            data = resp.text.strip()
            # Manejar respuestas JSON-stringified
            if data.startswith('"') and data.endswith('"'):
                return json.loads(data)
            return data
        except Exception as e:
            return f"Error al conectar con Frigate en {FRIGATE_URL}: {str(e)}"

@mcp.tool()
async def update_config(yaml_content: str) -> str:
    """Actualiza la configuración de Frigate enviando un nuevo contenido YAML."""
    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            resp = await client.post(
                f"{FRIGATE_URL}/api/config/save?save_option=save",
                content=yaml_content,
                headers={"Content-Type": "text/plain"}
            )
            if resp.status_code == 200:
                return "Configuración actualizada correctamente. Se requiere reiniciar Frigate para aplicar cambios."
            return f"Error de validación en Frigate: {resp.text}"
        except Exception as e:
            return f"Error al enviar configuración: {str(e)}"

@mcp.tool()
async def get_system_stats() -> str:
    """Obtiene estadísticas detalladas del sistema: CPU, TPU, FPS de cámaras y almacenamiento."""
    async with httpx.AsyncClient(timeout=15.0) as client:
        try:
            resp = await client.get(f"{FRIGATE_URL}/api/stats")
            resp.raise_for_status()
            return resp.text
        except Exception as e:
            return f"Error al obtener estadísticas: {str(e)}"

@mcp.tool()
async def restart_service() -> str:
    """Envía un comando de reinicio a la instancia de Frigate."""
    async with httpx.AsyncClient(timeout=10.0) as client:
        try:
            resp = await client.post(f"{FRIGATE_URL}/api/restart")
            if resp.status_code == 200:
                return "Orden de reinicio enviada con éxito."
            return f"Frigate rechazó el reinicio: {resp.status_code}"
        except Exception as e:
            return f"Error al contactar con el servicio: {str(e)}"

if __name__ == "__main__":
    logger.info(f"Iniciando MCP Frigate Optimizer apuntando a: {FRIGATE_URL}")
    mcp.run()
