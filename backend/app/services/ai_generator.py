import json
from app.services.llm.factory import get_llm_provider

def generate_questions_for_exam(title: str, num_questions: int = 5):

    provider = get_llm_provider()

    system_prompt = "Eres experto en oposiciones en España."

    user_prompt = f"""
    Genera {num_questions} preguntas tipo test para un examen de oposiciones.
    Título del examen: {title}

    Devuelve un JSON con esta estructura:
    [
      {{
        "statement": "...",
        "option_a": "...",
        "option_b": "...",
        "option_c": "...",
        "option_d": "...",
        "correct_answer": "A"
      }}
    ]
    """

    response = provider.generate(system_prompt, user_prompt)

    return json.loads(response)