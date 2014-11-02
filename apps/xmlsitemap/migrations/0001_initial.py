# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'XMLSitemap'
        db.create_table('xmlsitemap_xmlsitemap', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('changefreq', self.gf('django.db.models.fields.CharField')(default='weekly', max_length=20)),
        ))
        db.send_create_signal('xmlsitemap', ['XMLSitemap'])


    def backwards(self, orm):
        # Deleting model 'XMLSitemap'
        db.delete_table('xmlsitemap_xmlsitemap')


    models = {
        'xmlsitemap.xmlsitemap': {
            'Meta': {'object_name': 'XMLSitemap'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'changefreq': ('django.db.models.fields.CharField', [], {'default': "'weekly'", 'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['xmlsitemap']