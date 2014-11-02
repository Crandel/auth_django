# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'News.news_year'
        db.add_column(u'newsevents_news', 'news_year',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['newsevents.NewsYear']),
                      keep_default=False)


        # Changing field 'News.site'
        db.alter_column(u'newsevents_news', 'site_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site']))

    def backwards(self, orm):
        # Deleting field 'News.news_year'
        db.delete_column(u'newsevents_news', 'news_year_id')


        # Changing field 'News.site'
        db.alter_column(u'newsevents_news', 'site_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['newsevents.NewsYear']))

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
            'Meta': {'ordering': "['-sort_order']", 'object_name': 'News'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {}),
            'news_date_time': ('django.db.models.fields.DateTimeField', [], {}),
            'news_desc': ('ckeditor.fields.RichTextField', [], {}),
            'news_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'news_title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'news_year': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['newsevents.NewsYear']"}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'sort_order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        u'newsevents.newsyear': {
            'Meta': {'object_name': 'NewsYear'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'news_year': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['newsevents']