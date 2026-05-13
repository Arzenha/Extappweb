@echo off
chcp 65001 >nul
cd /d "C:\Users\Aszur\OneDrive\Área de Trabalho\Extappweb.worktrees\agents-rdo-transformacao-e-melhorias"
echo.
echo ============================================
echo  INICIANDO SERVIDOR RDO
echo ============================================
echo.
echo Acesse em:
echo   • Dashboard: http://localhost:8000/
echo   • RDOs: http://localhost:8000/rdo/
echo   • Admin: http://localhost:8000/admin/
echo.
echo Pressione CTRL+C para parar
echo.
python manage.py runserver 0.0.0.0:8000
