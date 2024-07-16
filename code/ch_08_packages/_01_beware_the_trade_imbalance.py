import statistics as stats
import sys
from os import path
from statistics import median, mean

# noinspection PyProtectedMember
from ch_06_packages._01_beware_the_trade_imbalance_support import mode

print(f"Current version: {sys.version_info.major}")
print(path.abspath('.'))
print(stats.median([1, 1, 1, 5, 8, 9, 100]))
print(median([1, 1, 1, 5, 8, 9, 100]))
print(mean([1, 1, 1, 5, 8, 9, 100]))
print(mode([42, 7, 7, 1]))
