import PhysicsTools.HeppyCore.framework.config as cfg

#Load all analyzers
from CMGTools.ObjectsStudies.analyzers.metCoreModules_cff import *

##------------------------------------------
##  PRODUCER
##------------------------------------------

from CMGTools.TTHAnalysis.samples.samples_13TeV_PHYS14 import triggers_1mu, triggers_mumu_iso, triggers_1mu_isolow

triggers_8TeV_mumu = ["HLT_Mu17_Mu8_v*","HLT_Mu17_TkMu8_v*"]
triggers_8TeV_1mu = [ 'HLT_IsoMu24_eta2p1_v*' ]

triggerFlagsAna.triggerBits = {
#            'SingleMu' : triggers_1mu_isolow,
#            'DoubleMu' : triggers_mumu_iso,
            'SingleMu' : triggers_8TeV_1mu,
            'DoubleMu' : triggers_8TeV_mumu,
}

#-------- SEQUENCE

##from CMGTools.TTHAnalysis.analyzers.treeProducerMET import *
from CMGTools.ObjectsStudies.analyzers.treeProducerMET import *

treeProducer = cfg.Analyzer(
     AutoFillTreeProducer, name='treeProducerMET',
     vectorTree = True,
     saveTLorentzVectors = False,  # can set to True to get also the TLorentzVectors, but trees will be bigger
     PDFWeights = PDFWeights,
     globalVariables = met_globalVariables,
     globalObjects = met_globalObjects,
     collections = met_collections,
     defaultFloatType = 'F',
)

## same as MET perf analyszer
treeProducer.treename = 'Events'

#-------- SEQUENCE

metAna.doTkMet = False ## broken in 74

metSequence = cfg.Sequence(
    metCoreSequence +[treeProducer]
    )
# -------------------- lepton modules below needed for the DoubleMuon

ttHLepSkim.minLeptons = 2

metSequence.insert(metSequence.index(lepAna)+1,
                   ttHLepSkim)
metSequence.insert(metSequence.index(lepAna)+2,
                   ttHZskim)

###---- to switch off the comptrssion
#treeProducer.isCompressed = 0

#-------- SAMPLES AND TRIGGERS -----------
#from CMGTools.TTHAnalysis.samples.samples_13TeV_CSA14 import * 
#from CMGTools.TTHAnalysis.samples.samples_13TeV_CSA14v2 import *
from CMGTools.TTHAnalysis.samples.samples_13TeV_PHYS14 import *
from CMGTools.ObjectsStudies.samples.samples_METPOG_private import *
from CMGTools.ObjectsStudies.samples.samples_METPOG_relVal import *

#-------- HOW TO RUN

test = 6

   # -----------------------PHYS14 options -------------------------------------------------------------------- #

if test==1:
    # test a single component, using a single thread.
    ## 40 ns ttbar DY
#    comp=DYJetsToLL_M50_PU4bx50
#    comp.files = comp.files[:1]
    ## 25 ns ttbar PHYS14
#    comp = TTJets
#    comp.files = comp.files[:1]
    comp=TTJets
    comp.files = ['/afs/cern.ch/work/d/dalfonso/public/ttjets_miniaodsim_00C90EFC-3074-E411-A845-002590DB9262.root']
    selectedComponents = [comp]
    comp.splitFactor = 1

elif test==2:
    # test all components (1 thread per component).
    selectedComponents = [ DYJetsToLL_M50_PU4bx50,DYJetsToLL_M50]
    for comp in selectedComponents:
        comp.splitFactor = 251
        comp.files = comp.files[:]
        #comp.files = comp.files[:1]

    # ----------------------re-reco options 723 --------------------------------------------------------------------- #

elif test==3:
    # test a single component, using a single thread.
    ##
    selectedComponents = [DoubleMuparked_HcalExtValid_zMu2012D_v1]
    comp=DoubleMuparked_HcalExtValid_zMu2012D_v1
    comp.files = comp.files[:1]
    comp.triggers = triggers_8TeV_mumu
    comp.json = dataDir+'/json/diMu_732overlap_miniAOD.json'
    selectedComponents = [comp]
    comp.splitFactor = 1

elif test==4:
    # test all components (1 thread per component).
##    selectedComponents = [ DYJetsToLL_M50_PU4bx50,DYJetsToLL_M50 ]
    selectedComponents = [DoubleMuparked_HcalExtValid_zMu2012D_v1]
    for comp in selectedComponents:
        comp.splitFactor = 250
        comp.fineSplitFactor = 10
#        comp.splitFactor = 1
        comp.files = comp.files[:]
        comp.triggers = triggers_8TeV_mumu
        comp.json = dataDir+'/json/diMu_732overlap_miniAOD.json'
        #comp.files = comp.files[:1]

    # ----------------------re-reco options 740_pre9 --------------------------------------------------------------------- #

