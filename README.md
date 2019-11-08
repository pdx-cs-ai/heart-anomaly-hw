# Heart Anomaly Homework Data
Bart Massey

This file contains the instance data and
[writeup](heart.pdf) for the heart anomaly homework given in
my Intro AI class, together with the writeup and the
[original paper](spect.pdf) describing the dataset.

* `heart.pdf`: Assignment writeup

* `spect.pdf`: Original paper

* `spect-orig.*.csv`: Binarized training and test data from
  the original paper. The dependent variable is in the first
  column.

* `spect-resplit.*.csv`: Original binarized data resplit
  proportionally to prevalence *in the sample.* Not clear
  that this is the same as prevalence in the population.
  Training / test instances are split 2::1.

* `spect-itg.*.csv`: Features and class are taken from the
  continuous version of the original data, and binarized for
  maximized information-theoretic gain.  Same training and
  test instances as original. Both the training and test
  instances are used in the binarization, which perhaps
  improves it unfairly.

* `spect-resplit-itg.*.csv`: Features and class are taken
  from the continuous version of the original data, and
  binarized for maximized information-theoretic
  gain. Resplit as above.

The original resources are also available:

* [SPECT](https://archive.ics.uci.edu/ml/datasets/SPECT+Heart):
  Binarized data from the original paper. This repo contains
  a copy of the data.
  
* [SPECTF](https://archive.ics.uci.edu/ml/datasets/SPECTF+Heart):
  Continuous version of the data from the original paper.
  This repo contains a copy of the data.

The binarization was via `itg.py`. The resplit was via `resplit.py`.
