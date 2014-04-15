# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Author'
        db.create_table(u'website_author', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'website', ['Author'])

        # Adding model 'Asset'
        db.create_table(u'website_asset', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(related_name='assets', to=orm['website.Book'])),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('original_file_path', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('asset_type', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal(u'website', ['Asset'])

        # Adding model 'Genre'
        db.create_table(u'website_genre', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'website', ['Genre'])

        # Adding model 'Tag'
        db.create_table(u'website_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'website', ['Tag'])

        # Adding model 'Book'
        db.create_table(u'website_book', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('isbn_10', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('isbn_13', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('amazon_url', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'website', ['Book'])

        # Adding M2M table for field genres on 'Book'
        m2m_table_name = db.shorten_name(u'website_book_genres')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm[u'website.book'], null=False)),
            ('genre', models.ForeignKey(orm[u'website.genre'], null=False))
        ))
        db.create_unique(m2m_table_name, ['book_id', 'genre_id'])

        # Adding M2M table for field authors on 'Book'
        m2m_table_name = db.shorten_name(u'website_book_authors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm[u'website.book'], null=False)),
            ('author', models.ForeignKey(orm[u'website.author'], null=False))
        ))
        db.create_unique(m2m_table_name, ['book_id', 'author_id'])

        # Adding M2M table for field tags on 'Book'
        m2m_table_name = db.shorten_name(u'website_book_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm[u'website.book'], null=False)),
            ('tag', models.ForeignKey(orm[u'website.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['book_id', 'tag_id'])


    def backwards(self, orm):
        # Deleting model 'Author'
        db.delete_table(u'website_author')

        # Deleting model 'Asset'
        db.delete_table(u'website_asset')

        # Deleting model 'Genre'
        db.delete_table(u'website_genre')

        # Deleting model 'Tag'
        db.delete_table(u'website_tag')

        # Deleting model 'Book'
        db.delete_table(u'website_book')

        # Removing M2M table for field genres on 'Book'
        db.delete_table(db.shorten_name(u'website_book_genres'))

        # Removing M2M table for field authors on 'Book'
        db.delete_table(db.shorten_name(u'website_book_authors'))

        # Removing M2M table for field tags on 'Book'
        db.delete_table(db.shorten_name(u'website_book_tags'))


    models = {
        u'website.asset': {
            'Meta': {'object_name': 'Asset'},
            'asset_type': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'book': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'assets'", 'to': u"orm['website.Book']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'original_file_path': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        },
        u'website.author': {
            'Meta': {'object_name': 'Author'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'website.book': {
            'Meta': {'object_name': 'Book'},
            'amazon_url': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'books'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['website.Author']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'genres': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'books'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['website.Genre']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn_10': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'isbn_13': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'books'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['website.Tag']"})
        },
        u'website.genre': {
            'Meta': {'object_name': 'Genre'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'website.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['website']