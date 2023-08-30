import openai
import os

# validate training file
openai.api_key = os.getenv("OPENAI_API_KEY_STINGRAY")
openai.File.create(
    file=open("D:/Git/StingrayCore/model-training-data-2.jsonl", "rb"),
    purpose='fine-tune',
)

# fine-tune the model
openai.FineTuningJob.create(
    training_file="D:/Git/StingrayCore/model-training-data-2.jsonl",
    model="davinci-002",
)