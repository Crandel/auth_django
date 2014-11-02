# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'HomeContents.site'
        db.delete_column(u'home_homecontents', 'site_id')


    def backwards(self, orm):
        # Adding field 'HomeContents.site'
        db.add_column(u'home_homecontents', 'site',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=2, to=orm['sites.Site'], unique=True),
                      keep_default=False)


    models = {
        u'home.homebanner': {
            'Meta': {'ordering': "('sort_order',)", 'object_name': 'HomeBanner'},
            'banner_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'home_banner'", 'to': u"orm['home.HomeContents']"}),
            'sort_order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'sub_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'home.homecontents': {
            'Meta': {'object_name': 'HomeContents'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_itle': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sub_title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['home']