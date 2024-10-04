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
plt.figure(figsize=(12, 8))

plt.plot(x, ff_active, 'o-', label='FF-Active')
plt.plot(x, vaal, 'o-', label='VAAL')
plt.plot(x, core_set_wsm, 'o-', label='Core set - WSM')
plt.plot(x, core_set_fsm, 'o-', label='Core set - FSM')
plt.plot(x, lc, 'o-', label='LC')
plt.plot(x, hc_lc, 'o-', label='HC+LC')
plt.plot(x, hc, 'o-', label='HC')

plt.title('CIFAR-100 Model Accuracy for VGG-16')
plt.xlabel('Data Fraction')
plt.ylabel('Model Accuracy')
plt.ylim(0, 100)

# Adjust legend
plt.legend(bbox_to_anchor=(0.5, -0.15), loc='upper center', ncol=4)

plt.tight_layout()
plt.show()