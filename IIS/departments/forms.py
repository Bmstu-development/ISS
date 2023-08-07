from django import forms
from django.contrib.auth.models import Group

from . import models
from people.models import Person


class DepartmentAddForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.people = Person.objects.all()

    name = forms.CharField(
        label='Название',
        help_text='Введенное название будет считаться официальным названием отдела',
        strip=True,
        widget=forms.TextInput(attrs={
            'placeholder': ''
        }),
    )

    descr = forms.CharField(
        label='Описание',
        help_text='Введенное описание будет считаться официальным описанием отдела',
        strip=True,
        widget=forms.Textarea(attrs={
            'placeholder': ''
        }),
    )

    permissions = forms.ChoiceField(
        label='Уровень доступа',
        help_text='Выбранный уровень будет определять права активистов, являющихся пользователями',
        choices=models.Department.PERMISSION_CHOICES,
    )

    supervisor_instance = forms.ModelChoiceField(
        label='Руководитель',
        help_text='Официальный руководитель, который сможет изменять информацию об отделе',
        queryset=Person.objects.all(),
        empty_label='Не выбран',
        required=False,
    )

    def save(self, commit=True):
        instance = super().save(commit=False)
        print('in form save')
        print(instance)
        print(self.cleaned_data)
        if commit:
            pass
            # instance.save()
            # self.save_m2m()
            # for pn in instance.activists.all():
            #     if pn.user_instance is None:
            #         continue
            #     Group.objects.get(name=instance.permissions).user_set.add(pn.user_instance)
        return instance

    class Meta:
        model = models.Department
        fields = 'name', 'descr', 'permissions', 'supervisor_instance',
