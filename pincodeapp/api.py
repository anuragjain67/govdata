from django.db.models.query_utils import Q
from tastypie.resources import ModelResource
from tastypie.utils.mime import determine_format
from tastypie.authorization import Authorization

from .models import PinCodeDirectory


class BaseModelResource(ModelResource):
    """
    Use BaseModelResource for every Resource
    which we will be creating for our app
    """

    def determine_format(self, request):
        """return application/json as the default format """
        fmt = determine_format(request, self._meta.serializer,\
                               default_format=self._meta.default_format)
        if fmt == 'text/html' and 'format' not in request:
            fmt = 'application/json'
        return fmt


class PincodeResource(BaseModelResource):
    """
    Resource for Pincode,
    It will be providing Rest APIs for curd Operations
    """
    class Meta:
        queryset = PinCodeDirectory.objects.all()
        resource_name = 'pincodes'
        authorization = Authorization()

    def build_filters(self, filters=None):
        """ Overrided build filters for search on the basis of
        pincode or region or circle or district or state"""

        if filters is None:
            filters = {}
        orm_filters = super(PincodeResource, self).build_filters(filters)

        if('q' in filters):
            query = filters['q']
            qset = (
                    Q(office_name__istartswith=query) |
                    Q(pincode__istartswith=query) |
                    Q(region_name__istartswith=query) |
                    Q(circle_name__istartswith=query) |
                    Q(district_name__istartswith=query) |
                    Q(state_name__istartswith=query)
                    )
            orm_filters.update({'custom': qset})
        return orm_filters

    def apply_filters(self, request, applicable_filters):
        if 'custom' in applicable_filters:
            custom = applicable_filters.pop('custom')
        else:
            custom = None
        semi_filtered = super(PincodeResource, self).apply_filters(request, applicable_filters)
        return semi_filtered.filter(custom) if custom else semi_filtered
