"""Checks that the template returns valid forecasts (made-up numbers only)."""

import pytest

from forecaster_template import K_MAX, TemplateForecaster, check_pmf


def test_valid_forecast_with_and_without_history() -> None:
    model = TemplateForecaster()
    check_pmf(model.forecast([28, 30, 27], 0))
    check_pmf(model.forecast([], 0))


def test_elapsed_days_remove_impossible_lengths() -> None:
    model = TemplateForecaster()
    pmf = model.forecast([28, 29, 28], 35)
    check_pmf(pmf, elapsed=35)
    assert pmf[:35].sum() == 0.0
    assert len(pmf) == K_MAX


def test_check_pmf_rejects_bad_input() -> None:
    with pytest.raises(ValueError):
        check_pmf([0.5, 0.5])
