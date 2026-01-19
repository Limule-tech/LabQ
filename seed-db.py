from app import app
from models import db, Subject, Experiment

with app.app_context():

    db.drop_all()   # This deletes the old tables
    db.create_all() # This creates new tables with your new columns

    # Clear existing data to avoid duplicates
    db.session.query(Experiment).delete()
    db.session.query(Subject).delete()
    
    # 1. Create Subjects
    bio = Subject(name='Biology')
    chem = Subject(name='Chemistry')
    phys = Subject(name='Physics')
    
    db.session.add_all([bio, chem, phys])
    db.session.commit() # Commit to get the IDs

    # 2. Create Experiments linked to Subjects
    experiments = [
        Experiment(
            title="Cell Structure", 
            description="Examine plant and animal cells under a virtual microscope.",
            youtube_url="https://www.youtube.com/embed/URUJD5NEXC8", # Example Bio Video
            subject_id=bio.id
        ),
        Experiment(
            title="Acid Base Titration", 
            description="Find the concentration of an unknown acid solution.",
            youtube_url="https://www.youtube.com/embed/sFpFCPTDv2w", # Example Chem Video
            subject_id=chem.id
        ),
        Experiment(
            title="Ohm's Law", 
            description="Explore the relationship between voltage, current, and resistance.",
            youtube_url="https://www.youtube.com/embed/HsLLq6Rm5tU", # Example Phys Video
            subject_id=phys.id
        )
    ]

    db.session.add_all(experiments)
    db.session.commit()
    print("Database seeded with Subjects and Experiments successfully!")