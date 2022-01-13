import numpy as np
import random as r
import matplotlib.pyplot as plt    
import matplotlib.animation as anim
import math
import pytest
import os
import Patterns as P
import HopfieldNetwork as H
import DataSaver as D
from timeit import default_timer as timer



# Setup for tests, so we don't have to recompute patterns and weights each time

patterns1 = P.Patterns(patterns = np.array([np.array([1, 1,-1,-1]),
                                          np.array([1, 1,-1, 1]),
                                          np.array([-1,1,-1, 1])]))


patterns2 = P.Patterns(patterns = np.array([np.array([1, 1, 1, 1]),
                                            np.array([1, 1,-1, 1]),
                                            np.array([-1,1,-1, 1])]))

patterns3 = P.Patterns(20,50)
random_index = r.randrange(patterns3.num_patterns)

perturbed_pattern3 = (P.Patterns(patterns = patterns3.patterns[random_index])).perturb_pattern(20)

H_weights_patterns1 = np.array([np.array([ 0.,  1., -1., -1.]),
                               np.array([ 1.,  0., -3.,  1.]),
                               np.array([-1., -3.,  0., -1.]),
                               np.array([-1.,  1., -1.,  0.])])/3

S_weights_patterns1 = np.array([np.array([1.125, 0.25, -0.25, -0.5]),
                               np.array([0.25, 0.625, -1., 0.25]),
                               np.array([-0.25, -1., 0.625, -0.25]),
                               np.array([-0.5, 0.25, -0.25, 1.125])])

perturbed_pattern1 = P.Patterns(patterns = np.array([1, 1, 1, 1]))


'''
    assert (3*hebbian == np.array([np.array([ 0.,  1., -1., -1.]),
                                   np.array([ 1.,  0., -3.,  1.]),
                                   np.array([-1., -3.,  0., -1.]),
                                   np.array([-1.,  1., -1.,  0.])])).all()
    
    
    assert (storkey == np.array([np.array([1.125, 0.25, -0.25, -0.5]),
                                 np.array([0.25, 0.625, -1., 0.25]),
                                np.array([-0.25, -1., 0.625, -0.25]),
                                np.array([-0.5, 0.25, -0.25, 1.125])])).all()
'''

def test_Network_initialization_hebbian():
    network = H.HopfieldNetwork(patterns1, 'hebbian')
    assert (network.patterns == patterns1.patterns).all() # Check that the patterns were correctly initialized
    assert network.rule == 'hebbian' # Check that the rule was correctly initialized
    assert (network.weights == H_weights_patterns1).all() # Check that the weights were calculated correctly
    
def test_Network_initialization_storkey():
    network = H.HopfieldNetwork(patterns1, 'storkey')
    assert (network.patterns == patterns1.patterns).all() # Check that the patterns were correctly initialized
    assert network.rule == 'storkey' # Check that the rule was correctly initialized
    assert (network.weights == S_weights_patterns1).all() # Check that the weights were calculated correctly
    
def test_Network_initialization_default():
    network = H.HopfieldNetwork()
    assert np.shape(network.patterns) == (3,5) # Check the size for default initialization
    assert network.rule == 'hebbian' # Check the rule for default initialization
    
def test_Network_wrong_rule_init():
    with pytest.raises(ValueError):
        network = H.HopfieldNetwork(rule = 'something') # Check that it is not possible to initialize a network with a non-defined rule
    
def test_Hebbian_calculation():
    network = H.HopfieldNetwork(patterns3, 'hebbian')
    zerovec = np.zeros(patterns3.patterns_size)
    assert (np.diagonal(network.weights) == zerovec).all() # Check that there are zeros on the diagonal
    assert (network.weights == np.transpose(network.weights)).all() # Check that the Hebbian weights matrix is symetric

'''   
def test_Storkey_calculation():
    network = H.HopfieldNetwork(patterns3, 'storkey')
    assert (network.weights == np.transpose(network.weights)).all() # Check that the Storkey weights matrix is symetric
'''

def test_Storkey_calculation():
    patterns = np.array([np.array([ 1., -1.,  1., -1.,  1.,  1., -1.,  1., -1.,  1.]),
                         np.array([ 1., -1., -1.,  1., -1., -1., -1., -1.,  1.,  1.]),
                         np.array([ 1., -1., -1., -1., -1., -1.,  1., -1., -1., -1.]),
                         np.array([ 1., -1.,  1., -1.,  1.,  1., -1.,  1., -1., -1.]),
                         np.array([ 1., -1.,  1.,  1.,  1.,  1., -1.,  1., -1., -1.])])
    network = H.HopfieldNetwork(patterns, 'storkey')
    assert (network.weights == np.transpose(network.weights)).all() # Check that the Storkey weights matrix is symetric

def test_Network_compute_weights():
    network = H.HopfieldNetwork(patterns2.patterns, 'hebbian')
    old_weights = network.weights
    network.patterns = patterns1.patterns
    network.compute_weights()
    assert (old_weights != network.weights).any() # Checks that the weights changed
    assert (network.weights ==  H_weights_patterns1).all() # Checks the weights are calculated correctly when the patterns change
    network.rule = 'storkey'
    network.compute_weights()
    assert (network.weights ==  S_weights_patterns1).all() # Checks the weights are calculated correctly when the rule changes
    

