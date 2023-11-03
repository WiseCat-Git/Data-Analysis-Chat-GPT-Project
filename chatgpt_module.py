from transformers import GPT2LMHeadModel, GPT2Tokenizer

def chat_with_gpt(user_input, chat_history=[]):
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

    input_text = "\n".join(chat_history + [user_input])
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    chat_response = model.generate(input_ids, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2, top_k=50, top_p=0.95, temperature=0.7)

    chat_response_text = tokenizer.decode(chat_response[0], skip_special_tokens=True)
    return chat_response_text