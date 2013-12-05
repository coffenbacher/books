# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Book'
        db.create_table(u'books_book', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('ISBN', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'books', ['Book'])

        # Adding model 'BookPrice'
        db.create_table(u'books_bookprice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(related_name='prices', to=orm['books.Book'])),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('price', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'books', ['BookPrice'])


    def backwards(self, orm):
        # Deleting model 'Book'
        db.delete_table(u'books_book')

        # Deleting model 'BookPrice'
        db.delete_table(u'books_bookprice')


    models = {
        u'books.book': {
            'ISBN': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'Meta': {'object_name': 'Book'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'books.bookprice': {
            'Meta': {'object_name': 'BookPrice'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'prices'", 'to': u"orm['books.Book']"}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['books']