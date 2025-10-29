@echo off
echo ========================================
echo    API RELIABILITY MONITOR PROJECT
echo ========================================
echo.
echo Installing dependencies...
pip install -r requirements.txt
echo.
echo Starting API Monitor on port 8080...
start "API Monitor" cmd /k python api_monitor.py
echo.
timeout /t 3 /nobreak >nul
echo Starting Prometheus on port 9090...
start "Prometheus" cmd /k prometheus.exe --config.file=prometheus.yml
echo.
echo ========================================
echo Project started successfully!
echo.
echo Access points:
echo - API Dashboard: Open api_dashboard.html
echo - Raw Metrics: http://localhost:8080/metrics
echo - Prometheus UI: http://localhost:9090
echo ========================================
pause