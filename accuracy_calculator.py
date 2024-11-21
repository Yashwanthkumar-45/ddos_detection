from sklearn.metrics import precision_score, recall_score, f1_score

def calculate_accuracy(detected_labels, true_labels):
    """
    Calculate the accuracy of attack detection.
    """
    correct_predictions = sum([1 for d, t in zip(detected_labels, true_labels) if d == t])
    accuracy = (correct_predictions / len(true_labels)) * 100
    return accuracy

def calculate_precision(detected_labels, true_labels):
    """
    Calculate precision.
    """
    return precision_score(true_labels, detected_labels, pos_label="attack")

def calculate_recall(detected_labels, true_labels):
    """
    Calculate recall.
    """
    return recall_score(true_labels, detected_labels, pos_label="attack")

def calculate_f1_score(detected_labels, true_labels):
    """
    Calculate F1-Score.
    """
    return f1_score(true_labels, detected_labels, pos_label="attack")
