from app.models.topic import Topic

def seed_topics(db, syllabus_id):

    topics = [
        (1, "Constitución Española de 1978"),
        (2, "Administración pública"),
        (3, "Procedimiento administrativo"),
        (4, "Acto administrativo"),
        (5, "Contratación pública"),
    ]

    for number, title in topics:

        topic = Topic(
            syllabus_id=syllabus_id,
            number=number,
            title=title
        )

        db.add(topic)

    db.commit()