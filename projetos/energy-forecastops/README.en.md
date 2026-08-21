# Energy ForecastOps

Energy ForecastOps is a mandatory time-series project for operational capacity
planning. Its primary user is an operations manager who must reserve capacity
while balancing the asymmetric costs of under- and over-forecasting.

Project documents: [data card](data_card.md), [backlog](backlog.md), and
[English presentation](docs/presentation-en.md).

The project uses the repository's synthetic daily energy dataset. The student
must freeze forecast horizons, rolling-origin folds, metrics, and the decision
rule before comparing models. Required baselines are the latest observation, a
seven-day seasonal naive forecast, and a past-only moving average. Candidate
approaches include ETS or SARIMA, regression with calendar and lag features,
and gradient boosting.

Evaluation must report MAE, RMSE, sMAPE, interval coverage, and an operational
cost metric for each horizon and fold. Random splits and features derived from
future observations are prohibited. Tests must verify date continuity, lag
construction, temporal folds, metric calculations, and reproducibility.

The final recommendation may keep the seasonal baseline. Model complexity is
not evidence of improvement; stability across time, decision cost, and honest
limitations are required.

Replace this overview with actual commands, results, and limitations before
publication.
