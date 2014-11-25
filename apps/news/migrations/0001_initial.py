# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NewsModel'
        db.create_table(u'news_newsmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=512)),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, max_length=255, blank=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')(default=2014, max_length=255)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=255, null=True)),
        ))
        db.send_create_signal(u'news', ['NewsModel'])


    def backwards(self, orm):
        # Deleting model 'NewsModel'
        db.delete_table(u'news_newsmodel')


    models = {
        u'news.newsmodel': {
            'Meta': {'object_name': 'NewsModel'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'max_length': '255', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '512'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '255', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'year': ('django.db.models.fields.IntegerField', [], {'default': '2014', 'max_length': '255'})
        }
    }

    complete_apps = ['news']