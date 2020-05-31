from import_export import resources
from .models import Snippet

class SnippetResouce(resources.ModelResource):
    class Meta:
        model = Snippet