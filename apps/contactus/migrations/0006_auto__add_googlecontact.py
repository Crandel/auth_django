# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GoogleContact'
        db.create_table(u'contactus_googlecontact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'], unique=True)),
            ('lati', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('long', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'contactus', ['GoogleContact'])


    def backwards(self, orm):
        # Deleting model 'GoogleContact'
        db.delete_table(u'contactus_googlecontact')


    models = {
        u'contactus.contactbanner': {
            'Meta': {'object_name': 'ContactBanner'},
            'con_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']", 'unique': 'True'})
        },
        u'contactus.contactus': {
            'Meta': {'object_name': 'ContactUs'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'enquiry': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'contactus.googlecontact': {
            'Meta': {'object_name': 'GoogleContact'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lati': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'long': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']", 'unique': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['contactus']