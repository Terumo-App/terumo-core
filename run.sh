# #!/bin/bash
# export PYTHONPATH= C:/Users/Maods/Documents/Development/Mestrado/terumo/apps/new_api:$PYTHONPATH
# python seu_script.py


@echo off
setlocal
set PYTHONPATH=C:\Users\Maods\Documents\Development\Mestrado\terumo\apps\new_api;%PYTHONPATH%
python seu_script.py
endlocal