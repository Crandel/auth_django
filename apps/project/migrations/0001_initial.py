# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'project_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('name_ar', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=50, populate_from=u'name', unique_with=())),
            ('order', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
        ))
        db.send_create_signal(u'project', ['Category'])

        # Adding model 'Project'
        db.create_table(u'project_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('project_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('project_ar', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=50, populate_from=u'project', unique_with=())),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'projects', to=orm['project.Category'])),
            ('client', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('client_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('client_ar', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('location_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('location_ar', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('scope', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('scope_en', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            ('scope_ar', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('description_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('description_ar', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('publish', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'project', ['Project'])

        # Adding model 'Image'
        db.create_table(u'project_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'images', to=orm['project.Project'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('title_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('title_ar', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=255)),
            ('publish', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'project', ['Image'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'project_category')

        # Deleting model 'Project'
        db.delete_table(u'project_project')

        # Deleting model 'Image'
        db.delete_table(u'project_image')


    models = {
        u'project.category': {
            'Meta': {'ordering': "(u'order',)", 'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_ar': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "u'name'", 'unique_with': '()'})
        },
        u'project.image': {
            'Meta': {'object_name': 'Image'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '255'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'images'", 'to': u"orm['project.Project']"}),
            'publish': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_ar': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'project.project': {
            'Meta': {'object_name': 'Project'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'projects'", 'to': u"orm['project.Category']"}),
            'client': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'client_ar': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'client_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'description_ar': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'location_ar': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'location_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'project_ar': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'project_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'publish': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'scope': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'scope_ar': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'scope_en': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "u'project'", 'unique_with': '()'})
        }
    }

    complete_apps = ['project']