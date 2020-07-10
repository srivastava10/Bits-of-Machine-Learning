{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Importing the libraries\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([-10,  -9,  -8,  -7,  -6,  -5,  -4,  -3,  -2,  -1,   0,   1,   2,\n",
       "         3,   4,   5,   6,   7,   8,   9,  10])"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Define the input or testing set or array\n",
    "x = np.array(list(range(-10,11)))\n",
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1.30289758e-09, 3.54164282e-09, 9.62718331e-09, 2.61693975e-08,\n",
       "       7.11357976e-08, 1.93367146e-07, 5.25626399e-07, 1.42880069e-06,\n",
       "       3.88388295e-06, 1.05574884e-05, 2.86982290e-05, 7.80098744e-05,\n",
       "       2.12052824e-04, 5.76419338e-04, 1.56687021e-03, 4.25919483e-03,\n",
       "       1.15776919e-02, 3.14714295e-02, 8.55482149e-02, 2.32544158e-01,\n",
       "       6.32120559e-01])"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Performing softmax activation function\n",
    "\n",
    "s  = np.exp(x)/np.sum(np.exp(x))\n",
    "s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x2231e53e0c8>]"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Plotting the softmax activation function's result\n",
    "plt.plot(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
