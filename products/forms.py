from django import forms
from .widgets import CustomClearableFileInput
#from .models import Product
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        #fields = ('category',)

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        #friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        name = [(c.id, c.get_name()) for c in categories]

        self.fields['category'].choices = name
        #self.fields['category'].choices = [(c.id, c.get_name()) for c in categories]
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
