# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'FooterSettings.copy_year'
        db.delete_column(u'general_footersettings', 'copy_year')

        # Deleting field 'FooterSettings.face_icon'
        db.delete_column(u'general_footersettings', 'face_icon')

        # Deleting field 'FooterSettings.twit_icon'
        db.delete_column(u'general_footersettings', 'twit_icon')

        # Deleting field 'FooterSettings.insta_icon'
        db.delete_column(u'general_footersettings', 'insta_icon')

        # Deleting field 'FooterSettings.insta_url'
        db.delete_column(u'general_footersettings', 'insta_url')

        # Deleting field 'FooterSettings.you_url'
        db.delete_column(u'general_footersettings', 'you_url')

        # Deleting field 'FooterSettings.hide_you'
        db.delete_column(u'general_footersettings', 'hide_you')

        # Deleting field 'FooterSettings.hide_face'
        db.delete_column(u'general_footersettings', 'hide_face')

        # Deleting field 'FooterSettings.you_icon'
        db.delete_column(u'general_footersettings', 'you_icon')

        # Deleting field 'FooterSettings.face_url'
        db.delete_column(u'general_footersettings', 'face_url')

        # Deleting field 'FooterSettings.hide_insta'
        db.delete_column(u'general_footersettings', 'hide_insta')

        # Adding field 'FooterSettings.lin_url'
        db.add_column(u'general_footersettings', 'lin_url',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True),
                      keep_default=False)

        # Adding field 'FooterSettings.hide_lin'
        db.add_column(u'general_footersettings', 'hide_lin',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'FooterSettings.copy_year'
        db.add_column(u'general_footersettings', 'copy_year',
                      self.gf('django.db.models.fields.CharField')(default=2014, max_length=100),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'FooterSettings.face_icon'
        raise RuntimeError("Cannot reverse this migration. 'FooterSettings.face_icon' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'FooterSettings.face_icon'
        db.add_column(u'general_footersettings', 'face_icon',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'FooterSettings.twit_icon'
        raise RuntimeError("Cannot reverse this migration. 'FooterSettings.twit_icon' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'FooterSettings.twit_icon'
        db.add_column(u'general_footersettings', 'twit_icon',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'FooterSettings.insta_icon'
        raise RuntimeError("Cannot reverse this migration. 'FooterSettings.insta_icon' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'FooterSettings.insta_icon'
        db.add_column(u'general_footersettings', 'insta_icon',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'FooterSettings.insta_url'
        raise RuntimeError("Cannot reverse this migration. 'FooterSettings.insta_url' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'FooterSettings.insta_url'
        db.add_column(u'general_footersettings', 'insta_url',
                      self.gf('django.db.models.fields.URLField')(max_length=200),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'FooterSettings.you_url'
        raise RuntimeError("Cannot reverse this migration. 'FooterSettings.you_url' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'FooterSettings.you_url'
        db.add_column(u'general_footersettings', 'you_url',
                      self.gf('django.db.models.fields.URLField')(max_length=200),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'FooterSettings.hide_you'
        raise RuntimeError("Cannot reverse this migration. 'FooterSettings.hide_you' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'FooterSettings.hide_you'
        db.add_column(u'general_footersettings', 'hide_you',
                      self.gf('django.db.models.fields.BooleanField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'FooterSettings.hide_face'
        raise RuntimeError("Cannot reverse this migration. 'FooterSettings.hide_face' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'FooterSettings.hide_face'
        db.add_column(u'general_footersettings', 'hide_face',
                      self.gf('django.db.models.fields.BooleanField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'FooterSettings.you_icon'
        raise RuntimeError("Cannot reverse this migration. 'FooterSettings.you_icon' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'FooterSettings.you_icon'
        db.add_column(u'general_footersettings', 'you_icon',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'FooterSettings.face_url'
        raise RuntimeError("Cannot reverse this migration. 'FooterSettings.face_url' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'FooterSettings.face_url'
        db.add_column(u'general_footersettings', 'face_url',
                      self.gf('django.db.models.fields.URLField')(max_length=200),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'FooterSettings.hide_insta'
        raise RuntimeError("Cannot reverse this migration. 'FooterSettings.hide_insta' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'FooterSettings.hide_insta'
        db.add_column(u'general_footersettings', 'hide_insta',
                      self.gf('django.db.models.fields.BooleanField')(),
                      keep_default=False)

        # Deleting field 'FooterSettings.lin_url'
        db.delete_column(u'general_footersettings', 'lin_url')

        # Deleting field 'FooterSettings.hide_lin'
        db.delete_column(u'general_footersettings', 'hide_lin')


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
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['general']