#!/usr/bin/env python
"""
Script para aplicar migrações e iniciar servidor Django
"""
import os
import sys
import django
import subprocess
from pathlib import Path

# Configurar ambiente Django
project_dir = Path(__file__).parent
os.chdir(project_dir)
sys.path.insert(0, str(project_dir))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')

print("\n" + "="*50)
print("  SISTEMA RDO - INICIALIZAÇÃO")
print("="*50 + "\n")

try:
    print("[1/2] Aplicando migrações Django...")
    result = subprocess.run(
        [sys.executable, 'manage.py', 'migrate', '--verbosity', '2'],
        cwd=str(project_dir),
        capture_output=False
    )
    
    if result.returncode != 0:
        print("\n❌ Erro ao aplicar migrações!")
        sys.exit(1)
    
    print("\n✓ Migrações aplicadas com sucesso!\n")
    
    # Setup Django após migrations
    django.setup()
    
    # Verificar modelo
    from listag.models import RDO
    count = RDO.objects.count()
    print(f"✓ Modelo RDO carregado. RDOs no banco: {count}\n")
    
    print("="*50)
    print("  ✓ PRONTO PARA TESTE")
    print("="*50 + "\n")
    print("Iniciando servidor Django...")
    print("\nAcesse em:")
    print("  • Dashboard: http://localhost:8000/")
    print("  • RDOs: http://localhost:8000/rdo/")
    print("  • Admin: http://localhost:8000/admin/")
    print("\nPressione CTRL+C para parar\n")
    
    # Iniciar servidor
    subprocess.run(
        [sys.executable, 'manage.py', 'runserver', '0.0.0.0:8000'],
        cwd=str(project_dir)
    )
    
except Exception as e:
    print(f"\n❌ Erro: {str(e)}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