def test_Network_compute_weights_wrong_rule():
    network = H.HopfieldNetwork(patterns1.patterns, 'hebbian')
    network.rule = 'something'
    with pytest.raises(ValueError):
        network.compute_weights()   # Checks that the weights cannot be calculated if rule is non defined
        
def test_Network_sigma():
    network = H.HopfieldNetwork()
    assert network.sigma(-0.5) == -1    #
    assert network.sigma(0.7) == 1      # Checks that the sigma function works well
    assert network.sigma(0.0) == 1      #
    
def test_Network_update():
    network = H.HopfieldNetwork(patterns1.patterns, 'hebbian')
    assert (network.update(perturbed_pattern1) == np.array([-1,-1,-1,-1])).all() # Update for hebbian rule with known values
    network = H.HopfieldNetwork(patterns1, 'storkey')
    assert (network.update(perturbed_pattern1) == np.array([ 1, 1,-1, 1])).all() # Update for storkey rule with known values
    
def test_Network_update_async():  # Checks that there was one modification at most with update_async()
    network = H.HopfieldNetwork(patterns3, 'hebbian')
    new_pattern = network.update_async(perturbed_pattern3)
    unchanged = np.count_nonzero(new_pattern + perturbed_pattern3)
    assert (np.size(perturbed_pattern3) - unchanged == 1) or (np.size(perturbed_pattern3) - unchanged == 0)
    
    
def test_Datasaver_initialisation():
    datasaver = D.DataSaver()
    assert type(datasaver.dataset) == list  #
    assert len(datasaver.dataset) == 0      # Checks that the DataSaver was initialized correctly
    
    
def test_Datasaver_compute_energy():
    network = H.HopfieldNetwork(patterns1)
    datasaver = D.DataSaver()
    state = np.array([1, 1, -1, -1])
    
    assert datasaver.compute_energy(state, network.weights) == -4/3

    
def test_Datasaver_store_iter():
    network = H.HopfieldNetwork(patterns1)
    datasaver = D.DataSaver()
    pattern_to_store = np.array([1, 1, -1, -1])
    datasaver.store_iter(pattern_to_store, network.weights)
    
    assert len(datasaver.dataset) != 0 # Checks that something was stored in dataset
    assert (datasaver.dataset[0][0] == pattern_to_store).all() # Checks the correct pattern was stroed
    assert datasaver.dataset[0][1] == -4/3 # Checks the correct energy was stored
    
def test_Dataset_reset():
    network = H.HopfieldNetwork()
    datasaver = D.DataSaver()
    
    datasaver.store_iter(network.patterns[0], network.weights)
    datasaver.reset()
    assert len(datasaver.dataset) == 0 # Checks the dataset was indeed reset
    
    
def test_dynamics():
    patterns = np.array([np.array([ 1., -1.,  1., -1.,  1.,  1., -1.,  1., -1.,  1.]),
                         np.array([ 1., -1., -1.,  1., -1., -1., -1., -1.,  1.,  1.]),
                         np.array([ 1., -1., -1., -1., -1., -1.,  1., -1., -1., -1.]),
                         np.array([ 1., -1.,  1., -1.,  1.,  1., -1.,  1., -1., -1.]),
                         np.array([ 1., -1.,  1.,  1.,  1.,  1., -1.,  1., -1., -1.])])
    
    network = H.HopfieldNetwork(patterns)
    datasaver = D.DataSaver()
    random_pattern = np.array([-1., -1., -1.,  1.,  1.,  1., -1.,  1.,  1.,  1.])
    network.dynamics(random_pattern, datasaver, 50)
    assert (datasaver.dataset[-1][0] == datasaver.dataset[-2][0]).all() # Checks that the convergence criteria is met
    assert pattern_match(network.patterns, datasaver.dataset[-1][0]) != None # Checks that it converges to a known pattern
    

def test_Dataset_energy_NonIncreasing():
    patterns = np.array([np.array([ 1., -1.,  1., -1.,  1.,  1., -1.,  1., -1.,  1.]),
                         np.array([ 1., -1., -1.,  1., -1., -1., -1., -1.,  1.,  1.]),
                         np.array([ 1., -1., -1., -1., -1., -1.,  1., -1., -1., -1.]),
                         np.array([ 1., -1.,  1., -1.,  1.,  1., -1.,  1., -1., -1.]),
                         np.array([ 1., -1.,  1.,  1.,  1.,  1., -1.,  1., -1., -1.])])
    
    network = H.HopfieldNetwork(patterns)
    datasaver = D.DataSaver()
    random_pattern = np.array([-1., -1., -1.,  1.,  1.,  1., -1.,  1.,  1.,  1.])
    network.dynamics_async(random_pattern, datasaver, 1000, 500)
    
    check_non_increasing = True

    for i in range(len(datasaver.dataset)-1):
        if datasaver.dataset[i+1][1]>datasaver.dataset[i][1]:
            check_non_increasing = False
    
    assert check_non_increasing