from django.contrib.flatpages.admin import FlatpageForm
from django.contrib.flatpages.models import FlatPage
from ckeditor.widgets import CKEditorWidget

class MyFlatpageForm(FlatpageForm):

    class Meta:
        model = FlatPage
        widgets = {
          'content_en':CKEditorWidget(),
          'content_ar':CKEditorWidget()
        }