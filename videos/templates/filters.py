import django_filters
from django_filters import DateFilter, CharFilter, FileFilter
from django.forms.widgets import DateInput
from videos.models import Vids

class NetworkFilter(django_filters.FilterSet):
    caption = CharFilter(field_name='caption', lookup_expr='icontains', label='Title')
    date = DateFilter(field_name='date', lookup_expr='icontains', label='Date Uploaded')
    playlist=CharFilter(field_name='playlist', lookup_expr='icontains', label='Playlist')

    class Meta:
        model = Vids
        fields = ['caption']    

