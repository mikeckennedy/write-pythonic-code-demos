# noinspection PyMethodMayBeStatic
class Sample:
    def simple(self):
        print("simple")

    def simple(self, details):
        print(f"Simple with details: {details}")


s = Sample()
s.simple("Some details")
s.simple()
