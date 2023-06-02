# Generated by Django 4.1.7 on 2023-06-02 04:20

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_student', models.BooleanField(default=False)),
                ('is_teacher', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ClassAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('assignment_name', models.CharField(max_length=250)),
                ('assignment', models.FileField(upload_to='assignments')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='StudentsInClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='Student', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=250)),
                ('roll_no', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('student_profile_pic', models.ImageField(blank=True, upload_to='classroom/student_profile_pic')),
            ],
            options={
                'ordering': ['roll_no'],
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='Teacher', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=250)),
                ('subject_name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('teacher_profile_pic', models.ImageField(blank=True, upload_to='classroom/teacher_profile_pic')),
                ('class_students', models.ManyToManyField(through='classroom.StudentsInClass', to='classroom.student')),
            ],
        ),
        migrations.CreateModel(
            name='SubmitAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('submit', models.FileField(upload_to='Submission')),
                ('submitted_assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submission_for_assignment', to='classroom.classassignment')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_submit', to='classroom.student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_submit', to='classroom.teacher')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='studentsinclass',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_student_name', to='classroom.student'),
        ),
        migrations.AddField(
            model_name='studentsinclass',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_teacher', to='classroom.teacher'),
        ),
        migrations.CreateModel(
            name='StudentMarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=250)),
                ('marks_obtained', models.IntegerField()),
                ('maximum_marks', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marks', to='classroom.student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='given_marks', to='classroom.teacher')),
            ],
        ),
        migrations.AddField(
            model_name='classassignment',
            name='student',
            field=models.ManyToManyField(related_name='student_assignment', to='classroom.student'),
        ),
        migrations.AddField(
            model_name='classassignment',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_assignment', to='classroom.teacher'),
        ),
        migrations.AlterUniqueTogether(
            name='studentsinclass',
            unique_together={('teacher', 'student')},
        ),
        migrations.CreateModel(
            name='MessageToTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('message', models.TextField()),
                ('message_html', models.TextField(editable=False)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='classroom.student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='classroom.teacher')),
            ],
            options={
                'ordering': ['-created_at'],
                'unique_together': {('student', 'message')},
            },
        ),
        migrations.CreateModel(
            name='ClassNotice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('message', models.TextField()),
                ('message_html', models.TextField(editable=False)),
                ('students', models.ManyToManyField(related_name='class_notice', to='classroom.student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to='classroom.teacher')),
            ],
            options={
                'ordering': ['-created_at'],
                'unique_together': {('teacher', 'message')},
            },
        ),
    ]
