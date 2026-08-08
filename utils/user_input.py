def user_input_int(end : int, prompt: str, warnings: dict) -> int | None:
   """ Przyjmuję pozycję następnego widoku. Jeśli walidacja przejdzie prawidłowo, zwraca liczbę widoku. Jeśli wprowadzona liczba to -1 zwraca None """
   while True:
       user_input = input(prompt)
       if user_input == "-1":
           return None

       if not user_input.isdecimal():
           print(warnings["warningInputInt"])
           continue
       user_input = int(user_input)
       if user_input < 0 or user_input > end:
           print(warnings["warningInputOutOfTheRange"])
           continue
       return user_input


