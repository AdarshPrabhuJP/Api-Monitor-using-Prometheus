@echo off
echo ========================================
echo    QUICK START - API MONITOR
echo ========================================
echo.
echo Step 1: Installing dependencies...
pip install prometheus_client requests
echo.
echo Step 2: Testing API Monitor...
python test_connection.py
echo.
echo Step 3: Starting API Monitor...
echo (This will run in the background)
start /min python api_monitor.py
echo.
echo Waiting 5 seconds for startup...
timeout /t 5 /nobreak >nul
echo.
echo Step 4: Testing connection again...
python test_connection.py
echo.
echo Step 5: Open api_dashboard.html in your browser
echo.
echo ========================================
echo If everything works, you should see:
echo - API Monitor running messages
echo - Dashboard showing API status
echo ========================================
pause