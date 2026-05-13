@echo off
chcp 65001 >nul
echo.
echo ============================================
echo  SISTEMA RDO - TESTE E CONFIGURAÇÃO
echo ============================================
echo.

cd /d "C:\Users\Aszur\OneDrive\Área de Trabalho\Extappweb.worktrees\agents-rdo-transformacao-e-melhorias"

echo [1/3] Aplicando migrações ao banco de dados...
echo.
python manage.py migrate
if errorlevel 1 (
    echo.
    echo ❌ Erro ao aplicar migrações!
    pause
    exit /b 1
)

echo.
echo ✓ Migrações aplicadas com sucesso!
echo.
echo [2/3] Testando modelo RDO...
echo.
python -c "import django; django.setup(); from listag.models import RDO; print('✓ Modelo RDO carregado com sucesso!')"
if errorlevel 1 (
    echo.
    echo ❌ Erro ao carregar modelo RDO!
    pause
    exit /b 1
)

echo.
echo ============================================
echo  ✓ SISTEMA PRONTO PARA TESTE
echo ============================================
echo.
echo [3/3] Iniciando servidor Django...
echo.
echo Acesse em: http://localhost:8000
echo Dashboard: http://localhost:8000/ (home)
echo RDOs: http://localhost:8000/rdo/
echo Admin: http://localhost:8000/admin/
echo.
echo Pressione CTRL+C para parar o servidor
echo.
python manage.py runserver 0.0.0.0:8000
