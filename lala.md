# Model analysis and summary

To further analyse our model, we determined its capacity (# of patterns that a network can store), and its robustness (to what extent we can perturb a pattern and still retrive the original one).

## 1. Capacity


### Experiment
To estimate the capacity our model, we performed multiple experiments, in which we varied the network size and number of random base patterns (sampled around the theoretical estimate of the network capacity). We perturbed 20% of the values of each base pattern and ran the dynamical system to study the convergence of the perturbed patterns.

We then plotted the fraction of retreived patterns according to the number of base patterns, and this for each of the network sizes.


### Results

#### These are the results table from our experiments:

##### For the Hebbian rule:

|    |   network_size | weight_rule   |   num_patterns |   num_perturb |   match_frac |
|---:|---------------:|:--------------|---------------:|--------------:|-------------:|
|  0 |             10 | hebbian       |              1 |             0 |          1   |
|  1 |             10 | hebbian       |              1 |             0 |          1   |
|  2 |             10 | hebbian       |              1 |             0 |          1   |
|  3 |             10 | hebbian       |              2 |             0 |          1   |
|  4 |             10 | hebbian       |              2 |             0 |          1   |
|  5 |             10 | hebbian       |              2 |             0 |          1   |
|  6 |             10 | hebbian       |              3 |             0 |          1   |
|  7 |             10 | hebbian       |              3 |             0 |          0.9 |
|  8 |             10 | hebbian       |              3 |             0 |          0.7 |
|  9 |             10 | hebbian       |              4 |             0 |          0.6 |
| 10 |             18 | hebbian       |              1 |             0 |          1   |
| 11 |             18 | hebbian       |              2 |             0 |          1   |
| 12 |             18 | hebbian       |              2 |             0 |          1   |
| 13 |             18 | hebbian       |              3 |             0 |          1   |
| 14 |             18 | hebbian       |              3 |             0 |          1   |
| 15 |             18 | hebbian       |              4 |             0 |          1   |
| 16 |             18 | hebbian       |              4 |             0 |          0.8 |
| 17 |             18 | hebbian       |              5 |             1 |          0.6 |
| 18 |             18 | hebbian       |              5 |             1 |          0.5 |
| 19 |             18 | hebbian       |              6 |             1 |          0.7 |
| 20 |             34 | hebbian       |              2 |             0 |          1   |
| 21 |             34 | hebbian       |              3 |             0 |          1   |
| 22 |             34 | hebbian       |              4 |             0 |          1   |
| 23 |             34 | hebbian       |              4 |             0 |          1   |
| 24 |             34 | hebbian       |              5 |             1 |          1   |
| 25 |             34 | hebbian       |              6 |             1 |          0.7 |
| 26 |             34 | hebbian       |              7 |             1 |          0.8 |
| 27 |             34 | hebbian       |              8 |             1 |          0.7 |
| 28 |             34 | hebbian       |              8 |             1 |          0.5 |
| 29 |             34 | hebbian       |              9 |             1 |          0.3 |
| 30 |             63 | hebbian       |              3 |             0 |          1   |
| 31 |             63 | hebbian       |              5 |             1 |          1   |
| 32 |             63 | hebbian       |              6 |             1 |          1   |
| 33 |             63 | hebbian       |              7 |             1 |          0.9 |
| 34 |             63 | hebbian       |              8 |             1 |          1   |
| 35 |             63 | hebbian       |             10 |             2 |          0.8 |
| 36 |             63 | hebbian       |             11 |             2 |          0.5 |
| 37 |             63 | hebbian       |             12 |             2 |          0.6 |
| 38 |             63 | hebbian       |             13 |             2 |          0.2 |
| 39 |             63 | hebbian       |             15 |             3 |          0   |
| 40 |            116 | hebbian       |              6 |             1 |          1   |
| 41 |            116 | hebbian       |              8 |             1 |          1   |
| 42 |            116 | hebbian       |             10 |             2 |          1   |
| 43 |            116 | hebbian       |             12 |             2 |          1   |
| 44 |            116 | hebbian       |             14 |             2 |          0.8 |
| 45 |            116 | hebbian       |             16 |             3 |          0.6 |
| 46 |            116 | hebbian       |             18 |             3 |          0.5 |
| 47 |            116 | hebbian       |             20 |             4 |          0.6 |
| 48 |            116 | hebbian       |             22 |             4 |          0.5 |
| 49 |            116 | hebbian       |             24 |             4 |          0.1 |
| 50 |            215 | hebbian       |             10 |             2 |          1   |
| 51 |            215 | hebbian       |             13 |             2 |          1   |
| 52 |            215 | hebbian       |             16 |             3 |          1   |
| 53 |            215 | hebbian       |             20 |             4 |          0.9 |
| 54 |            215 | hebbian       |             23 |             4 |          0.8 |
| 55 |            215 | hebbian       |             26 |             5 |          0.7 |
| 56 |            215 | hebbian       |             30 |             6 |          0.4 |
| 57 |            215 | hebbian       |             33 |             6 |          0.4 |
| 58 |            215 | hebbian       |             36 |             7 |          0.3 |
| 59 |            215 | hebbian       |             40 |             8 |          0.2 |
| 60 |            397 | hebbian       |             16 |             3 |          1   |
| 61 |            397 | hebbian       |             22 |             4 |          1   |
| 62 |            397 | hebbian       |             27 |             5 |          1   |
| 63 |            397 | hebbian       |             33 |             6 |          1   |
| 64 |            397 | hebbian       |             38 |             7 |          0.7 |
| 65 |            397 | hebbian       |             44 |             8 |          0.7 |
| 66 |            397 | hebbian       |             49 |             9 |          0.8 |
| 67 |            397 | hebbian       |             55 |            11 |          0   |
| 68 |            397 | hebbian       |             60 |            12 |          0.4 |
| 69 |            397 | hebbian       |             66 |            13 |          0.1 |
| 70 |            733 | hebbian       |             27 |             5 |          1   |
| 71 |            733 | hebbian       |             37 |             7 |          1   |
| 72 |            733 | hebbian       |             46 |             9 |          1   |
| 73 |            733 | hebbian       |             55 |            11 |          1   |
| 74 |            733 | hebbian       |             64 |            12 |          0.7 |
| 75 |            733 | hebbian       |             74 |            14 |          0.5 |
| 76 |            733 | hebbian       |             83 |            16 |          0.3 |
| 77 |            733 | hebbian       |             92 |            18 |          0.3 |
| 78 |            733 | hebbian       |            101 |            20 |          0   |
| 79 |            733 | hebbian       |            111 |            22 |          0.1 |
| 80 |           1354 | hebbian       |             46 |             9 |          1   |
| 81 |           1354 | hebbian       |             62 |            12 |          1   |
| 82 |           1354 | hebbian       |             78 |            15 |          1   |
| 83 |           1354 | hebbian       |             93 |            18 |          0.9 |
| 84 |           1354 | hebbian       |            109 |            21 |          0.7 |
| 85 |           1354 | hebbian       |            125 |            25 |          0.6 |
| 86 |           1354 | hebbian       |            140 |            28 |          0.2 |
| 87 |           1354 | hebbian       |            156 |            31 |          0   |
| 88 |           1354 | hebbian       |            172 |            34 |          0   |
| 89 |           1354 | hebbian       |            187 |            37 |          0   |
| 90 |           2500 | hebbian       |             79 |            15 |          1   |
| 91 |           2500 | hebbian       |            106 |            21 |          1   |
| 92 |           2500 | hebbian       |            133 |            26 |          1   |
| 93 |           2500 | hebbian       |            159 |            31 |          1   |
| 94 |           2500 | hebbian       |            186 |            37 |          0.6 |
| 95 |           2500 | hebbian       |            213 |            42 |          0.7 |
| 96 |           2500 | hebbian       |            239 |            47 |          0.1 |
| 97 |           2500 | hebbian       |            266 |            53 |          0.1 |
| 98 |           2500 | hebbian       |            292 |            58 |          0   |
| 99 |           2500 | hebbian       |            319 |            63 |          0   |

###### For the Storkey rule:

|    |   network_size | weight_rule   |   num_patterns |   num_perturb |   match_frac |
|---:|---------------:|:--------------|---------------:|--------------:|-------------:|
|  0 |             10 | storkey       |              1 |             0 |          1   |
|  1 |             10 | storkey       |              2 |             0 |          1   |
|  2 |             10 | storkey       |              2 |             0 |          1   |
|  3 |             10 | storkey       |              3 |             0 |          1   |
|  4 |             10 | storkey       |              3 |             0 |          1   |
|  5 |             10 | storkey       |              4 |             0 |          1   |
|  6 |             10 | storkey       |              4 |             0 |          1   |
|  7 |             10 | storkey       |              5 |             1 |          0.6 |
|  8 |             10 | storkey       |              6 |             1 |          0.3 |
|  9 |             10 | storkey       |              6 |             1 |          0.7 |
| 10 |             18 | storkey       |              2 |             0 |          1   |
| 11 |             18 | storkey       |              3 |             0 |          1   |
| 12 |             18 | storkey       |              4 |             0 |          1   |
| 13 |             18 | storkey       |              5 |             1 |          1   |
| 14 |             18 | storkey       |              6 |             1 |          1   |
| 15 |             18 | storkey       |              7 |             1 |          0.9 |
| 16 |             18 | storkey       |              7 |             1 |          1   |
| 17 |             18 | storkey       |              8 |             1 |          1   |
| 18 |             18 | storkey       |              9 |             1 |          0.8 |
| 19 |             18 | storkey       |             10 |             2 |          0.6 |
| 20 |             34 | storkey       |              4 |             0 |          1   |
| 21 |             34 | storkey       |              6 |             1 |          1   |
| 22 |             34 | storkey       |              7 |             1 |          1   |
| 23 |             34 | storkey       |              9 |             1 |          1   |
| 24 |             34 | storkey       |             10 |             2 |          1   |
| 25 |             34 | storkey       |             12 |             2 |          0.9 |
| 26 |             34 | storkey       |             13 |             2 |          0.9 |
| 27 |             34 | storkey       |             15 |             3 |          0.9 |
| 28 |             34 | storkey       |             16 |             3 |          0.9 |
| 29 |             34 | storkey       |             18 |             3 |          0.5 |
| 30 |             63 | storkey       |              7 |             1 |          1   |
| 31 |             63 | storkey       |             10 |             2 |          1   |
| 32 |             63 | storkey       |             12 |             2 |          1   |
| 33 |             63 | storkey       |             15 |             3 |          1   |
| 34 |             63 | storkey       |             18 |             3 |          1   |
| 35 |             63 | storkey       |             20 |             4 |          0.9 |
| 36 |             63 | storkey       |             23 |             4 |          1   |
| 37 |             63 | storkey       |             25 |             5 |          0.9 |
| 38 |             63 | storkey       |             28 |             5 |          0.4 |
| 39 |             63 | storkey       |             30 |             6 |          0.5 |
| 40 |            116 | storkey       |             13 |             2 |          1   |
| 41 |            116 | storkey       |             17 |             3 |          1   |
| 42 |            116 | storkey       |             22 |             4 |          1   |
| 43 |            116 | storkey       |             26 |             5 |          1   |
| 44 |            116 | storkey       |             31 |             6 |          1   |
| 45 |            116 | storkey       |             35 |             7 |          0.9 |
| 46 |            116 | storkey       |             39 |             7 |          1   |
| 47 |            116 | storkey       |             44 |             8 |          0.9 |
| 48 |            116 | storkey       |             48 |             9 |          0.5 |
| 49 |            116 | storkey       |             53 |            10 |          0.4 |
| 50 |            215 | storkey       |             23 |             4 |          1   |
| 51 |            215 | storkey       |             30 |             6 |          1   |
| 52 |            215 | storkey       |             38 |             7 |          1   |
| 53 |            215 | storkey       |             46 |             9 |          1   |
| 54 |            215 | storkey       |             54 |            10 |          1   |
| 55 |            215 | storkey       |             61 |            12 |          1   |
| 56 |            215 | storkey       |             69 |            13 |          0.9 |
| 57 |            215 | storkey       |             77 |            15 |          0.9 |
| 58 |            215 | storkey       |             85 |            17 |          0.7 |
| 59 |            215 | storkey       |             92 |            18 |          0.6 |
| 60 |            397 | storkey       |             40 |             8 |          1   |
| 61 |            397 | storkey       |             54 |            10 |          1   |
| 62 |            397 | storkey       |             67 |            13 |          1   |
| 63 |            397 | storkey       |             81 |            16 |          1   |
| 64 |            397 | storkey       |             94 |            18 |          1   |
| 65 |            397 | storkey       |            108 |            21 |          1   |
| 66 |            397 | storkey       |            121 |            24 |          1   |
| 67 |            397 | storkey       |            135 |            27 |          0.9 |
| 68 |            397 | storkey       |            148 |            29 |          0.4 |
| 69 |            397 | storkey       |            162 |            32 |          0.5 |
| 70 |            733 | storkey       |             71 |            14 |          1   |
| 71 |            733 | storkey       |             95 |            19 |          1   |
| 72 |            733 | storkey       |            118 |            23 |          1   |
| 73 |            733 | storkey       |            142 |            28 |          1   |
| 74 |            733 | storkey       |            166 |            33 |          1   |
| 75 |            733 | storkey       |            190 |            38 |          1   |
| 76 |            733 | storkey       |            214 |            42 |          1   |
| 77 |            733 | storkey       |            237 |            47 |          0.9 |
| 78 |            733 | storkey       |            261 |            52 |          0.7 |
| 79 |            733 | storkey       |            285 |            57 |          0.5 |
| 80 |           1354 | storkey       |            126 |            25 |          1   |
| 81 |           1354 | storkey       |            168 |            33 |          1   |
| 82 |           1354 | storkey       |            210 |            42 |          1   |
| 83 |           1354 | storkey       |            252 |            50 |          1   |
| 84 |           1354 | storkey       |            294 |            58 |          1   |
| 85 |           1354 | storkey       |            336 |            67 |          1   |
| 86 |           1354 | storkey       |            378 |            75 |          1   |
| 87 |           1354 | storkey       |            420 |            84 |          0.9 |
| 88 |           1354 | storkey       |            462 |            92 |          0.7 |
| 89 |           1354 | storkey       |            504 |           100 |          0.2 |
| 90 |           2500 | storkey       |            223 |            44 |          1   |
| 91 |           2500 | storkey       |            297 |            59 |          1   |
| 92 |           2500 | storkey       |            372 |            74 |          1   |
| 93 |           2500 | storkey       |            446 |            89 |          1   |
| 94 |           2500 | storkey       |            521 |           104 |          1   |
| 95 |           2500 | storkey       |            595 |           119 |          1   |
| 96 |           2500 | storkey       |            670 |           134 |          1   |
| 97 |           2500 | storkey       |            744 |           148 |          0.8 |
| 98 |           2500 | storkey       |            819 |           163 |          0.4 |
| 99 |           2500 | storkey       |            893 |           178 |          0.5 |

#### These are the plots we obtained:

##### Capacity Curves for each of the 10 Network Sizes -- Fraction of Retrieved Patterns vs # of Base Patterns)

<p align="center">
<img src="https://github.com/annahk43/Images-for-README/blob/master/frac%20retrieved%20vs%20num%20perturb.jpeg">
</p>

##### Summary capacity plot -- # of patterns that can be retrieved with >= 0.9 probability vs. # of neurons

In this graph 'estimated' corresponds to the theoretical value, and 'experimental' corresponds to what we observed in our experiments.

<p align="center">
<img src="https://github.com/annahk43/Images-for-README/blob/master/Capacity%20(experimental:estimate).jpeg">
</p>

## 2. Robustness

### Experiment

We performed the same experiment, but with a fixed number of base patterns (for which we know that the pattern retrieval works correctly -- we chose 2). We progessively increased the number of perturbations by steps of 5%, to see at which point the system stops converging.

### Results

These are the result tables we obtained from our experiment:

###### For the Hebbian rule:

|     |   network_size | weight_rule   |   num_patterns |   num_perturb |   match_frac |
|----:|---------------:|:--------------|---------------:|--------------:|-------------:|
|   0 |             10 | hebbian       |              2 |             2 |          0.9 |
|   1 |             10 | hebbian       |              2 |             3 |          0.6 |
|   2 |             10 | hebbian       |              2 |             4 |          0.4 |
|   3 |             10 | hebbian       |              2 |             5 |          0   |
|   4 |             10 | hebbian       |              2 |             6 |          0.1 |
|   5 |             10 | hebbian       |              2 |             7 |          0   |
|   6 |             10 | hebbian       |              2 |             8 |          0   |
|   7 |             10 | hebbian       |              2 |             9 |          0   |
|   8 |             10 | hebbian       |              2 |            10 |          0   |
|   9 |             18 | hebbian       |              2 |             3 |          0.9 |
|  10 |             18 | hebbian       |              2 |             4 |          1   |
|  11 |             18 | hebbian       |              2 |             5 |          0.8 |
|  12 |             18 | hebbian       |              2 |             6 |          0.7 |
|  13 |             18 | hebbian       |              2 |             7 |          0.5 |
|  14 |             18 | hebbian       |              2 |             8 |          0.3 |
|  15 |             18 | hebbian       |              2 |             9 |          0   |
|  16 |             18 | hebbian       |              2 |            10 |          0   |
|  17 |             18 | hebbian       |              2 |            11 |          0   |
|  18 |             18 | hebbian       |              2 |            12 |          0   |
|  19 |             18 | hebbian       |              2 |            13 |          0   |
|  20 |             18 | hebbian       |              2 |            14 |          0   |
|  21 |             18 | hebbian       |              2 |            15 |          0   |
|  22 |             18 | hebbian       |              2 |            16 |          0   |
|  23 |             18 | hebbian       |              2 |            17 |          0   |
|  24 |             18 | hebbian       |              2 |            18 |          0   |
|  25 |             34 | hebbian       |              2 |             6 |          1   |
|  26 |             34 | hebbian       |              2 |             8 |          1   |
|  27 |             34 | hebbian       |              2 |            10 |          1   |
|  28 |             34 | hebbian       |              2 |            12 |          1   |
|  29 |             34 | hebbian       |              2 |            14 |          0.8 |
|  30 |             34 | hebbian       |              2 |            16 |          0.1 |
|  31 |             34 | hebbian       |              2 |            18 |          0   |
|  32 |             34 | hebbian       |              2 |            20 |          0   |
|  33 |             34 | hebbian       |              2 |            22 |          0   |
|  34 |             34 | hebbian       |              2 |            24 |          0   |
|  35 |             34 | hebbian       |              2 |            26 |          0   |
|  36 |             34 | hebbian       |              2 |            28 |          0   |
|  37 |             34 | hebbian       |              2 |            30 |          0   |
|  38 |             34 | hebbian       |              2 |            32 |          0   |
|  39 |             34 | hebbian       |              2 |            34 |          0   |
|  40 |             63 | hebbian       |              2 |            12 |          1   |
|  41 |             63 | hebbian       |              2 |            16 |          1   |
|  42 |             63 | hebbian       |              2 |            20 |          1   |
|  43 |             63 | hebbian       |              2 |            24 |          0.9 |
|  44 |             63 | hebbian       |              2 |            28 |          0.6 |
|  45 |             63 | hebbian       |              2 |            32 |          0   |
|  46 |             63 | hebbian       |              2 |            36 |          0   |
|  47 |             63 | hebbian       |              2 |            40 |          0   |
|  48 |             63 | hebbian       |              2 |            44 |          0   |
|  49 |             63 | hebbian       |              2 |            48 |          0   |
|  50 |             63 | hebbian       |              2 |            52 |          0   |
|  51 |             63 | hebbian       |              2 |            56 |          0   |
|  52 |             63 | hebbian       |              2 |            60 |          0   |
|  53 |            116 | hebbian       |              2 |            23 |          1   |
|  54 |            116 | hebbian       |              2 |            29 |          1   |
|  55 |            116 | hebbian       |              2 |            35 |          1   |
|  56 |            116 | hebbian       |              2 |            41 |          1   |
|  57 |            116 | hebbian       |              2 |            47 |          0.9 |
|  58 |            116 | hebbian       |              2 |            53 |          0.6 |
|  59 |            116 | hebbian       |              2 |            59 |          0   |
|  60 |            116 | hebbian       |              2 |            65 |          0   |
|  61 |            116 | hebbian       |              2 |            71 |          0   |
|  62 |            116 | hebbian       |              2 |            77 |          0   |
|  63 |            116 | hebbian       |              2 |            83 |          0   |
|  64 |            116 | hebbian       |              2 |            89 |          0   |
|  65 |            116 | hebbian       |              2 |            95 |          0   |
|  66 |            116 | hebbian       |              2 |           101 |          0   |
|  67 |            116 | hebbian       |              2 |           107 |          0   |
|  68 |            116 | hebbian       |              2 |           113 |          0   |
|  69 |            215 | hebbian       |              2 |            43 |          1   |
|  70 |            215 | hebbian       |              2 |            54 |          1   |
|  71 |            215 | hebbian       |              2 |            65 |          1   |
|  72 |            215 | hebbian       |              2 |            76 |          1   |
|  73 |            215 | hebbian       |              2 |            87 |          1   |
|  74 |            215 | hebbian       |              2 |            98 |          0.7 |
|  75 |            215 | hebbian       |              2 |           109 |          0   |
|  76 |            215 | hebbian       |              2 |           120 |          0   |
|  77 |            215 | hebbian       |              2 |           131 |          0   |
|  78 |            215 | hebbian       |              2 |           142 |          0   |
|  79 |            215 | hebbian       |              2 |           153 |          0   |
|  80 |            215 | hebbian       |              2 |           164 |          0   |
|  81 |            215 | hebbian       |              2 |           175 |          0   |
|  82 |            215 | hebbian       |              2 |           186 |          0   |
|  83 |            215 | hebbian       |              2 |           197 |          0   |
|  84 |            215 | hebbian       |              2 |           208 |          0   |
|  85 |            397 | hebbian       |              2 |            79 |          1   |
|  86 |            397 | hebbian       |              2 |            99 |          1   |
|  87 |            397 | hebbian       |              2 |           119 |          1   |
|  88 |            397 | hebbian       |              2 |           139 |          1   |
|  89 |            397 | hebbian       |              2 |           159 |          1   |
|  90 |            397 | hebbian       |              2 |           179 |          1   |
|  91 |            397 | hebbian       |              2 |           199 |          0   |
|  92 |            397 | hebbian       |              2 |           219 |          0   |
|  93 |            397 | hebbian       |              2 |           239 |          0   |
|  94 |            397 | hebbian       |              2 |           259 |          0   |
|  95 |            397 | hebbian       |              2 |           279 |          0   |
|  96 |            397 | hebbian       |              2 |           299 |          0   |
|  97 |            397 | hebbian       |              2 |           319 |          0   |
|  98 |            397 | hebbian       |              2 |           339 |          0   |
|  99 |            397 | hebbian       |              2 |           359 |          0   |
| 100 |            397 | hebbian       |              2 |           379 |          0   |
| 101 |            733 | hebbian       |              2 |           146 |          1   |
| 102 |            733 | hebbian       |              2 |           183 |          1   |
| 103 |            733 | hebbian       |              2 |           220 |          1   |
| 104 |            733 | hebbian       |              2 |           257 |          1   |
| 105 |            733 | hebbian       |              2 |           294 |          1   |
| 106 |            733 | hebbian       |              2 |           331 |          1   |
| 107 |            733 | hebbian       |              2 |           368 |          0   |
| 108 |            733 | hebbian       |              2 |           405 |          0   |
| 109 |            733 | hebbian       |              2 |           442 |          0   |
| 110 |            733 | hebbian       |              2 |           479 |          0   |
| 111 |            733 | hebbian       |              2 |           516 |          0   |
| 112 |            733 | hebbian       |              2 |           553 |          0   |
| 113 |            733 | hebbian       |              2 |           590 |          0   |
| 114 |            733 | hebbian       |              2 |           627 |          0   |
| 115 |            733 | hebbian       |              2 |           664 |          0   |
| 116 |            733 | hebbian       |              2 |           701 |          0   |
| 117 |           1354 | hebbian       |              2 |           270 |          1   |
| 118 |           1354 | hebbian       |              2 |           338 |          1   |
| 119 |           1354 | hebbian       |              2 |           406 |          1   |
| 120 |           1354 | hebbian       |              2 |           474 |          1   |
| 121 |           1354 | hebbian       |              2 |           542 |          1   |
| 122 |           1354 | hebbian       |              2 |           610 |          1   |
| 123 |           1354 | hebbian       |              2 |           678 |          0   |
| 124 |           1354 | hebbian       |              2 |           746 |          0   |
| 125 |           1354 | hebbian       |              2 |           814 |          0   |
| 126 |           1354 | hebbian       |              2 |           882 |          0   |
| 127 |           1354 | hebbian       |              2 |           950 |          0   |
| 128 |           1354 | hebbian       |              2 |          1018 |          0   |
| 129 |           1354 | hebbian       |              2 |          1086 |          0   |
| 130 |           1354 | hebbian       |              2 |          1154 |          0   |
| 131 |           1354 | hebbian       |              2 |          1222 |          0   |
| 132 |           1354 | hebbian       |              2 |          1290 |          0   |
| 133 |           2500 | hebbian       |              2 |           500 |          1   |
| 134 |           2500 | hebbian       |              2 |           625 |          1   |
| 135 |           2500 | hebbian       |              2 |           750 |          1   |
| 136 |           2500 | hebbian       |              2 |           875 |          1   |
| 137 |           2500 | hebbian       |              2 |          1000 |          1   |
| 138 |           2500 | hebbian       |              2 |          1125 |          1   |
| 139 |           2500 | hebbian       |              2 |          1250 |          0   |
| 140 |           2500 | hebbian       |              2 |          1375 |          0   |
| 141 |           2500 | hebbian       |              2 |          1500 |          0   |
| 142 |           2500 | hebbian       |              2 |          1625 |          0   |
| 143 |           2500 | hebbian       |              2 |          1750 |          0   |
| 144 |           2500 | hebbian       |              2 |          1875 |          0   |
| 145 |           2500 | hebbian       |              2 |          2000 |          0   |
| 146 |           2500 | hebbian       |              2 |          2125 |          0   |
| 147 |           2500 | hebbian       |              2 |          2250 |          0   |
| 148 |           2500 | hebbian       |              2 |          2375 |          0   |
| 149 |           2500 | hebbian       |              2 |          2500 |          0   |

###### For the Storkey rule:

|     |   network_size | weight_rule   |   num_patterns |   num_perturb |   match_frac |
|----:|---------------:|:--------------|---------------:|--------------:|-------------:|
|   0 |             10 | storkey       |              2 |             2 |          0.9 |
|   1 |             10 | storkey       |              2 |             3 |          0.7 |
|   2 |             10 | storkey       |              2 |             4 |          0.3 |
|   3 |             10 | storkey       |              2 |             5 |          0   |
|   4 |             10 | storkey       |              2 |             6 |          0   |
|   5 |             10 | storkey       |              2 |             7 |          0   |
|   6 |             10 | storkey       |              2 |             8 |          0   |
|   7 |             10 | storkey       |              2 |             9 |          0   |
|   8 |             10 | storkey       |              2 |            10 |          0   |
|   9 |             18 | storkey       |              2 |             3 |          1   |
|  10 |             18 | storkey       |              2 |             4 |          0.9 |
|  11 |             18 | storkey       |              2 |             5 |          1   |
|  12 |             18 | storkey       |              2 |             6 |          1   |
|  13 |             18 | storkey       |              2 |             7 |          0.3 |
|  14 |             18 | storkey       |              2 |             8 |          0.3 |
|  15 |             18 | storkey       |              2 |             9 |          0   |
|  16 |             18 | storkey       |              2 |            10 |          0   |
|  17 |             18 | storkey       |              2 |            11 |          0   |
|  18 |             18 | storkey       |              2 |            12 |          0   |
|  19 |             18 | storkey       |              2 |            13 |          0   |
|  20 |             18 | storkey       |              2 |            14 |          0   |
|  21 |             18 | storkey       |              2 |            15 |          0   |
|  22 |             18 | storkey       |              2 |            16 |          0   |
|  23 |             18 | storkey       |              2 |            17 |          0   |
|  24 |             18 | storkey       |              2 |            18 |          0   |
|  25 |             34 | storkey       |              2 |             6 |          1   |
|  26 |             34 | storkey       |              2 |             8 |          1   |
|  27 |             34 | storkey       |              2 |            10 |          1   |
|  28 |             34 | storkey       |              2 |            12 |          1   |
|  29 |             34 | storkey       |              2 |            14 |          0.7 |
|  30 |             34 | storkey       |              2 |            16 |          0.1 |
|  31 |             34 | storkey       |              2 |            18 |          0   |
|  32 |             34 | storkey       |              2 |            20 |          0   |
|  33 |             34 | storkey       |              2 |            22 |          0   |
|  34 |             34 | storkey       |              2 |            24 |          0   |
|  35 |             34 | storkey       |              2 |            26 |          0   |
|  36 |             34 | storkey       |              2 |            28 |          0   |
|  37 |             34 | storkey       |              2 |            30 |          0   |
|  38 |             34 | storkey       |              2 |            32 |          0   |
|  39 |             34 | storkey       |              2 |            34 |          0   |
|  40 |             63 | storkey       |              2 |            12 |          1   |
|  41 |             63 | storkey       |              2 |            16 |          1   |
|  42 |             63 | storkey       |              2 |            20 |          1   |
|  43 |             63 | storkey       |              2 |            24 |          0.7 |
|  44 |             63 | storkey       |              2 |            28 |          0.7 |
|  45 |             63 | storkey       |              2 |            32 |          0   |
|  46 |             63 | storkey       |              2 |            36 |          0   |
|  47 |             63 | storkey       |              2 |            40 |          0   |
|  48 |             63 | storkey       |              2 |            44 |          0   |
|  49 |             63 | storkey       |              2 |            48 |          0   |
|  50 |             63 | storkey       |              2 |            52 |          0   |
|  51 |             63 | storkey       |              2 |            56 |          0   |
|  52 |             63 | storkey       |              2 |            60 |          0   |
|  53 |            116 | storkey       |              2 |            23 |          1   |
|  54 |            116 | storkey       |              2 |            29 |          1   |
|  55 |            116 | storkey       |              2 |            35 |          1   |
|  56 |            116 | storkey       |              2 |            41 |          1   |
|  57 |            116 | storkey       |              2 |            47 |          0.9 |
|  58 |            116 | storkey       |              2 |            53 |          0.5 |
|  59 |            116 | storkey       |              2 |            59 |          0   |
|  60 |            116 | storkey       |              2 |            65 |          0   |
|  61 |            116 | storkey       |              2 |            71 |          0   |
|  62 |            116 | storkey       |              2 |            77 |          0   |
|  63 |            116 | storkey       |              2 |            83 |          0   |
|  64 |            116 | storkey       |              2 |            89 |          0   |
|  65 |            116 | storkey       |              2 |            95 |          0   |
|  66 |            116 | storkey       |              2 |           101 |          0   |
|  67 |            116 | storkey       |              2 |           107 |          0   |
|  68 |            116 | storkey       |              2 |           113 |          0   |
|  69 |            215 | storkey       |              2 |            43 |          1   |
|  70 |            215 | storkey       |              2 |            54 |          1   |
|  71 |            215 | storkey       |              2 |            65 |          1   |
|  72 |            215 | storkey       |              2 |            76 |          1   |
|  73 |            215 | storkey       |              2 |            87 |          1   |
|  74 |            215 | storkey       |              2 |            98 |          1   |
|  75 |            215 | storkey       |              2 |           109 |          0   |
|  76 |            215 | storkey       |              2 |           120 |          0   |
|  77 |            215 | storkey       |              2 |           131 |          0   |
|  78 |            215 | storkey       |              2 |           142 |          0   |
|  79 |            215 | storkey       |              2 |           153 |          0   |
|  80 |            215 | storkey       |              2 |           164 |          0   |
|  81 |            215 | storkey       |              2 |           175 |          0   |
|  82 |            215 | storkey       |              2 |           186 |          0   |
|  83 |            215 | storkey       |              2 |           197 |          0   |
|  84 |            215 | storkey       |              2 |           208 |          0   |
|  85 |            397 | storkey       |              2 |            79 |          1   |
|  86 |            397 | storkey       |              2 |            99 |          1   |
|  87 |            397 | storkey       |              2 |           119 |          1   |
|  88 |            397 | storkey       |              2 |           139 |          1   |
|  89 |            397 | storkey       |              2 |           159 |          1   |
|  90 |            397 | storkey       |              2 |           179 |          1   |
|  91 |            397 | storkey       |              2 |           199 |          0   |
|  92 |            397 | storkey       |              2 |           219 |          0   |
|  93 |            397 | storkey       |              2 |           239 |          0   |
|  94 |            397 | storkey       |              2 |           259 |          0   |
|  95 |            397 | storkey       |              2 |           279 |          0   |
|  96 |            397 | storkey       |              2 |           299 |          0   |
|  97 |            397 | storkey       |              2 |           319 |          0   |
|  98 |            397 | storkey       |              2 |           339 |          0   |
|  99 |            397 | storkey       |              2 |           359 |          0   |
| 100 |            397 | storkey       |              2 |           379 |          0   |
| 101 |            733 | storkey       |              2 |           146 |          1   |
| 102 |            733 | storkey       |              2 |           183 |          1   |
| 103 |            733 | storkey       |              2 |           220 |          1   |
| 104 |            733 | storkey       |              2 |           257 |          1   |
| 105 |            733 | storkey       |              2 |           294 |          1   |
| 106 |            733 | storkey       |              2 |           331 |          1   |
| 107 |            733 | storkey       |              2 |           368 |          0   |
| 108 |            733 | storkey       |              2 |           405 |          0   |
| 109 |            733 | storkey       |              2 |           442 |          0   |
| 110 |            733 | storkey       |              2 |           479 |          0   |
| 111 |            733 | storkey       |              2 |           516 |          0   |
| 112 |            733 | storkey       |              2 |           553 |          0   |
| 113 |            733 | storkey       |              2 |           590 |          0   |
| 114 |            733 | storkey       |              2 |           627 |          0   |
| 115 |            733 | storkey       |              2 |           664 |          0   |
| 116 |            733 | storkey       |              2 |           701 |          0   |
| 117 |           1354 | storkey       |              2 |           270 |          1   |
| 118 |           1354 | storkey       |              2 |           338 |          1   |
| 119 |           1354 | storkey       |              2 |           406 |          1   |
| 120 |           1354 | storkey       |              2 |           474 |          1   |
| 121 |           1354 | storkey       |              2 |           542 |          1   |
| 122 |           1354 | storkey       |              2 |           610 |          1   |
| 123 |           1354 | storkey       |              2 |           678 |          0   |
| 124 |           1354 | storkey       |              2 |           746 |          0   |
| 125 |           1354 | storkey       |              2 |           814 |          0   |
| 126 |           1354 | storkey       |              2 |           882 |          0   |
| 127 |           1354 | storkey       |              2 |           950 |          0   |
| 128 |           1354 | storkey       |              2 |          1018 |          0   |
| 129 |           1354 | storkey       |              2 |          1086 |          0   |
| 130 |           1354 | storkey       |              2 |          1154 |          0   |
| 131 |           1354 | storkey       |              2 |          1222 |          0   |
| 132 |           1354 | storkey       |              2 |          1290 |          0   |
| 133 |           2500 | storkey       |              2 |           500 |          1   |
| 134 |           2500 | storkey       |              2 |           625 |          1   |
| 135 |           2500 | storkey       |              2 |           750 |          1   |
| 136 |           2500 | storkey       |              2 |           875 |          1   |
| 137 |           2500 | storkey       |              2 |          1000 |          1   |
| 138 |           2500 | storkey       |              2 |          1125 |          1   |
| 139 |           2500 | storkey       |              2 |          1250 |          0   |
| 140 |           2500 | storkey       |              2 |          1375 |          0   |
| 141 |           2500 | storkey       |              2 |          1500 |          0   |
| 142 |           2500 | storkey       |              2 |          1625 |          0   |
| 143 |           2500 | storkey       |              2 |          1750 |          0   |
| 144 |           2500 | storkey       |              2 |          1875 |          0   |
| 145 |           2500 | storkey       |              2 |          2000 |          0   |
| 146 |           2500 | storkey       |              2 |          2125 |          0   |
| 147 |           2500 | storkey       |              2 |          2250 |          0   |
| 148 |           2500 | storkey       |              2 |          2375 |          0   |
| 149 |           2500 | storkey       |              2 |          2500 |          0   |


These are the corresponding plots -- fraction of retrieved patterns vs # of perturbations

<p align="center">
<img src="https://github.com/annahk43/Images-for-README/blob/master/frac%20retrieved%20vs%20num%20perturb.jpeg">
</p>


