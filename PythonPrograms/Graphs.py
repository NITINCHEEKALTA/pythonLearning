import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])

ff_active = np.array([61, 64, 65, 66, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan])
vaal = np.array([34.2, 37.7, 44, 47.6, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan])
core_set_wsm = np.array([30, 45, 52, 59, 59.5, 60, 61, 63, 69, 70])
core_set_fsm = np.array([28, 45, 50, 55, 56, 57, 60, 61, 63, 65])
lc = np.array([np.nan, 51.3, 59.79, 63.93, 66.6, 68.8, 70.33, 71.30, 71.45, 71.42])
hc_lc = np.array([np.nan, 49.62, 58.17, 62.79, 65.65, 67.74, 69.88, 70.30, 70.82, 71.29])
hc = np.array([np.nan, 49.64, 54.22, 57.81, 60.42, 63.4, 65.63, 68.81, 69.78, 71.18])

# Create the plot
plt.figure(figsize=(14, 10))

plt.plot(x, ff_active, 'o-', linewidth=2, markersize=8, label='FF-Active')
plt.plot(x, vaal, 'o-', linewidth=2, markersize=8, label='VAAL')
plt.plot(x, core_set_wsm, 'o-', linewidth=2, markersize=8, label='Core set - WSM')
plt.plot(x, core_set_fsm, 'o-', linewidth=2, markersize=8, label='Core set - FSM')
plt.plot(x, lc, 'o-', linewidth=2, markersize=8, label='LC')
plt.plot(x, hc_lc, 'o-', linewidth=2, markersize=8, label='HC+LC')
plt.plot(x, hc, 'o-', linewidth=2, markersize=8, label='HC')

plt.title('CIFAR-100 Accuracy for VGG-16', fontsize=20, fontweight='bold')
plt.xlabel('Percentage of Data', fontsize=16)
plt.ylabel('Model Accuracy (%)', fontsize=16)

# Adjust axes
plt.ylim(20, 80)
plt.yticks(range(20, 81, 10), fontsize=12)
plt.xlim(0.1, 1.0)
plt.xticks(np.arange(0.1, 1.1, 0.1), fontsize=12)

# Adjust legend
plt.legend(bbox_to_anchor=(0.5, -0.15), loc='upper center', ncol=4, fontsize=14, frameon=True, facecolor='white', edgecolor='black')

plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()