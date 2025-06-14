def search_placeholder(self):
    """
    Bug in version 1.5.3: the join on placeholders fails with _LazyString
    """
    if not self.column_searchable_list:
        return 'Search'

    placeholders = []

    for searchable in self.column_searchable_list:
        if isinstance(searchable, InstrumentedAttribute):
            placeholders.append(
                str(self.column_labels.get(searchable.key, searchable.key)))
        else:
            placeholders.append(
                str(self.column_labels.get(searchable, searchable)))

    return gettext('Search') + ': %s' % u', '.join(placeholders)
