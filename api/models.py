from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import uuid

from datetime import datetime


def get_proj_image_filename(instance, filename):
    title = instance.project.uniq_id
    slug = slugify(title)
    return f"static/img/profiles/{slug}-{filename}"


def get_prof_image_filename(instance, filename):
    title = instance.profile.profile_id
    slug = slugify(title)
    return f"static/img/projects/{slug}/{slug}-{filename}"

class Faculty(models.Model):
    name = models.CharField(max_length=20, default="")
    display_name = models.CharField(max_length=100, default="")

class Tags(models.Model):
    tag = models.CharField(max_length=20, primary_key=True)
    display_tag = models.CharField(max_length=20, default='#')
    is_visible = models.BooleanField()

    def save(self, *args, **kwargs):
        self.tag = f'#{self.tag}'
        super(Tags, self).save(*args, **kwargs)

class Roles(models.Model):
    role = models.TextField(default='participant')
    role_display = models.TextField(default='Участник')
    role_color = models.CharField(max_length=20)
    role_level = models.IntegerField()

class ProfileImages(models.Model):
    profile_id = models.ForeignKey('Profile', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_prof_image_filename)

class ProjectRoles(models.Model):
    project_id = models.ForeignKey('Project', on_delete=models.CASCADE)
    user_id = models.ForeignKey('Profile', on_delete=models.PROTECT)
    role = models.TextField(default='Участник')


class Project(models.Model):
    desc = models.TextField(default="none")
    label = models.CharField(max_length=50)
    uniq_id = models.CharField(max_length=50, primary_key=True)
    profiles = models.ManyToManyField('Profile')
    description = models.TextField()
    tags = models.ManyToManyField(Tags)
    pub_date = models.DateTimeField()
    is_verifyied = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.PROTECT)


    def __str__(self):
        return f'{self.label} {self.uniq_id}'
    
    def save(self, *args, **kwargs):
        self.pub_date = datetime.now()
        self.uniq_id = str(uuid.uuid4())
        # if self.id is None:
        #     try:
        #         last_obj = Project.objects.latest('id')
        #     except:
        #         last_obj = None
        #     if last_obj:
        #         self.id = last_obj.id+1
        #     else:
        #         self.id = 1
        super(Project, self).save(*args ,**kwargs)
    



class ProjectImages(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, to_field='uniq_id')
    image = models.ImageField(upload_to=get_proj_image_filename)

class Profile(User):
    profile_id = models.CharField(max_length=100, primary_key=True)
    tags = models.ManyToManyField(Tags)
    phone_number = models.CharField(max_length=50)
    description = models.TextField(default='Описание')
    roles = models.ManyToManyField(Roles)
    is_verifyied = models.BooleanField(default=False)


class ProjectsToVerify(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    auth_key = models.TextField(default='NaN')

class ProfilesToVerify(models.Model):
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    