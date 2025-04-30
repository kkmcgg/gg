---
tags:
  - Stats
  - Function
---

# Silhouette Score

>> A metric for testing how well a data point fits within a cluster. Its calculated as the distance to the nearest cluster center (b) and the overall mean intra-cluster distance (a), as (b-a)/max(a,b)

## Notes

- can be done in scirkit-learn [https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html]()
- Used in 