from django.db import models

import json

# Create your models here.

class AcademicDetail(models.Model):
    academic_id = models.AutoField(primary_key=True)
    # highschool & intermediate detail should be json type data
    # consist of marks, is_cgpa & school_name keys respectively
    highschool_detail = models.TextField()
    intermediate_detail = models.TextField()
    academic_activities = models.TextField(blank=True)

    @property
    def highschool_details(self):
        return json.loads(self.highschool_detail)
    
    @property
    def intermediate_details(self):
        return json.loads(self.intermediate_detail)

class ProfessionalDetail(models.Model):
    professional_id = models.AutoField(primary_key=True)
    company = models.TextField()
    designation = models.CharField(max_length=90)
    join_date = models.DateField()
    last_wd = models.DateField()
    certification = models.TextField(blank=True)
    valid_from = models.DateField(blank=True)
    valid_till = models.DateField(blank=True)

class profile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    contact_number = models.IntegerField()
    location = models.CharField(max_length=180)
    email = models.EmailField()
    academic_data = models.OneToOneField(
        AcademicDetail,
        on_delete=models.CASCADE,
    )
    professional_data = models.OneToOneField(
        ProfessionalDetail,
        on_delete=models.CASCADE,
    )
    @property
    def name(self):
        return ' '.join([self.first_name, self.last_name])
