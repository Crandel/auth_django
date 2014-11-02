# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CEOImages'
        db.create_table(u'home_ceoimages', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('homecontent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ceo_images', to=orm['home.HomeContents'])),
            ('image_url', self.gf('django.db.models.fields.URLField')(max_length=100, null=True, blank=True)),
            ('ceo_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('sort_order', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
        ))
        db.send_create_signal(u'home', ['CEOImages'])

        # Deleting field 'HomeBanner.sub_title'
        db.delete_column(u'home_homebanner', 'sub_title')

        # Deleting field 'HomeBanner.site'
        db.delete_column(u'home_homebanner', 'site_id')

        # Adding field 'HomeBanner.home_content'
        db.add_column(u'home_homebanner', 'home_content',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=23, related_name='home_banner', to=orm['home.HomeContents']),
                      keep_default=False)

        # Adding field 'HomeBanner.banner_title'
        db.add_column(u'home_homebanner', 'banner_title',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'CEOImages'
        db.delete_table(u'home_ceoimages')

        # Adding field 'HomeBanner.sub_title'
        db.add_column(u'home_homebanner', 'sub_title',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'HomeBanner.site'
        db.add_column(u'home_homebanner', 'site',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=datetime.datetime(2014, 8, 3, 0, 0), related_name='home_banner', to=orm['home.HomeContents']),
                      keep_default=False)

        # Deleting field 'HomeBanner.home_content'
        db.delete_column(u'home_homebanner', 'home_content_id')

        # Deleting field 'HomeBanner.banner_title'
        db.delete_column(u'home_homebanner', 'banner_title')


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