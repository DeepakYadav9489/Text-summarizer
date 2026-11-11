from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
import re
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

# initialize fastapi app
app = FastAPI(title="Text Summarize App", description="Text summarization using T5", version="1.0")

# model and tokenizer
model = T5ForConditionalGeneration.from_pretrained("./saved_summary_model")
tokenizer = T5Tokenizer.from_pretrained("./saved_summary_model")

# device setup
if torch.cuda.is_available():
    device = torch.device("cuda")
elif torch.backends.mps.is_available():
    device = torch.device("mps")
else:
    device = torch.device("cpu")

model.to(device)

# templating
templates = Jinja2Templates(directory=".") # ui where does existed

# input schema for dialogue => string
class DialogueInput(BaseModel):
    dialogue:str


def clean_text(text):
    text = re.sub(r"\r\n", " ", text) # line
    text = re.sub(r"\s+", " ", text) # space
    text = re.sub(r"<.*?>", " ", text) # html
    text = text.strip().lower()
    return text

def summarize_dialogue(dialogue):
  # clean
  dialogue  = clean_text(dialogue)

  # tokenize
  inputs = tokenizer(
      dialogue,
      max_length=512,
      padding="max_length",
      truncation=True,
      return_tensors="pt"
  )

  # generate the summary => token ids
  targets = model.generate(
      input_ids=inputs["input_ids"],
      attention_mask=inputs["attention_mask"],
      max_length=150,
      num_beams=4,
      early_stopping=True
  )

  # tokens ids convert summary => decoding output
  summary = tokenizer.decode(targets[0], skip_special_tokens=True)
  return summary

# API endpoints
@app.post("/summarize/")
async def summarize(dialogue_input: DialogueInput):
    summary = summarize_dialogue(dialogue_input.dialogue)
    return {"summary":summary}


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse( request=request, name="index.html")





