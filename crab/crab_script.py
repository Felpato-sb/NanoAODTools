#!/usr/bin/env python3
import os
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2 import *
from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles,runsAndLumis
from PhysicsTools.NanoAODTools.postprocessing.modules.common.MCweight_writer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.TagSkim import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.GenPart_MomFirstCp import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.nanoprepro_v2 import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.nanoTopcandidate_v2 import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.nanoTopevaluate import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.topselection import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.nanoTopEvaluate_MultiScore import *
p=PostProcessor('.', inputFiles(), '', modules=[MCweight_writer(), PreSkimSetup(), InitSkim(), GenPart_MomFirstCp(flavour='-5,-4,-3,-2,-1,1,2,3,4,5,6,-6,24,-24'), nanoprepro(), nanoTopcand(True), W_Top_Tagger(), Re_Bo_Tagger(), Merge_Tagger(), nanoTopevaluate_MultiScore()], provenance=True, fwkJobReport=True, histFileName='hist.root', histDirName='plots', outputbranchsel='keep_and_drop.txt')
p.run()
print('DONE')
