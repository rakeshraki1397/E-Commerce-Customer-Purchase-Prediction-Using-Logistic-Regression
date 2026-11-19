import joblib

file_path = "model.joblib"

model = joblib.load(file_path)

print("=" * 50)
print("MODEL INFORMATION")
print("=" * 50)

print("Model type:", type(model))
print("\nModel structure:")
print(model)

if hasattr(model, "get_params"):
    print("\nModel parameters:")
    print(model.get_params())

if hasattr(model, "feature_names_in_"):
    print("\nInput features:")
    print(model.feature_names_in_)

if hasattr(model, "classes_"):
    print("\nOutput classes:")
    print(model.classes_)