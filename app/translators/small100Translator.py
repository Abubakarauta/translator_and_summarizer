# Load model directly 
# Done and working large language model
import transformers
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("alirezamsh/small100")
model = AutoModelForSeq2SeqLM.from_pretrained("alirezamsh/small100")

hi_text = "जीवन एक चॉकलेट बॉक्स की तरह है।"
chinese_text = "生活就像一盒巧克力。"

# translate Hindi to english
tokenizer.tgt_lang = "en"
encoded_hi = tokenizer(hi_text, return_tensors="pt")
generated_tokens = model.generate(**encoded_hi)
translated_hi_fr = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)

print("Hindi to French Translation:")
print(translated_hi_fr)

# translate Chinese to English
tokenizer.tgt_lang = "en"
encoded_zh = tokenizer(chinese_text, return_tensors="pt")
generated_tokens = model.generate(**encoded_zh)
translated_zh_en = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)

print("Chinese to English Translation:")
print(translated_zh_en)
# Output: Chinese to English Translation: Life is like a box of chocolates.



japanese_text = "人生はチョコレートの箱のようなものです。"

# translate Japanese to English
tokenizer.tgt_lang = "en"
encoded_ja = tokenizer(japanese_text, return_tensors="pt")
generated_tokens = model.generate(**encoded_ja)
translated_ja_en = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)

print("Japanese to English Translation:")
print(translated_ja_en)
# Output: japanese to English Translation: Life is like a box of chocolates.

