# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Events.event_title_en'
        db.add_column(u'newsevents_events', 'event_title_en',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Events.event_title_ar'
        db.add_column(u'newsevents_events', 'event_title_ar',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Events.event_desc_en'
        db.add_column(u'newsevents_events', 'event_desc_en',
                      self.gf('ckeditor.fields.RichTextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Events.event_desc_ar'
        db.add_column(u'newsevents_events', 'event_desc_ar',
                      self.gf('ckeditor.fields.RichTextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'News.news_title_en'
        db.add_column(u'newsevents_news', 'news_title_en',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'News.news_title_ar'
        db.add_column(u'newsevents_news', 'news_title_ar',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'News.news_desc_en'
        db.add_column(u'newsevents_news', 'news_desc_en',
                      self.gf('ckeditor.fields.RichTextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'News.news_desc_ar'
        db.add_column(u'newsevents_news', 'news_desc_ar',
                      self.gf('ckeditor.fields.RichTextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Events.event_title_en'
        db.delete_column(u'newsevents_events', 'event_title_en')

        # Deleting field 'Events.event_title_ar'
        db.delete_column(u'newsevents_events', 'event_title_ar')

        # Deleting field 'Events.event_desc_en'
        db.delete_column(u'newsevents_events', 'event_desc_en')

        # Deleting field 'Events.event_desc_ar'
        db.delete_column(u'newsevents_events', 'event_desc_ar')

        # Deleting field 'News.news_title_en'
        db.delete_column(u'newsevents_news', 'news_title_en')

        # Deleting field 'News.news_title_ar'
        db.delete_column(u'newsevents_news', 'news_title_ar')

        # Deleting field 'News.news_desc_en'
        db.delete_column(u'newsevents_news', 'news_desc_en')

        # Deleting field 'News.news_desc_ar'
        db.delete_column(u'newsevents_news', 'news_desc_ar')


    models = {
        u'newsevents.events': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'Events'},
            'event_date_time': ('django.db.models.fields.DateTimeField', [], {}),
            'event_desc': ('ckeditor.fields.RichTextField', [], {}),
            'event_desc_ar': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'event_desc_en': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'event_title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'event_title_ar': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'event_title_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
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
            'news_desc_ar': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'news_desc_en': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'news_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'news_title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'news_title_ar': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'news_title_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
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