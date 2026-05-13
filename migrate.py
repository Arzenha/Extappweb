#!/usr/bin/env python
import os
import sys
import subprocess
from pathlib import Path

project_dir = Path(__file__).parent
os.chdir(project_dir)

print("\n" + "="*50)
print("  Aplicando migrações...")
print("="*50 + "\n")

# Executar migrate
result = subprocess.run(
    [sys.executable, 'manage.py', 'migrate'],
    cwd=str(project_dir)
)

if result.returncode == 0:
    print("\n" + "="*50)
    print("  ✓ Migrações aplicadas com sucesso!")
    print("="*50 + "\n")
    print("Agora execute: python manage.py runserver")
else:
    print("\n❌ Erro ao aplicar migrações")
    sys.exit(1)
