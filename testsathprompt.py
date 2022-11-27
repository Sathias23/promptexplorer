import sathprompt
import sathexif

x = sathprompt.promptFragments()
x.addFragment("A cow, A bird, A camel", 1, 1)
x.addFragment("by John, by Bill, by Jane, by Sarah, by Mary", 2, 0.5)
x.addFragment("in the field, in the forest, in the desert", 1, 0.5)
x.addFragment("with a hat, with a scarf, with a jacket", 1, -0.5)
#x.addFragment("normal, poor quality, boring, tedious, interesting, exciting", 3, -0.5)
print(x.combineFragments(sathprompt.CombineMethod.SELECT_NUM_WITH_BRACKETS, sathprompt.Direction.POSITIVE))
print(x.combineFragments(sathprompt.CombineMethod.SELECT_NUM_WITH_BRACKETS, sathprompt.Direction.NEGATIVE))

