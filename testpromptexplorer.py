import promptexplorer
from promptmutator import synonymiser

x = promptexplorer.promptFragments()
x.addFragment("A cow, A bird, A camel", 1, 1)
x.addFragment("by John, by Bill, by Jane, by Sarah, by Mary", 2, 0.5)
x.addFragment("in the field, in the forest, in the desert", 1, 0.5)
x.addFragment("with a hat, with a scarf, with a jacket", 1, -0.5)
#x.addFragment("normal, poor quality, boring, tedious, interesting, exciting", 3, -0.5)
pos = x.combineFragments(promptexplorer.CombineMethod.SELECT_NUM_DIRECTIONAL, promptexplorer.Direction.POSITIVE)
neg = x.combineFragments(promptexplorer.CombineMethod.SELECT_NUM_DIRECTIONAL, promptexplorer.Direction.NEGATIVE)

print(pos)
print(neg)
syn = synonymiser(pos, 16)
prompt, distance = syn.synonymise()
print(f'Pos: {prompt} k:{distance}')
syn = synonymiser(neg, 4)
prompt, distance = syn.synonymise()
print(f'Neg: {prompt} k:{distance}')

pos = "centered horrific detailed side view profile portrait of the angel of death, Día de los Muertos, red roses, skull makeup, stone wall background, ornamentation, thorns, vines, elegant"
neg = "lacklustre, repetitive, cropped, lowres, deformed, old, childish, cartoonish"
syn = synonymiser(pos, 4)
prompt, distance = syn.synonymise()
print(f'Pos: {prompt} k:{distance}')
syn = synonymiser(neg, 4)
prompt, distance = syn.synonymise()
print(f'Neg: {prompt} k:{distance}')


for i in range(1, 10):
    syn = synonymiser(pos, i)
    prompt, distance = syn.synonymise()
    print(f'TopK: {i} Pos: {prompt} k:{distance}')