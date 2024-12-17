class BaseTest:
    def open_browser(self):
        print("starting the browser")

    def read_from_excel(self):
        print("Read from excel")

    def close_browser(self):
        print("closing the browser")

class TestCase1(BaseTest):
    def test_positive(self):
        self.open_browser()
        print("Test case p1 executed")
        self.read_from_excel()
        self.close_browser()

    def test_negative(self):
        self.open_browser()
        print("Test case N1 executed")
        self.read_from_excel()
        self.close_browser()


class TestCase2(BaseTest):
    def test_positive(self):
        self.open_browser()
        print("Test case p2 executed")
        self.read_from_excel()
        self.close_browser()

    def test_negative(self):
        self.open_browser()
        print("Test case N2 executed")
        self.read_from_excel()
        self.close_browser()

TestCase1_ref = TestCase1()
TestCase1_ref.read_from_excel()
TestCase1_ref.open_browser()

