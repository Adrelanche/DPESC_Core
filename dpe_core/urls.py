from django.contrib import admin
from django.urls import path
from core.views import (
    FaqView,
    UnitView,
    CoreView,
    CoreUnitsView,
    PopupView,
    PopupIncrementClickView,
    PopupIncrementVisualizationView,
    TagView,
    TagIncrementTimesUsedView,
    AreaOfActivityView,
    WebsiteInformationView,
    SocialMediaView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/faq/', FaqView.as_view(), name='faq-list-create'),
    path('api/faq/<int:pk>/', FaqView.as_view(), name='faq-detail'),
    
    path('api/unit/', UnitView.as_view(), name='unit-list-create' ),
    path('api/unit/<int:pk>/', UnitView.as_view(), name='unit-detail' ),
    
    path('api/core/', CoreView.as_view(), name='core-list-create' ),
    path('api/core/<int:pk>/', CoreView.as_view(), name='core-detail' ),
    path('api/cores/<int:pk>/units/', CoreUnitsView.as_view(), name="core-units"),
    
    path('api/popup/', PopupView.as_view(), name='popup-list-create'),
    path('api/popup/<int:pk>/', PopupView.as_view(), name='popup-detail'),
    path('api/popup/<int:pk>/increment_click/', PopupIncrementClickView.as_view(), name='popup-increase-click'),
    path('api/popup/<int:pk>/increment_visualization/', PopupIncrementVisualizationView.as_view(), name='popup-increase-visualization'),
    
    path('api/tag/', TagView.as_view(), name='tag-list-create'),
    path('api/tag/<int:pk>/', TagView.as_view(), name='tag-detail'),
    path('api/tag/<int:pk>/increment_times_used/', TagIncrementTimesUsedView.as_view(), name='tag-increase-times-used'),
    
    path('api/area-of-activity/', AreaOfActivityView.as_view(), name='area_of_activity-list-create'),
    path('api/area-of-activity/<int:pk>/', AreaOfActivityView.as_view(), name='area_of_activity-detail'),
    
    path('api/website-information/', WebsiteInformationView.as_view(), name='website_information-list-create-detail'),

    path('api/social-media/', SocialMediaView.as_view(), name='social_media-list-create'),
    path('api/social-media/<int:pk>/', SocialMediaView.as_view(), name='social_media-detail'),
]
