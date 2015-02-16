import PhysicsTools.HeppyCore.framework.config as cfg

from PhysicsTools.Heppy.analyzers.core.all import *
from PhysicsTools.Heppy.analyzers.objects.all import *
from PhysicsTools.Heppy.analyzers.gen.all import *
import os

##------------------------------------------
##  Core modules
##------------------------------------------

from CMGTools.TTHAnalysis.analyzers.ttHhistoCounterAnalyzer import ttHhistoCounterAnalyzer
susyCounter = cfg.Analyzer(
    ttHhistoCounterAnalyzer, name="ttHhistoCounterAnalyzer",
    )

skimAnalyzer = cfg.Analyzer(
    SkimAnalyzerCount, name='skimAnalyzerCount',
    useLumiBlocks = False,
    )

# Pick individual events (normally not in the path)
eventSelector = cfg.Analyzer(
    EventSelector,name="EventSelector",
    toSelect = []  # here put the event numbers (actual event numbers from CMSSW)
    )

PDFWeights = []

# Apply json file (if the dataset has one)
jsonAna = cfg.Analyzer(
    JSONAnalyzer, name="JSONAnalyzer",
    )

# Filter using the 'triggers' and 'vetoTriggers' specified in the dataset
triggerAna = cfg.Analyzer(
    TriggerBitFilter, name="TriggerBitFilter",
    )

# Create flags for trigger bits
triggerFlagsAna = cfg.Analyzer(
    TriggerBitAnalyzer, name="TriggerFlags",
    processName = 'HLT',
    triggerBits = {
        # "<name>" : [ 'HLT_<Something>_v*', 'HLT_<SomethingElse>_v*' ] 
    }
    )
# Create flags for MET filter bits
eventFlagsAna = cfg.Analyzer(
    TriggerBitAnalyzer, name="EventFlags",
    processName = 'PAT',
    outprefix   = 'Flag',
    triggerBits = {
        "HBHENoiseFilter" : [ "Flag_HBHENoiseFilter" ],
        "CSCTightHaloFilter" : [ "Flag_CSCTightHaloFilter" ],
        "hcalLaserEventFilter" : [ "Flag_hcalLaserEventFilter" ],
        "EcalDeadCellTriggerPrimitiveFilter" : [ "Flag_EcalDeadCellTriggerPrimitiveFilter" ],
        "goodVertices" : [ "Flag_goodVertices" ],
        "trackingFailureFilter" : [ "Flag_trackingFailureFilter" ],
        "eeBadScFilter" : [ "Flag_eeBadScFilter" ],
        "ecalLaserCorrFilter" : [ "Flag_ecalLaserCorrFilter" ],
        "trkPOGFilters" : [ "Flag_trkPOGFilters" ],
        "trkPOG_manystripclus53X" : [ "Flag_trkPOG_manystripclus53X" ],
        "trkPOG_toomanystripclus53X" : [ "Flag_trkPOG_toomanystripclus53X" ],
        "trkPOG_logErrorTooManyClusters" : [ "Flag_trkPOG_logErrorTooManyClusters" ],
        "METFilters" : [ "Flag_METFilters" ],
    }
    )

# Select a list of good primary vertices (generic)
vertexAna = cfg.Analyzer(
    VertexAnalyzer, name="VertexAnalyzer",
    vertexWeight = None,
    fixedWeight = 1,
    verbose = False
    )


# This analyzer actually does the pile-up reweighting (generic)
pileUpAna = cfg.Analyzer(
    PileUpAnalyzer, name="PileUpAnalyzer",
    true = True,  # use number of true interactions for reweighting
    makeHists=False
    )

##------------------------------------------
##  gen
##------------------------------------------

