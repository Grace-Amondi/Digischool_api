# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models
from django.contrib.postgres.fields import HStoreField


class School(models.Model):
    name = models.CharField(max_length=100)
    county = models.CharField(max_length=100, null=True)
    delivered = models.BooleanField(default=False)
    enrollment = models.IntegerField()
    location = models.PointField(srid=4326)
    electricity_availability = models.BooleanField(default=False)
    total_devices_present = models.IntegerField(null=False,default=0)
    emmis_code = models.IntegerField(null=False,default=0)

    def __unicode__(self):
        return self.name


class Issue(models.Model):
    TYPE_CHOICES = (
        ('GOIP', 'GOIP'),
        ('E-WASTE', 'E-WASTE'),
        ('TRAINING', 'TRAINING'),
        ('G4S', 'G4S')
    )
    issue = models.ForeignKey(School)
    consortium = models.CharField(choices=TYPE_CHOICES, default='GOIP', max_length=300)
    serial_no = models.CharField(max_length=300)
    esc_issue = models.CharField(max_length=300)
    resolved = models.BooleanField()
    date = models.DateField()

    def __unicode__(self):
        return self.consortium + " " + self.esc_issue


class Link(models.Model):
    """
    Metadata is stored in a PostgreSQL HStore field, which allows us to
    store arbitrary key-value pairs with a link record.
    """
    metadata = HStoreField(blank=True, null=True, default=dict)
    geo = models.LineStringField()
    objects = models.GeoManager()