# Contributing to Aadya

Thank you for helping. Small, focused contributions are the easiest to review.

## Ways to help

- **Report a bug** or unclear behaviour using the issue templates.
- **Propose a forecasting method.** Implement the interface in [`forecaster_template.py`](forecaster_template.py), open a pull request, and describe the idea in plain words.
- **Improve documentation** and examples.
- **Review privacy and safety wording.** Careful readers are especially welcome.

## Ground rules

1. **No real people's data.** Never put cycle logs, health records, or anything that could identify someone in an issue, a pull request, or a test. Use made-up numbers.
2. **No medical claims.** Contributions must not diagnose, give contraception or fertility advice, or mark "safe days".
3. **Show uncertainty.** A forecast is a probability distribution over possible cycle lengths, never a single date presented as certain.
4. **Keep it private by design.** Nothing in this project should send a user's data off their device.
5. **Be kind.** See the [Code of Conduct](CODE_OF_CONDUCT.md).

## How submitted methods are evaluated

Maintainers run submitted methods on a fixed evaluation of their own and report aggregate results in the pull request. No raw data is shared in either direction.

## Development

Python 3.10 or newer and NumPy are enough for the template.

```bash
pip install numpy pytest
pytest
```

## Licensing

By contributing you agree that your contribution is licensed under the [Apache License 2.0](LICENSE).
