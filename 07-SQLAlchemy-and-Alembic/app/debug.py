
# 3.✅ CRUD practice
# To run the file run `python3 console.py` in the app directory
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import (Base, Pet)

if __name__ == '__main__':
    #3.1 ✅ Uncomment bellow to create the engine
    # engine = create_engine('sqlite:///pet_app.db')
    engine = create_engine('sqlite:///pet_app.db')
    Base.metadata.create_all(engine)
    # Base.metadata.create_all(engine)
    #3.2 ✅ Uncomment bellow to create sessions and bind o the engine
    # Session = sessionmaker(bind=engine)
    # session = Session()
    Session = sessionmaker(bind=engine)
    session = Session()
    #3.3 ✅  -- Creating records
        # Create a pet and save it to the data base with session.add and session.commit
    tracker = Pet(name="Tracker", species = "Dog", breed = "Golden Lab", temperament="Angel", owner_id=1)
    # session.add(tracker)
    # session.commit()
        # Create multiple pets and bulk save them with  session.bulk_save_objects and session.commit
        #session.add(rose)
    leo = Pet(name = "Leo", species = "Dog", breed ="Corgi", temperament="Mean as hell", owner_id=2)
    brindle = Pet(name="Brindle", species = "Dog", breed ="Shitsu", temperament = "Good Boy", owner_id = 1)

        #Note: bulk save will not contain the id
    session.add_all([leo, brindle])
    session.commit()
        #verify by checking the db 
    #3.4 ✅ Read
        # Get all with session.query
        # Print the pets 
    pets = session.query(Pet)
    
        #Get all of the pet names and print them with session.query
    print([pet for pet in pets])
        #Get all the pet names and print them in order with session.query and order_by
    names = [name for name in session.query(Pet.name)]
    # print(names)
    names_order_by = [name for name in session.query(Pet.name).order_by(Pet.name)]
    # print(names_order_by)
        #Get the first pet with session.query and first
    first = session.query(Pet).first()
    print(first)
        #Filter pet by temperament with session.query and filter 
    f = session.query(Pet).filter(Pet.temperament.like('%Angel%'))
    for record in f:
        print(record)

    #3.5 ✅ Update 
        # Update the pets name and print the updated pet info
    first.name = "Trucker"
    print(first)
    session.commit()
    print(first)
        # Update all the pets temperament to 'cool' and print the pets 
    session.query(Pet).update({Pet.temperament: "Cool"})
    pets = session.query(Pet)
    print([pet for pet in pets])

    #3.6 ✅  Delete
        # Delete one item by querying the first pet, deleting it and committing it
    delete_one = session.query(Pet).first()
    session.delete(delete_one)
    session.commit()
        #delete all the pets with session.query and .delete
    session.query(Pet).delete()
    session.commit()
    # optional Break point for debugging and testing
    # import ipdb; ipdb.set_trace()