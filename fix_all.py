from app import app, db
from models import Experiment, Question # Ensure these match your models.py

def run_fix():
    with app.app_context():
        # 1. Clear the quizzes first to avoid duplicates
        db.session.query(Question).delete()
        db.session.query(Experiment).delete()
        db.session.commit()

        # 2. Re-create the Experiments
        # We save them as variables so we can grab their IDs immediately
        chem = Experiment(title="Acid Base Titration", description="Find the concentration...", youtube_url="https://www.youtube.com/embed/sFpFCPTDv2w")
        phys = Experiment(title="Ohm's Law", description="Explore voltage and current...", youtube_url="https://www.youtube.com/embed/HsLLq6Rm5tU")
        bio = Experiment(title="Cell Structure", description="Examine plant and animal cells...", youtube_url="https://www.youtube.com/embed/URUJD5NEXC8")

        db.session.add_all([chem, phys, bio])
        db.session.commit() # This generates the IDs in the database!

        # 3. Now add the Quizzes using the exact IDs from above
        quiz_data = [
            # CHEMISTRY
            {"exp": chem, "q": "Which tool is used to add titrant drop by drop?", "a": "Burette", "b": "Beaker", "c": "Flask", "d": "Pipette", "ans": "A"},
            # PHYSICS
            {"exp": phys, "q": "What is the unit of electrical Resistance?", "a": "Volt", "b": "Ampere", "c": "Ohm", "d": "Watt", "ans": "C"},
            # BIOLOGY
            {"exp": bio, "q": "Which organelle is known as the 'brain' of the cell?", "a": "Mitochondria", "b": "Nucleus", "c": "Ribosome", "d": "Vacuole", "ans": "B"}
        ]

        for item in quiz_data:
            new_q = Question(
                exp_id=item["exp"].id, # This uses the REAL ID created 2 seconds ago
                question=item["q"],
                option_a=item["a"],
                option_b=item["b"],
                option_c=item["c"],
                option_d=item["d"],
                correct_answer=item["ans"]
            )
            db.session.add(new_q)
        
        db.session.commit()
        print("Success! Everything is synced and seeded.")

if __name__ == "__main__":
    run_fix()