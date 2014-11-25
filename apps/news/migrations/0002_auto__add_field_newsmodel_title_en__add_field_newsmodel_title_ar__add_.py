# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'NewsModel.title_en'
        db.add_column(u'news_newsmodel', 'title_en',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'NewsModel.title_ar'
        db.add_column(u'news_newsmodel', 'title_ar',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'NewsModel.description_en'
        db.add_column(u'news_newsmodel', 'description_en',
                      self.gf('django.db.models.fields.TextField')(max_length=512, null=True, blank=True),
                      keep_default=False)

        # Adding field 'NewsModel.description_ar'
        db.add_column(u'news_newsmodel', 'description_ar',
                      self.gf('django.db.models.fields.TextField')(max_length=512, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'NewsModel.title_en'
        db.delete_column(u'news_newsmodel', 'title_en')

        # Deleting field 'NewsModel.title_ar'
        db.delete_column(u'news_newsmodel', 'title_ar')

        # Deleting field 'NewsModel.description_en'
        db.delete_column(u'news_newsmodel', 'description_en')

        # Deleting field 'NewsModel.description_ar'
        db.delete_column(u'news_newsmodel', 'description_ar')


    models = {
        u'news.newsmodel': {
            'Meta': {'object_name': 'NewsModel'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'max_length': '255', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '512'}),
            'description_ar': ('django.db.models.fields.TextField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '255', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title_ar': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'default': '2014', 'max_length': '255'})
        }
    }

    complete_apps = ['news']