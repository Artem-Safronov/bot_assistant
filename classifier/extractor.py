from natasha import Doc, Segmenter, NewsEmbedding, NewsMorphTagger, NewsSyntaxParser, NewsNERTagger
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def entity_extraction(text):
    segmenter = Segmenter()
    emb = NewsEmbedding()
    morph_tagger = NewsMorphTagger(emb)
    syntax_parser = NewsSyntaxParser(emb)
    ner_tagger = NewsNERTagger(emb)

    text = text.title()

    doc = Doc(text)
    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)
    doc.parse_syntax(syntax_parser)
    doc.tag_ner(ner_tagger)

    entities = dict()
    for span in doc.spans:
        entities[span.type] = span.text

    logger.info(f"Extracted entities: {entities}")

    return entities
