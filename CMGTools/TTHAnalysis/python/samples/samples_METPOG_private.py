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

#-----------DATA---------------

for comp in dataSamplesAll:
    comp.splitFactor = 1
    comp.triggers = []
#    comp.isMC = False
#    comp.isData = True

#if __name__ == "__main__":
#   import sys
#   if "test" in sys.argv:
#       from CMGTools.TTHAnalysis.samples.ComponentCreator import testSamples
#       testSamples(mcSamples)
