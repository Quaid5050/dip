import numpy as np
import matplotlib.pyplot as plt

# 10x 7 image 
img = np.array([
[0, 6, 5, 4, 6, 6, 0],
[2, 5, 4, 2, 2, 2, 3],
[2, 2, 2, 2, 3, 5, 5],
[0, 4, 3, 5, 4, 4, 0],
[4, 5, 4, 2, 2, 2, 3],
[4, 3, 4, 5, 6, 6, 6],
[0, 4, 5, 5, 3, 4, 0],
[0, 4, 5, 4, 5, 5, 0],
[0, 5, 4, 2, 2, 2, 3],
[3, 3, 3, 3, 4, 5, 5]
])
print("hello")
# Calculate the histogram of the original image
hist, bins = np.histogram(img.flatten(), 255, [0, 255])
# Calculate the cumulative distribution function (CDF)
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max() / cdf.max()

# Calculate the transformation function
transformation = np.round(cdf_normalized).astype(np.uint8)

# Apply the transformation to the image
img_equalized = transformation[img]

# Calculate the histogram of the equalized image
hist_eq, bins_eq = np.histogram(img_equalized.flatten(), 255, [0, 255])

# Plot the histograms
fig, axs = plt.subplots(2, 2, figsize=(10, 10))
axs[0, 0].imshow(img, cmap='gray')
axs[0, 0].set_title('Original Image')
axs[0, 1].hist(img.flatten(), 256, [0, 255], color='b')
axs[0, 1].set_title('Original Histogram')
axs[1, 0].imshow(img_equalized, cmap='gray')
axs[1, 0].set_title('Equalized Image')
axs[1, 1].hist(img_equalized.flatten(), 256, [0, 255], color='b')
axs[1, 1].set_title('Equalized Histogram')

# Show the plot
plt.show()

