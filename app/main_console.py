from app.services import storage_service as ss
from app.domain.athlete import Athlete
from app.domain.injury import Injury
import datetime


def legend():
    print("0: exit\n1: add athlete\n2: add injury\n3: remove athlete\n4: get athletes\n5: get injuries\n")


if __name__ == "__main__":
    print("Hello, this is athlete manager app!\n")
    choice = ""
    while choice != "0":
        legend()
        choice = input("Your choice: ")
        if choice == "1":
            first_name = input("First name: ")
            last_name = input("Last name: ")
            ss.add_athlete(Athlete.default_constructor(first_name, last_name))
        elif choice == "2":
            a_id = input("Athlete's id: ")
            date = input("Enter date in format 'mm/dd/yyyy':")
            date = datetime.datetime.strptime(date, "%m/%d/%Y")
            injury_kind = input("Kind of injury: ")
            muscle = input("Muscle: ")
            side = input("Side: ")
            out_of_training = input("Out of training: ")
            injury = Injury(date, injury_kind, muscle, side, out_of_training)
            is_added = ss.add_injury(a_id, injury)
            if is_added:
                print("Injury added successfully!\n")
            else:
                print("Injury not added due to error!\n")
        elif choice == "3":
            a_id = input("Athlete's id: ")
            is_deleted = ss.remove(a_id)
            if is_deleted:
                print("Athlete deleted successfully!\n")
            else:
                print("Athlete was not deleted due to error!\n")
        elif choice == "4":
            athletes = ss.get_athletes()
            for n, athlete in enumerate(athletes):
                print(f"{n + 1}: Id-> {athlete.id}; First name-> {athlete.first_name}; "
                      f"Last name-> {athlete.last_name}.")
            print()
        elif choice == "5":
            a_id = input("Enter athlete's id: ")
            injuries = ss.get_injuries(a_id)
            for n, injury in enumerate(injuries):
                print(f"{n + 1}: Date-> {injury.date.date()}; Kind of injury-> {injury.injury_kind}; "
                      f"Muscle-> {injury.muscle}; Side-> {injury.side}; Out of training-> {injury.out_of_training}.")
            print()
        elif choice == "0":
            print("Goodbye!")
        else:
            print("This operation does not exist!\n")
