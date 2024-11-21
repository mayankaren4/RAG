from typing import Any
from sklearn.feature_extraction.text import TfidfVectorizer

# Simulated embedding generator (using TF-IDF Vectorizer)
vectorizer = TfidfVectorizer(stop_words='english')


# Default response appended to each API to highlight the application name, version.
API_DEFAULT_TAG: dict[str, str] = {
    "application_name": "Retrieval Augmented System",
    "application_version": "v0.1.0",
    "api_version": "v1",
}

# Add the default api tag to the api response
def add_application_tag(api_response: Any) -> dict:
    """
    Adds the application tag to all the api response

    Args:
        api_response (any): the api response in which the tag should be added

    Returns:
        dict: the api response along with the application tag
    """
    result: dict = API_DEFAULT_TAG
    result.update({"response": api_response})
    return result
