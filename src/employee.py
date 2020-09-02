# Employee class primarily for validating entered text input data for saving
class Employee:

    def __init__(self, name, classification):
        self.name = name
        self.classification = classification

    @property
    def name(self):
        return self._name

    @property
    def classification(self):
        return self._classification

    @name.setter
    def name(self, new_name):
        if len(new_name) > 0 and not any(i.isdigit() for i in new_name):
            self._name = new_name
        else:
            self._name = ""

    @classification.setter
    def classification(self, new_classification):
        if len(new_classification) > 0 and not any(i.isdigit() for i in new_classification):
            self._classification = new_classification
        else:
            self._classification = ""
