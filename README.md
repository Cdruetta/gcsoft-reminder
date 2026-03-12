<div align="center">

# 🔧 GCsoft Reminder

### Recordatorio inteligente de mantenimiento de PC

*Mantene a tus clientes conectados con tu taller — automaticamente.*

[![Version](https://img.shields.io/badge/version-1.0.0-e94560?style=for-the-badge)](https://github.com)
[![Platform](https://img.shields.io/badge/Windows-10%2F11-0078D6?style=for-the-badge&logo=windows)](https://github.com)
[![Python](https://img.shields.io/badge/Python-3.10%2B-FFD43B?style=for-the-badge&logo=python&logoColor=black)](https://python.org)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey?style=for-the-badge)](https://creativecommons.org/licenses/by/4.0/)

---

**[Descargar](#instalacion) · [Como usarlo](#uso) · [Roadmap](#roadmap) · [Contacto](#autor)**

</div>

---

## Que problema resuelve?

Cuando un cliente retira su PC del taller, es facil que olvide volver para el mantenimiento preventivo. Meses despues, el equipo falla, pierde datos, o tiene que pagar una reparacion costosa que se podria haber evitado.

**GCsoft Reminder** soluciona esto de forma silenciosa y automatica:

> Installas el programa una sola vez al entregar la PC. El cliente ni lo nota. Cuando llega la fecha, aparece un aviso con tu nombre y telefono. El cliente te llama. Vos trabajas.

---

## Como funciona

```
  TECNICO                          CLIENTE
     |                                |
     | 1. Instala el programa         |
     | 2. Configura la fecha          |
     | 3. Entrega la PC               |
     |                                |
     |         ...pasan 6 meses...    |
     |                                |
     |              4. Aparece aviso -|
     |              5. Cliente llama -|
     | 6. Nuevo trabajo!              |
```

---

## Caracteristicas

| | Funcion |
|---|---|
| ⚙️ | Panel exclusivo para el tecnico |
| 🕐 | Corre silencioso en segundo plano |
| 🚀 | Arranca automaticamente con Windows |
| 📅 | Botones rapidos: 3 meses, 6 meses, 1 ano |
| 🔔 | Aviso con nombre y telefono del taller |
| ⏰ | El cliente puede posponer 7 dias |
| ✅ | Al marcar como hecho, reinicia el ciclo |
| 📦 | Sin dependencias para el usuario final |

---

## Instalacion

### Requisitos

- Windows 10 / 11
- Python 3.10 o superior

> Al instalar Python, tildar **"Add Python to PATH"**
> [Descargar Python](https://www.python.org/downloads/)

### Pasos

```bash
# 1. Clonar el repositorio
git clone https://github.com/TU_USUARIO/gcsoft-reminder.git
cd gcsoft-reminder

# 2. Compilar (doble clic en Windows)
COMPILAR_EN_WINDOWS.bat
```

Esto genera `GCsoft_Reminder.exe` en la misma carpeta. Tarda 1-2 minutos.

---

## Uso

### Como tecnico

1. Copia `GCsoft_Reminder.exe` a la PC del cliente
2. Ejecutalo — se abre el **Panel del Tecnico**
3. Configura la fecha del proximo mantenimiento
4. Clic en **Guardar e Instalar**
5. Listo — el programa queda activo en segundo plano

### Como ve el cliente

Cuando llega la fecha, aparece esta ventana automaticamente:

```
+----------------------------------------------+
|  Recordatorio de Mantenimiento               |
+----------------------------------------------+
|                                              |
|   Es momento de llevar tu PC a revision     |
|   para su mantenimiento preventivo.          |
|                                              |
|   Esto ayuda a que tu equipo dure mas       |
|   y funcione siempre al 100%.               |
|                                              |
|   GCsoft              358-4268768            |
|                                              |
|   [ Posponer 7 dias ]   [ Ya lo hice ]      |
|                                              |
+----------------------------------------------+
```

---

## Estructura del proyecto

```
gcsoft-reminder/
|
+-- reminder.py                # Codigo principal
+-- COMPILAR_EN_WINDOWS.bat    # Script para generar el .exe
+-- .gitignore                 # Archivos excluidos del repo
+-- README.md                  # Este archivo
```

---

## Roadmap

### v1.0 — Actual

- [x] Panel de configuracion para el tecnico
- [x] Monitor silencioso en segundo plano
- [x] Aviso automatico al cliente
- [x] Opciones de posponer o marcar como hecho

### v2.0 — Proximo

- [ ] Boton para abrir WhatsApp directo con el taller
- [ ] Logo personalizado del taller en el aviso
- [ ] Sonido de notificacion
- [ ] Instalador .msi profesional

---

## Autor

<div align="center">

### GCsoft — Servicio Tecnico

358-4268768

*Desarrollado con dedicacion para talleres de servicio tecnico.*

</div>

---

## Licencia

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

Este proyecto esta bajo licencia **Creative Commons Attribution 4.0 (CC BY 4.0)**.

Podes usar, modificar y distribuir este software siempre que des el credito correspondiente al autor original:

> **GCsoft — Servicio Tecnico** | Tel: 358-4268768

---

<div align="center">

*Hecho con dedicacion por GCsoft*

</div>
