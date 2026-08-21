# English thesis presentation template

Target duration: 4–6 minutes. Replace TODOs only with executed evidence.

## Slide 1 — Problem and user

TODO: Introduce the telecom retention manager, the limited contact capacity,
and the decision that must be made.

## Slide 2 — Research question

TODO: State the primary hypothesis and explain why high churn risk is not the
same as a high treatment effect.

## Slide 3 — Data and synthetic boundary

TODO: Describe sources, unit, period, decision time, outcome horizon, and
temporal splits.

TODO: Say explicitly that customer records, campaign assignment, and causal
outcomes are synthetic and cannot establish real operator impact.

## Slide 4 — Baselines and methods

TODO: Present the random policy, business rule, logistic regression, XGBoost,
and one incremental-effect estimator. Explain one methodological trade-off.

## Slide 5 — Evaluation protocol

TODO: Explain fixed eligibility and capacity, predictive metrics, calibration,
uncertainty, incremental gain, policy value, costs, and segment checks.

## Slide 6 — Executed results

TODO: Insert only reproducible results. Include confidence intervals and one
result that did not match the initial expectation.

## Slide 7 — Monitoring and rollback

TODO: Explain the untouched monitoring window, drift checks, experiment/model
versions, retraining trigger, champion/challenger rule, and rollback evidence.

## Slide 8 — Conclusion and limitations

TODO: Answer the research question without claiming real-world causal impact.
State the most important limitation and the next validation required.

## Defense prompts

- Why can a high-risk customer have a low incremental treatment effect?
- Which assumption is required for the causal estimate?
- Why is PR-AUC more useful than accuracy here?
- What would make you keep the baseline?
- What triggers retraining, and what triggers rollback?
- What evidence would be needed before a real campaign?

