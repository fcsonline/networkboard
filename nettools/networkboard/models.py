from django.db import models

# Create your models here.

class Node(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    nodetype = models.CharField(max_length=50)
    enabled = models.BooleanField()
    ip = models.CharField(max_length=25)
    posx = models.IntegerField()
    posy = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    params = models.CharField(max_length=2000)
    relation = models.ManyToManyField('Node', through='NodeRelation', related_name='node_relation', null=True)

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    servicetype = models.CharField(max_length=50)
    enabled = models.BooleanField()
    params = models.CharField(max_length=2000)

class NodeService(models.Model):
    source = models.ForeignKey(Node, unique=True)
    service = models.ForeignKey(Service)

class NodeRelation(models.Model):
    source = models.ForeignKey(Node, related_name='sources')
    target = models.ForeignKey(Node, related_name='targets')
