# drf-replace-ordering-filter
Django Rest Framework OrderingFilter backend to replace field name in ordering params.

This package is useful if you have custom hidden fields in you model to help with a better ordering.

## Usage
You can user ```ReplaceFieldOrderingFilter``` as a Default Filter Backend in Rest Framework setting or specifying in a certain APIView.

```ReplaceFieldOrderingFilter``` works in the same way as ```rest_framework.filters.OrderingFilter```, if you do not define fields in a View to be replaced.


### 1. As a default setting
First of all, add ```ReplaceFieldOrderingFilter``` to DEFAULT_FILTER_BACKENDS in ```setting.py``` file of your Django's project.

``` python
REST_FRAMEWORK = {
  'DEFAULT_FILTER_BACKENDS': (
    'drf_replace_ordering_filter.filters.ReplaceFieldOrderingFilter',
  )
}
```

Lastly, in a view that you want to change some ordering filed to another, add the following attribute.

```python
from rest_framework import views


class MyAPIView(views.APIView):
  replace_ordering_fields = {
    'field_to_be_replaced': 'new_field'
  }

  def get(self, request, *args, **kwargs):
    pass
```

### 2. In a specific view
The second option is using ```ReplaceFieldOrderingFilter``` only in a specfic view or viewset.

For example:

```python
from drf_replace_ordering_filter.filters import ReplaceFieldOrderingFilter
from rest_framework import views


class MyAPIView(views.APIView):
  filter_backends = (ReplaceFieldOrderingFilter,)
  replace_ordering_fields = {
    'field_to_be_replaced': 'new_field'
  }

  def get(self, request, *args, **kwargs):
    pass
```
