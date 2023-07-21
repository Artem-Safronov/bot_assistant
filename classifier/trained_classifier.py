from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
import yaml


def trained_classifier():
    with open("classifier/training_data.yml") as file:
        data = yaml.safe_load(file)

    x_train = []
    y_train = []
    for intent in data["intents"]:
        for example in intent["examples"].split("\n"):
            train = example.strip(" .,-!?")
            if train:
                x_train.append(train)
                y_train.append(intent["intent"])

    vectorizer = CountVectorizer()
    training_features = vectorizer.fit_transform(x_train)

    classifier = MultinomialNB()
    classifier.fit(training_features, y_train)

    with open("classifier/trained_models/trained_model.pkl", "wb") as file:
        pickle.dump(classifier, file)

    return classifier, vectorizer
