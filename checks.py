import setup


class Checker():

    def __init__(self):
        self.TOK = setup.TOK
        self.OWNER_UID = setup.OWNER_UID
        self.SELFBOT_UID = setup.SELFBOT_UID
        self.BALL_TYPE = setup.BALL_TYPE
        self.CAPTURE_CHANCE = setup.CAPTURE_CHANCE

        

    def verifyVals(self):
        if self.OWNER_UID == 0:
            sys.exit("OWNER_UID varibale not set. Refer to the github README for information about this.")
        if self.SELFBOT_UID == 0:
            sys.exit("SELFBOT_UID varibale not set. Refer to the github README for information about this.")
        if self.TOK == "":
            sys.exit("TOKEN value not set. Refer to the github README for information about this.")
        if self.BALL_TYPE != "POKEBALL" and self.BALL_TYPE != "GREATBALL" and self.BALL_TYPE != "ULTRABALL":
            sys.exit("Pokeball Either Configured Incorrectly or not set.")
        if self.CAPTURE_CHANCE == 100:
            print("Consider changing CAPTURE_CHANCE from 100 in order to seem more legit.")
        #CAPTURE_CHANCE
        print("All Checks Complete. No Issues Found.")
