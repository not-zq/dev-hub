from django.db import models

class SpotifyExtendedStreamingHistory(models.Model):
    id = models.IntegerField(primary_key=True)
    ts = models.DateTimeField(blank=True, null=True)
    platform = models.CharField(max_length=255, blank=True, null=True)
    ms_played = models.IntegerField(blank=True, null=True)
    conn_country = models.CharField(max_length=2, blank=True, null=True)
    ip_addr = models.CharField(max_length=16, blank=True, null=True)
    master_metadata_track_name = models.CharField(max_length=255, blank=True, null=True)
    master_metadata_album_artist_name = models.CharField(max_length=255, blank=True, null=True)
    master_metadata_album_album_name = models.CharField(max_length=255, blank=True, null=True)
    reason_start = models.CharField(max_length=32, blank=True, null=True)
    reason_end = models.CharField(max_length=32, blank=True, null=True)
    shuffle = models.BooleanField(blank=True, null=True)
    skipped = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SpotifyExtendedStreamingHistoryView'
