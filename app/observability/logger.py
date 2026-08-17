import logging
import time
import uuid
import inspect
from functools import wraps


logger = logging.getLogger("enterprise_ai")


def create_request_id() -> str:
    return str(uuid.uuid4())

def log_node_start(
    request_id: str,
    node: str,
):
    logger.info(
        "request_id=%s node=%s status=start",
        request_id,
        node,
    )


def log_node_end(
        request_id: str,
        node: str,
        start_time: float,
):
    latency = time.perf_counter() - start_time

    logger.info(
        "request_id=%s, node=%s status=complete latency=%.3fs",
        request_id,
        node,
        latency,
    )


def log_error(
        request_id: str,
        node: str,
        error: Exception,
):
    logger.info(
        "request_id=%s node=%s status=error error=%s",
        request_id,
        node,
        error,
    )


def observe_node(node_name: str):

    def decorator(func):

        if inspect.iscoroutinefunction(func):

            @wraps(func)
            async def async_wrapper(state, *args, **kwargs):

                request_id = state.get(
                    "request_id",
                    "unknown",
                )

                start_time = time.perf_counter()

                log_node_start(
                    request_id,
                    node_name,
                )

                try:

                    result = await func(
                        state,
                        *args,
                        **kwargs,
                    )

                    log_node_end(
                        request_id,
                        node_name,
                        start_time,
                    )

                    return result

                except Exception as error:

                    log_error(
                        request_id,
                        node_name,
                        error,
                    )

                    raise

            return async_wrapper

        @wraps(func)
        def sync_wrapper(state, *args, **kwargs):

            request_id = state.get(
                "request_id",
                "unknown",
            )

            start_time = time.perf_counter()

            log_node_start(
                request_id,
                node_name,
            )

            try:

                result = func(
                    state,
                    *args,
                    **kwargs,
                )

                log_node_end(
                    request_id,
                    node_name,
                    start_time,
                )

                return result

            except Exception as error:

                log_error(
                    request_id,
                    node_name,
                    error,
                )

                raise

        return sync_wrapper

    return decorator