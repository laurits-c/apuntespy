
from django.core.exceptions import ValidationError
import apuntespy.models as mod
def tag_unico(value):
    try:
        if mod.Tag.objects.get(tag_text=value):
            raise ValidationError('Ya existe una categoría: '+value)
    except mod.Tag.DoesNotExist:
        pass
def tip_unico(value):
    try:

        if mod.Tip.objects.get(tip_nombre=value):
            raise ValidationError('Ya existe un tip: '+value)
    except mod.Tip.DoesNotExist:
        pass