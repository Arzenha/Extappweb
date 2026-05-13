@echo off
chcp 65001 >nul
cd /d "C:\Users\Aszur\OneDrive\Área de Trabalho\Extappweb.worktrees\agents-rdo-transformacao-e-melhorias"
echo Aplicando migrações do Django...
python migrate.py
echo.
echo Migrações concluídas!
echo.
echo Para iniciar o servidor, execute:
echo   python manage.py runserver
echo.
pause
