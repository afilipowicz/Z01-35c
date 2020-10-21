@echo off

set /p extension=Podaj rozszerzenie: 
set /p directory=Podaj sciezke: 

dir %directory% /s (*.%extension%) | find "%extension%"

exit /b %errorlevel%