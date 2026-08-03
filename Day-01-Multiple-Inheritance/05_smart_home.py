class Light:
    def turn_on_light(self):
        print("Light on")

    def turn_off_light(self):
        print("Light off")

class Fan:
    def turn_on_fan(self):
        print("Fan on")

    def turn_off_fan(self):
        print("Fan off")

class SmartRoom(Light, Fan):
    def menu(self):
        while True:
            choice = int(input("""Enter choice: 
            1 Turn on light
            2 Turn off light
            3 Turn on fan
            4 Turn off fan
            5 Exit      
            """))
            match choice:
                case 1:
                    self.turn_on_light()
                case 2:
                    self.turn_off_light()
                case 3:
                    self.turn_on_fan()
                case 4:
                    self.turn_off_fan()
                case 5:
                    print("Exit")
                    return
                case _:
                    print("Invalid choice")

s = SmartRoom()
s.menu()