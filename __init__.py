from mycroft import MycroftSkill, intent_file_handler


class OpaTestB(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('b.test.opa.intent')
    def handle_b_test_opa(self, message):
        self.speak_dialog('b.test.opa')


def create_skill():
    return OpaTestB()

