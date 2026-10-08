"""Locale-aware number parsing. All results are Decimal, never float."""
from __future__ import annotations

import re
from decimal import Decimal, InvalidOperation

PT_BR = "pt-BR"
EN_US = "en-US"

_NOISE = re.compile(r"R\$|BRL|\s| ")
_VALID = re.compile(r"^[0-9.,]+$")


class NumberParseError(ValueError):
    pass


class AmbiguousNumberError(NumberParseError):
    """Raised when a separator could be decimal or thousands and no locale hint is given."""


def parse_decimal(value, locale: str | None = None) -> Decimal:
    """Parse '1.234,56', 'R$ 1.234,56', '1,234.56', '(10,00)', '-5' into Decimal.

    `locale` is "pt-BR" or "en-US". With no hint, a lone separator followed by exactly
    three digits (e.g. '1.200', '1,500') is ambiguous and raises AmbiguousNumberError.
    Floats and ints from spreadsheets are converted through repr so no binary noise leaks in.
    """
    if value is None:
        raise NumberParseError("empty value")
    if isinstance(value, Decimal):
        return value
    if isinstance(value, bool):
        raise NumberParseError("boolean is not a number")
    if isinstance(value, int):
        return Decimal(value)
    if isinstance(value, float):
        return Decimal(repr(value))

    text = _NOISE.sub("", str(value))
    if not text:
        raise NumberParseError("empty value")

    negative = False
    if text.startswith("(") and text.endswith(")"):
        negative, text = True, text[1:-1]
    if text.startswith("-"):
        negative, text = not negative, text[1:]
    if text.endswith("-"):
        negative, text = not negative, text[:-1]
    if not text or not _VALID.match(text):
        raise NumberParseError(f"not a number: {value!r}")

    dec, thou = _separators(text, locale)
    if thou:
        text = text.replace(thou, "")
    if dec and dec != ".":
        text = text.replace(dec, ".")
    if text.count(".") > 1:
        raise NumberParseError(f"malformed number: {value!r}")
    try:
        result = Decimal(text)
    except InvalidOperation as exc:
        raise NumberParseError(f"not a number: {value!r}") from exc
    return -result if negative else result


def _separators(text: str, locale: str | None) -> tuple[str | None, str | None]:
    """Return (decimal_separator, thousands_separator) for a cleaned numeric string."""
    has_dot, has_comma = "." in text, "," in text
    if has_dot and has_comma:
        # The separator that appears last is the decimal one.
        return (",", ".") if text.rfind(",") > text.rfind(".") else (".", ",")
    if not has_dot and not has_comma:
        return None, None
    sep = "." if has_dot else ","
    other = "," if has_dot else "."
    parts = text.split(sep)
    if len(parts) > 2:  # '1.234.567' -> must be thousands
        return None, sep
    after = parts[1]
    if locale == PT_BR:
        return (",", None) if sep == "," else (None, ".")
    if locale == EN_US:
        return (".", None) if sep == "." else (None, ",")
    if len(after) != 3:
        return sep, None  # '12,5' / '9.35' -> decimal
    raise AmbiguousNumberError(f"ambiguous separator in {text!r}; pass locale='pt-BR' or 'en-US'")
