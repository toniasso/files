# -*- coding: mbcs -*-
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
import math
from abaqus import *
from abaqusConstants import *
from caeModules import *
import time
import numpy

data = numpy.array( [ [ 1, 'Uni_Truss', 0.01, 0, 0, 0, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 2, 'Uni_Truss', 0.01, 0, 0, 5, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 3, 'Uni_Truss', 0.01, 0, 0, 10, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 4, 'Uni_Truss', 0.01, 0, 0, 15, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 5, 'Uni_Truss', 0.01, 0, 0, 20, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 6, 'Uni_Truss', 0.01, 0, 0, 25, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 7, 'Uni_Truss', 0.01, 0, 0, 30, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 8, 'Uni_Truss', 0.01, 0, 0, 35, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 9, 'Uni_Truss', 0.01, 0, 0, 40, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 10, 'Uni_Truss', 0.01, 0, 0, 45, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 11, 'Uni_Truss', 0.01, 0, 0, 50, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 12, 'Uni_Truss', 0.01, 0, 0, 55, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 13, 'Uni_Truss', 0.01, 0, 0, 60, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 14, 'Uni_Truss', 0.01, 0, 0, 65, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 15, 'Uni_Truss', 0.01, 0, 0, 70, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 16, 'Uni_Truss', 0.01, 0, 0, 75, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 17, 'Uni_Truss', 0.01, 0, 0, 80, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 18, 'Uni_Truss', 0.01, 0, 0, 85, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 19, 'Uni_Truss', 0.01, 0, 0, 90, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 20, 'Uni_Beam', 0.01, 0, 1, 0, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 21, 'Uni_Beam', 0.01, 0, 1, 5, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 22, 'Uni_Beam', 0.01, 0, 1, 10, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 23, 'Uni_Beam', 0.01, 0, 1, 15, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 24, 'Uni_Beam', 0.01, 0, 1, 20, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 25, 'Uni_Beam', 0.01, 0, 1, 25, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 26, 'Uni_Beam', 0.01, 0, 1, 30, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 27, 'Uni_Beam', 0.01, 0, 1, 35, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 28, 'Uni_Beam', 0.01, 0, 1, 40, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 29, 'Uni_Beam', 0.01, 0, 1, 45, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 30, 'Uni_Beam', 0.01, 0, 1, 50, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 31, 'Uni_Beam', 0.01, 0, 1, 55, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 32, 'Uni_Beam', 0.01, 0, 1, 60, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 33, 'Uni_Beam', 0.01, 0, 1, 65, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 34, 'Uni_Beam', 0.01, 0, 1, 70, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 35, 'Uni_Beam', 0.01, 0, 1, 75, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 36, 'Uni_Beam', 0.01, 0, 1, 80, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 37, 'Uni_Beam', 0.01, 0, 1, 85, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 38, 'Uni_Beam', 0.01, 0, 1, 90, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 39, 'Bi_Truss', 0.01, 0.01, 0, 0, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 40, 'Bi_Truss', 0.01, 0.01, 0, 5, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 41, 'Bi_Truss', 0.01, 0.01, 0, 10, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 42, 'Bi_Truss', 0.01, 0.01, 0, 15, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 43, 'Bi_Truss', 0.01, 0.01, 0, 20, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 44, 'Bi_Truss', 0.01, 0.01, 0, 25, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 45, 'Bi_Truss', 0.01, 0.01, 0, 30, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 46, 'Bi_Truss', 0.01, 0.01, 0, 35, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 47, 'Bi_Truss', 0.01, 0.01, 0, 40, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 48, 'Bi_Truss', 0.01, 0.01, 0, 45, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 49, 'Bi_Truss', 0.01, 0.01, 0, 50, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 50, 'Bi_Truss', 0.01, 0.01, 0, 55, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 51, 'Bi_Truss', 0.01, 0.01, 0, 60, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 52, 'Bi_Truss', 0.01, 0.01, 0, 65, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 53, 'Bi_Truss', 0.01, 0.01, 0, 70, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 54, 'Bi_Truss', 0.01, 0.01, 0, 75, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 55, 'Bi_Truss', 0.01, 0.01, 0, 80, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 56, 'Bi_Truss', 0.01, 0.01, 0, 85, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 57, 'Bi_Truss', 0.01, 0.01, 0, 90, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 58, 'Bi_Beam', 0.01, 0.01, 1, 0, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 59, 'Bi_Beam', 0.01, 0.01, 1, 5, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 60, 'Bi_Beam', 0.01, 0.01, 1, 10, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 61, 'Bi_Beam', 0.01, 0.01, 1, 15, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 62, 'Bi_Beam', 0.01, 0.01, 1, 20, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 63, 'Bi_Beam', 0.01, 0.01, 1, 25, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 64, 'Bi_Beam', 0.01, 0.01, 1, 30, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 65, 'Bi_Beam', 0.01, 0.01, 1, 35, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 66, 'Bi_Beam', 0.01, 0.01, 1, 40, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 67, 'Bi_Beam', 0.01, 0.01, 1, 45, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 68, 'Bi_Beam', 0.01, 0.01, 1, 50, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 69, 'Bi_Beam', 0.01, 0.01, 1, 55, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 70, 'Bi_Beam', 0.01, 0.01, 1, 60, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 71, 'Bi_Beam', 0.01, 0.01, 1, 65, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 72, 'Bi_Beam', 0.01, 0.01, 1, 70, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 73, 'Bi_Beam', 0.01, 0.01, 1, 75, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 74, 'Bi_Beam', 0.01, 0.01, 1, 80, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 75, 'Bi_Beam', 0.01, 0.01, 1, 85, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 76, 'Bi_Beam', 0.01, 0.01, 1, 90, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2, 0.01, ],
                      [ 77, 'Uni_BeamVF', 0.01, 0, 1, 45, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2,
                        0.0050, ],
                      [ 78, 'Uni_BeamVF', 0.01, 0, 1, 45, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2,
                        0.0075, ],
                      [ 79, 'Uni_BeamVF', 0.01, 0, 1, 45, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2,
                        0.0100, ],
                      [ 80, 'Uni_BeamVF', 0.01, 0, 1, 45, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2,
                        0.0125, ],
                      [ 81, 'Uni_BeamVF', 0.01, 0, 1, 45, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2,
                        0.0150, ],
                      [ 82, 'Uni_BeamVF', 0.01, 0, 1, 45, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2,
                        0.0175, ],
                      [ 83, 'Uni_BeamVF', 0.01, 0, 1, 45, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2,
                        0.0200, ],
                      [ 84, 'Uni_BeamVF', 0.01, 0, 1, 45, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2,
                        0.0225, ],
                      [ 85, 'Uni_BeamVF', 0.01, 0, 1, 45, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2,
                        0.0250, ],
                      [ 86, 'Uni_BeamVF', 0.01, 0, 1, 45, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2,
                        0.0275, ],
                      [ 87, 'Uni_BeamVF', 0.01, 0, 1, 45, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2,
                        0.0300, ],
                      [ 88, 'Uni_BeamVF', 0.01, 0, 1, 45, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2,
                        0.0325, ],
                      [ 89, 'Uni_BeamVF', 0.01, 0, 1, 45, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2,
                        0.0350, ],
                      [ 90, 'Uni_BeamVF', 0.01, 0, 1, 45, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2,
                        0.0375, ],
                      [ 91, 'Uni_BeamVF', 0.01, 0, 1, 45, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2,
                        0.0400, ],
                      [ 92, 'Bi_BeamVF', 0.01, 0.01, 1, 45, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2,
                        0.0050, ],
                      [ 93, 'Bi_BeamVF', 0.01, 0.01, 1, 45, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2,
                        0.0075, ],
                      [ 94, 'Bi_BeamVF', 0.01, 0.01, 1, 45, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2,
                        0.0100, ],
                      [ 95, 'Bi_BeamVF', 0.01, 0.01, 1, 45, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2,
                        0.0125, ],
                      [ 96, 'Bi_BeamVF', 0.01, 0.01, 1, 45, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2,
                        0.0150, ],
                      [ 97, 'Bi_BeamVF', 0.01, 0.01, 1, 45, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2,
                        0.0175, ],
                      [ 98, 'Bi_BeamVF', 0.01, 0.01, 1, 45, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2,
                        0.0200, ],
                      [ 99, 'Bi_BeamVF', 0.01, 0.01, 1, 45, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2,
                        0.0225, ],
                      [ 100, 'Bi_BeamVF', 0.01, 0.01, 1, 45, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2,
                        0.0250, ],
                      [ 101, 'Bi_BeamVF', 0.01, 0.01, 1, 45, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2,
                        0.0275, ],
                      [ 102, 'Bi_BeamVF', 0.01, 0.01, 1, 45, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2,
                        0.0300, ],
                      [ 103, 'Bi_BeamVF', 0.01, 0.01, 1, 45, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2,
                        0.0325, ],
                      [ 104, 'Bi_BeamVF', 0.01, 0.01, 1, 45, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2,
                        0.0350, ],
                      [ 105, 'Bi_BeamVF', 0.01, 0.01, 1, 45, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2,
                        0.0375, ],
                      [ 106, 'Bi_BeamVF', 0.01, 0.01, 1, 45, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2,
                        0.0400, ],
                      [ 107, 'Bi_BeamMesh', 0.01, 0.01, 1, 45, 1, 1, 0.5, 0.0321, 0.0161, 75000, 0.36, 1000000, 0.2,
                        0.01, ],
                      [ 108, 'Bi_BeamMesh', 0.01, 0.01, 1, 45, 1, 1, 0.5, 0.0226, 0.0113, 75000, 0.36, 1000000, 0.2,
                        0.01, ],
                      [ 109, 'Bi_BeamMesh', 0.01, 0.01, 1, 45, 1, 1, 0.5, 0.0184, 0.0092, 75000, 0.36, 1000000, 0.2,
                        0.01, ],
                      [ 110, 'Bi_BeamMesh', 0.01, 0.01, 1, 45, 1, 1, 0.5, 0.0159, 0.008, 75000, 0.36, 1000000, 0.2,
                        0.01, ],
                      [ 111, 'Bi_BeamMesh', 0.01, 0.01, 1, 45, 1, 1, 0.5, 0.0142, 0.0071, 75000, 0.36, 1000000, 0.2,
                        0.01, ],
                      [ 112, 'Bi_BeamMesh', 0.01, 0.01, 1, 45, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2,
                        0.01, ],
                      [ 113, 'Bi_BeamMesh', 0.01, 0.01, 1, 45, 1, 1, 0.5, 0.012, 0.006, 75000, 0.36, 1000000, 0.2,
                        0.01, ],
                      [ 114, 'Bi_BeamMesh', 0.01, 0.01, 1, 45, 1, 1, 0.5, 0.0112, 0.0056, 75000, 0.36, 1000000, 0.2,
                        0.01, ],
                      [ 115, 'Bi_BeamMesh', 0.01, 0.01, 1, 45, 1, 1, 0.5, 0.0106, 0.0053, 75000, 0.36, 1000000, 0.2,
                        0.01, ],
                      [ 116, 'Bi_BeamMesh', 0.01, 0.01, 1, 45, 1, 1, 0.5, 0.0101, 0.005, 75000, 0.36, 1000000, 0.2,
                        0.01, ],
                      [ 117, 'Bi_BeamMesh', 0.01, 0.01, 1, 30, 1, 1, 0.5, 0.0321, 0.0161, 75000, 0.36, 1000000, 0.2,
                        0.01, ],
                      [ 118, 'Bi_BeamMesh', 0.01, 0.01, 1, 30, 1, 1, 0.5, 0.0226, 0.0113, 75000, 0.36, 1000000, 0.2,
                        0.01, ],
                      [ 119, 'Bi_BeamMesh', 0.01, 0.01, 1, 30, 1, 1, 0.5, 0.0184, 0.0092, 75000, 0.36, 1000000, 0.2,
                        0.01, ],
                      [ 120, 'Bi_BeamMesh', 0.01, 0.01, 1, 30, 1, 1, 0.5, 0.0159, 0.008, 75000, 0.36, 1000000, 0.2,
                        0.01, ],
                      [ 121, 'Bi_BeamMesh', 0.01, 0.01, 1, 30, 1, 1, 0.5, 0.0142, 0.0071, 75000, 0.36, 1000000, 0.2,
                        0.01, ],
                      [ 122, 'Bi_BeamMesh', 0.01, 0.01, 1, 30, 1, 1, 0.5, 0.013, 0.0065, 75000, 0.36, 1000000, 0.2,
                        0.01, ],
                      [ 123, 'Bi_BeamMesh', 0.01, 0.01, 1, 30, 1, 1, 0.5, 0.012, 0.006, 75000, 0.36, 1000000, 0.2,
                        0.01, ],
                      [ 124, 'Bi_BeamMesh', 0.01, 0.01, 1, 30, 1, 1, 0.5, 0.0112, 0.0056, 75000, 0.36, 1000000, 0.2,
                        0.01, ],
                      [ 125, 'Bi_BeamMesh', 0.01, 0.01, 1, 30, 1, 1, 0.5, 0.0106, 0.0053, 75000, 0.36, 1000000, 0.2,
                        0.01, ],
                      [ 126, 'Bi_BeamMesh', 0.01, 0.01, 1, 30, 1, 1, 0.5, 0.0101, 0.005, 75000, 0.36, 1000000, 0.2,
                        0.01, ] ] )

