# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CareerInfo.title_en'
        db.add_column(u'careers_careerinfo', 'title_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CareerInfo.title_ar'
        db.add_column(u'careers_careerinfo', 'title_ar',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CareerInfo.description_en'
        db.add_column(u'careers_careerinfo', 'description_en',
                      self.gf('ckeditor.fields.RichTextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'CareerInfo.description_ar'
        db.add_column(u'careers_careerinfo', 'description_ar',
                      self.gf('ckeditor.fields.RichTextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Career.designation_en'
        db.add_column(u'careers_career', 'designation_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Career.designation_ar'
        db.add_column(u'careers_career', 'designation_ar',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Career.short_desc_en'
        db.add_column(u'careers_career', 'short_desc_en',
                      self.gf('ckeditor.fields.RichTextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Career.short_desc_ar'
        db.add_column(u'careers_career', 'short_desc_ar',
                      self.gf('ckeditor.fields.RichTextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'JobCategory.catog_en'
        db.add_column(u'careers_jobcategory', 'catog_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'JobCategory.catog_ar'
        db.add_column(u'careers_jobcategory', 'catog_ar',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'CareerInfo.title_en'
        db.delete_column(u'careers_careerinfo', 'title_en')

        # Deleting field 'CareerInfo.title_ar'
        db.delete_column(u'careers_careerinfo', 'title_ar')

        # Deleting field 'CareerInfo.description_en'
        db.delete_column(u'careers_careerinfo', 'description_en')

        # Deleting field 'CareerInfo.description_ar'
        db.delete_column(u'careers_careerinfo', 'description_ar')

        # Deleting field 'Career.designation_en'
        db.delete_column(u'careers_career', 'designation_en')

        # Deleting field 'Career.designation_ar'
        db.delete_column(u'careers_career', 'designation_ar')

        # Deleting field 'Career.short_desc_en'
        db.delete_column(u'careers_career', 'short_desc_en')

        # Deleting field 'Career.short_desc_ar'
        db.delete_column(u'careers_career', 'short_desc_ar')

        # Deleting field 'JobCategory.catog_en'
        db.delete_column(u'careers_jobcategory', 'catog_en')

        # Deleting field 'JobCategory.catog_ar'
        db.delete_column(u'careers_jobcategory', 'catog_ar')


    models = {
        u'careers.appliedjobs': {
            'Meta': {'object_name': 'AppliedJobs'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'designation': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'tele': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'upload_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        u'careers.career': {
            'Meta': {'ordering': "('-sort_order',)", 'object_name': 'Career'},
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
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']", 'unique': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_ar': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'careers.jobcategory': {
            'Meta': {'ordering': "('sort_order',)", 'object_name': 'JobCategory'},
            'catog': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'catog_ar': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'catog_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sort_order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['careers']