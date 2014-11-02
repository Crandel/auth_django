# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'HomeContents.ceo_desc'
        db.alter_column(u'home_homecontents', 'ceo_desc', self.gf('ckeditor.fields.RichTextField')())

    def backwards(self, orm):

        # Changing field 'HomeContents.ceo_desc'
        db.alter_column(u'home_homecontents', 'ceo_desc', self.gf('django.db.models.fields.TextField')())

    models = {
        u'home.ceoimages': {
            'Meta': {'ordering': "('sort_order',)", 'object_name': 'CEOImages'},
            'ceo_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'homecontent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ceo_images'", 'to': u"orm['home.HomeContents']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.URLField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'sort_order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        u'home.homebanner': {
            'Meta': {'ordering': "('sort_order',)", 'object_name': 'HomeBanner'},
            'banner_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'banner_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'home_content': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'home_banner'", 'to': u"orm['home.HomeContents']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sort_order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        u'home.homecontents': {
            'Meta': {'object_name': 'HomeContents'},
            'ceo_desc': ('ckeditor.fields.RichTextField', [], {}),
            'ceo_title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_itle': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']", 'unique': 'True'}),
            'sub_title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['home']