for i in range( 0, data.shape[0], 1 ):
    JobName = str( data[ i, 0 ] )
    ModelName = str( data[ i, 1 ] )
    displacementU1 = float( data[ i, 2 ] )
    displacementU2 = float( data[ i, 3 ] )
    print( '\n' )
    print( 'ID ' + JobName)
    if str( data[ i, 4 ] ) == '0':
        type = 0
    else:
        type = 1
    tetha = float( data[ i, 5 ] )
    size = float( data[ i, 6 ] )
    width = float( data[ i, 7 ] )
    wire = float( data[ i, 8 ] )
    seedMatrix = float( data[ i, 9 ] )
    seedGraphene = float( data[ i, 10 ] )
    Ealuminum = float( data[ i, 11 ] )
    vAluminum = float( data[ i, 12 ] )
    Egraphene = float( data[ i, 13 ] )
    vGraphene = float( data[ i, 14 ] )
    VF = float( data[ i, 15 ] )

    # SECTION
    if type == 1:
        depth = wire
        height = float( VF * size * size * width / wire * wire )
        print( height )
        print( depth )
    else:
        GrapheneArea = float( VF * size * size * width / wire )

    direction = 0
    if displacementU2 != 0:
        direction = 1
        # 0 UNI,
        # 1 BI
    if type == 1:
        BeamOrientation = [ 0.0, 1.0, 0.0 ]
    mdb.Model( modelType=STANDARD_EXPLICIT, name=ModelName )

    # MATRIX
    mdb.models[ ModelName ].ConstrainedSketch( name='__profile__', sheetSize=1.0 )
    mdb.models[ ModelName ].sketches[ '__profile__' ].rectangle( point1=(size / 2.0, size / 2.0),
                                                                 point2=(-size / 2.0, -size / 2.0) )
    mdb.models[ ModelName ].Part( dimensionality=TWO_D_PLANAR, name='MatrixPart', type=DEFORMABLE_BODY )
    mdb.models[ ModelName ].parts[ 'MatrixPart' ].BaseShell( sketch=mdb.models[ ModelName ].sketches[ '__profile__' ] )
    del mdb.models[ ModelName ].sketches[ '__profile__' ]

    # GRAPHENE
    mdb.models[ ModelName ].ConstrainedSketch( name='__profile__', sheetSize=1.0 )
    mdb.models[ ModelName ].sketches[ '__profile__' ].Line(
        point1=(math.cos( tetha / 180.0 * pi ) * wire / 2.0, math.sin( tetha / 180.0 * pi ) * wire / 2.0),
        point2=(-math.cos( tetha / 180.0 * pi ) * wire / 2.0, -math.sin( tetha / 180.0 * pi ) * wire / 2.0) )
    mdb.models[ ModelName ].Part( dimensionality=TWO_D_PLANAR, name='GraphenePart', type=DEFORMABLE_BODY )
    mdb.models[ ModelName ].parts[ 'GraphenePart' ].BaseWire( sketch=mdb.models[ ModelName ].sketches[ '__profile__' ] )
    del mdb.models[ ModelName ].sketches[ '__profile__' ]

    # MESH MATRIX
    mdb.models[ ModelName ].parts[ 'MatrixPart' ].seedPart( deviationFactor=0.1,
                                                            minSizeFactor=0.1, size=seedMatrix )
    mdb.models[ ModelName ].parts[ 'MatrixPart' ].generateMesh()

    # MESH GRAPHENE ASSIGNMENT
    if type == 0:
        mdb.models[ ModelName ].parts[ 'GraphenePart' ].setElementType(
            elemTypes=(ElemType( elemCode=T2D2, elemLibrary=STANDARD ),), regions=(
                mdb.models[ ModelName ].parts[ 'GraphenePart' ].edges.getSequenceFromMask(
                    ('[#1 ]',), ),) )
    if type == 1:
        mdb.models[ ModelName ].parts[ 'GraphenePart' ].setElementType( elemTypes=(
            ElemType( elemCode=B21, elemLibrary=STANDARD ),), regions=(
            mdb.models[ ModelName ].parts[ 'GraphenePart' ].edges.getSequenceFromMask(
                ('[#1 ]',), ),) )

    # MESH GRAPHENE
    mdb.models[ ModelName ].parts[ 'GraphenePart' ].seedPart( deviationFactor=0.1,
                                                              minSizeFactor=0.1, size=seedGraphene )
    mdb.models[ ModelName ].parts[ 'GraphenePart' ].generateMesh()

    # MATERIALS
    mdb.models[ ModelName ].Material( name='AluminumMaterial' )
    mdb.models[ ModelName ].materials[ 'AluminumMaterial' ].Elastic( table=((Ealuminum, vAluminum),) )
    mdb.models[ ModelName ].Material( name='GrapheneMaterial' )
    mdb.models[ ModelName ].materials[ 'GrapheneMaterial' ].Elastic( table=((Egraphene, vGraphene),) )

    # SECTION MATRIZ
    mdb.models[ ModelName ].HomogeneousSolidSection( material='AluminumMaterial',
                                                     name='MatrixSection', thickness=1.0 )

    # SECTION GRAPHENE
    if type == 0:
        mdb.models[ ModelName ].TrussSection( area=GrapheneArea, material='GrapheneMaterial',
                                              name='GrapheneSection' )
    if type == 1:
        # PROFILE BEAM GRAPHENE
        mdb.models[ ModelName ].RectangularProfile( a=depth, b=height, name='BeamProfile' )
        mdb.models[ ModelName ].BeamSection( consistentMassMatrix=False, integration=
        DURING_ANALYSIS, material='GrapheneMaterial', name='GrapheneSection',
                                             poissonRatio=0.0, profile='BeamProfile', temperatureVar=LINEAR )

    # SECTIONS ASSIGNMENT
    mdb.models[ ModelName ].parts[ 'GraphenePart' ].Set( edges=
    mdb.models[ ModelName ].parts[ 'GraphenePart' ].edges.getSequenceFromMask(
        ('[#1 ]',), ), name='GrapheneSectionSet' )
    mdb.models[ ModelName ].parts[ 'GraphenePart' ].SectionAssignment(
        offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=
        mdb.models[ ModelName ].parts[ 'GraphenePart' ].sets[ 'GrapheneSectionSet' ]
        , sectionName='GrapheneSection', thicknessAssignment=FROM_SECTION )
    mdb.models[ ModelName ].parts[ 'MatrixPart' ].Set( faces=
    mdb.models[ ModelName ].parts[ 'MatrixPart' ].faces.getSequenceFromMask( (
        '[#1 ]',), ), name='MatrixSectionSet' )
    mdb.models[ ModelName ].parts[ 'MatrixPart' ].SectionAssignment( offset=0.0,
                                                                     offsetField='', offsetType=MIDDLE_SURFACE, region=
                                                                     mdb.models[ ModelName ].parts[ 'MatrixPart' ].sets[
                                                                         'MatrixSectionSet' ],
                                                                     sectionName='MatrixSection',
                                                                     thicknessAssignment=FROM_SECTION )

    # ASSEMBLY
    mdb.models[ ModelName ].rootAssembly.DatumCsysByDefault( CARTESIAN )
    mdb.models[ ModelName ].rootAssembly.Instance( dependent=ON, name='MatrixAssemblyInstance',
                                                   part=mdb.models[ ModelName ].parts[ 'MatrixPart' ] )
    mdb.models[ ModelName ].rootAssembly.Instance( dependent=ON, name='GrapheneAssemblyInstance',
                                                   part=mdb.models[ ModelName ].parts[ 'GraphenePart' ] )

    # EMBEDDED REGION
    mdb.models[ ModelName ].EmbeddedRegion( absoluteTolerance=0.0, embeddedRegion=
    Region(
        edges=mdb.models[ ModelName ].rootAssembly.instances[ 'GrapheneAssemblyInstance' ].edges.getSequenceFromMask(
            mask=('[#1 ]',), ) ), fractionalTolerance=0.05, hostRegion=None, name=
                                            'EmbeddedRegion', toleranceMethod=BOTH, weightFactorTolerance=1e-06 )
    # CREATE STEP
    mdb.models[ ModelName ].StaticStep( name='Step-1', previous='Initial' )

    # REFERENCE POINT
    mdb.models[ ModelName ].rootAssembly.ReferencePoint( point=[ width / 2 * 1.1, -width / 2 * 1.1, 0 ] )

    # SETS
    mdb.models[ ModelName ].rootAssembly.Set( name='RF', referencePoints=(
        mdb.models[ ModelName ].rootAssembly.referencePoints[ 7 ],) )
    mdb.models[ ModelName ].parts[ 'MatrixPart' ].Set( edges=
    mdb.models[ ModelName ].parts[ 'MatrixPart' ].edges.getSequenceFromMask( (
        '[#8 ]',), ), name='MatrixXset' )
    mdb.models[ ModelName ].parts[ 'MatrixPart' ].Set( edges=
    mdb.models[ ModelName ].parts[ 'MatrixPart' ].edges.getSequenceFromMask( (
        '[#4 ]',), ), name='MatrixYset' )

    # EQUATIONS
    mdb.models[ ModelName ].Equation( name='X_Const', terms=((1.0, 'MatrixAssemblyInstance.MatrixXset', 1), (-1.0,
                                                                                                             'RF', 1)) )
    mdb.models[ ModelName ].Equation( name='Y_Const', terms=((1.0, 'MatrixAssemblyInstance.MatrixYset', 2), (1.0,
                                                                                                             'RF', 2)) )

    # BOUNDARY CONDITIONS
    if direction:
        mdb.models[ ModelName ].DisplacementBC( amplitude=UNSET, createStepName=
        'Step-1', distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None
                                                , name='HorizontalDisplacement', region=Region(
                edges=mdb.models[ ModelName ].rootAssembly.instances[
                    'MatrixAssemblyInstance' ].edges.getSequenceFromMask(
                    mask=('[#2 ]',), ) ), u1=0.0, u2=UNSET, ur3=UNSET )
    else:
        mdb.models[ ModelName ].EncastreBC( createStepName='Step-1', localCsys=
        None, name='Engaste', region=Region(
            edges=mdb.models[ ModelName ].rootAssembly.instances[ 'MatrixAssemblyInstance' ].edges.getSequenceFromMask(
                mask=('[#2 ]',), ) ) )
    mdb.models[ ModelName ].DisplacementBC( amplitude=UNSET, createStepName=
    'Step-1', distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None
                                            , name='LateralDisplacement', region=Region(
            edges=mdb.models[ ModelName ].rootAssembly.instances[ 'MatrixAssemblyInstance' ].edges.getSequenceFromMask(
                mask=('[#1 ]',), ) ), u1=UNSET, u2=0.0, ur3=UNSET )
    mdb.models[ ModelName ].DisplacementBC( amplitude=UNSET, createStepName='Step-1',
                                            distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
                                            'Displacement', region=mdb.models[ ModelName ].rootAssembly.sets[ 'RF' ],
                                            u1=displacementU1,
                                            u2=displacementU2, u3=UNSET )

    # BEAM ORIENTATION
    if type == 1:
        mdb.models[ ModelName ].parts[ 'GraphenePart' ].Set( edges=
        mdb.models[ ModelName ].parts[ 'GraphenePart' ].edges.getSequenceFromMask( (
            '[#1 ]',), ), name='BeamPropertySet' )
        mdb.models[ ModelName ].parts[ 'GraphenePart' ].assignBeamSectionOrientation( method=
                                                                                      N1_COSINES, n1=[ 0.0, 1.0, 0.0 ],
                                                                                      region=
                                                                                      mdb.models[ ModelName ].parts[
                                                                                          'GraphenePart' ].sets[
                                                                                          'BeamPropertySet' ] )
        mdb.models[ ModelName ].rootAssembly.regenerate()

    # JOB CREATION AND SUBMISSION
    JobName = "ID_" + JobName
    mdb.Job( atTime=None, contactPrint=OFF, description='', echoPrint=OFF,
             explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF,
             memory=90, memoryUnits=PERCENTAGE, model=ModelName, modelPrint=OFF,
             multiprocessingMode=DEFAULT, name=JobName, nodalOutputPrecision=SINGLE,
             numCpus=1, numGPUs=0, queue=None, resultsFormat=ODB, scratch='', type=
             ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0 )
    mdb.jobs[ JobName ].submit( consistencyChecking=OFF )

