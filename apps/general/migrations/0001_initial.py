# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FooterSettings'
        db.create_table(u'general_footersettings', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'], unique=True)),
            ('copyright', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('copy_year', self.gf('django.db.models.fields.CharField')(default=2014, max_length=100)),
            ('face_icon', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('twit_icon', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('insta_icon', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('you_icon', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'general', ['FooterSettings'])


    def backwards(self, orm):
        # Deleting model 'FooterSettings'
        db.delete_table(u'general_footersettings')


    models = {
        u'general.footersettings': {
            'Meta': {'object_name': 'FooterSettings'},
            'copy_year': ('django.db.models.fields.CharField', [], {'default': '2014', 'max_length': '100'}),
            'copyright': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'face_icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insta_icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']", 'unique': 'True'}),
            'twit_icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'you_icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['general']