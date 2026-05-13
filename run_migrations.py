#!/usr/bin/env python
import os
import sys
import django
from pathlib import Path

# Adicionar o diretório do projeto ao path
project_dir = Path(__file__).parent
sys.path.insert(0, str(project_dir))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from django.core.management import call_command

print("Aplicando migrações...")
call_command('migrate')
print("✓ Migrações aplicadas com sucesso!")

from listag.models import RDO
print(f"✓ Modelo RDO carregado: {RDO}")
print("✓ Sistema RDO pronto para uso!")
