from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from translator.models import Translation
from translator.serializers import TranslationSerializer

# Create your views here.

class FrenchSpanishTranslationViewSet(APIView):

    def get(self, request):
        import google.generativeai as genai

        prompt="""traduis "je suis éléve et je me balade" """
        API_KEY = "AIzaSyCPDuTpNgQgN2foSezAbSop104MMD0UJdI"
        genai.configure(api_key=API_KEY)

        model = genai.GenerativeModel("gemini-1.5-flash")

        # Générer du contenu avec une invite
        response = model.generate_content(prompt)

        # Afficher le texte généré
        print(response.text)

        return Response(data={"result": response.text}, status=status.HTTP_200_OK)
    
    def post(self, request):
        return Response(data={}, status=None)
    
    def put(self, request, pk):
        return Response(data={}, status=None)
    
    def delete(self, request, pk):
        return Response(data={}, status=None)
    
class FrenchEnglishTranslationViewSet(APIView):

    def get(self, request):
        return Response(data={}, status=None)
    
    def post(self, request):
        return Response(data={}, status=None)
    
    def put(self, request, pk):
        return Response(data={}, status=None)
    
    def delete(self, request, pk):
        return Response(data={}, status=None)
    
class Alltranslation(APIView):
    def get(self, request):
        data = Translation.objects.all()
        serialized_data = TranslationSerializer(data, many=True)
        return Response(data=serialized_data.data, status=None)
def index(request):
    return render(request, 'index.html', context={})