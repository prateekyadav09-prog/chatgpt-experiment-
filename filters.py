"""
filters.py

Filters vacancy listings to keep only relevant Chemistry positions.
"""

from config import (
    TRACKED_SUBJECTS,
    TRACKED_POSITIONS,
    EXCLUDED_KEYWORDS,
)


def normalize(text):
    """
    Convert text to lowercase for case-insensitive matching.
    """
    if text is None:
        return ""

    return str(text).lower().strip()


def contains_subject(text):
    """
    Check whether any tracked Chemistry subject appears in text.
    """
    text = normalize(text)

    return any(subject.lower() in text for subject in TRACKED_SUBJECTS)


def contains_position(text):
    """
    Check whether any tracked position appears in text.
    """
    text = normalize(text)

    return any(position.lower() in text for position in TRACKED_POSITIONS)


def contains_excluded_keyword(text):
    """
    Reject advertisements containing unwanted keywords.
    """
    text = normalize(text)

    return any(keyword.lower() in text for keyword in EXCLUDED_KEYWORDS)


def is_relevant(title, description=""):
    """
    Returns True if the vacancy should be included.
    """

    combined = f"{title} {description}"

    if contains_excluded_keyword(combined):
        return False

    if not contains_position(combined):
        return False

    if not contains_subject(combined):
        return False

    return True