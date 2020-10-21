@echo off

set count=0

call:funkcja %cd%
exit /b %errorlevel%

:funkcja
cd %1
set /a count += 1

setlocal enableextensions enabledelayedexpansion
for /l %%i in (0,1,%count%) do ( set "temp=!temp! ")
echo %temp% %1
endlocal

for /f "delims=" %%a in ('dir /a:d /b') do (
    call:funkcja %%a
)
set /a count -= 1
cd ..
exit /b 0

