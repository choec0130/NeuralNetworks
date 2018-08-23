# UNFINISHED CODE

import sklearn
import pandas 
import cv2

# train with convolutional neural network 

def get_hog() : 
    winSize = (20,20) #size of images 
    blockSize = (10,10) # typically blocksize is 2x cell size (varies on illuminance variation)
    blockStride = (5,5) # determines overlap of neighboring blocks and controls contrast normalization degree. usually 50% blocksize
    cellSize = (10,10)
    nbins = 9 # number bins in HOG
    derivAperture = 1
    winSigma = -1.
    histogramNormType = 0
    L2HysThreshold = 0.2
    gammaCorrection = 1
    nlevels = 64
    signedGradient = True

    hog = cv2.HOGDescriptor(winSize,blockSize,blockStride,cellSize,nbins,derivAperture,winSigma,histogramNormType,L2HysThreshold,gammaCorrection,nlevels, signedGradient)

    return hog
    # affine_flags = cv2.WARP_INVERSE_MAP|cv2.INTER_LINEAR 

class SVM(StatModel):
    def __init__(self, C = 12.5, gamma = 0.50625):
        # set up SVM for OpenCV 3
        self.model = cv2.ml.SVM_create()
        #set parameters C and gamma
        self.model.setGamma(gamma)
        self.model.setC(C)
        # set SVM Kernel to Radial Basis Function (RBF) 
        self.model.setKernel(cv2.ml.SVM_RBF)
        # set SVM type
        self.model.setType(cv2.ml.SVM_C_SVC)

    # train SVM on training data 
    def train(self, samples, responses):
        self.model.train(samples, cv2.ml.ROW_SAMPLE, responses)
        # Save trained model 
        svm.save("fruit_svm_model.yml");

    # test on test data and return
    def predict(self, samples):

        return self.model.predict(samples)[1].ravel()
