# Generated by Django 4.1.3 on 2023-12-10 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Certificados',
            fields=[
                ('id_certificado', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_emision', models.DateField(blank=True, null=True)),
                ('rut', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'certificados',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comisiones',
            fields=[
                ('id_comision', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'comisiones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GruposFamiliares',
            fields=[
                ('id_grupo_familiar', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_completo', models.CharField(blank=True, max_length=255, null=True)),
                ('rut', models.CharField(max_length=12)),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('comentario', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'grupos_familiares',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Parentescos',
            fields=[
                ('id_parentesco', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_parentesco', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'parentescos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Perfiles',
            fields=[
                ('id_perfil', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_perfil', models.CharField(blank=True, max_length=13, null=True)),
            ],
            options={
                'db_table': 'perfiles',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Socios',
            fields=[
                ('rut', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
                ('apellido', models.CharField(blank=True, max_length=255, null=True)),
                ('direccion', models.CharField(blank=True, max_length=255, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('telefono', models.IntegerField(blank=True, null=True)),
                ('correo', models.CharField(blank=True, max_length=255, null=True)),
                ('estado_civil', models.CharField(blank=True, max_length=7, null=True)),
                ('jefe_hogar', models.IntegerField(blank=True, null=True)),
                ('id_certificado', models.IntegerField(blank=True, null=True)),
                ('ide_comision', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'socios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoCertificados',
            fields=[
                ('id_tipo_certificado', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_tipo_certificado', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'tipo_certificados',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoComisiones',
            fields=[
                ('id_tipo_comision', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_comision', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'tipo_comisiones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UnionSocioCertificado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'union_socio_certificado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UnionSocioComision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'union_socio_comision',
                'managed': False,
            },
        ),
    ]
