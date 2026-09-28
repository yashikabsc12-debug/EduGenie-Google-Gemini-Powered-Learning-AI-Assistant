@echo off

echo ========================================
echo        EduGenie Setup
echo ========================================

echo.

if not exist ".venv" (

    echo Creating virtual environment...

    python -m venv .venv
)


echo Activating virtual environment...

call .venv\Scripts\activate


echo.

echo Installing dependencies...

python -m pip install --upgrade pip

pip install -r requirements.txt


echo.

echo ========================================
echo        Starting EduGenie
echo ========================================

echo.

uvicorn main:app --reload

pause