# Load model directly
# DONE and working perfectly
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("Falconsai/text_summarization")
model = AutoModelForSeq2SeqLM.from_pretrained("Falconsai/text_summarization")


context = """" India wicket-keeper batsman Rishabh Pant has said
someone from the crowd threw a ball on pacer Mohammed Siraj while he 
was fielding in the ongoing third Test against England on Wednesday. 
Pant revealed the incident made India skipper Virat Kohli "upset". "I think, 
somebody threw a ball inside, at Siraj, so he [Kohli] was upset," said Pant in a 
virtual press conference after the close of the first day's play."You can say whatever you want to chant, 
but don't throw things at the fielders and all those things. It is not good for cricket, I guess," he added.
In the third session of the opening day of the third Test, a section of spectators seemed to have asked Siraj 
the score of the match to tease the pacer. The India pacer however came with a brilliant reply as he gestured 1-0
(India leading the Test series) towards the crowd.Earlier this month, during the second Test match, there was some 
bad crowd behaviour on a show as some unruly fans threw champagne corks at India batsman KL Rahul.Kohli also intervened 
and he was seen gesturing towards the opening batsman to know more about the incident. An over later, the TV visuals
showed that many champagne corks were thrown inside the playing field, and the Indian players were visibly left frustrated.
Coming back to the game, after bundling out India for 78, openers Rory Burns and Haseeb Hameed ensured that England took 
the honours on the opening day of the ongoing third Test.At stumps, England's score reads 120/0 and the hosts have extended 
their lead to 42 runs. For the Three Lions, Burns (52*) and Hameed (60*) are currently unbeaten at the crease.Talking about 
the pitch on opening day, Pant said, "They took the heavy roller, the wicket was much more settled down, and they batted
nicely also," he said. "But when we batted, the wicket was slightly soft, and they bowled in good areas, but 
we could have applied [ourselves] much better."Both England batsmen managed to see off the final session and 
the hosts concluded the opening 
day with all ten wickets intact, extending the lead to 42.(ANI) """

def get_response(input_text):
  batch = tokenizer([input_text],truncation=True,padding='longest',max_length=1024, return_tensors="pt")
  gen_out = model.generate(**batch,max_length=128,num_beams=5, num_return_sequences=1, temperature=1.5)
  output_text = tokenizer.batch_decode(gen_out, skip_special_tokens=True)
  print(output_text)
  return output_text

get_response(context)
