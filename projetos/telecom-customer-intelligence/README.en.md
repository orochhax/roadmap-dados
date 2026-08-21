# Telecom Customer Intelligence

This mandatory, incremental project covers product analytics, causal inference,
tabular machine learning, data engineering, and MLOps for a telecom scenario.

Project documents: [data card](data_card.md), [backlog](backlog.md), and
[English presentation](docs/presentation-en.md).

The product serves a product manager who needs reliable activation, retention,
churn, support, and revenue metrics, and an operations team that must prioritize
retention actions under limited capacity. The student must start with auditable
SQL and rule-based baselines, then evaluate causal and predictive approaches
without using information from the future.

The project uses the synthetic telecom, customer, plan, ticket, payment, and
incident datasets already available in the repository. Expected work includes
cohort analysis, a pre-specified causal study, logistic regression, tree-based
models, XGBoost or LightGBM, threshold selection based on cost, and a
reproducible feature pipeline. The final release must track experiments with
MLflow, expose a FastAPI contract, run in Docker, monitor data/model behavior,
and demonstrate retraining and rollback.

Success is not defined as beating every baseline. A valid negative result is
acceptable when metrics, assumptions, errors, and business trade-offs are
reported honestly. The README, reports, dashboard, model card, tests, and
English presentation must all reconcile with generated artifacts.

This file must be updated with actual commands and results before publication.
