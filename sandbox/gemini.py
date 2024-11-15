import google.generativeai as genai

API_KEY = "AIzaSyCPDuTpNgQgN2foSezAbSop104MMD0UJdI"
genai.configur(api_ekey=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

# Générer du contenu avec une invite
response = model.generate_content("donne moi le code d'une page d'index.html")

# Afficher le texte généré
print(response.text)
