@echo off
title Eclipse IDE Launcher
echo Launching Eclipse IDE Java Workspace...

:: Try launching in Chrome or Edge app mode (frameless / no address bar for total stealth)
where msedge >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    start msedge --app="%~dp0index.html"
    exit
)

where chrome >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    start chrome --app="%~dp0index.html"
    exit
)

:: Fallback to default browser
start "" "%~dp0index.html"
exit

