import PhysicsTools.HeppyCore.framework.config as cfg

import os

#####COMPONENT CREATOR

from CMGTools.TTHAnalysis.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

dataDir = os.environ['CMSSW_BASE']+"/src/CMGTools/TTHAnalysis/data"
json=dataDir+'/json/Cert_Run2012ABCD_22Jan2013ReReco.json'
### samples for HCAL reco validation
JetHT_HcalExtValid_jet2012D_v1 = cfg.DataComponent(
    name = 'JetHT_HcalExtValid_jet2012D_v1',
    files = kreator.getFilesFromEOS('JetHT_HcalExtValid_jet2012D_v1', '/JetHT/CMSSW_7_3_2_patch1-GR_R_73_V0_HcalExtValid_RelVal_jet2012D-v1/MINIAOD', '/store/relval/CMSSW_7_3_2_patch1/JetHT/MINIAOD/GR_R_73_V0_HcalExtValid_RelVal_jet2012D-v1/00000/'),
    intLumi = 1,
    triggers = [],
    json = json
    )
JetHT_HcalExtValid_jet2012D_v2 = cfg.DataComponent(
    name = 'JetHT_HcalExtValid_jet2012D_v2',
    files = kreator.getFilesFromEOS('JetHT_HcalExtValid_jet2012D_v2', '/JetHT/CMSSW_7_3_2_patch1-GR_R_73_V0_HcalExtValid_RelVal_jet2012D-v2/MINIAOD', '/store/relval/CMSSW_7_3_2_patch1/JetHT/MINIAOD/GR_R_73_V0_HcalExtValid_RelVal_jet2012D-v2/00000/'),
    intLumi = 1,
    triggers = [],
    json = json
    )

DoubleMuparked_HcalExtValid_zMu2012D_v1 = cfg.DataComponent(
    name = 'DoubleMuparked_HcalExtValid_zMu2012D_v1',
    files = kreator.getFilesFromEOS('DoubleMuparked_HcalExtValid_zMu2012D_v1', '/DoubleMuParked/CMSSW_7_3_2_patch1-GR_R_73_V0_HcalExtValid_RelVal_zMu2012D-v1/MINIAOD', '/store/relval/CMSSW_7_3_2_patch1/DoubleMuParked/MINIAOD/GR_R_73_V0_HcalExtValid_RelVal_zMu2012D-v1/00000/'),
    intLumi = 1,
    triggers = [],
#    json = json
# below the json that correspond the the 740_pre9 re-reco of the same runD     
    json = json
    )


#----------- 74X re-reco ---------------

DoubleMuparked_1Apr_RelVal_dm2012D_v2 = cfg.DataComponent(
    name = 'DoubleMuparked_1Apr_RelVal_dm2012D_v2',
    files = kreator.getFilesFromEOS('DoubleMuparked_1Apr_RelVal_dm2012D_v2', '/DoubleMuParked/CMSSW_7_4_0_pre9_ROOT6-GR_R_74_V8_1Apr_RelVal_dm2012D-v2/MINIAOD', '/store/relval/CMSSW_7_4_0_pre9_ROOT6/DoubleMuParked/MINIAOD/GR_R_74_V8_1Apr_RelVal_dm2012D-v2/00000/'),
    intLumi = 1,
    triggers = [],
#    json = json
# below the json that correspond the the 740_pre9 re-reco of the same runD     
    json = dataDir+'/json/diMu_740pre9_miniAOD.json' 
    )

dataSamplesAll = [JetHT_HcalExtValid_jet2012D_v1, JetHT_HcalExtValid_jet2012D_v2, DoubleMuparked_HcalExtValid_zMu2012D_v1, DoubleMuparked_1Apr_RelVal_dm2012D_v2]


#----------- 2011 re-reco ---------------

DoubleMu_zMu2011A_CMSSW_7_0_6 = cfg.DataComponent(
    name = 'DoubleMu_zMu2011A_7_0_6',
    files = kreator.getFilesFromEOS('DoubleMu_zMu2011A_7_0_6', '/DoubleMu/MINIAOD/GR_70_V2_AN1_RelVal_zMu2011A-v1/MINIAOD', '/store/relval/CMSSW_7_0_6/DoubleMu/MINIAOD/GR_70_V2_AN1_RelVal_zMu2011A-v1/00000/'),
    )

DoubleMu_zMu2011A_CMSSW_7_3_0 = cfg.DataComponent(
    name = 'DoubleMu_zMu2011A_CMSSW_7_3_0',
    files = kreator.getFilesFromEOS('DoubleMu_zMu2011A_7_3_0', '/DoubleMu/MINIAOD/GR_R_73_V0A_RelVal_zMu2011A-v1/MINIAOD', '/eos/cms/store/relval/CMSSW_7_3_0/DoubleMu/MINIAOD/GR_R_73_V0A_RelVal_zMu2011A-v1/00000/'),
    )

DoubleMu_zMu2011A_CMSSW_7_3_1_patch1 = cfg.DataComponent(
    name = 'DoubleMu_zMu2011A_CMSSW_7_3_1_patch1',
    files = kreator.getFilesFromEOS('DoubleMu_zMu2011A_7_3_1_patch1', '/DoubleMu/MINIAOD/GR_R_73_V0A_RelVal_zMu2011A-v1/MINIAOD', '/store/relval/CMSSW_7_3_1_patch1/DoubleMu/MINIAOD/GR_R_73_V0A_RelVal_zMu2011A-v1/00000/'),
    )

