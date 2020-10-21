@echo off

set /p source=Podaj sciezke do pliku wideo: 

ffmpeg -i %source% -ss 00:00:01.000 -frames:v 1 thumbnail.png

exit /b %errorlevel%