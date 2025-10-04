Contributing — architecture notes
================================

Core principles
- Keep adapters isolated: each external provider (TEMPO, PurpleAir, NOAA) should implement a common interface and live under `backend/app/adapters/`.
- Forecasting engine lives under `backend/app/forecast/` and exposes a simple function `predict(features) -> (predictions, intervals)`.
- Frontend consumes the backend via a small REST surface: `/api/airquality` and `/api/forecast`.

Quick adapter template

```python
class ProviderAdapter:
    def fetch_observations(self, **kwargs):
        raise NotImplementedError

    def normalize(self, raw):
        # return normalized schema
        pass
```
