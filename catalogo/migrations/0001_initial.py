# Generated by Django 4.1.2 on 2024-07-10 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id_autor', models.AutoField(db_column='idAutor', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('nacionalidad', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(db_column='idCategoria', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NavBar',
            fields=[
                ('id_navbar', models.AutoField(db_column='idNavbar', primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id_libro', models.AutoField(db_column='idLibro', primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('anio_publicacion', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('id_autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='libros', to='catalogo.autor')),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='libros', to='catalogo.categoria')),
            ],
        ),
    ]
