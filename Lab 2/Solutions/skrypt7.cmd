@echo off

set /a input=%1

if %input% == 0 (
    echo 0
) else if %input% LSS 0 (
    echo Podaj nieujemna liczbe calkowita
) else (
    setlocal enableextensions enabledelayedexpansion

    set /a answ=1
    for /l %%i in (1,1,%input%) do ( set /a answ = !answ! * %%i )
    echo !answ!

    endlocal
)

exit /b %errorlevel%


