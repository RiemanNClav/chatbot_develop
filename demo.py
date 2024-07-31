import openai

# Configura la clave de API
openai.api_key = "sk-proj-YyiawSlAlXBJFXtLGdymT3BlbkFJi0oOXhNBzHFpyD2ky8Nc"

# Realiza una solicitud para crear una imagen
response = openai.Image.create(
    prompt='Duck with glasses',
    n=1,
    size='1024x1024'
)

# Imprime la respuesta
print(response)