DoubleMu_zMu2011A_CMSSW_7_3_3 = cfg.DataComponent(
    name = 'DoubleMu_zMu2011A_CMSSW_7_3_3',
    files = kreator.getFilesFromEOS('DoubleMu_zMu2011A_7_3_3', '/DoubleMu/MINIAOD/GR_R_73_V2A_RelVal_zMu2011A-v1/MINIAOD', '/store/relval/CMSSW_7_3_3/DoubleMu/MINIAOD/GR_R_73_V2A_RelVal_zMu2011A-v1/00000/'),
    )

DoubleMu_zMu2011A_7_4_0_pre9 = cfg.DataComponent(
    name = 'DoubleMu_zMu2011A_7_4_0_pre9',
    files = kreator.getFilesFromEOS('DoubleMu_zMu2011A_7_4_0_pre9', '/DoubleMu/MINIAOD/GR_R_74_V8A_RelVal_zMu2011A-v1/MINIAOD', '/store/relval/CMSSW_7_4_0_pre9/DoubleMu/MINIAOD/GR_R_74_V8A_RelVal_zMu2011A-v1/00000/'),
    )

data2011All = [ DoubleMu_zMu2011A_CMSSW_7_0_6 , DoubleMu_zMu2011A_CMSSW_7_3_0, DoubleMu_zMu2011A_CMSSW_7_3_1_patch1, DoubleMu_zMu2011A_CMSSW_7_3_3, DoubleMu_zMu2011A_7_4_0_pre9 ]

#----------- MC relVal --------------

RelValZMM_25ns_7_3_1_patch1 = cfg.DataComponent(
    name = 'RelValZMM_25ns_7_3_1_patch1',
    files = kreator.getFilesFromEOS('RelValZMM_25ns_7_3_1_patch1', '/RelValZMM_13/MINIAOD/PU25ns_MCRUN2_73_V9-v1/MINIAOD', '/store/relval/CMSSW_7_3_1_patch1/RelValZMM_13/MINIAODSIM/PU25ns_MCRUN2_73_V9-v1/00000/'),
    )

RelValZMM_25ns_7_3_3 = cfg.DataComponent(
    name = 'RelValZMM_25ns_7_3_3',
    files = kreator.getFilesFromEOS('RelValZMM_25ns_7_3_3', '/RelValZMM_13/MINIAOD/PU25ns_MCRUN2_73_V11-v1/MINIAOD', '/eos/cms/store/relval/CMSSW_7_3_3/RelValZMM_13/MINIAODSIM/PU25ns_MCRUN2_73_V11-v1/00000/'),
    )

RelValZMM_25ns_7_4_0_pre9 = cfg.DataComponent(
    name = 'RelValZMM_25ns_7_4_0_pre9',
    files = kreator.getFilesFromEOS('RelValZMM_25ns_7_4_0_pre9', '/RelValZMM_7_4_0_pre9/MINIAOD/PU25ns_MCRUN2_74_V7-v1/MINIAOD', '/store/relval/CMSSW_7_4_0_pre9/RelValZMM_13/MINIAODSIM/PU25ns_MCRUN2_74_V7-v1/00000/'),
    )

#------

RelValZMM_50ns_7_3_1_patch1 = cfg.DataComponent(
    name = 'RelValZMM_50ns_7_3_1_patch1',
    files = kreator.getFilesFromEOS('RelValZMM_50ns_7_3_1_patch1', '/RelValZMM_13/MINIAOD/PU50ns_MCRUN2_73_V9-v1/MINIAOD', '/store/relval/CMSSW_7_3_1_patch1/RelValZMM_13/MINIAODSIM/PU50ns_MCRUN2_73_V9-v1/00000/'),
    )

RelValZMM_50ns_7_3_3 = cfg.DataComponent(
    name = 'RelValZMM_50ns_7_3_3',
    files = kreator.getFilesFromEOS('RelValZMM_50ns_7_3_3', '/RelValZMM_13/MINIAOD/PU50ns_MCRUN2_73_V10-v1/MINIAOD', '/eos/cms/store/relval/CMSSW_7_3_3/RelValZMM_13/MINIAODSIM/PU50ns_MCRUN2_73_V10-v1/00000/'),
    )

RelValZMM_50ns_7_4_0_pre9 = cfg.DataComponent(
    name = 'RelValZMM_50ns_7_4_0_pre9',
    files = kreator.getFilesFromEOS('RelValZMM_50ns_7_4_0_pre9', '/RelValZMM_7_4_0_pre9/MINIAOD/PU50ns_MCRUN2_74_V6-v1/MINIAOD', '/store/relval/CMSSW_7_4_0_pre9/RelValZMM_13/MINIAODSIM/PU50ns_MCRUN2_74_V6-v1/00000/'),
    )


relValMC = [ RelValZMM_25ns_7_3_1_patch1, RelValZMM_25ns_7_3_3, RelValZMM_25ns_7_4_0_pre9, RelValZMM_50ns_7_3_1_patch1, RelValZMM_50ns_7_3_3, RelValZMM_50ns_7_4_0_pre9 ]

#-----------DATA---------------

for comp in dataSamplesAll:
    comp.splitFactor = 1
    comp.triggers = []
#    comp.isMC = False
#    comp.isData = True

for comp in data2011All:
    comp.splitFactor = 1
    comp.triggers = []
    comp.intLumi = 1
    comp.json = dataDir+'/json/Cert_160404-180252_7TeV_ReRecoNov08_Collisions11.json'
#    comp.isMC = False
#    comp.isData = True

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
