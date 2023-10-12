# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Catalogo(models.Model):
    id = models.IntegerField(primary_key=True)
    sub_id = models.IntegerField(blank=True, null=True)
    tematica = models.TextField(blank=True, null=True)  # This field type is a guess.
    carpeta = models.TextField(blank=True, null=True)  # This field type is a guess.
    nombre = models.TextField(blank=True, null=True)  # This field type is a guess.
    ano = models.TextField(blank=True, null=True)  # This field type is a guess.
    utlima_modificacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    tipo = models.TextField(blank=True, null=True)  # This field type is a guess.
    fuente = models.TextField(blank=True, null=True)  # This field type is a guess.
    escala = models.TextField(blank=True, null=True)  # This field type is a guess.
    unidad_espacial = models.TextField(blank=True, null=True)  # This field type is a guess.
    formato = models.TextField(blank=True, null=True)  # This field type is a guess.
    descripcion = models.TextField(blank=True, null=True)  # This field type is a guess.
    palabras_clave = models.TextField(blank=True, null=True)  # This field type is a guess.
    ruta_relativa = models.TextField(blank=True, null=True)  # This field type is a guess.
    observaciones = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'catalogo'


class Catalogo2(models.Model):
    id = models.IntegerField(primary_key=True)
    sub_id = models.IntegerField(blank=True, null=True)
    tematica = models.CharField(max_length=400, blank=True, null=True)
    carpeta = models.CharField(max_length=400, blank=True, null=True)
    nombre = models.CharField(max_length=400, blank=True, null=True)
    ano = models.CharField(max_length=400, blank=True, null=True)
    ultima_modificacion = models.CharField(max_length=400, blank=True, null=True)
    tipo = models.CharField(max_length=400, blank=True, null=True)
    fuente = models.CharField(max_length=400, blank=True, null=True)
    escala = models.CharField(max_length=400, blank=True, null=True)
    unidad_espacial = models.CharField(max_length=400, blank=True, null=True)
    formato = models.CharField(max_length=400, blank=True, null=True)
    descripcion = models.CharField(max_length=400, blank=True, null=True)
    palabras_clave = models.CharField(max_length=400, blank=True, null=True)
    ruta_relativa = models.CharField(max_length=400, blank=True, null=True)
    observacion = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalogo2'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Post(models.Model):

    class Meta:
        managed = False
        db_table = 'post'


class Usuarios(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios'
