# MCP Frigate 0.17
Servidor MCP (Model Context Protocol) desarrollado con **FastMCP** para la interacción avanzada con **Frigate NVR v0.17.0**.

## Características
- **Lectura/Escritura de Configuración**: Obtiene y guarda el `config.yaml` directamente vía API.
- **Monitoreo de Estadísticas**: Acceso a frames por segundo (FPS), uso de CPU/TPU y estado de cámaras.
- **Control**: Reinicio remoto del servicio Frigate.
- **Optimización LPR**: Diseñado para facilitar el ajuste de parámetros de Reconocimiento de Placas.

## Requisitos
- Python 3.10+
- `fastmcp`
- `httpx`

## Configuración de Entorno
Puedes definir la URL de tu servidor Frigate mediante una variable de entorno:
```bash
export FRIGATE_URL="http://TU_IP:5000"
```

## Uso
Para ejecutar el servidor localmente:
```bash
python server.py
```

---
*Desarrollado por Antigravity*
