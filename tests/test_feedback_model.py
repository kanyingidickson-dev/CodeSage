from src.feedback_model import FeedbackModel

def test_model_predict():
    model = FeedbackModel()
    feedback = model.predict("def foo(): pass")
    assert isinstance(feedback, str)
    assert len(feedback) > 0
