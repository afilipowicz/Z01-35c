@echo off

set /p count=Podaj ile liczb Fibonacciego wypisac: 

setlocal enableextensions enabledelayedexpansion

if %count% lss 1 (
    exit /b %errorlevel%
) else (
    set n1=0
    set n2=1
    
    for /l %%i in (1,1,%count%) do (
	echo.!n1!
	
	set /a next = !n1! + !n2!
	set /a n1 = !n2!
	set /a n2 = !next!
    )
)

endlocal

exit /b %errorlevel%