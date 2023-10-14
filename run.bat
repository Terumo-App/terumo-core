
@echo off
setlocal
set PYTHONPATH=C:\Users\Maods\Documents\Development\Mestrado\terumo\apps\new_api;%PYTHONPATH%
python src/main.py
endlocal


setlocal
set PYTHONPATH=C:\Users\Maods\Documents\Development\Mestrado\terumo\apps\new_api;%PYTHONPATH%
& 'C:\Users\Maods\.virtualenvs\terumo-service-search-monolith-tK6ZlZEC\Scripts\python.exe' 'c:\Users\Maods\.vscode\extensions\ms-python.python-2023.18.0\pythonFiles\lib\python\debugpy\adapter/../..\debugpy\launcher' '50099' '--' 'c:\Users\Maods\Documents\Development\Mestrado\terumo\apps\new_api\src\main.py'
endlocal