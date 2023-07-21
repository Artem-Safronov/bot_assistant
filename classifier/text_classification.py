import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def text_classification(text, classifier, vectorizer):
    test_features = vectorizer.transform([text])

    probabilities = classifier.predict_proba(test_features)[0]
    intents = classifier.classes_

    classification_result = list(zip(probabilities, intents))
    sorted_classification_result = sorted(classification_result, reverse=True)

    max_probabilities = sorted_classification_result[0]
    logger.info(f"Final intent and probability: {max_probabilities}")
    final_intent = max_probabilities[1]

    return final_intent
