# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'News.news_image'
        db.add_column(u'newsevents_news', 'news_image',
                      self.gf('django.db.models.fields.files.ImageField')(default='ff', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'News.news_image'
        db.delete_column(u'newsevents_news', 'news_image')


    models = {
        u'newsevents.events': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'Events'},
            'event_date_time': ('django.db.models.fields.DateTimeField', [], {}),
            'event_desc': ('ckeditor.fields.RichTextField', [], {}),
            'event_title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'sort_order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        u'newsevents.news': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'News'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {}),
            'news_date_time': ('django.db.models.fields.DateTimeField', [], {}),
            'news_desc': ('ckeditor.fields.RichTextField', [], {}),
            'news_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'news_title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'sort_order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['newsevents']