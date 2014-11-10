# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ContactAddress.web'
        db.delete_column(u'contact_plugin_contactaddress', 'web')

        # Deleting field 'ContactAddress.city'
        db.delete_column(u'contact_plugin_contactaddress', 'city')

        # Deleting field 'ContactAddress.name'
        db.delete_column(u'contact_plugin_contactaddress', 'name')

        # Deleting field 'ContactAddress.country'
        db.delete_column(u'contact_plugin_contactaddress', 'country')

        # Deleting field 'ContactAddress.line2'
        db.delete_column(u'contact_plugin_contactaddress', 'line2')

        # Deleting field 'ContactAddress.line1'
        db.delete_column(u'contact_plugin_contactaddress', 'line1')

        # Adding field 'ContactAddress.head_office'
        db.add_column(u'contact_plugin_contactaddress', 'head_office',
                      self.gf('django.db.models.fields.TextField')(null=True),
                      keep_default=False)

        # Adding field 'ContactAddress.postal_address'
        db.add_column(u'contact_plugin_contactaddress', 'postal_address',
                      self.gf('django.db.models.fields.CharField')(max_length=1000, null=True),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'ContactAddress.web'
        raise RuntimeError("Cannot reverse this migration. 'ContactAddress.web' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'ContactAddress.web'
        db.add_column(u'contact_plugin_contactaddress', 'web',
                      self.gf('django.db.models.fields.CharField')(max_length=100),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'ContactAddress.city'
        raise RuntimeError("Cannot reverse this migration. 'ContactAddress.city' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'ContactAddress.city'
        db.add_column(u'contact_plugin_contactaddress', 'city',
                      self.gf('django.db.models.fields.CharField')(max_length=100),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'ContactAddress.name'
        raise RuntimeError("Cannot reverse this migration. 'ContactAddress.name' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'ContactAddress.name'
        db.add_column(u'contact_plugin_contactaddress', 'name',
                      self.gf('django.db.models.fields.CharField')(max_length=255),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'ContactAddress.country'
        raise RuntimeError("Cannot reverse this migration. 'ContactAddress.country' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'ContactAddress.country'
        db.add_column(u'contact_plugin_contactaddress', 'country',
                      self.gf('django.db.models.fields.CharField')(max_length=100),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'ContactAddress.line2'
        raise RuntimeError("Cannot reverse this migration. 'ContactAddress.line2' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'ContactAddress.line2'
        db.add_column(u'contact_plugin_contactaddress', 'line2',
                      self.gf('django.db.models.fields.CharField')(max_length=100),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'ContactAddress.line1'
        raise RuntimeError("Cannot reverse this migration. 'ContactAddress.line1' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'ContactAddress.line1'
        db.add_column(u'contact_plugin_contactaddress', 'line1',
                      self.gf('django.db.models.fields.CharField')(max_length=255),
                      keep_default=False)

        # Deleting field 'ContactAddress.head_office'
        db.delete_column(u'contact_plugin_contactaddress', 'head_office')

        # Deleting field 'ContactAddress.postal_address'
        db.delete_column(u'contact_plugin_contactaddress', 'postal_address')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        u'contact_plugin.contactaddress': {
            'Meta': {'object_name': 'ContactAddress', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'head_office': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'postal_address': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'tele': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['contact_plugin']