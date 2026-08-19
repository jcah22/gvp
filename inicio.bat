@echo off

IF NOT EXIST env(
    echo la carpeta "venv" no existe.
    pause
    exit /b
)

call env\Scripts\activate.bat

echo Entorno virtual activado.

cmd \k