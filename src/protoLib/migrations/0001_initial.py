# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TeamHierarchy'
        db.create_table('protoLib_teamhierarchy', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('parentNode', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='downHierachy', null=True, to=orm['protoLib.TeamHierarchy'])),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'], null=True, blank=True)),
        ))
        db.send_create_signal('protoLib', ['TeamHierarchy'])

        # Adding model 'UserProfile'
        db.create_table('protoLib_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], unique=True)),
            ('userTeam', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['protoLib.TeamHierarchy'], null=True, blank=True)),
            ('userTree', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
        ))
        db.send_create_signal('protoLib', ['UserProfile'])

        # Adding model 'UserShare'
        db.create_table('protoLib_usershare', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('userTeam', self.gf('django.db.models.fields.related.ForeignKey')(related_name='userShares', to=orm['protoLib.TeamHierarchy'])),
        ))
        db.send_create_signal('protoLib', ['UserShare'])

        # Adding model 'ProtoDefinition'
        db.create_table('protoLib_protodefinition', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('metaDefinition', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('overWrite', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('protoLib', ['ProtoDefinition'])

        # Adding model 'CustomDefinition'
        db.create_table('protoLib_customdefinition', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('smOwningUser', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['auth.User'])),
            ('smOwningTeam', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['protoLib.TeamHierarchy'])),
            ('smCreatedBy', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['auth.User'])),
            ('smCreatedOn', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('smModifiedBy', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['auth.User'])),
            ('smModifiedOn', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('smRegStatus', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('smWflowStatus', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('metaDefinition', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('overWrite', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('protoLib', ['CustomDefinition'])

        # Adding unique constraint on 'CustomDefinition', fields ['smOwningTeam', 'code']
        db.create_unique('protoLib_customdefinition', ['smOwningTeam_id', 'code'])


    def backwards(self, orm):
        # Removing unique constraint on 'CustomDefinition', fields ['smOwningTeam', 'code']
        db.delete_unique('protoLib_customdefinition', ['smOwningTeam_id', 'code'])

        # Deleting model 'TeamHierarchy'
        db.delete_table('protoLib_teamhierarchy')

        # Deleting model 'UserProfile'
        db.delete_table('protoLib_userprofile')

        # Deleting model 'UserShare'
        db.delete_table('protoLib_usershare')

        # Deleting model 'ProtoDefinition'
        db.delete_table('protoLib_protodefinition')

        # Deleting model 'CustomDefinition'
        db.delete_table('protoLib_customdefinition')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'protoLib.customdefinition': {
            'Meta': {'unique_together': "(('smOwningTeam', 'code'),)", 'object_name': 'CustomDefinition'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metaDefinition': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'overWrite': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'smCreatedBy': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'smCreatedOn': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'smModifiedBy': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'smModifiedOn': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'smOwningTeam': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['protoLib.TeamHierarchy']"}),
            'smOwningUser': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'smRegStatus': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'smWflowStatus': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'protoLib.protodefinition': {
            'Meta': {'object_name': 'ProtoDefinition'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metaDefinition': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'overWrite': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'protoLib.teamhierarchy': {
            'Meta': {'object_name': 'TeamHierarchy'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parentNode': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'downHierachy'", 'null': 'True', 'to': "orm['protoLib.TeamHierarchy']"}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']", 'null': 'True', 'blank': 'True'})
        },
        'protoLib.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'userTeam': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['protoLib.TeamHierarchy']", 'null': 'True', 'blank': 'True'}),
            'userTree': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        },
        'protoLib.usershare': {
            'Meta': {'object_name': 'UserShare'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'userTeam': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'userShares'", 'to': "orm['protoLib.TeamHierarchy']"})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['protoLib']