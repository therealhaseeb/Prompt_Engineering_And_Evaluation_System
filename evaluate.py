import yaml
from llm import run_llm
from nltk.translate.bleu_score import sentence_bleu

REFERENCE = "Refunds are processed within 5 business days."

def load_prompt(path):
    with open(path) as f:
        return yaml.safe_load(f)

def run(prompt_file, user_input):
    data = load_prompt(prompt_file)
    prompt = data["prompt"].format(input=user_input)
    output = run_llm(prompt)
    score = sentence_bleu([REFERENCE.split()], output.split())
    return output, score

if __name__ == "__main__":
    for p in ["prompts/base.yaml", "prompts/v1.yaml"]:
        out, score = run(p, "How do I get a refund?")
        print(f"\n{p}")
        print("Output:", out)
        print("BLEU:", round(score, 3))
