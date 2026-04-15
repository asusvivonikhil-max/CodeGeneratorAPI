import google.generativeai as genai
from django.conf import settings

# Initialize Gemini (do this once)
genai.configure(api_key=settings.GEMINI_API_KEY)

# Create model instance with good settings for code generation
model = genai.GenerativeModel(
    model_name='gemini-2.5-flash',   # Fast & Free
    generation_config={
        "temperature": 0.7,
        "max_output_tokens": 4096,
    },
    system_instruction="You are an expert coding assistant. Always respond with only clean code in the requested language. No explanations, no markdown, no ``` blocks unless asked."
)

def Search(query, lan):
    try:
        if lan == "Python":
            prompt = f"Write only Python code for the following request. Output only the code, nothing else:\n{query}"
        
        elif lan == "Java":
            prompt = f"Write only Java code for the following request. Output only the code, nothing else:\n{query}"
        
        elif lan == "C":
            prompt = f"Write only C code for the following request. Output only the code, nothing else:\n{query}"
        
        else:
            prompt = f"Write only Python code for the following request. Output only the code, nothing else:\n{query}"

        response = model.generate_content(prompt)
        content = response.text

        return content.strip()

    except Exception as e:
        return f"Error generating code: {str(e)}"