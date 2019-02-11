import re

from rest_framework import filters


class ReplaceFieldsOrderingFilter(filters.OrderingFilter):
    """
    View must define 'replace_ordering_fields' of type dict.
    Example:
        {
            'field_to_replace': 'new_field'
        }
    """
    def get_ordering(self, request, queryset, view):
        ordering = super(ReplaceFieldsOrderingFilter, self).get_ordering(request, queryset, view)

        fields_to_replace = getattr(view, 'replace_ordering_fields', None)

        if fields_to_replace and ordering:
            ordering_regex = r'^([-|+]?)(.*)$'

            new_ordering = []
            for ordering_field in ordering:
                asc_desc, field = re.match(ordering_regex, ordering_field).groups()

                if fields_to_replace.get(field):
                    new_ordering.append(f'{asc_desc}{fields_to_replace[field]}')
                else:
                    new_ordering.append(ordering_field)

            return new_ordering

        return ordering
