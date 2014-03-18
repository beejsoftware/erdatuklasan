

from models import UploadModel
from dbindexer.lookups import StandardLookup
from dbindexer.api import register_index

register_index(UploadModel, {'date': 'year'})
register_index(UploadModel, {'date': 'month'})
