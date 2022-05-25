from django.forms import ModelForm

from app.models import App

class AppCreateForm(ModelForm):
    class Meta:
        model = App
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # for name, field in self.fields.items():
        #     field.widget.attrs['class']