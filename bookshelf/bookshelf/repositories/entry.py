from typing import List

from mappers import Mapper

from bookshelf import models
from bookshelf.entities import Category
from bookshelf.entities import Entry

mapper = Mapper(Entry, models.Entry, {"primary_key": "id"})


@mapper.reader
def load_entries(category: Category) -> List[Entry]:
    return models.Entry.objects.filter(category=category)
