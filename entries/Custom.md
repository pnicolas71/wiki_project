# Custom
 
Add custom CSS styling to model form django
Ask Question
Asked 2 years, 11 months ago
Active 2 years, 11 months ago
Viewed 8k times
2

I am using a bootstrap variant to help style a model form. There is a certain class I would like one of the fields to be and I have read around on the subject and the general consensus is to add a widget to the ModelForm's meta, like I tried below:

forms.py

class EmailForm(forms.ModelForm):
    class Meta:
        model = MarketingEmails
        fields = ['messageid','subject','body','name','altsubject','utm_source','utm_content','utm_campaign',]
        widgets = {
            'body': Textarea(attrs={'class': 'summernote'}),