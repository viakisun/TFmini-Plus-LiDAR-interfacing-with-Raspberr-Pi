class ManageConfigFile():
    def __init__(self):
        self.distanceModeSprayTime = None
        self.distanceModeDetectDistance = None
        self.autoModeCycleTime = None
        self.autoModeSprayTime = None
        self.readFile()

        print(self.distanceModeSprayTime)
        print(self.distanceModeDetectDistance)
        print(self.autoModeCycleTime)
        print(self.autoModeSprayTime)

    def readFile(self):
        with open("config.txt", mode="r") as file:
            while True:
                sentence = file.readline()
                if sentence:
                    splitStr = sentence.split(":")
                    value = splitStr[1].replace("\n", "")
                    if (splitStr[0] == "distanceModeSprayTime") :
                        self.distanceModeSprayTime = value
                    elif (splitStr[0] == "distanceModeDetectDistance") :
                        self.distanceModeDetectDistance = value
                    elif (splitStr[0] == "autoModeCycleTime") :
                        self.autoModeCycleTime = value
                    elif (splitStr[0] == "autoModeSprayTime") :
                        self.autoModeSprayTime = value
                else:
                    break

if __name__ == "__main__" :
    manageConfigFile = ManageConfigFile()