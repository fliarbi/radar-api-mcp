from __future__ import annotations

from datetime import datetime, timezone


class RadarError(Exception):
    def __init__(self, kind: str, message: str, status: int = 502, retry_after: int | None = None):
        super().__init__(message)
        self.kind, self.message, self.status, self.retry_after = kind, message, status, retry_after


def envelope(feature: str, data=None, *, error: RadarError | None = None,
             notes: list[str] | None = None, partial: bool = False, window: dict | None = None):
    out = {"ok": error is None, "feature": feature, "data": data,
           "window": window or {"data_through": None},
           "meta": {"retrieved_at": datetime.now(timezone.utc).isoformat(),
                    "partial": partial, "notes": notes or [], "provider": "Fliar BI"}}
    if error:
        out["error"] = {"kind": error.kind, "message": error.message}
        if error.retry_after is not None:
            out["error"]["retry_after"] = error.retry_after
    return out
