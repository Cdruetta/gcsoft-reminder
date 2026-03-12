@echo off
title GCsoft Reminder - Compilador

echo.
echo ==========================================
echo   GCsoft Reminder - Compilador v1.0
echo ==========================================
echo.

echo [1/3] Verificando Python...
py --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    python --version >nul 2>&1
    IF %ERRORLEVEL% NEQ 0 (
        echo ERROR: Python no esta instalado.
        echo Bajalo de: https://www.python.org/downloads/
        pause
        exit /b 1
    )
    set PYCMD=python
) ELSE (
    set PYCMD=py
)
%PYCMD% --version
echo OK - Python encontrado.
echo.

echo [2/3] Instalando dependencias...
%PYCMD% -m pip install pyinstaller pillow --quiet --disable-pip-version-check
IF %ERRORLEVEL% NEQ 0 (
    echo ERROR: No se pudieron instalar las dependencias.
    pause
    exit /b 1
)
echo OK - Dependencias listas.
echo.

echo [3/3] Compilando .exe (1-2 minutos)...
%PYCMD% -m PyInstaller --onefile --windowed --name="GCsoft_Reminder" --clean reminder.py

IF %ERRORLEVEL% NEQ 0 (
    echo ERROR: Fallo la compilacion.
    pause
    exit /b 1
)

IF EXIST "dist\GCsoft_Reminder.exe" (
    copy "dist\GCsoft_Reminder.exe" "GCsoft_Reminder.exe" >nul
    echo.
    echo ==========================================
    echo   LISTO! GCsoft_Reminder.exe generado.
    echo   Esta en esta misma carpeta.
    echo ==========================================
) ELSE (
    echo ERROR: No se encontro el archivo compilado.
)

pause
