# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TopMenuUrl'
        db.create_table(u'general_topmenuurl', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=1000)),
            ('sort', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
        ))
        db.send_create_signal(u'general', ['TopMenuUrl'])


    def backwards(self, orm):
        # Deleting model 'TopMenuUrl'
        db.delete_table(u'general_topmenuurl')


    models = {
        u'general.adminemails': {
            'Meta': {'object_name': 'AdminEmails'},
            'career_email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'con_email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']", 'unique': 'True'})
        },
        u'general.bannerimages': {
            'Meta': {'ordering': "('sort_order', 'title')", 'object_name': 'BannerImages'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '200'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sort_order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_ar': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'general.bannersettings': {
            'Meta': {'object_name': 'BannerSettings'},
            'career_page': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'cont_page': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'flat_page': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'news_page': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'search_page': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']", 'unique': 'True'}),
            'sitemap_page': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
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
            'copyright': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'copyright_ar': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'copyright_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'hide_lin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hide_twi': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lin_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']", 'unique': 'True'}),
            'twit_url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'general.topmenuurl': {
            'Meta': {'ordering': "('-sort',)", 'object_name': 'TopMenuUrl'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'sort': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '1000'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['general']