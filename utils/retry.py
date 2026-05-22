"""
Tenacity retry decorators for LLM calls.
"""
from tenacity import retry, stop_after_attempt, wait_exponential
import logging

logger = logging.getLogger(__name__)
if not logger.handlers:
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.INFO)

def _log_retry(retry_state):
    logger.info(f"Retrying LLM call, attempt {retry_state.attempt_number}")

def llm_retry():
    """
    Returns a tenacity @retry decorator for LLM calls.
    Retries on any Exception as Groq rate limits inherit from Exception.
    """
    return retry(
        wait=wait_exponential(multiplier=1, min=1, max=8),
        stop=stop_after_attempt(3),
        before_sleep=_log_retry,
        reraise=True
    )
