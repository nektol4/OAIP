class Button:
    def __init__(self, w=100, h=50, position=(5, 10), color="red"):
        self.w = w
        self.h = h
        self.position = position
        self.color = color
        self.current_page = "home"

    def set_position(self, x, y):
        print(f'Button position: {x, y}')
        self.position = x, y

    def set_w_h(self, w, h):
        print(f'Button size: {w, h}')
        self.w = w
        self.h = h

    def press(self):
        if self.current_page != "home":
            self.current_page = "home"
            print("You have navigated to the home page.")
        else:
            print("You are already on the home page.")

    def go_to_settings(self):
        if self.current_page != "settings":
            self.current_page = "settings"
            print("You have navigated to the site settings.")
        else:
            print("You are already in the settings.")

    def exit_site(self):
        if self.current_page != "exit":
            self.current_page = "exit"
            print("You have left the site.")
        else:
            print("You have already left the site.")

    def display_info(self):
        print(f"Button Color: {self.color}")