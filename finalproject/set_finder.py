from skimage import graph
from skimage import data, segmentation, color, filters, io
from matplotlib import pyplot as plt
import os

os.chdir(os.path.dirname(__file__))

filename = "SET+board.jpg"
img = io.imread(filename)
gimg = color.rgb2gray(img)

labels = segmentation.slic(img, compactness=30, n_segments=400, start_label=1)
edges = filters.sobel(gimg)
edges_rgb = color.gray2rgb(edges)

g = graph.rag_boundary(labels, edges)
lc = graph.show_rag(labels, g, edges_rgb, img_cmap=None, edge_cmap='viridis',
                    edge_width=1.2)

plt.colorbar(lc, fraction=0.03)
io.show()
io.show()