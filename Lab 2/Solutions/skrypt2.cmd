@echo off

set /p source=Podaj sciezke zrodla: 
set /p destination=Podaj sciezke docelowa: 

robocopy %source% %destination% /e /xf *

exit /b %errorlevel%