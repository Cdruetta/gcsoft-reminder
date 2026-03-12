# 🔧 GCsoft Reminder

> Recordatorio automático de mantenimiento de PC para talleres de servicio técnico.

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Platform](https://img.shields.io/badge/platform-Windows-informational)
![Python](https://img.shields.io/badge/python-3.10%2B-yellow)
![License](https://img.shields.io/badge/license-MIT-green)

---

## ¿Qué es?

**GCsoft Reminder** es una pequeña aplicación para Windows que recuerda a los clientes de talleres de servicio técnico cuándo es momento de hacer el mantenimiento preventivo de su PC.

El técnico instala el programa en la PC del cliente al momento de entregar el equipo, configura la fecha del próximo mantenimiento, y el programa se encarga del resto: corre silencioso en segundo plano y muestra un aviso en pantalla cuando llega la fecha indicada.

---

## Capturas

### Panel del técnico
> Se abre al ejecutar el programa. Solo lo usa el técnico al momento de configurar.

```
+------------------------------------------+
|  Panel de Tecnico - GCsoft               |
|                                          |
|  Nombre del taller: [GCsoft          ]   |
|  Telefono:          [358-4268768     ]   |
|  Fecha:             [12/03/2026      ]   |
|                [3 meses][6 meses][1 año] |
|                                          |
|  [ Guardar e Instalar ] [ Previsualizar ]|
+------------------------------------------+
```

### Aviso al cliente
> Aparece automáticamente en la fecha configurada.

```
+------------------------------------------+
|  Recordatorio de Mantenimiento           |
|                                          |
|  Es momento de llevar tu PC a revision  |
|  para su mantenimiento preventivo.       |
|                                          |
|  GCsoft  |  358-4268768                  |
|                                          |
|  [ Posponer 7 dias ]  [ Ya lo hice ]    |
+------------------------------------------+
```

---

## Caracteristicas

- Corre silencioso en segundo plano
- Arranca automaticamente con Windows
- Panel de configuracion exclusivo para el tecnico
- Botones rapidos: 3 meses, 6 meses o 1 año
- El cliente puede posponer 7 dias o marcar como hecho
- Al marcar como hecho, reinicia el ciclo automaticamente
- Sin dependencias externas para el usuario final

---

## Requisitos para compilar

- Windows 10 / 11
- Python 3.10 o superior → [descargar](https://www.python.org/downloads/)
  - Durante la instalacion tildar **"Add Python to PATH"**

---

## Instalacion y uso

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/gcsoft-reminder.git
cd gcsoft-reminder
```

### 2. Compilar el ejecutable

Hacer doble clic en:

```
COMPILAR_EN_WINDOWS.bat
```

El script instala las dependencias necesarias y genera `GCsoft_Reminder.exe` en la misma carpeta. Tarda entre 1 y 2 minutos.

### 3. Usar con un cliente

1. Copiar `GCsoft_Reminder.exe` a la PC del cliente
2. Ejecutarlo — se abre el Panel del Tecnico
3. Configurar la fecha del proximo mantenimiento
4. Clic en **Guardar e Instalar**
5. El programa queda activo y arranca con Windows automaticamente

---

## Estructura del proyecto

```
gcsoft-reminder/
├── reminder.py                 # Codigo principal
├── COMPILAR_EN_WINDOWS.bat     # Script de compilacion
├── .gitignore
└── README.md
```

---

## Roadmap v2

- [ ] Boton para abrir WhatsApp directo con el numero del taller
- [ ] Logo personalizado del taller en el aviso
- [ ] Sonido de notificacion al aparecer el aviso
- [ ] Instalador .msi profesional

---

## Autor

**GCsoft** — Servicio Tecnico  
Tel: 358-4268768

---

## Licencia

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

Este proyecto esta bajo licencia **Creative Commons Attribution 4.0 (CC BY 4.0)**.

Podés usar, modificar y distribuir este software siempre que des el credito correspondiente al autor original:

> GCsoft — Servicio Tecnico | Tel: 358-4268768
