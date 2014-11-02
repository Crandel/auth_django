# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'FooterSettings.face_url'
        db.add_column(u'general_footersettings', 'face_url',
                      self.gf('django.db.models.fields.URLField')(default='ff', max_length=200),
                      keep_default=False)

        # Adding field 'FooterSettings.twit_url'
        db.add_column(u'general_footersettings', 'twit_url',
                      self.gf('django.db.models.fields.URLField')(default='dfdf', max_length=200),
                      keep_default=False)

        # Adding field 'FooterSettings.insta_url'
        db.add_column(u'general_footersettings', 'insta_url',
                      self.gf('django.db.models.fields.URLField')(default='ff', max_length=200),
                      keep_default=False)

        # Adding field 'FooterSettings.you_url'
        db.add_column(u'general_footersettings', 'you_url',
                      self.gf('django.db.models.fields.URLField')(default='fd', max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'FooterSettings.face_url'
        db.delete_column(u'general_footersettings', 'face_url')

        # Deleting field 'FooterSettings.twit_url'
        db.delete_column(u'general_footersettings', 'twit_url')

        # Deleting field 'FooterSettings.insta_url'
        db.delete_column(u'general_footersettings', 'insta_url')

        # Deleting field 'FooterSettings.you_url'
        db.delete_column(u'general_footersettings', 'you_url')


    models = {
        u'general.footersettings': {
            'Meta': {'object_name': 'FooterSettings'},
            'copy_year': ('django.db.models.fields.CharField', [], {'default': '2014', 'max_length': '100'}),
            'copyright': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'face_icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'face_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insta_icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'insta_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']", 'unique': 'True'}),
            'twit_icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'twit_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'you_icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'you_url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['general']