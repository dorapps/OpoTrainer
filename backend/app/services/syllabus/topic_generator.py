from app.services.llm.openrouter_provider import OpenRouterProvider
from app.rag.retrieve import retrieve_context


class TopicGenerator:

    def __init__(self):
        self.llm = OpenRouterProvider()

    def generate_topic(self, title: str) -> str:
        """
        Genera el contenido completo de un tema de oposición usando RAG.
        """

        context = retrieve_context(title)

        system_prompt = """
Eres un experto en oposiciones administrativas en España.

Tu tarea es redactar temas de estudio claros, estructurados y útiles para opositores.

Debes:
- Explicar los conceptos de forma clara
- Mantener rigor jurídico
- Priorizar lo importante para examen
"""

        user_prompt = f"""
Genera el contenido del siguiente tema de oposición.

TEMA:
{title}

CONTEXTO DE REFERENCIA:
{context}

INSTRUCCIONES:

1. Introducción breve
2. Desarrollo del tema
3. Explicación de artículos clave
4. Esquema resumen final
5. 5 preguntas tipo test con 4 opciones y respuesta correcta

El texto debe estar bien estructurado para estudiar.
"""

        return self.llm.generate(system_prompt, user_prompt)