import river.anomaly
import random
model = river.anomaly.HalfSpaceTrees()

for _ in range(100):
    data= { "feature": random.random()}
    score = model.score_one(data)
    model.learn_one(data)
    if score > 0.8:
        print(f'Anomaly detected: { data["feature"]}')