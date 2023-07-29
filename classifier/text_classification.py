import logging
from classifier.extractor import entity_extraction


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def text_classification(text, classifier, vectorizer):
    test_features = vectorizer.transform([text])

    probabilities = classifier.predict_proba(test_features)[0]
    intents = classifier.classes_

    classification_result = list(zip(probabilities, intents))
    sorted_classification_result = sorted(classification_result, reverse=True)

    max_probabilities = sorted_classification_result[0]
    logger.info(f"Max probability and intent: {max_probabilities}")

    entities = await entity_extraction(text)

    if max_probabilities[0] > 0.3:
        final_intent = max_probabilities[1]
    else:
        final_intent = "global"

    return final_intent, entities
