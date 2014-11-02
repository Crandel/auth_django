# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'AppliedJobs.file'
        db.delete_column(u'careers_appliedjobs', 'file')

        # Adding field 'AppliedJobs.upload_file'
        db.add_column(u'careers_appliedjobs', 'upload_file',
                      self.gf('django.db.models.fields.files.FileField')(default='try', max_length=100),
                      keep_default=False)


        # Changing field 'AppliedJobs.tele'
        db.alter_column(u'careers_appliedjobs', 'tele', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'AppliedJobs.date'
        db.alter_column(u'careers_appliedjobs', 'date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

    def backwards(self, orm):
        # Adding field 'AppliedJobs.file'
        db.add_column(u'careers_appliedjobs', 'file',
                      self.gf('django.db.models.fields.files.FileField')(default='gfg', max_length=100),
                      keep_default=False)

        # Deleting field 'AppliedJobs.upload_file'
        db.delete_column(u'careers_appliedjobs', 'upload_file')


        # Changing field 'AppliedJobs.tele'
        db.alter_column(u'careers_appliedjobs', 'tele', self.gf('django.db.models.fields.EmailField')(max_length=255))

        # Changing field 'AppliedJobs.date'
        db.alter_column(u'careers_appliedjobs', 'date', self.gf('django.db.models.fields.DateTimeField')())

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
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'designation': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {}),
            'job_cat': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['careers.JobCategory']"}),
            'short_desc': ('ckeditor.fields.RichTextField', [], {}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'sort_order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        u'careers.jobcategory': {
            'Meta': {'ordering': "('sort_order',)", 'object_name': 'JobCategory'},
            'catog': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
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