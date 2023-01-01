import promptexplorer
from promptmutator import promptmutator

pos = "centered horrific detailed side view profile portrait of the angel of death, Día de los Muertos, red roses, skull makeup, stone wall background, ornamentation, thorns, vines, elegant"
neg = "lacklustre, repetitive, cropped, lowres, deformed, old, childish, cartoonish"
syn = promptmutator(pos, 4)
prompt, distance = syn.mutate()
#print(f'Pos: {prompt} k:{distance}')
syn = promptmutator(neg, 4)
prompt, distance = syn.mutate()
#print(f'Neg: {prompt} k:{distance}')


#for i in range(1, 1):
#    syn = promptmutator(pos, i)
#    prompt, distance = syn.mutate()
#    print(f'TopK: {i} Pos: {prompt} k:{distance}')

# loop from 4 to 32 stepping by 4 each time
for i in range(4, 68, 4):
    pos = "a painting of a [[cow]] in a [[field]], [[smoking]] a [[pipe]], and wearing a [[blue]] [[jacket]], by [[Zdzisław Beksiński]]"
    mutator = promptmutator(pos, i)
    prompt = mutator.mutate_specific_words()
    print(f'TopK: {i} Pos: {prompt}')
