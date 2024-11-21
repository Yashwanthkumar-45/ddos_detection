from flask import Flask, render_template, jsonify
from packet_simulator import simulate_packets
from accuracy_calculator import calculate_accuracy, calculate_precision, calculate_recall, calculate_f1_score

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/simulate')
def simulate():
    detected_labels = []
    true_labels = []
    packet_details = []

    # Simulate traffic
    for _ in range(5):  # Simulate 5 rounds
        packets, entropy_value, predicted_label, true_label = simulate_packets(normal_rate=5, attack_rate=1000, duration=20, attack_start=10)
        detected_labels.append(predicted_label)
        true_labels.append(true_label)
        packet_details.append({
            "packets": len(packets),
            "entropy": entropy_value,
            "predicted_label": predicted_label,
            "actual_label": true_label
        })

    # Calculate metrics
    accuracy = calculate_accuracy(detected_labels, true_labels)
    precision = calculate_precision(detected_labels, true_labels)
    recall = calculate_recall(detected_labels, true_labels)
    f1 = calculate_f1_score(detected_labels, true_labels)

    return jsonify({
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1_score": f1,
        "packet_details": packet_details
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)

