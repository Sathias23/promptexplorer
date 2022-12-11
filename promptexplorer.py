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
        selectPrompt = random.sample(splitPrompt, k=self.numSelections)
        return ", ".join(selectPrompt)

    def selectNumWithWeight(self, direction):
        splitPrompt = self.prompt.split(", ")
        selectPrompt = random.sample(splitPrompt, k=self.numSelections)
        if direction == Direction.POSITIVE:
            return " ".join([s + f":{self.weight}" for s in selectPrompt])
        else:
            return " ".join([s + f":{self.weight * -1}" for s in selectPrompt])

    def selectNumWithBrackets(self, direction):
        splitPrompt = self.prompt.split(", ")
        selectPrompt = random.sample(splitPrompt, k=self.numSelections)
        if direction == Direction.POSITIVE:
            return " ".join([f"({s}:{self.weight})" for s in selectPrompt])
        else:
            return " ".join([f"({s}:{self.weight * -1})" for s in selectPrompt])

    def selectNumWithRandWeight(self, direction):
        splitPrompt = self.prompt.split(", ")
        selectPrompt = random.sample(splitPrompt, k=self.numSelections)
        if direction == Direction.POSITIVE:
            return " ".join([s + f":{round(random.uniform(self.weight - self.variance, self.weight + self.variance),2)}" for s in selectPrompt])
        else:
            return " ".join([s + f":{round(random.uniform(self.weight - self.variance, self.weight + self.variance),2) * -1}" for s in selectPrompt])

class CombineMethod(Enum):
    AS_IS = 0
    SELECT_NUM = 1
    SELECT_NUM_DIRECTIONAL = 2
    SELECT_NUM_WITH_WEIGHT = 3
    SELECT_NUM_WITH_BRACKETS = 4
    SELECT_NUM_WITH_RAND_WEIGHT = 5

class Direction(Enum):
    POSITIVE = 1
    NEGATIVE = 2

class promptFragments:
    def __init__(self):
        self.fragments = []

    def clear(self):
        self.fragments.clear()

    def addFragment(self, prompt: str, numSelections: int, weight: decimal, variance: decimal=0):
        self.fragments.append(promptFragment(prompt, numSelections, weight, variance))

    def combineFragments(self, method:CombineMethod, direction:Direction=Direction.POSITIVE):
        if method == CombineMethod.AS_IS:
            return ", ".join([f.asIs() for f in self.fragments])
        elif method == CombineMethod.SELECT_NUM:
            return ", ".join([f.selectNum() for f in self.fragments])
        elif method == CombineMethod.SELECT_NUM_DIRECTIONAL and direction == Direction.POSITIVE:
            return ", ".join([f.selectNum() for f in filter(lambda f: f.weight > 0, self.fragments)])
        elif method == CombineMethod.SELECT_NUM_DIRECTIONAL and direction == Direction.NEGATIVE:
            return ", ".join([f.selectNum() for f in filter(lambda f: f.weight < 0, self.fragments)])
        elif method == CombineMethod.SELECT_NUM_WITH_WEIGHT and direction == Direction.POSITIVE:
            return " ".join([f.selectNumWithWeight(direction) for f in filter(lambda f: f.weight > 0, self.fragments)])
        elif method == CombineMethod.SELECT_NUM_WITH_WEIGHT and direction == Direction.NEGATIVE:
            return " ".join([f.selectNumWithWeight(direction) for f in filter(lambda f: f.weight < 0, self.fragments)])
        elif method == CombineMethod.SELECT_NUM_WITH_BRACKETS and direction == Direction.POSITIVE:
            return " ".join([f.selectNumWithBrackets(direction) for f in filter(lambda f: f.weight > 0, self.fragments)])
        elif method == CombineMethod.SELECT_NUM_WITH_BRACKETS and direction == Direction.NEGATIVE:
            return " ".join([f.selectNumWithBrackets(direction) for f in filter(lambda f: f.weight < 0, self.fragments)])
        elif method == CombineMethod.SELECT_NUM_WITH_RAND_WEIGHT and direction == Direction.POSITIVE:
            return " ".join([f.selectNumWithRandWeight(direction) for f in filter(lambda f: f.weight > 0, self.fragments)])
        elif method == CombineMethod.SELECT_NUM_WITH_RAND_WEIGHT and direction == Direction.NEGATIVE:
            return " ".join([f.selectNumWithRandWeight(direction) for f in filter(lambda f: f.weight < 0, self.fragments)])
        else:
            return "Error: Invalid combination of method and direction"
            

        


    