

from django.urls import path

from squaring.views import SquaringView, RoarLouderView

urlpatterns = [
    path('', RoarLouderView.as_view(), name='home'),
    path("<int:number>", SquaringView.as_view(), name="number"), #int:number can be a variable as well ie number from the view. But if variable then cascade has to be at bottom
    
]