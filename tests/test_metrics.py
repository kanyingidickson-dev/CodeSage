from src.metrics import calculate_accuracy

def test_accuracy():
    preds = ["a", "b", "c"]
    labels = ["a", "b", "d"]
    acc = calculate_accuracy(preds, labels)
    assert acc == 2/3
