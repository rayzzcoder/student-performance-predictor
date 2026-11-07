study_hours = 5

def predict_performance(hours):
    if hours >= 4:
        return "Likely to pass"
    else:
        return "Needs more preparation"

result = predict_performance(study_hours)

print("Prediction:", result)