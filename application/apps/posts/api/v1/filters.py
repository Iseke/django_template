from django_filters import rest_framework as dj_filters


class PostAnalyticsFilter(dj_filters.FilterSet):
    date_from = dj_filters.DateFilter(method='_date_from', required=True)
    date_to = dj_filters.DateFilter(method='_date_to', required=True)

    def _date_from(self, queryset, name, value):
        return queryset

    def _date_to(self, queryset, name, value):
        return queryset


