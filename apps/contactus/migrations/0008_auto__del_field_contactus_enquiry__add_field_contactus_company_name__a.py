# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ContactUs.enquiry'
        db.delete_column(u'contactus_contactus', 'enquiry')

        # Adding field 'ContactUs.company_name'
        db.add_column(u'contactus_contactus', 'company_name',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True),
                      keep_default=False)

        # Adding field 'ContactUs.subject'
        db.add_column(u'contactus_contactus', 'subject',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True),
                      keep_default=False)

        # Adding field 'ContactUs.details'
        db.add_column(u'contactus_contactus', 'details',
                      self.gf('django.db.models.fields.TextField')(null=True),
                      keep_default=False)


        # Changing field 'ContactUs.date'
        db.alter_column(u'contactus_contactus', 'date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'ContactUs.enquiry'
        raise RuntimeError("Cannot reverse this migration. 'ContactUs.enquiry' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'ContactUs.enquiry'
        db.add_column(u'contactus_contactus', 'enquiry',
                      self.gf('django.db.models.fields.TextField')(),
                      keep_default=False)

        # Deleting field 'ContactUs.company_name'
        db.delete_column(u'contactus_contactus', 'company_name')

        # Deleting field 'ContactUs.subject'
        db.delete_column(u'contactus_contactus', 'subject')

        # Deleting field 'ContactUs.details'
        db.delete_column(u'contactus_contactus', 'details')


        # Changing field 'ContactUs.date'
        db.alter_column(u'contactus_contactus', 'date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

    models = {
        u'contactus.contactus': {
            'Meta': {'object_name': 'ContactUs'},
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
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