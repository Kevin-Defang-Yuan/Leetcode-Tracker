from django.forms import ModelForm, ModelMultipleChoiceField, CharField, CheckboxSelectMultiple
from .models import Collection, Question, Task


class CustomMMCF(ModelMultipleChoiceField):
    queryset = Question.objects.all(),
    widget=CheckboxSelectMultiple
    # def label_from_instance(self, question):
    #     return "%s" % question.topic

class CreateCollectionForm(ModelForm):
    class Meta:
        model = Collection
        fields = ['name', 'questions']
    name = CharField()

    questions = ModelMultipleChoiceField(
        queryset = Question.objects.all(),
        widget=CheckboxSelectMultiple 
    )

    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(CreateCollectionForm, self).__init__(*args, **kwargs)
        self.fields['questions'].queryset = Question.objects.filter(user=user)


        






