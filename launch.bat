@echo off
title Professional LinkedIn AI System

echo.
echo ========================================
echo  Professional LinkedIn AI System
echo ========================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python not found!
    echo Please install Python 3.8+ from https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Check if .env exists
if not exist ".env" (
    echo ERROR: .env file not found!
    echo Please copy .env.example to .env and configure your API keys.
    pause
    exit /b 1
)

REM Launch the application
echo Starting Professional LinkedIn AI System...
python launch.py

pause
