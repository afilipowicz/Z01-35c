@echo off

net session >nul 2>&1

if %errorlevel% NEQ 0 (
    echo Current user does not have admin privileges.
)

exit /b %errorlevel%