elif test==5:
    # test a single component, using a single thread.
    ##
    selectedComponents = [DoubleMuparked_1Apr_RelVal_dm2012D_v2]
    comp=DoubleMuparked_1Apr_RelVal_dm2012D_v2
    comp.files = comp.files[:1]
    comp.triggers = triggers_8TeV_mumu
    comp.json = dataPrivDir+'/json/diMu_740pre9_miniAOD.json'
    selectedComponents = [comp]
    comp.splitFactor = 1

elif test==6:
    # test all components (1 thread per component).
##    selectedComponents = [ DYJetsToLL_M50_PU4bx50,DYJetsToLL_M50 ]
##    selectedComponents = [DoubleMuparked_1Apr_RelVal_dm2012D_v2]
    selectedComponents = [DoubleMuParked_740_fixes] 
    for comp in selectedComponents:
#        comp.splitFactor = 251
        comp.splitFactor = 1
        comp.files = comp.files[:]
        comp.triggers = triggers_8TeV_mumu
        comp.json = dataPrivDir+'/json/diMu_740pre9_miniAOD.json'
        #comp.files = comp.files[:1]

    # ----------------------relVal --------------------------------------------------------------------- #

elif test==7:
#    selectedComponents = [ DoubleMu_zMu2011A_CMSSW_7_0_6 , DoubleMu_zMu2011A_CMSSW_7_3_0, DoubleMu_zMu2011A_CMSSW_7_3_1_patch1, DoubleMu_zMu2011A_CMSSW_7_3_3, DoubleMu_zMu2011A_7_4_0_pre9 ]
    selectedComponents = [ DoubleMu_zMu2011A_CMSSW_7_3_0 ]
    for comp in selectedComponents:
        comp.splitFactor = 1
        comp.files = comp.files[:]
#        comp.triggers = triggers_8TeV_mumu
#        comp.json = dataDir+'/json/diMu_740pre9_miniAOD.json'

    # ---------------------- PF (hadron and egamma) calibration studies --------------------------------------------------------------------- #

elif test==8:
#    selectedComponents = [ RelValZMM_25ns_7_3_1_patch1, RelValZMM_25ns_7_3_3, RelValZMM_25ns_7_4_0_pre9, RelValZMM_50ns_7_3_1_patch1, RelValZMM_50ns_7_3_3, RelValZMM_50ns_7_4_0_pre9 ]
#    selectedComponents = [ RelValZMM_25ns_7_4_0_pre9, RelValZMM_50ns_7_4_0_pre9 ]
#    selectedComponents = MVAegammaMC
    selectedComponents = [ DoubleMuParked_1Apr_RelVal_dm2012D_v2_newPFHCalib , DoubleMuParked_1Apr_RelVal_dm2012D_v2_oldPFHCalib , DoubleMuparked_1Apr_RelVal_dm2012D_v2 ]

    for comp in selectedComponents:
        comp.splitFactor = 1
        comp.files = comp.files[:]
        comp.triggers = triggers_8TeV_mumu

elif test==9:
    selectedComponents = [ JetHT_GR_R_74_V8_1Apr_v1_oldPFHCalib , JetHT_GR_R_74_V8_1Apr_v1_newPFHCalib ]
    for comp in selectedComponents:
#        comp.splitFactor = 1
        comp.splitFactor = 250
        comp.files = comp.files[:]

elif test==10:
    selectedComponents = relValMC
#    selectedComponents = [ RelValZMM_7_4_1 ]    selectedComponents = [ RelValZMM_7_4_1 ]
#    selectedComponents = [ RelValZMM_7_4_0_pre9 ]
    for comp in selectedComponents:
#        comp.splitFactor = 1
        comp.splitFactor = 250
        comp.files = comp.files[:]


    # ------------------------------------------------------------------------------------------- #


from PhysicsTools.HeppyCore.framework.services.tfile import TFileService 
output_service = cfg.Service(
      TFileService,
      'outputfile',
      name="outputfile",
      fname='METtree.root',
      option='recreate'
    )

from PhysicsTools.HeppyCore.framework.heppy import getHeppyOption


# the following is declared in case this cfg is used in input to the heppy.py script                                                                                                                   
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events


from CMGTools.TTHAnalysis.tools.EOSEventsWithDownload import EOSEventsWithDownload
event_class = EOSEventsWithDownload
if getHeppyOption("nofetch"):
    event_class = Events 

config = cfg.Config( components = selectedComponents,
                     sequence = metSequence,
                     services = [output_service],
#                     events_class = event_class)
                     events_class = Events)

#printComps(config.components, True)
        
