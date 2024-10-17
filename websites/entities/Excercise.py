class Exercise:
    def __init__(self, id, name, description, question):
        self.id = id
        self.name = name
        self.description = description
        self.question = question

    # Getter and Setter for id
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    # Getter and Setter for name
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    # Getter and Setter for description
    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    # Getter and Setter for question
    def get_question(self):
        return self.question

    def set_question(self, question):
        self.question = question
