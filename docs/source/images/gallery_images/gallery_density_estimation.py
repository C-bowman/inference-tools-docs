
from numpy import linspace
from numpy.random import normal, random, exponential
from inference.pdf_tools import UnimodalPdf
import matplotlib.pyplot as plt

N = 5000
s1 = normal(size=N)*0.5 + exponential(size=N)
s2 = normal(size=N)*0.5 + 3*random(size=N) + 2.5

pdf_axis = linspace(-2,7.5,100)
pdf1 = UnimodalPdf(s1)
pdf2 = UnimodalPdf(s2)






fig = plt.figure(figsize = (5,4))
ax = fig.add_subplot(111)
ax.plot(pdf_axis, pdf1(pdf_axis), alpha = 0.2, c = 'C0', lw=2)
ax.fill_between(pdf_axis, pdf1(pdf_axis), alpha = 0.2, color = 'C0')
ax.plot(pdf_axis, pdf2(pdf_axis), alpha = 0.2, c = 'C1', lw=2)
ax.fill_between(pdf_axis, pdf2(pdf_axis), alpha = 0.2, color = 'C1')
ax.set_xticks([])
ax.set_yticks([])
# ax.set_title('Density estimation')
plt.tight_layout()
plt.savefig('gallery_density_estimation.png')
plt.show()