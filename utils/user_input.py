import datetime


def user_input_int(end : int, prompt: str, warnings: dict[ str, str]) -> int:
   """ Przyjmuję pozycję następnego widoku. Jeśli walidacja przejdzie prawidłowo, zwraca liczbę widoku. Jeśli wprowadzona liczba to -1 zwraca -1 """
   while True:
       user_input = input(prompt)
       try:
           user_input = int(user_input)
       except ValueError:
           print(warnings["warningInputInt"])
           continue
       if user_input == -1:
           return user_input
       if user_input <= 0 or user_input > end:
           print(warnings["warningInputOutOfTheRange"])
           continue
       return user_input

def user_input_str(prompt : str, warnings: dict[str, str]) -> str | int:
   """ Prosi użytkownika o wprowadzenie danych, jeśli przejdzię walidację zwraca dane. Jeśli wprowadzi -1 zwraca -1"""
   while True:
       user_input = input(prompt).strip()
       if user_input == "-1":
           return int(user_input)
       if user_input == "":
           print(warnings["warningEmptyInput"])
           continue
       return user_input
def user_input_date(prompt : str, warnings: dict [str, str]):
    """ Prosi użytkownika o datę w formacie (xxxx-xx-xx), waliduję oraz zwraca obiekt datetime"""
    while True:
        user_input = user_input_str(prompt, warnings)
        if user_input == -1:
            return user_input

        try:
            split_date = user_input.split("-")
            if len(split_date) != 3:
                print(warnings["warningWrongDate"])
                continue
            year = int(split_date[0])
            month = int(split_date[1])
            day = int(split_date[2])
            user_date = datetime.datetime(year, month, day).date()
            if user_date > datetime.datetime.now().date():
                print(warnings["warningWrongDate"])
                continue
            return user_date
        except ValueError:
            print(warnings["warningWrongDate"])
            continue

