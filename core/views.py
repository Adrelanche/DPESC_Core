from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import (
    FAQ,
    Core,
    TypeOfService,
    AreaOfDuty,
    Unit,
    Popup,
    Tag,
    AreaOfActivity,
    WebsiteInformations,
    SocialMedia,
    EmailWebsite,
    )
from .serializers import (
    FAQSerializer,
    CoreSerializer,
    AreaOfDutySerializer,
    TypeOfServiceSerializer,
    UnitSerializer,
    PopupSerializer,
    TagSerializer,
    AreaOfActivitySerializer,
    WebsiteInformationsSerializer,
    SocialMediaSerializer,
    EmailWebsiteSerializer,
    )

class FaqView(generics.GenericAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()] 

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, *args, **kwargs):
        faqs = self.get_queryset()
        serializer = self.get_serializer(faqs, many=True)
        return Response(serializer.data)
    
    def delete(self, request, pk, *args, **kwargs):
        try:
            faq = FAQ.objects.get(pk=pk)
        except FAQ.DoesNotExist:
            return Response({'error': 'FAQ not found'}, status=status.HTTP_404_NOT_FOUND)

        faq.delete()
        return Response({'message': f'FAQ {pk}, deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk, *args, **kwargs):
        try:
            faq = FAQ.objects.get(pk=pk)
        except FAQ.DoesNotExist:
            return Response({'error': 'FAQ not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(faq, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CoreView(generics.GenericAPIView):
    queryset = Core.objects.all()
    serializer_class = CoreSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]
    
    def get(self, request, *args, **kwargs):
        core = self.get_queryset()
        serializer = self.get_serializer(core, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, *args, **kwargs):
        try:
            core = Core.objects.get(pk=pk)
        except Core.DoesNotExist:
            return Response({'error': 'Core not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(core, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        try:
            core = Core.objects.get(pk=pk)
        except Core.DoesNotExist:
            return Response({'error': 'Core not found'}, status=status.HTTP_404_NOT_FOUND)

        core.delete()
        return Response({'message': f'Core {pk}, deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
    
class UnitView(generics.GenericAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()] 
    
    def get(self, request, *args, **kwargs):
        unit = self.get_queryset()
        serializer = self.get_serializer(unit, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, *args, **kwargs):
        try:
            unit = Unit.objects.get(pk=pk)
        except Unit.DoesNotExist:
            return Response({'Error': 'Unit not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(unit, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, *args, **kwargs):
        try:
            unit = Unit.objects.get(pk=pk)
        except Unit.DoesNotExist:
            return Response({'Error': 'Unit not found'}, status=status.HTTP_404_NOT_FOUND)
        
        unit.delete()
        return Response({'message': f'Unit {pk}, deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
class CoreUnitsView(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            core = Core.objects.get(pk=pk)
        except Core.DoesNotExist:
            return Response({'error': 'Core not found'}, status=status.HTTP_404_NOT_FOUND)

        units = core.units.all()
        serializer = UnitSerializer(units, many=True)
        return Response(serializer.data)

    
class AreaOfDutyView(generics.GenericAPIView):
    queryset = AreaOfDuty.objects.all()
    serializer_class = AreaOfDutySerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
    def get(self, request, *args, **kwargs):
        duty = self.get_queryset()
        serializer = self.get_serializer(duty, many=True)
        return Response(serializer.data)
    
    def patch(self, request, pk, *args, **kwargs):
        try:
            duty = AreaOfDuty.objects.get(pk=pk)
        except AreaOfDuty.DoesNotExist:
            return Response({'Error': 'Duty not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(duty, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, *args, **kwargs):
        try:
            duty = AreaOfDuty.objects.get(pk=pk)
        except AreaOfDuty.DoesNotExist:
            return Response({'Error': 'Duty not found'}, status=status.HTTP_404_NOT_FOUND)
        
        duty.delete()
        return Response({'message': f'Duty {pk}, deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
class TypeOfServiceView(generics.GenericAPIView):
    queryset = TypeOfService.objects.all()
    serializer_class = TypeOfServiceSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]

    def get(self, request, *args, **kwargs):
        type_of_service = self.get_queryset()
        serializer = self.get_serializer(type_of_service, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, *args, **kwargs):
        try: 
            type_of_service = TypeOfService.objects.get(pk=pk)
        except TypeOfService.DoesNotExist:
            return Response({'Error': 'Type of service not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(type_of_service, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, *args, **kwargs):
        try:
            type_of_service = TypeOfService.objects.get(pk=pk)
        except TypeOfService.DoesNotExist:
            return Response({'Error': 'Type of service not found'}, status=status.HTTP_404_NOT_FOUND)
        
        type_of_service.delete()
        return Response({'message': f'Type of service {pk}, deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
class PopupView(generics.GenericAPIView):
    queryset = Popup.objects.all()
    serializer_class = PopupSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()] 

    def get(self, request, *args, **kwargs):
        popup = self.get_queryset()
        serializer = self.get_serializer(popup, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, *args, **kwargs):
        try:
            popup = Popup.objects.get(pk=pk)
        except Popup.DoesNotExist:
            return Response({'Error': 'Popup not found'})
        
        serializer = self.get_serializer(popup, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, *args, **kwargs):
        try:
            popup = Popup.objects.get(pk=pk)
        except Popup.DoesNotExist:
            return Response({'Error': 'Popup not found'}, status=status.HTTP_404_NOT_FOUND)
        
        popup.delete()
        return Response({'message': f'Popup {pk}, deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
class PopupIncrementClickView(generics.GenericAPIView):
    [IsAdminUser()]
    def post(self, request, pk):
        try:
            popup = Popup.objects.get(pk=pk)
        except Popup.DoesNotExist:
            return Response({'error': 'Popup not found'}, status=status.HTTP_404_NOT_FOUND)
        
        popup.increment_click()
        return Response({'Clicks': popup.click}, status=status.HTTP_200_OK)
    
class PopupIncrementVisualizationView(generics.GenericAPIView):
    [IsAdminUser()]

    def post(self, request, pk):
        try:
            popup = Popup.objects.get(pk=pk)
        except Popup.DoesNotExist:
            return Response({'error': 'Popup not found'}, status=status.HTTP_404_NOT_FOUND)
        
        popup.increment_visualization()
        return Response({'Visualization': popup.visualization}, status=status.HTTP_200_OK)
    
class TagView(generics.GenericAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]

    def get(self, request, *args, **kwargs):
        tag = self.get_queryset()
        serializer = self.get_serializer(tag, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer= self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, *args, **kwargs):
        try:
            tag = Tag.objects.get(pk=pk)
        except Tag.DoesNotExist:
            return Response({'Error': 'Tag not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(tag, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, *args, **kwargs):
        try:
            tag = Tag.objects.get(pk=pk)
        except Tag.DoesNotExist:
            return Response({'Error': 'Tag not found'}, status=status.HTTP_404_NOT_FOUND)
        
        tag.delete()
        return Response({f'Tag {pk}, deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
    
class TagIncrementTimesUsedView(generics.GenericAPIView):
    [IsAdminUser()]
    
    def post(self, request, pk, *args, **kwargs):
        try:
            obj = Tag.objects.get(pk=pk)
        except Tag.DoesNotExist:
            return Response({'Error': 'Object tag not found'}, status=status.HTTP_404_NOT_FOUND)
        
        obj.increment_times_used()
        return Response({f'times used of the tag: {pk}': obj.times_used}, status=status.HTTP_200_OK)
    
class AreaOfActivityView(generics.GenericAPIView):
    queryset = AreaOfActivity.objects.all()
    serializer_class = AreaOfActivitySerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]
    
    def get(self, request, *args, **kwargs):
        area_of_activity = self.get_queryset()
        serializer = self.get_serializer(area_of_activity, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk,*args, **kwargs):
        try:
            area_of_activity = AreaOfActivity.objects.get(pk)
        except AreaOfActivity.DoesNotExist:
            return Response({'Error': 'Area of Activity not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(area_of_activity, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, *args, **kwargs):
        try:
            area_of_activity = AreaOfActivity.objects.get(pk)
        except AreaOfActivity.DoesNotExist:
            return Response({'Error': 'Area of Activity not found'}, status=status.HTTP_404_NOT_FOUND)
        
        area_of_activity.delete()
        return Response({f'Area of Activity {pk}, deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    

class WebsiteInformationView(generics.GenericAPIView):
    serializer_class = WebsiteInformationsSerializer
    queryset = WebsiteInformations.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]

    def get(self, request, *args, **kwargs):
        website_information = WebsiteInformations.objects.first()
        if not website_information:
            return Response({'error': 'there is no information to show'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(website_information)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        if WebsiteInformations.objects.exists():
            return Response({'error': 'it already exists'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        website_information = WebsiteInformations.objects.first()
        if not website_information:
            return Response({'error': 'there is no information to edit'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(website_information, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        website_information = WebsiteInformations.objects.first()
        if not website_information:
            return Response({'error': 'there is no information to delete'}, status=status.HTTP_404_NOT_FOUND)
        
        website_information.delete()
        return Response({f'Website information deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
class SocialMediaView(generics.GenericAPIView):
    serializer_class = SocialMediaSerializer
    queryset = SocialMedia.objects.all()

    def get(self, request, *args, **kwargs):
        social_media = self.get_queryset()
        serializer = self.get_serializer(social_media, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

    def patch(self, request, pk, *args, **kwargs):
        try:
            social_media = SocialMedia.objects.get(pk=pk)
        except SocialMedia.DoesNotExist:
            return Response({'error': 'Social media not found'}, status=status.HTTP_404_NOT_FOUND) 
        
        serializer = self.get_serializer(social_media, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        try:
            social_media = SocialMedia.objects.get(pk=pk)
        except SocialMedia.DoesNotExist:
            return Response({'error': 'Social media not found'}, status=status.HTTP_404_NOT_FOUND)
        
        social_media.delete()
        return Response({f'Social media {pk}, deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
class EmailWebsiteView(generics.GenericAPIView):
    queryset = EmailWebsite.objects.all()
    serializer_class = EmailWebsiteSerializer

    def get(self, request, *args, **kwargs):
        email_website = self.get_queryset()
        serializer = self.get_serializer(email_website, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, *args, **kwargs):
        try:
            email_website = EmailWebsite.objects.get(pk=pk)
        except EmailWebsite.DoesNotExist:
            return Response({'error': 'Email not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(email_website, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, *args, **kwargs):
        try:
            email_website = EmailWebsite.objects.get(pk=pk)
        except EmailWebsite.DoesNotExist:
            return Response({'error': 'Email not found'}, status=status.HTTP_404_NOT_FOUND)
        
        email_website.delete()
        return Response({f'Email {pk}, deleted successfully'}, status=status.HTTP_204_NO_CONTENT)