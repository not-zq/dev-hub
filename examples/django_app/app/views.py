from .models import SpotifyExtendedStreamingHistory
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.shortcuts import render

def home(request):

    top_artists = (
        SpotifyExtendedStreamingHistory.objects
        .values("master_metadata_album_artist_name")
        .annotate(total_min = Sum("ms_played") / 60000)
        .order_by("-total_min")[:10]
    )

    selected_artist = top_artists[0].get("master_metadata_album_artist_name")

    top_songs = (
        SpotifyExtendedStreamingHistory.objects
        .filter(master_metadata_album_artist_name = selected_artist)
        .values("master_metadata_track_name")
        .annotate(total_min = Sum("ms_played") / 60000)
        .order_by("-total_min")[:20]
    )

    monthly_listening_time = (
        SpotifyExtendedStreamingHistory.objects
        .annotate(month=TruncMonth("ts"))
        .values("month")
        .annotate(total_hrs=Sum("ms_played") / 3600000)
        .order_by("month")
    )

    return render(
        request, 
        "home.html",
        { 
            "topArtists": list(top_artists),
            "selectedArtist": selected_artist,
            "topSongs": list(top_songs),
            "monthlyListeningTime": list(monthly_listening_time)
        }
    )

from django.http import JsonResponse

def get_top_songs(request):

    selected_artist = request.GET.get("artist")

    top_songs = (
        SpotifyExtendedStreamingHistory.objects
        .filter(master_metadata_album_artist_name = selected_artist)
        .values("master_metadata_track_name")
        .annotate(total_min = Sum("ms_played") / 60000)
        .order_by("-total_min")[:20]
    )

    return JsonResponse(list(top_songs), safe=False)
