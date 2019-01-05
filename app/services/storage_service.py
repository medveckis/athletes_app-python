
import csv
import os
import datetime
from app.domain.athlete import Athlete
from app.domain.injury import Injury


def add_athlete(athlete):
    """Function adds new athlete info to the file athletes.csv"""
    record = f"{athlete.id},{athlete.first_name},{athlete.last_name}\n"
    cwd = os.getcwd()
    file_dir = os.path.join(cwd, "data", "athletes.csv")
    with open(file_dir, "a") as f:
        f.write(record)


def add_injury(athlete_id, injury):
    """Function adds new injury info to the file associated with the athlete's id"""
    record = f"{injury.date.date()},{injury.injury_kind},{injury.muscle}," \
        f"{injury.side},{injury.out_of_training}\n"
    cwd = os.getcwd()
    athletes_dir = os.path.join(cwd, "data", "athletes.csv")
    with open(athletes_dir, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        is_added = False
        for line in csv_reader:
            if line["id"] == athlete_id:
                injuries_dir = os.path.join(cwd, "data", f"{athlete_id}_injuries.csv")
                exists = os.path.isfile(injuries_dir)
                if exists:
                    with open(injuries_dir, "a") as f:
                        f.write(record)
                else:
                    with open(injuries_dir, "a") as f:
                        first_row = "date,injury_kind,muscle,side,out_of_training\n"
                        f.write(first_row)
                        f.write(record)
                is_added = True
    return is_added


def remove(athlete_id):
    """Function deletes athlete's record from the file and corresponding injuries file also"""
    cwd = os.getcwd()
    athletes_dir = os.path.join(cwd, "data", "athletes.csv")
    is_deleted = False
    with open(athletes_dir, "r+") as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            if line[0] != athlete_id:
                f.write(line)
            else:
                is_deleted = True
        f.truncate()
    if is_deleted:
        injury_dir = os.path.join(cwd, "data", f"{athlete_id}_injuries.csv")
        os.remove(injury_dir)
    return is_deleted


def get_athletes():
    """Function gets all athlete records from the file"""
    cwd = os.getcwd()
    file_dir = os.path.join(cwd, "data", "athletes.csv")
    with open(file_dir, "r") as csv_file:
        lines = csv_file.readlines()
        len_lines = len(lines)
        if len_lines < 2:
            return []
        else:
            csv_file.seek(0)  # return pointer to the beginning of the file
            csv_reader = csv.DictReader(csv_file)
            athletes = []
            for row in csv_reader:
                athlete = Athlete(row["id"], row["first_name"], row["last_name"])
                athletes.append(athlete)
    return athletes


def get_injuries(athlete_id):
    """Function gets all the injury records from the file"""
    cwd = os.getcwd()
    file_dir = os.path.join(cwd, "data", f"{athlete_id}_injuries.csv")
    with open(file_dir, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        injuries = []
        for line in csv_reader:
            injury = Injury(datetime.datetime.strptime(line["date"], "%Y-%m-%d"), line["injury_kind"], line["muscle"],
                            line["side"], line["out_of_training"])
            injuries.append(injury)
    return injuries


def set_up():
    """Function is called when module downloads, checks for athletes.cvs file existence"""
    cwd = os.getcwd()
    athletes_dir = os.path.join(cwd, "data", "athletes.csv")
    exists = os.path.isfile(athletes_dir)
    if not exists:
        with open(athletes_dir, "w") as f:
            f.write("id,first_name,last_name\n")


set_up()
