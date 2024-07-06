from transformers import pipeline
from transformers import AutoModelForSeq2SeqLM,AutoTokenizer

class PredictPipeline:
    def __init__(self):
        self.model_ckpt = "Govardhan-06/nllb-200-distilled-600M" #Loading the fine-tuned model from hugging face hub
        self.translator = pipeline("translation", model=self.model_ckpt)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_ckpt)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_ckpt)
    
    def predict(self,inputText):
        input_ids = self.tokenizer(inputText, return_tensors="pt").input_ids
        translated_ids = self.model.generate(input_ids=input_ids, num_beams=4, early_stopping=True)
        translated_text = self.tokenizer.decode(translated_ids[0], skip_special_tokens=True)
        return translated_text