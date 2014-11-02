# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Events.event_desc'
        db.alter_column(u'newsevents_events', 'event_desc', self.gf('ckeditor.fields.RichTextField')())

        # Changing field 'Events.event_date_time'
        db.alter_column(u'newsevents_events', 'event_date_time', self.gf('django.db.models.fields.DateTimeField')())

    def backwards(self, orm):

        # Changing field 'Events.event_desc'
        db.alter_column(u'newsevents_events', 'event_desc', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Events.event_date_time'
        db.alter_column(u'newsevents_events', 'event_date_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

    models = {
        u'newsevents.events': {
            'Meta': {'object_name': 'Events'},
            'event_date_time': ('django.db.models.fields.DateTimeField', [], {}),
            'event_desc': ('ckeditor.fields.RichTextField', [], {}),
            'event_title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['newsevents']