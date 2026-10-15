"""
Task 1: Pretrained Transformer inference on five sample sentences.
Model: DistilBERT fine-tuned for binary sentiment analysis.
"""
from transformers import pipeline

def main():
    classifier = pipeline(
        task="sentiment-analysis",
        model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
    )

    samples = [
        "I absolutely loved this movie. It was wonderful!",
        "This is the worst experience I have ever had.",
        "The food was delicious and the staff were friendly.",
        "I am disappointed with the poor service.",
        "The story was interesting and I enjoyed every minute.",
    ]

    print("Pretrained Transformer: Sentiment Analysis")
    print("-" * 55)
    for number, sentence in enumerate(samples, start=1):
        result = classifier(sentence)[0]
        print(f"Example {number}")
        print(f"Input:      {sentence}")
        print(f"Prediction: {result['label']}")
        print(f"Score:      {result['score']:.4f}")
        print("-" * 55)

if __name__ == "__main__":
    main()
