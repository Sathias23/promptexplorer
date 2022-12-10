import sathprompt
import sathexif
import synonymiser

x = sathprompt.promptFragments()
x.addFragment("A cow, A bird, A camel", 1, 1)
x.addFragment("by John, by Bill, by Jane, by Sarah, by Mary", 2, 0.5)
x.addFragment("in the field, in the forest, in the desert", 1, 0.5)
x.addFragment("with a hat, with a scarf, with a jacket", 1, -0.5)
#x.addFragment("normal, poor quality, boring, tedious, interesting, exciting", 3, -0.5)
pos = x.combineFragments(sathprompt.CombineMethod.SELECT_NUM_DIRECTIONAL, sathprompt.Direction.POSITIVE)
neg = x.combineFragments(sathprompt.CombineMethod.SELECT_NUM_DIRECTIONAL, sathprompt.Direction.NEGATIVE)

print(pos)
print(neg)
syn = synonymiser.synonymiser(pos, 16)
print(syn.synonymise())
syn = synonymiser.synonymiser(neg, 16)
print(syn.synonymise())

