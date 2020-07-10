{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Importing Libraries\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([-5, -4, -3, -2, -1,  0,  1,  2,  3,  4,  5])"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Declaring the testing set\n",
    "x = np.array(list(range(-5,6)))\n",
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([-0.9999092 , -0.9993293 , -0.99505475, -0.96402758, -0.76159416,\n",
       "        0.        ,  0.76159416,  0.96402758,  0.99505475,  0.9993293 ,\n",
       "        0.9999092 ])"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Defining the tanh function\n",
    "tanh_array = (np.exp(x)-np.exp(-x))/(np.exp(x)+(np.exp(-x)))\n",
    "tanh_array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x2bbc9a7e448>]"
      ]
     },
     "execution_count": 6,
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
    "# Plotting the final output after the tanh function\n",
    "plt.plot(tanh_array)"
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
