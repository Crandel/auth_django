# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Nationality.nationality_en'
        db.add_column(u'careers_nationality', 'nationality_en',
                      self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Nationality.nationality_ar'
        db.add_column(u'careers_nationality', 'nationality_ar',
                      self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Nationality.nationality_en'
        db.delete_column(u'careers_nationality', 'nationality_en')

        # Deleting field 'Nationality.nationality_ar'
        db.delete_column(u'careers_nationality', 'nationality_ar')


    models = {
        u'careers.appliedjobs': {
            'Meta': {'object_name': 'AppliedJobs'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'designation': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_cat': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['careers.JobCategory']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'tele': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'upload_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        u'careers.career': {
            'Meta': {'ordering': "(u'-sort_order',)", 'object_name': 'Career'},
            'cl_time': ('django.db.models.fields.DateTimeField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'designation': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'designation_ar': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'designation_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {}),
            'job_cat': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['careers.JobCategory']"}),
            'short_desc': ('ckeditor.fields.RichTextField', [], {}),
            'short_desc_ar': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'short_desc_en': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'sort_order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        u'careers.careerinfo': {
            'Meta': {'object_name': 'CareerInfo'},
            'description': ('ckeditor.fields.RichTextField', [], {}),
            'description_ar': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'description_en': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '255', 'null': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']", 'unique': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_ar': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'careers.jobcategory': {
            'Meta': {'ordering': "(u'sort_order',)", 'object_name': 'JobCategory'},
            'catog': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'catog_ar': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'catog_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sort_order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        u'careers.nationality': {
            'Meta': {'ordering': "(u'nationality',)", 'object_name': 'Nationality'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'nationality_ar': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'nationality_en': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'})
        },
        u'careers.svmodel': {
            'Meta': {'ordering': "(u'created',)", 'object_name': 'SVModel'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'cv': ('django.db.models.fields.files.FileField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
        },
        u'careers.vacancy': {
            'Meta': {'ordering': "(u'sort', u'-created')", 'object_name': 'Vacancy'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 11, 13, 0, 0)'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'position_ar': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'position_en': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'requirement': ('ckeditor.fields.RichTextField', [], {}),
            'requirement_ar': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'requirement_en': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'sort': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'})
        },
        u'careers.vacancyapply': {
            'Meta': {'ordering': "(u'-created',)", 'object_name': 'VacancyApply'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'cv': ('django.db.models.fields.files.FileField', [], {'max_length': '255'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'nationality': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['careers.Nationality']"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'vacancy': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['careers.Vacancy']"})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['careers']