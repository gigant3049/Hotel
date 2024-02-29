from django import forms

from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'check_in', 'check_out', 'adults', 'children']

    # room = forms.ChoiceField(
    #     choices=[('00', '00'), ('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'), ('05', '05'), ('06', '06')],
    #     widget=forms.Select(attrs={'class': 'form-control'}))
    #
    # adults = forms.ChoiceField(
    #     choices=[('00', '00'), ('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'), ('05', '05'), ('06', '06')],
    #     widget=forms.Select(attrs={'class': 'form-control'}))
    #
    # children = forms.ChoiceField(
    #     choices=[('00', '00'), ('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'), ('05', '05'), ('06', '06')],
    #     widget=forms.Select(attrs={'class': 'form-control'}))
    #
    # check_in = forms.DateField(
    #     widget=forms.DateInput(attrs={'class': 'form-control', 'id': 'checkIn', 'name': 'checkin-date'}))
    #
    # check_out = forms.DateField(
    #     widget=forms.DateInput(attrs={'class': 'form-control', 'id': 'checkIn', 'name': 'checkin-date'}))
    #
    # def __init__(self, *args, **kwargs):
    #     super(BookingForm, self).__init__(*args, **kwargs)
    #     self.fields['room'].widget.attrs.update({
    #         'class': 'form-control',
    #         'name': 'room',
    #         'id': 'room',
    #     })
    #     self.fields['check_in'].widget.attrs.update({
    #         'class': 'form-control',
    #         'id': 'checkIn',
    #         'name': 'check_in',
    #         'type': 'data'
    #     })
    #     self.fields['check_out'].widget.attrs.update({
    #         'class': 'form-control',
    #         'id': 'checkOut',
    #         'name': 'check_out',
    #         'type': 'data'
    #     })
    #     self.fields['adults'].widget.attrs.update({
    #         'class': 'form-control',
    #         'id': 'adults',
    #         'name': 'adults'
    #     })
    #     self.fields['children'].widget.attrs.update({
    #         'class': 'form-control',
    #         'id': 'children',
    #         'name': 'adults'
    #     })