# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'News'
        db.create_table(u'newsevents_news', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('news_title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('news_date_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('news_desc', self.gf('ckeditor.fields.RichTextField')()),
            ('is_published', self.gf('django.db.models.fields.BooleanField')()),
            ('sort_order', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
        ))
        db.send_create_signal(u'newsevents', ['News'])


    def backwards(self, orm):
        # Deleting model 'News'
        db.delete_table(u'newsevents_news')


    models = {
        u'newsevents.events': {
            'Meta': {'object_name': 'Events'},
            'event_date_time': ('django.db.models.fields.DateTimeField', [], {}),
            'event_desc': ('ckeditor.fields.RichTextField', [], {}),
            'event_title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"})
        },
        u'newsevents.news': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'News'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {}),
            'news_date_time': ('django.db.models.fields.DateTimeField', [], {}),
            'news_desc': ('ckeditor.fields.RichTextField', [], {}),
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