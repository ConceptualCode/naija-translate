import argparse
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

def translate_text(model_name, source_lang, target_lang, text):
    model = M2M100ForConditionalGeneration.from_pretrained(model_name)
    tokenizer = M2M100Tokenizer.from_pretrained(model_name)

    tokenizer.src_lang = source_lang
    tokenizer.tgt_lang = target_lang

    encoded_text = tokenizer(text, return_tensors="pt")

    generated_tokens = model.generate(
        **encoded_text,
        forced_bos_token_id=tokenizer.get_lang_id(target_lang)
    )

    translated_text = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    
    return translated_text[0]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Translate English text to a specified language.")
    parser.add_argument(
        "--model_name",
        type=str,
        default="model",
        help="Name or path of the model"
    )
    parser.add_argument(
        "--source_lang",
        type=str,
        default="en",
        help="Source language code (default: 'en' for English)"
    )
    parser.add_argument(
        "--target_lang",
        type=str,
        required=True,
        help="Target language code (e.g., 'ig' for Igbo, 'yo' for Yoruba, 'ha' for Hausa)"
    )
    parser.add_argument(
        "--text",
        type=str,
        required=True,
        help="Text to be translated"
    )

    args = parser.parse_args()

    translation = translate_text(args.model_name, args.source_lang, args.target_lang, args.text)
    
    print(f"Translated text ({args.target_lang}): {translation}")