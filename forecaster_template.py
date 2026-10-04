"""Template for a community forecaster.

A forecaster predicts the length of the next cycle (days between period starts) as a
probability distribution over 1..120 days, given the person's past cycle lengths and the
number of days elapsed since the last period started.

Copy this file, rename the class, and replace the body of ``forecast``. Use made-up numbers
when testing; never real people's data.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

import numpy as np

K_MAX = 120  # pmf[k - 1] is the probability that the next cycle is k days long


class TemplateForecaster:
    name = "template-rolling-median"
    version = "0.1.0"

    def fit(self, train: Sequence[Any], calib: Sequence[Any]) -> None:
        """Optional: learn from example sequences. This template learns nothing."""

    def forecast(self, past_lengths: Sequence[int], elapsed: int, cohort: Any = None) -> np.ndarray:
        """Return a probability for each cycle length, conditional on length > elapsed."""
        recent = list(past_lengths)[-3:]
        centre = float(np.median(recent)) if recent else 28.0
        days = np.arange(1, K_MAX + 1)
        pmf = np.exp(-0.5 * ((days - centre) / 3.0) ** 2)
        pmf[:elapsed] = 0.0  # a cycle already `elapsed` days long cannot be shorter
        if pmf.sum() <= 0:
            pmf[min(elapsed, K_MAX - 1)] = 1.0
        return pmf / pmf.sum()


def check_pmf(pmf: np.ndarray, elapsed: int = 0) -> None:
    """Raise ValueError if ``pmf`` is not a valid forecast."""
    pmf = np.asarray(pmf, dtype=float)
    if pmf.shape != (K_MAX,):
        raise ValueError(f"expected {K_MAX} probabilities, got shape {pmf.shape}")
    if not np.all(np.isfinite(pmf)) or np.any(pmf < 0):
        raise ValueError("probabilities must be finite and non-negative")
    if abs(float(pmf.sum()) - 1.0) > 1e-9:
        raise ValueError("probabilities must sum to 1")
    if elapsed > 0 and np.any(pmf[:elapsed] > 0):
        raise ValueError("no probability allowed on cycle lengths <= elapsed days")
