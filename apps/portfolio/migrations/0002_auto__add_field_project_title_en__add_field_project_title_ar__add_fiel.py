# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Project.title_en'
        db.add_column(u'portfolio_project', 'title_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Project.title_ar'
        db.add_column(u'portfolio_project', 'title_ar',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Project.client_en'
        db.add_column(u'portfolio_project', 'client_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Project.client_ar'
        db.add_column(u'portfolio_project', 'client_ar',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Project.location_en'
        db.add_column(u'portfolio_project', 'location_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Project.location_ar'
        db.add_column(u'portfolio_project', 'location_ar',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Project.scope_en'
        db.add_column(u'portfolio_project', 'scope_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Project.scope_ar'
        db.add_column(u'portfolio_project', 'scope_ar',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Project.description_en'
        db.add_column(u'portfolio_project', 'description_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Project.description_ar'
        db.add_column(u'portfolio_project', 'description_ar',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'PortfolioInfo.title_en'
        db.add_column(u'portfolio_portfolioinfo', 'title_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'PortfolioInfo.title_ar'
        db.add_column(u'portfolio_portfolioinfo', 'title_ar',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Category.title_en'
        db.add_column(u'portfolio_category', 'title_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Category.title_ar'
        db.add_column(u'portfolio_category', 'title_ar',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Project.title_en'
        db.delete_column(u'portfolio_project', 'title_en')

        # Deleting field 'Project.title_ar'
        db.delete_column(u'portfolio_project', 'title_ar')

        # Deleting field 'Project.client_en'
        db.delete_column(u'portfolio_project', 'client_en')

        # Deleting field 'Project.client_ar'
        db.delete_column(u'portfolio_project', 'client_ar')

        # Deleting field 'Project.location_en'
        db.delete_column(u'portfolio_project', 'location_en')

        # Deleting field 'Project.location_ar'
        db.delete_column(u'portfolio_project', 'location_ar')

        # Deleting field 'Project.scope_en'
        db.delete_column(u'portfolio_project', 'scope_en')

        # Deleting field 'Project.scope_ar'
        db.delete_column(u'portfolio_project', 'scope_ar')

        # Deleting field 'Project.description_en'
        db.delete_column(u'portfolio_project', 'description_en')

        # Deleting field 'Project.description_ar'
        db.delete_column(u'portfolio_project', 'description_ar')

        # Deleting field 'PortfolioInfo.title_en'
        db.delete_column(u'portfolio_portfolioinfo', 'title_en')

        # Deleting field 'PortfolioInfo.title_ar'
        db.delete_column(u'portfolio_portfolioinfo', 'title_ar')

        # Deleting field 'Category.title_en'
        db.delete_column(u'portfolio_category', 'title_en')

        # Deleting field 'Category.title_ar'
        db.delete_column(u'portfolio_category', 'title_ar')


    models = {
        u'portfolio.category': {
            'Meta': {'ordering': "(u'order',)", 'object_name': 'Category'},
            'header_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "u'title'", 'unique_with': '()'}),
            'thumbnail_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '255', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_ar': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'portfolio.image': {
            'Meta': {'object_name': 'Image'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '255'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'images'", 'to': u"orm['portfolio.Project']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'portfolio.portfolioinfo': {
            'Meta': {'object_name': 'PortfolioInfo'},
            'header_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_ar': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'portfolio.project': {
            'Meta': {'object_name': 'Project'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'projects'", 'to': u"orm['portfolio.Category']"}),
            'client': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'client_ar': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'client_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'description_ar': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'description_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'location_ar': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'location_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'scope': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'scope_ar': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'scope_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "u'title'", 'unique_with': '()'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_ar': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['portfolio']