from record import Record

# třída pro Správu pojišťovny
class InsuranceAdministration:

    def __init__(self):
        self.records = []

    # metoda pro vytvoření záznamu pojištěnce
    def create_record(self):
        while True:
            name = input("Zadejte jméno: ").strip()
            # vrací True, pokud abeced. znaky a pokud neprázdné
            if name.isalpha() and name:
                break
            print("Jméno může obsahovat pouze písmena.")
        while True:
            surname = input("Zadejte příjmení: ").strip()
            if surname.isalpha() and surname:
                break
            print("Příjmení může obsahovat pouze písmena.")
        while True:
            age = input("Zadejte věk: ")
            try:
                age = int(age)
                if 0 <= age <= 150:
                    break
                else:
                    print("Věk pro naše pojištěnce musí být max 150 let.")
            except ValueError:
                print("Věk musí být číslo, zkuste zadat znovu.")
        while True:
            phone = input("Zadejte telefonní číslo: ")
            if phone.isdigit() and len(phone) == 9:
                break
            else:
                print("Číslo musí obsahovat 9 číslic.")
        new_record = Record(name, surname, age, phone)
        self.records.append(new_record)
        print(f"Nový záznam byl přidán do evidence.\n")

    # pro výpis všech pojištěnců
    def get_all_records(self):
        print("Výpis všech pojištěnců:")
        for record in self.records:
            print(record)
        print()

    def find_record(self):
        while True:
            name_and_surname = input("Zadejte jméno a příjmení pojištěnce:")
            if " " in name_and_surname:
                name, surname = name_and_surname.split(" ")
                if name.isalpha() and surname.isalpha():
                    break
                else:
                    print("Jméno a příjmení mohou obsahovat pouze písmena.")
            print("Jméno a příjmení musí být odděleny mezerou.")
        for record in self.records:
            if record._name == name and record._surname == surname:
                print("Hledaný pojištěnec: ", record, "\n")
                return
        print("Hledaný pojištěnec nebyl nalezen.\n")

    #metoda pro ošetření vztupu jméno:
    # není použito, bylo mi inspirací, funkci si tu zatím ponechám
    def get_valid_name(self):
        name = input("Zadejte jméno: ")
        while not name.isalpha():
            print("Jméno může obsahovat pouze písmena.")
        return name



