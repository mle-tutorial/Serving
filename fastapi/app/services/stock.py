from typing import List

import numpy as np
from app.repository.model_registry import load_rf_model


def predict_stock_ts(model_name: str, ts: List[float]) -> float:
    ts = np.array(ts).reshape(1, -1)
    model = load_rf_model(model_name)
    pred_result = model.predict(ts)

    return pred_result
