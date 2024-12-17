# super().start_browser() >> class parents start_browser

class OldBrowser:

    def start_browser(self):
        print("IE browser is staring")

    def stop_browser(self):
        print("IE borswer is closing")


class Chrome(OldBrowser):

    def start_browser(self):
        super().start_browser()
        print("BETTER chrome browser is staring")

    def stop_browser(self):
        print("BETTER chrome browser is closing")

C = Chrome()
C.start_browser()
C.stop_browser()