## Gen Info Analyzer (generic, but should be revised)
genAna = cfg.Analyzer(
    GeneratorAnalyzer, name="GeneratorAnalyzer",
    # BSM particles that can appear with status <= 2 and should be kept
    stableBSMParticleIds = [ 1000022 ],
    # Particles of which we want to save the pre-FSR momentum (a la status 3).
    # Note that for quarks and gluons the post-FSR doesn't make sense,
    # so those should always be in the list
    savePreFSRParticleIds = [ 1,2,3,4,5, 11,12,13,14,15,16, 21 ],
    # Make also the list of all genParticles, for other analyzers to handle
    makeAllGenParticles = True,
    # Make also the splitted lists
    makeSplittedGenLists = True,
    allGenTaus = False,
    # Print out debug information
    verbose = False,
    )

##------------------------------------------
##  leptons 
##------------------------------------------

# Lepton Analyzer (generic)
lepAna = cfg.Analyzer(
    LeptonAnalyzer, name="leptonAnalyzer",
    # input collections
    muons='slimmedMuons',
    electrons='slimmedElectrons',
    rhoMuon= 'fixedGridRhoFastjetAll',
    rhoElectron = 'fixedGridRhoFastjetAll',
    # energy scale corrections and ghost muon suppression (off by default)
    doMuScleFitCorrections=False, # "rereco"
    doRochesterCorrections=False,
    doElectronScaleCorrections=False, # "embedded" in 5.18 for regression
    doSegmentBasedMuonCleaning=False,
    # inclusive very loose muon selection
    inclusive_muon_id  = "POG_ID_Loose",
    inclusive_muon_pt  = 3,
    inclusive_muon_eta = 2.4,
    inclusive_muon_dxy = 0.5,
    inclusive_muon_dz  = 1.0,
    # loose muon selection
    loose_muon_id     = "POG_ID_Loose",
    loose_muon_pt     = 5,
    loose_muon_eta    = 2.4,
    loose_muon_dxy    = 0.05,
    loose_muon_dz     = 0.1,
    loose_muon_relIso = 0.5,
    # inclusive very loose electron selection
    inclusive_electron_id  = "",
    inclusive_electron_pt  = 5,
    inclusive_electron_eta = 2.5,
    inclusive_electron_dxy = 0.5,
    inclusive_electron_dz  = 1.0,
    inclusive_electron_lostHits = 1.0,
    # loose electron selection
    loose_electron_id     = "POG_Cuts_ID_2012_Veto_full5x5",
    loose_electron_pt     = 7,
    loose_electron_eta    = 2.4,
    loose_electron_dxy    = 0.05,
    loose_electron_dz     = 0.1,
    loose_electron_relIso = 0.5,
    loose_electron_lostHits = 1.0,
    # muon isolation correction method (can be "rhoArea" or "deltaBeta")
    mu_isoCorr = "rhoArea" ,
    mu_effectiveAreas = "Phys14_25ns_v1", #(can be 'Data2012' or 'Phys14_25ns_v1')
    # electron isolation correction method (can be "rhoArea" or "deltaBeta")
    ele_isoCorr = "rhoArea" ,
    el_effectiveAreas = "Phys14_25ns_v1" , #(can be 'Data2012' or 'Phys14_25ns_v1')
    ele_tightId = "Cuts_2012" ,
    # Mini-isolation, with pT dependent cone: will fill in the miniRelIso, miniRelIsoCharged, miniRelIsoNeutral variables of the leptons (see https://indico.cern.ch/event/368826/ )
    doMiniIsolation = False, # off by default since it requires access to all PFCandidates 
    packedCandidates = 'packedPFCandidates',
    miniIsolationPUCorr = 'rhoArea', # Allowed options: 'rhoArea' (EAs for 03 cone scaled by R^2), 'deltaBeta', 'raw' (uncorrected), 'weights' (delta beta weights; not validated)
    miniIsolationVetoLeptons = None, # use 'inclusive' to veto inclusive leptons and their footprint in all isolation cones
    # minimum deltaR between a loose electron and a loose muon (on overlaps, discard the electron)
    min_dr_electron_muon = 0.02,
    # do MC matching 
    do_mc_match = True, # note: it will in any case try it only on MC, not on data
    match_inclusiveLeptons = False, # match to all inclusive leptons
    )

