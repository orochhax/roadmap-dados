# Entity Matching Lab

Entity Matching Lab is a mandatory NLP, retrieval, and ranking project for
reconciling noisy company records with a canonical database. Its primary users
are master-data, CRM, and commercial operations teams. A false match can be
more damaging than sending an ambiguous record to human review, so the system
must support abstention.

Project documents: [data card](data_card.md), [backlog](backlog.md), and
[English presentation](docs/presentation-en.md).

The student will create a deterministic labeled dataset containing company
names, aliases, domains, countries, spelling errors, abbreviations, lookalikes,
missing values, accents, and multilingual examples. Entity-level splits are
required to prevent variants of the same company from leaking across train and
test data.

Required baselines include normalized domain matching, normalized exact-name
matching, and fuzzy matching. Candidate methods include character TF-IDF,
blocking, embeddings, and a simple supervised ranker. Evaluation separates
candidate generation from ranking and reports pair precision/recall/F1,
recall@K, MRR, candidate reduction, latency, cost, and error slices.

Embeddings must be compared with lower-cost methods. The final recommendation
must define confidence thresholds and a human-review policy instead of forcing
every record to match.

Replace this overview with actual commands and results before publication.
