def generate_adaptive_questions(db, user_id, num_questions=10):

    stats = get_user_topic_stats(db, user_id)

    weak_topics = [
        s["topic"] for s in stats if s["level"] == "low"
    ]

    system_prompt = """
    Eres experto en oposiciones en España.
    Genera preguntas tipo test realistas.
    """

    user_prompt = f"""
    Genera {num_questions} preguntas tipo test.

    Prioriza estos temas:
    {weak_topics}

    Incluye:
    - pregunta
    - 4 opciones
    - respuesta correcta
    - tema
    - dificultad

    Devuelve JSON.
    """

    provider = get_llm_provider()

    response = provider.generate(system_prompt, user_prompt)

    return json.loads(response)