## Lepton-based Skim (generic, but requirements depend on the final state)
from CMGTools.TTHAnalysis.analyzers.ttHLepSkimmer import ttHLepSkimmer
ttHLepSkim = cfg.Analyzer(
    ttHLepSkimmer, name='ttHLepSkimmer',
    minLeptons = 0,
    maxLeptons = 999,
    #idCut  = "lepton.relIso03 < 0.2" # can give a cut
    #ptCuts = [20,10],                # can give a set of pt cuts on the leptons
    )

##------------------------------------------
##  MET
##------------------------------------------

metAna = cfg.Analyzer(
    METAnalyzer, name="metAnalyzer",
    doTkMet = True,
    doMetNoMu = False,
    doMetNoPhoton = False,
    recalibrate = False,
    candidates='packedPFCandidates',
    candidatesTypes='std::vector<pat::PackedCandidate>',
    dzMax = 0.1,
    )


##------------------------------------------
##  Z skim
##------------------------------------------

from CMGTools.TTHAnalysis.analyzers.ttHmllSkimmer import ttHmllSkimmer
# Tree Producer                                                                                                                                                                         
ttHZskim = cfg.Analyzer(
            ttHmllSkimmer, name='ttHmllSkimmer',
            lepId=[13],
            maxLeps=3,
            massMin=60,
            massMax=120,
            doZGen = False,
            doZReco = True
            )


##------------------------------------------
##  PRODUCER
##------------------------------------------

from CMGTools.TTHAnalysis.samples.samples_13TeV_PHYS14 import triggers_1mu, triggers_mumu_iso, triggers_1mu_isolow

triggerFlagsAna.triggerBits = {
            'SingleMu' : triggers_1mu_isolow,
            'DoubleMu' : triggers_mumu_iso,
}

#-------- SEQUENCE

from CMGTools.TTHAnalysis.analyzers.treeProducerMET import *

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


metSequence = [
    susyCounter,
    skimAnalyzer,
   #eventSelector,
    jsonAna,
    triggerAna,
    pileUpAna,
    genAna,
    vertexAna,
##### lepton modules below
    lepAna,
    ttHLepSkim,
    ttHZskim,
##### met modules below
    metAna,
    eventFlagsAna,
##### tree
    treeProducer,
]


###---- to switch off the comptrssion
#treeProducer.isCompressed = 0

#-------- SAMPLES AND TRIGGERS -----------
#from CMGTools.TTHAnalysis.samples.samples_13TeV_CSA14 import * 
#from CMGTools.TTHAnalysis.samples.samples_13TeV_CSA14v2 import *
from CMGTools.TTHAnalysis.samples.samples_13TeV_PHYS14 import *

#-------- HOW TO RUN
test = 2
if test==1:
    # test a single component, using a single thread.
    ## 25 ns ttbar PHYS14
#    comp = TTJets
#    comp.files = comp.files[:1]
#    comp=TTJets
#    comp.files = ['/afs/cern.ch/work/d/dalfonso/public/ttjets_miniaodsim_00C90EFC-3074-E411-A845-002590DB9262.root']
    comp=DYJetsToLL_M50_PU4bx50
    comp.files = comp.files[:1]

    selectedComponents = [comp]
    comp.splitFactor = 10
elif test==2:
    selectedComponents = [ DYJetsToLL_M50_PU4bx50,DYJetsToLL_M50 ]
    # test all components (1 thread per component).
    for comp in selectedComponents:
        comp.splitFactor = 251
        comp.files = comp.files[:]
        #comp.files = comp.files[:1]

from PhysicsTools.HeppyCore.framework.services.tfile import TFileService 
output_service = cfg.Service(
      TFileService,
      'outputfile',
      name="outputfile",
      fname='METtree.root',
      option='recreate'
    )

# the following is declared in case this cfg is used in input to the heppy.py script                                                                                                                   
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
config = cfg.Config( components = selectedComponents,
                     sequence = metSequence,
                     services = [output_service],
                     events_class = Events)

#printComps(config.components, True)
        
