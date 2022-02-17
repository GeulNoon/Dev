import torch
from transformers.models.bart import BartForConditionalGeneration
from transformers import PreTrainedTokenizerFast

model = BartForConditionalGeneration.from_pretrained('./kobart_summary')
tokenizer = PreTrainedTokenizerFast.from_pretrained('gogamza/kobart-base-v1')

text = "코로나19 신규 확진자가 나흘째 3천명을 넘어섰다. 위중증 환자도 다시 500명대로 올라섰다. 중앙방역대책본부는 20일 0시 기준으로 신규 확진자가 3212명 늘어났다고 밝혔다. 신규 확진자는 전날(3034명)보다 178명 증가해 지난 17일(3187명) 이후 나흘 연속 3천명을 웃돌았다."

text = text.replace('\n', '')
input_ids = tokenizer.encode(text)
input_ids = torch.tensor(input_ids)
input_ids = input_ids.unsqueeze(0)
output = model.generate(input_ids, eos_token_id=1, max_length=512, num_beams=5)
output = tokenizer.decode(output[0], skip_special_tokens=True)
print(output)
