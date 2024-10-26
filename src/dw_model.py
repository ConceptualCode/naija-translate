import argparse
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def download_model(model_name, save_dir):
    # Load the tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    # Save the tokenizer and model to the specified directory
    tokenizer.save_pretrained(save_dir)
    model.save_pretrained(save_dir)

    print(f"Model and tokenizer downloaded successfully to '{save_dir}'")
    
if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Download a Hugging Face model to local system.")
    parser.add_argument(
        "--model_name",
        type=str,
        help="The Hugging Face model name/path"
    )
    parser.add_argument(
        "--save_dir",
        type=str,
        default="./model",
        help="Directory to save the model and tokenizer (default: './model')"
    )

    # Parse arguments
    args = parser.parse_args()

    # Download the model
    download_model(args.model_name, args.save_dir)