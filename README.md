# MCP Frigate Optimizer 🚀
[![MCP](https://img.shields.io/badge/MCP-Protocol-orange)](https://modelcontextprotocol.io)
[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://python.org)

Este servidor implementa el **Model Context Protocol (MCP)** para permitir que agentes de IA (como Claude, Cursor o cualquier cliente MCP) puedan auditar, gestionar y optimizar configuraciones de **Frigate NVR**.

Especialmente útil para optimización de **LPR (Reconocimiento de Placas)**, sintonización de detectores y gestión de grabaciones.

## 🛠️ Herramientas Incluidas

- `get_config`: Recupera el `config.yaml` actual del servidor.
- `update_config`: Sube y valida una nueva configuración.
- `get_system_stats`: Monitorea FPS, uso de Coral TPU y CPU en tiempo real.
- `restart_service`: Reinicia la instancia para aplicar cambios.

## 🚀 Instalación Rápida

### 1. Clonar el repositorio
```bash
git clone https://github.com/avargas2026/MCP-Frigate-0.17.git
cd MCP-Frigate-0.17
```

### 2. Crear entorno virtual e instalar dependencias
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Ejecución Directa
```bash
export FRIGATE_URL="http://IP_DE_TU_FRIGATE:5000"
python server.py
```

## 🤖 Configuración en Claude Desktop

Añade esto a tu archivo de configuración de Claude (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "frigate-optimizer": {
      "command": "python3",
      "args": ["/RUTA/A/MCP-Frigate-0.17/server.py"],
      "env": {
        "FRIGATE_URL": "http://192.168.1.XX:5000"
      }
    }
  }
}
```

## 📄 Licencia
Este proyecto está bajo la Licencia MIT. Libre para uso personal y comercial.

---
*Powered by Antigravity AI Engine*
