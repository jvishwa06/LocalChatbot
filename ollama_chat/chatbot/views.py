from django.shortcuts import render
from django.http import JsonResponse
from langchain_ollama import OllamaLLM
from django.http import HttpResponse  # Add this import

# Initialize the Ollama model
llm = OllamaLLM(model="qwen2.5:0.5b")

def chat_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')  # Get user input from POST data
        if user_input:
            response = llm.invoke(input=user_input)  # Get response from Ollama model
            return JsonResponse({'response': response})
        else:
            return JsonResponse({'error': 'No input provided'}, status=400)
    else:
        return render(request, 'chatbot/chat.html')  # Render the chat interface template

def home(request):
    return HttpResponse("Welcome to the Chatbot Home Page!")  # or render a template
