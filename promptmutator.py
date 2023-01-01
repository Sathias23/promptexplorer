import torch
import gc
import warnings
import clip
import re
from IPython.display import HTML, display
from random import sample
warnings.filterwarnings('ignore')
torch.set_grad_enabled(False)

def clear_mem():
    torch.cuda.empty_cache()
    gc.collect()

torch.set_grad_enabled(False)

perceptor, clip_preprocess = clip.load('ViT-B/16')
#perceptor, clip_preprocess = clip.load('ViT-B/32')
perceptor.eval().float().requires_grad_(False);

tokenizer = clip.simple_tokenizer.SimpleTokenizer()

class promptmutator:
    def __init__(self, prompt:str, topk:int):
        self.prompt = prompt
        self.topk = topk
        self.stripcommas = False
        
    def asIs(self):
        return self.prompt

    def mutate_word(self, word):
        target_tokens = tokenizer.encode(word)
        new_word = ""
        num_word = 0
        total_index = 0
        for now_token in target_tokens:
            target_emb = perceptor.token_embedding.weight[now_token,None].detach()
            token_sim  = torch.cosine_similarity(target_emb,perceptor.token_embedding.weight.detach(),-1)
            top_token_sim = torch.topk(token_sim,self.topk+1,-1,True,True)
            top_indices = top_token_sim.indices[1:]
            top_values  = top_token_sim.values[1:]
            output = []
            for i in range(top_indices.shape[0]):
                output.append([tokenizer.decode([top_indices[i].item()]), top_values[i].item()]) 
            shuffle_output = sample(output, len(output))
            new_token = shuffle_output[0][0]
            new_index = shuffle_output[0][1]
            new_word += new_token
            total_index += new_index
            num_word += 1
        total_index = total_index / num_word
        # strip any unicode characters from new_word
        new_word = new_word.encode('ascii', 'ignore').decode('ascii')
        # strip any commas from new_word
        if self.stripcommas:
            new_word = new_word.replace(", ","")
        return new_word, total_index

    def mutate(self):
        return self.mutate_word(self.prompt)

    def mutate_specific_words(self):
        # find all instances of words in the prompt enclosed in double square-brackets
        # e.g. picture of [[cow]] riding a [[bike]]
        # will find a list of the strings '[[cow]]' and '[[bike]]'
        list_squared_brackets = re.findall(r'\[\[.*?\]\]', self.prompt)
        # mutate each word in the list of words
        for word in list_squared_brackets:
            # remove the double square-brackets
            word = word[2:-2]
            # mutate the word
            new_word, distance = self.mutate_word(word)
            #trim new_word
            new_word = new_word.strip()
            # replace the word in the prompt with the mutated word
            self.prompt = self.prompt.replace(f'[[{word}]]', f'{new_word}')
        return self.prompt

        

