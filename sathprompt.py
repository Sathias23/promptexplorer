import decimal
import random
from enum import Enum

class promptFragment:
    def __init__(self, prompt:str, numSelections:int, weight:decimal, variance:decimal=0):
        self.prompt = prompt
        self.weight = weight
        self.variance = variance
        self.numSelections = numSelections

    def asIs(self):
        return self.prompt

    def selectNum(self):
        splitPrompt = self.prompt.split(", ")
        selectPrompt = random.choices(splitPrompt, k=self.numSelections)
        return ", ".join(selectPrompt)

    def selectNumWithWeight(self):
        splitPrompt = self.prompt.split(", ")
        selectPrompt = random.choices(splitPrompt, k=self.numSelections)
        return " ".join([s + f":{self.weight}" for s in selectPrompt])

    def selectNumWithRandWeight(self):
        splitPrompt = self.prompt.split(", ")
        selectPrompt = random.choices(splitPrompt, k=self.numSelections)
        return " ".join([s + f":{round(random.uniform(self.weight - self.variance, self.weight + self.variance),2)}" for s in selectPrompt])

class CombineMethod(Enum):
    AS_IS = 1
    SELECT_NUM = 2
    SELECT_NUM_WITH_WEIGHT = 3
    SELECT_NUM_WITH_RAND_WEIGHT = 4

class promptFragments:
    fragments = []

    def addFragment(self, prompt: str, numSelections: int, weight: decimal, variance: decimal=0):
        self.fragments.append(promptFragment(prompt, numSelections, weight, variance))

    def combineFragments(self, method: CombineMethod):
        if method == CombineMethod.AS_IS:
            return ", ".join([f.asIs() for f in self.fragments])
        elif method == CombineMethod.SELECT_NUM:
            return ", ".join([f.selectNum() for f in self.fragments])
        elif method == CombineMethod.SELECT_NUM_WITH_WEIGHT:
            return " ".join([f.selectNumWithWeight() for f in self.fragments])
        elif method == CombineMethod.SELECT_NUM_WITH_RAND_WEIGHT:
            return " ".join([f.selectNumWithRandWeight() for f in self.fragments])

        


    