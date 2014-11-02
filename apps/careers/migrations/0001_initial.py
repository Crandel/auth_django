# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'JobCategory'
        db.create_table(u'careers_jobcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('catog', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('sort_order', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
        ))
        db.send_create_signal(u'careers', ['JobCategory'])

        # Adding model 'Career'
        db.create_table(u'careers_career', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('job_cat', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['careers.JobCategory'])),
            ('designation', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('short_desc', self.gf('ckeditor.fields.RichTextField')()),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('is_published', self.gf('django.db.models.fields.BooleanField')()),
            ('sort_order', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
        ))
        db.send_create_signal(u'careers', ['Career'])


    def backwards(self, orm):
        # Deleting model 'JobCategory'
        db.delete_table(u'careers_jobcategory')

        # Deleting model 'Career'
        db.delete_table(u'careers_career')


    models = {
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