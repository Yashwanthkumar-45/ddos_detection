import random
import time
from entropy_calculator import calculate_entropy
import logging

logging.basicConfig(filename='simulation.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

ATTACK_ENTROPY_THRESHOLD = 0.013  # Adjust based on experiments

def simulate_packets(normal_rate=5, attack_rate=1000, duration=20, attack_start=10, burst_factor=2):
    packet_timestamps = []
    start_time = time.time()
    label = "normal"

    while time.time() - start_time < duration:
        current_time = time.time() - start_time
        if current_time < attack_start:
            rate = normal_rate
            label = "normal"
        else:
            rate = random.randint(attack_rate, attack_rate * burst_factor)
            label = "attack"

        for _ in range(rate):
            packet_timestamps.append(time.time())

        time.sleep(1)

    entropy_value = calculate_entropy(packet_timestamps)
    predicted_label = "attack" if entropy_value > ATTACK_ENTROPY_THRESHOLD else "normal"

    logging.info(f"Simulated {len(packet_timestamps)} packets. Entropy: {entropy_value:.4f}")
    logging.info(f"Predicted: {predicted_label}, Actual: {label}")

    return packet_timestamps, entropy_value, predicted_label, label
