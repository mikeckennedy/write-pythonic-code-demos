# noinspection PyMethodMayBeStatic
class Sample:
    def simple(self):
        print("simple")

    def simple(self, details):
        print("Simple with details: {}".format(details))

s = Sample()
s.simple("Some details")
s.simple()
