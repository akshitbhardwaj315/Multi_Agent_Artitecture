import time
from typing import Callable, Any
from utils.logger import get_logger
from utils.telemetry import TelemetryCollector

logger = get_logger(__name__)


def retry_with_backoff(
    fn: Callable,
    telemetry: TelemetryCollector,
    max_retries: int = 3,
    base_delay: float = 1.0
) -> Any:
    last_exception = None
    
    for attempt in range(max_retries):
        try:
            return fn()
        except Exception as e:
            last_exception = e
            telemetry.add_retry()
            logger.warning(
                f"[retry] Attempt {attempt + 1}/{max_retries} failed — "
                f"retrying in {base_delay * (2 ** attempt):.1f}s | error={type(e).__name__}: {str(e)}"
            )
            if attempt < max_retries - 1:
                time.sleep(base_delay * (2 ** attempt))
    
    raise last_exception
