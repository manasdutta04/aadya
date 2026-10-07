<p align="center">
  <img src="assets/banner.png" alt="aadya-m1" width="100%">
</p>

<p align="center">
  <a href="https://huggingface.co/manasdutta04/aadya-m1"><img src="https://img.shields.io/badge/Model-Hugging%20Face-e85d4c" alt="Model on Hugging Face"></a>
  <a href="https://huggingface.co/spaces/manasdutta04/aadya-m1-try"><img src="https://img.shields.io/badge/Live%20demo-Space-15202b" alt="Live demo"></a>
  <img src="https://img.shields.io/badge/License-Apache--2.0-2b6cb0" alt="Apache-2.0">
  <img src="https://img.shields.io/badge/Runs-on%20device-9aa5b1" alt="Runs on device">
</p>

# Aadya

Open, privacy-first forecasting of when the next period is likely to start, expressed as a probability distribution instead of a single date.

*Aadya* (आद्या) is Sanskrit for “the first” or “the beginning”, a fitting name for a model that forecasts the start of a cycle, whose day one is the first day of bleeding.

- **Models:** [aadya-m1](https://huggingface.co/manasdutta04/aadya-m1) (256M parameters, full capacity) and [aadya-m1-mini](https://huggingface.co/manasdutta04/aadya-m1-mini) (0.84M parameters, 3.4 MB, for phones and low-power devices). Same API.
- **Live demos:** [aadya-m1](https://huggingface.co/spaces/manasdutta04/aadya-m1-try) and [aadya-m1-mini](https://huggingface.co/spaces/manasdutta04/aadya-m1-mini-try)
- **This repository** is for the community: bug reports, ideas, and new forecasting methods that follow the interface in [`forecaster_template.py`](forecaster_template.py).

Not a medical device. It does not diagnose, and it makes no contraception or fertility claims.

## Try it in your browser

Run the model in Google Colab, build a fresh test dataset, and check the scores, calibration, missed logs, the optional ovulation-test input and edge cases, with plain matplotlib and pandas charts. No setup, nothing to install.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/manasdutta04/aadya/blob/main/notebooks/aadya_m1_playground.ipynb)

## How it performs

Mean error (lower is better) on the public boards: simulated users (539), and 364 real users from two public cohorts (251 Creighton, scored cross-fitted, and 113 Marquette). aadya-m1 is first on mean error on all of them. On the pooled real users its lead over the classical Bayesian reference is small (about 1% lower error) but clear; on each small cohort alone it is within noise. On an unseen simulated generator the lead over the strongest methods disappears; it stays clearly ahead of simple heuristics. The numbers behind each chart are in the [model repo](https://huggingface.co/manasdutta04/aadya-m1/tree/main/benchmarks).

![Mean error on the three boards](assets/fig_benchmarks.png)

![Error removed compared with the usual tracker method](assets/fig_error_removed.png)

It outputs a probability for every possible cycle length, so an app can show a window instead of one date:

![Example forecasts](assets/fig_forecast.png)

Full tables, method and caveats are on the [model card](https://huggingface.co/manasdutta04/aadya-m1).

## Which model should I use?

| | aadya-m1 | aadya-m1-mini |
|---|---|---|
| Parameters | 256M | 0.84M |
| Weights | about 1 GB | 3.4 MB |
| Best for | servers, desktops, research, fine-tuning | phones, browsers, low-power devices |
| Mean error on 364 public real users (lower is better) | 1.930 | 1.932 (level) |

Both are measured the same way. On the real data we have, the small model matches the large one, so choosing it costs nothing in accuracy there; the difference is size and capacity.

## Contribute

Read [CONTRIBUTING.md](CONTRIBUTING.md). In short: keep real people's data out of issues and pull requests, show uncertainty, and keep changes small and focused.

## License

[Apache-2.0](LICENSE)
