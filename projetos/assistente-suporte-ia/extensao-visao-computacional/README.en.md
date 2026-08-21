# Mandatory extension — Visual field triage

This extension adds a separate computer-vision capability to the existing
support assistant. Text questions continue to use the evaluated RAG pipeline,
while field images are handled by a PyTorch model. The interface must not imply
that these independent components form a single multimodal model.

Project documents: [data card](data_card.md), [backlog](backlog.md), and
[English presentation](docs/presentation-en.md).

The primary user is a field-maintenance supervisor who needs to prioritize
images with possible cable or equipment defects. The system may recommend an
urgent queue, a normal queue, or human review; it cannot authorize a repair.

The student must document a permitted public image source, freeze a leakage-safe
split, and compare a low-cost visual baseline with compact transfer learning in
PyTorch. Required evaluation includes PR-AUC, defect recall, macro-F1,
confidence behavior, CPU latency, and an error gallery. Tests must cover data
loading, shapes, train-only augmentation, duplicates, reproducibility, model
outputs, and CPU inference.

Publication requires a model card, limitations, a separate CLI or API route,
and honest analysis of false positives and false negatives. Replace this
overview with actual commands and results after completing the exercise.
