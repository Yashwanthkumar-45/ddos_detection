#entropy_calculator.py
import math
from collections import Counter

def calculate_entropy(timestamps):
    """
    Calculate the Shannon entropy for packet arrival intervals (time differences between packets).
    """
    # Calculate the intervals (time differences) between consecutive packets
    time_deltas = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps) - 1)]
    
    # Count the frequency of each delta
    delta_counts = Counter(time_deltas)
    
    # Calculate the total number of intervals
    total_intervals = len(time_deltas)
    
    # Calculate entropy using Shannon formula
    entropy = -sum((count / total_intervals) * math.log(count / total_intervals, 2) for count in delta_counts.values())
    
    return entropy
