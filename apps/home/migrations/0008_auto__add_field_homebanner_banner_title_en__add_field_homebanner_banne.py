# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'HomeBanner.banner_title_en'
        db.add_column(u'home_homebanner', 'banner_title_en',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'HomeBanner.banner_title_ar'
        db.add_column(u'home_homebanner', 'banner_title_ar',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'HomeContents.main_itle_en'
        db.add_column(u'home_homecontents', 'main_itle_en',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'HomeContents.main_itle_ar'
        db.add_column(u'home_homecontents', 'main_itle_ar',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'HomeContents.sub_title_en'
        db.add_column(u'home_homecontents', 'sub_title_en',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'HomeContents.sub_title_ar'
        db.add_column(u'home_homecontents', 'sub_title_ar',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'HomeContents.ceo_title_en'
        db.add_column(u'home_homecontents', 'ceo_title_en',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'HomeContents.ceo_title_ar'
        db.add_column(u'home_homecontents', 'ceo_title_ar',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'HomeContents.ceo_desc_en'
        db.add_column(u'home_homecontents', 'ceo_desc_en',
                      self.gf('ckeditor.fields.RichTextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'HomeContents.ceo_desc_ar'
        db.add_column(u'home_homecontents', 'ceo_desc_ar',
                      self.gf('ckeditor.fields.RichTextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'HomeBanner.banner_title_en'
        db.delete_column(u'home_homebanner', 'banner_title_en')

        # Deleting field 'HomeBanner.banner_title_ar'
        db.delete_column(u'home_homebanner', 'banner_title_ar')

        # Deleting field 'HomeContents.main_itle_en'
        db.delete_column(u'home_homecontents', 'main_itle_en')

        # Deleting field 'HomeContents.main_itle_ar'
        db.delete_column(u'home_homecontents', 'main_itle_ar')

        # Deleting field 'HomeContents.sub_title_en'
        db.delete_column(u'home_homecontents', 'sub_title_en')

        # Deleting field 'HomeContents.sub_title_ar'
        db.delete_column(u'home_homecontents', 'sub_title_ar')

        # Deleting field 'HomeContents.ceo_title_en'
        db.delete_column(u'home_homecontents', 'ceo_title_en')

        # Deleting field 'HomeContents.ceo_title_ar'
        db.delete_column(u'home_homecontents', 'ceo_title_ar')

        # Deleting field 'HomeContents.ceo_desc_en'
        db.delete_column(u'home_homecontents', 'ceo_desc_en')

        # Deleting field 'HomeContents.ceo_desc_ar'
        db.delete_column(u'home_homecontents', 'ceo_desc_ar')


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
            'banner_title_ar': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'banner_title_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'home_content': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'home_banner'", 'to': u"orm['home.HomeContents']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sort_order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        u'home.homecontents': {
            'Meta': {'object_name': 'HomeContents'},
            'ceo_desc': ('ckeditor.fields.RichTextField', [], {}),
            'ceo_desc_ar': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'ceo_desc_en': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'ceo_title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ceo_title_ar': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'ceo_title_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_itle': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'main_itle_ar': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'main_itle_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']", 'unique': 'True'}),
            'sub_title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sub_title_ar': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'sub_title_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['home']