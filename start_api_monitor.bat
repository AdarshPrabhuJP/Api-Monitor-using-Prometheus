@echo off
echo Installing Python dependencies...
pip install -r requirements.txt

echo.
echo Starting API Monitor Exporter...
python api_monitor.py