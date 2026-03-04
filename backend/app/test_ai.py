from app.services.ai_generator import generate_questions_for_exam

if __name__ == "__main__":
    result = generate_questions_for_exam("Constitución Española", 2)
    print(result)