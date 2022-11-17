import sathprompt

x = sathprompt.promptFragments()
x.addFragment("1920's haunted Massachusetts mansion, vintage portrait of a retired admiral, shadow lurking in a hedge maze, abandoned mental asylum, a lonely night in Arkham Massachusetts, vintage photo of a portal to the beyond, cursed painting that is alive, portrait of the last surviving sailor, hidden temple in the basement", 3, 0.7, 0.2)
x.addFragment("by artgerm, by beeple, by zdzislaw beksinski", 1, 0.3, 0.2)
print(x.combineFragments(sathprompt.CombineMethod.SELECT_NUM_WITH_RAND_WEIGHT))