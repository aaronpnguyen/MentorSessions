from human import Human

aaron = Human("Aaron", "Nguyen", "11/23/2001", 21, 100, "Computer Science")
jorgan = Human("Jor", "Gan", "2000/12/12", 22, 100, "Computer Science")

aaron.print_name()
print(aaron.check_old_enough_to_drink())
aaron.attack_human(jorgan)
print(jorgan.health)