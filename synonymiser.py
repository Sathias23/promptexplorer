import torch
import gc
import warnings
import clip
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

class synonymiser:
    def __init__(self, prompt:str, topk:int):
        self.prompt = prompt
        self.topk = topk
        self.stripcommas = False
        
    def asIs(self):
        return self.prompt

    def synonymise(self):
        target_tokens = tokenizer.encode(self.prompt)
        new_prompt = ""
        for now_token in target_tokens:
            target_emb = perceptor.token_embedding.weight[now_token,None].detach()
            token_sim  = torch.cosine_similarity(target_emb,perceptor.token_embedding.weight.detach(),-1)
            top_token_sim = torch.topk(token_sim,self.topk+1,-1,True,True)
            top_indices = top_token_sim.indices[1:]
            top_values  = top_token_sim.values[1:]
            output = []
            for i in range(top_indices.shape[0]):
                output.append([tokenizer.decode([top_indices[i].item()]), top_values[i].item()]) 
            new_token = sample(output, len(output))[0][0]
            new_prompt += new_token
        # strip any commas from new_prompt
        if self.stripcommas:
            new_prompt = new_prompt.replace(", ","")
        return new_prompt

