# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BannerSettings'
        db.create_table(u'general_bannersettings', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'], unique=True)),
            ('cont_page', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('career_page', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('flat_page', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('news_page', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('subsideri_page', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'general', ['BannerSettings'])


    def backwards(self, orm):
        # Deleting model 'BannerSettings'
        db.delete_table(u'general_bannersettings')


    models = {
        u'general.adminemails': {
            'Meta': {'object_name': 'AdminEmails'},
            'career_email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'con_email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']", 'unique': 'True'})
        },
        u'general.bannersettings': {
            'Meta': {'object_name': 'BannerSettings'},
            'career_page': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'cont_page': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'flat_page': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'news_page': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']", 'unique': 'True'}),
            'subsideri_page': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'general.commonsettings': {
            'Meta': {'object_name': 'CommonSettings'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo_icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'logo_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']", 'unique': 'True'})
        },
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