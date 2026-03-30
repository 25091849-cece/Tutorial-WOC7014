@echo off
REM Phone Radar - Quick Start Script for Windows

echo.
echo ================================
echo   Phone Radar - Quick Start
echo ================================
echo.

REM Check if virtual environment exists
if not exist ".venv" (
    echo Creating virtual environment...
    python -m venv .venv
)

REM Activate virtual environment
call .venv\Scripts\activate.bat
if errorlevel 1 (
    echo Error: Could not activate virtual environment
    exit /b 1
)

echo Virtual environment activated!
echo.

REM Install/Update dependencies
echo Installing dependencies...
pip install -q django==6.0.3
if errorlevel 1 (
    echo Error: Could not install dependencies
    exit /b 1
)

echo.
echo Running Django checks...
python manage.py check
if errorlevel 1 (
    echo Error: Django checks failed
    exit /b 1
)

echo.
echo ================================
echo   Setup Complete!
echo ================================
echo.
echo To start the server, run:
echo   python manage.py runserver
echo.
echo Then visit: http://localhost:8000
echo.
echo To access admin panel:
echo   http://localhost:8000/admin
echo.
echo Default credentials (if superuser created):
echo   Username: admin
echo   Password: (the one you set during superuser creation)
echo.

pause

