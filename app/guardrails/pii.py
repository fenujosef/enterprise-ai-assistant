from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine


analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()


def redact_pii(text: str) -> str:

    results = analyzer.analyze(
        text=text,
        language="en",
    )

    anonymized = anonymizer.anonymize(
        text=text,
        analyzer_results=results,
    )

    return anonymized.text

# Update the changes in this function
def redact_input_pii(text: str) -> str:
    return redact_pii(text)