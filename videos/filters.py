import django_filters
from django_filters import DateFilter, CharFilter
from django.forms.widgets import TextInput
from videos.models import Vids

class VideoFilter(django_filters.FilterSet):
    caption = CharFilter(field_name='caption', lookup_expr='icontains', widget=TextInput(attrs={'placeholder': 'Search Videos'}), label='')
    #date = DateFilter(lookup_expr='icontains')
    #playlist = CharFilter(lookup_expr='icontains')
    #remarks = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Vids
        fields = ['caption']    

