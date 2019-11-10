from bookshelf.models import Entry


def load_entries(category):

    return Entry.objects.filter(category=category)
