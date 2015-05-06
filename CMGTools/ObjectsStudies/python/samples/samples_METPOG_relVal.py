import PhysicsTools.HeppyCore.framework.config as cfg

import os

#####COMPONENT CREATOR

from CMGTools.TTHAnalysis.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

dataDir = os.environ['CMSSW_BASE']+"/src/CMGTools/TTHAnalysis/data"
dataPrivDir = os.environ['CMSSW_BASE']+"/src/CMGTools/ObjectsStudies/data"

json=dataDir+'/json/Cert_Run2012ABCD_22Jan2013ReReco.json'


#------

RelValZMM_7_4_1 = cfg.DataComponent(
    name = 'RelValZMM_7_4_1',
    files = kreator.getFilesFromEOS('RelValZMM_7_4_1', '/RelValZMM_7_4_1/MINIAOD/MCRUN2_74_V9_extended-v2/MINIAOD', '/store/relval/CMSSW_7_4_1//RelValZMM_13/MINIAODSIM/MCRUN2_74_V9_extended-v2/00000/'),
    )

RelValZMM_7_4_0_pre9 = cfg.DataComponent(
    name = 'RelValZMM_7_4_0_pre9',
    files = kreator.getFilesFromEOS('RelValZMM_7_4_0_pre9', '/RelValZMM_7_4_0_pre9/MINIAOD/MCRUN2_74_V7_extended-v2/MINIAOD', '/store/relval/CMSSW_7_4_0_pre9/RelValZMM_13/MINIAODSIM/MCRUN2_74_V7_extended-v2/00000/'),
    )

relValMC = [ RelValZMM_7_4_1, RelValZMM_7_4_0_pre9 ]


#----------- settingg ---------------


for comp in relValMC:
    comp.splitFactor = 1
    comp.triggers = []
    comp.isMC = True
    comp.isData = False

#if __name__ == "__main__":
#   import sys
#   if "test" in sys.argv:
#       from CMGTools.TTHAnalysis.samples.ComponentCreator import testSamples
#       testSamples(mcSamples)
