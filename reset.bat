
@echo off
setlocal
rmdir /s /q .\milvus\volumes
docker compose build && docker compose up
endlocal

