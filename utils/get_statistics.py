import math
import statistics
from schemas.image import ImageStatistics
from utils.csv_handler import get_list_values_count


def get_statistics(sizes):
    max_particle_size = max(sizes)
    min_particle_size = min(sizes)
    mean = statistics.mean(sizes)
    mean = math.ceil(mean * 100) / 100
    median = statistics.median(sizes)
    amount = len(sizes)
    sizes = get_list_values_count(sizes)
    return ImageStatistics(amount=amount, maxSize=max_particle_size, minSize=min_particle_size,
                           sizes=sizes, mean=mean, median=median)
