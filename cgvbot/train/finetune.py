from openai import OpenAI

OPENAI_TOKEN = "file-EjdG7jQNdt8zSMiMNQMVzm"
OPENAI_FILE_ID = "xx"
OPENAI_MODEL = "gpt-4.1-nano-2025-04-14"

client = OpenAI(api_key=OPENAI_TOKEN)

ft_job = client.fine_tuning.jobs.create(
  training_file=OPENAI_FILE_ID,
  model=OPENAI_MODEL
)

# Notez absolument le modèle fine-tuné, il sera nécessaire pour l'utilisation du modèle fine-tuné
print("Fine Tune Job has been created with id ", ft_job.id)

