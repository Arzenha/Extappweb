# Generated migration for RDO model

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listag', '0002_escola_delete_listag'),
    ]

    operations = [
        migrations.CreateModel(
            name='RDO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obra', models.CharField(max_length=100, verbose_name='Obra')),
                ('responsavel', models.CharField(max_length=100, verbose_name='Responsável')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('data', models.DateField(verbose_name='Data')),
                ('clima', models.CharField(choices=[('ensolarado', 'Ensolarado'), ('nublado', 'Nublado'), ('chuvoso', 'Chuvoso'), ('parcialmente_nublado', 'Parcialmente Nublado'), ('tempestuoso', 'Tempestuoso')], max_length=50, verbose_name='Clima')),
                ('funcionarios', models.IntegerField(verbose_name='Número de Funcionários')),
                ('observacoes', models.TextField(blank=True, null=True, verbose_name='Observações')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='rdo_fotos/', verbose_name='Foto')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'RDO',
                'verbose_name_plural': 'RDOs',
                'ordering': ['-data'],
            },
        ),
        migrations.DeleteModel(
            name='Escola',
        ),
    ]
