from django import forms
from django.forms import inlineformset_factory
from workouts.models import Workout, Exercise


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['title', 'duration_min', 'date']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Назва тренування'
            }),
            'duration_min': forms.NumberInput(attrs={
                'min': 1,
                'step': 1,
                'placeholder': 'Тривалість, хв'
            }),
            'date': forms.DateInput(attrs={
                'type': 'date'
            }),
        }


ExerciseFormSet = inlineformset_factory(
    Workout, Exercise,
    fields=['name', 'sets', 'repetitions'],
    extra=1,
    can_delete=True,
    min_num=1,
    validate_min=True,
    widgets={
        'name': forms.TextInput(attrs={'placeholder': 'Назва вправи'}),
        'sets': forms.NumberInput(attrs={'min': 1, 'placeholder': 'Підходи'}),
        'repetitions': forms.NumberInput(attrs={'min': 1, 'placeholder': 'Повторення'}),
    }
)
