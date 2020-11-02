# training skills app

import sqlite3

class base_skills_app:

    choice_message = """
-------Welcome to skills app------
what do you want to do ?

1 => show all skills
2 => add a new skill
3 => update a skill
4 => delete a skill
5 => quit the app

write the number of your choice : """

    id_message = "\nwrite your user id : "

    skill_message = "\nwrite your skill : "

    n_skill_message = "\nwrite your new skill : "

    choice_list = [1, 2, 3, 4, 5]

    def set_choice(self):
        self.choice = int(input(base_skills_app.choice_message).strip())

    def set_u_id(self):
        self.u_id = int(input(base_skills_app.id_message).strip())

    def set_skill(self):
        self.skill = input(base_skills_app.skill_message).strip().capitalize()

    def set_n_skill(self):
        self.n_skill = input(
            base_skills_app.n_skill_message).strip().capitalize()

    def connection(self):
        self.db6 = sqlite3.connect("skills.db")
        self.cr6 = self.db6.cursor()
        self.cr6.execute(
            "create table if not exists skills (u_id integer, skills text)")

    def show_skills(self):
        self.cr6.execute(f"select * from skills where u_id = {self.u_id}")
        self.result = self.cr6.fetchall()
        print(f"\nyou have {len(self.result)} skill")
        for record in self.result:
            print(f"\nuser id --> {record[0]}, skill --> {record[1]}")
        if len(self.result):
            print("\nskills printed")

    def add_skill(self):
        self.cr6.execute(
            f"select skills from skills where u_id = {self.u_id} and skills = '{self.skill}'")
        self.resul = self.cr6.fetchone()
        if self.resul == None:
            self.cr6.execute(
                f"insert into skills (u_id, skills) values ({self.u_id}, '{self.skill}')")
            self.db6.commit()
            print("\nskill added")
        else:
            print("\nskill exists, you can not add it")

    def update_skills(self):
        self.cr6.execute(
            f"update skills set skills = '{self.n_skill}' where u_id = {self.u_id} and skills = '{self.skill}'")
        self.db6.commit()
        print("\nskill updated")

    def delete_skills(self):
        self.cr6.execute(
            f"delete from skills where u_id = {self.u_id} and skills = '{self.skill}'")
        self.db6.commit()
        print("\nskills deleted")


class skills_app(base_skills_app):

    def __init__(self):
        self.set_choice()

    def execute_choice(self):

        if self.choice in base_skills_app.choice_list:

            if self.choice == 5:
                print("\napp has been closed")

            else:
                self.set_u_id()
                self.connection()
                if self.choice == 1:
                    self.show_skills()

                else:
                    self.set_skill()
                    if self.choice == 2:
                        self.add_skill()

                    elif self.choice == 3:
                        self.set_n_skill()
                        self.update_skills()

                    else:
                        self.delete_skills()

                self.db6.close()
                print("\nconnection to database has been closed\n")

        else:
            print("\nwrong choice")


skills_app().execute_choice()
