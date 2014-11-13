# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Career'
        db.delete_table(u'careers_career')

        # Deleting model 'JobCategory'
        db.delete_table(u'careers_jobcategory')

        # Deleting model 'AppliedJobs'
        db.delete_table(u'careers_appliedjobs')


    def backwards(self, orm):
        # Adding model 'Career'
        db.create_table(u'careers_career', (
            ('short_desc_en', self.gf('ckeditor.fields.RichTextField')(null=True, blank=True)),
            ('designation_ar', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('short_desc_ar', self.gf('ckeditor.fields.RichTextField')(null=True, blank=True)),
            ('job_cat', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['careers.JobCategory'])),
            ('sort_order', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cl_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('designation', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('designation_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('short_desc', self.gf('ckeditor.fields.RichTextField')()),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('is_published', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'careers', ['Career'])

        # Adding model 'JobCategory'
        db.create_table(u'careers_jobcategory', (
            ('catog_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('catog', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('catog_ar', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('sort_order', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'careers', ['JobCategory'])

        # Adding model 'AppliedJobs'
        db.create_table(u'careers_appliedjobs', (
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('tele', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('designation', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('upload_file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('job_cat', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['careers.JobCategory'], null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=255)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'careers', ['AppliedJobs'])


    models = {
        u'careers.careerinfo': {
            'Meta': {'object_name': 'CareerInfo'},
            'description': ('ckeditor.fields.RichTextField', [], {}),
            'description_ar': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'description_en': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '255', 'null': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']", 'unique': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_ar': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'careers.nationality': {
            'Meta': {'ordering': "(u'nationality',)", 'object_name': 'Nationality'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'nationality_ar': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'nationality_en': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'})
        },
        u'careers.svmodel': {
            'Meta': {'ordering': "(u'created',)", 'object_name': 'SVModel'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'cv': ('django.db.models.fields.files.FileField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
        },
        u'careers.vacancy': {
            'Meta': {'ordering': "(u'sort', u'-created')", 'object_name': 'Vacancy'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 11, 13, 0, 0)'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'position_ar': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'position_en': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'requirement': ('ckeditor.fields.RichTextField', [], {}),
            'requirement_ar': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'requirement_en': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'sort': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'})
        },
        u'careers.vacancyapply': {
            'Meta': {'ordering': "(u'-created',)", 'object_name': 'VacancyApply'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'cv': ('django.db.models.fields.files.FileField', [], {'max_length': '255'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'nationality': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['careers.Nationality']"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'vacancy': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['careers.Vacancy']"})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['careers']