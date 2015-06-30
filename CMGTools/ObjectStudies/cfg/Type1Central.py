import FWCore.ParameterSet.Config as cms
import os

# Define the CMSSW process
process = cms.Process("TREE")

# Load the standard set of configuration modules
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

# Message Logger settings
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.destinations = ['cout', 'cerr']
process.MessageLogger.cerr.FwkReport.reportEvery = 100

# Set the process options -- Display summary at the end, enable unscheduled execution
process.options = cms.untracked.PSet(
    allowUnscheduled = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(True) 
)

#-----------------  global Tag and  JEC parameters from local database file ------------------------

process.GlobalTag.globaltag = 'MCRUN2_74_V9A::All'   # for Simulation #same globalTag

from CondCore.DBCommon.CondDBSetup_cfi import *
era = 'Summer15_V5_MC'
process.jec = cms.ESSource("PoolDBESSource",CondDBSetup,
                           connect = cms.string('sqlite_file:'+os.path.expandvars('$CMSSW_BASE/src/CMGTools/RootTools/data/jec/'+era+'.db')),
                           toGet =  cms.VPSet(
          cms.PSet(
              record = cms.string("JetCorrectionsRecord"),
              tag = cms.string("JetCorrectorParametersCollection_"+era+"_AK4PF"),
              label= cms.untracked.string("AK4PF")
              ),
            cms.PSet(
              record = cms.string("JetCorrectionsRecord"),
              tag = cms.string("JetCorrectorParametersCollection_"+era+"_AK4PFchs"),
              label= cms.untracked.string("AK4PFchs")
              ),
          )
)
process.es_prefer_jec = cms.ESPrefer("PoolDBESSource",'jec')


#-----------------  Define the input source  --------------------------------------------

process.load('listDY')
#process.load('listW')

# How many events to process
process.maxEvents = cms.untracked.PSet(
#   input = cms.untracked.int32(10)
   input = cms.untracked.int32(-1)
)



#-----------------   re-run pfMET  and pfJets ------------------------

process.load("RecoMET.METProducers.PFMET_cfi")
process.pfMet.src = "packedPFCandidates"
process.pfMet.calculateSignificance = False

from RecoJets.JetProducers.ak4PFJets_cfi import ak4PFJets
process.ak4PFJets = ak4PFJets.clone(src = "packedPFCandidates")
process.ak4PFJets.doAreaFastjet = True

#-----------------   standard sequence  ------------------------

process.load("JetMETCorrections.Configuration.JetCorrectionServices_cff")
process.load("JetMETCorrections.Configuration.JetCorrectors_cff")
from JetMETCorrections.Type1MET.correctionTermsPfMetType1Type2_cff import corrPfMetType1
process.corrPfMetType1 = corrPfMetType1.clone()

from JetMETCorrections.Type1MET.correctedMet_cff import pfMetT1
process.pfType1CorrectedMet = pfMetT1.clone()
process.corrPfMetType1.jetCorrEtaMax = cms.double(9.9)

#-----------------   CHS standard sequence  ------------------------
#http://cmslxr.fnal.gov/source/PhysicsTools/PatAlgos/test/miniAOD/example_jet_and_met.py#0013

process.chs = cms.EDFilter("CandPtrSelector", src = cms.InputTag("packedPFCandidates"), cut = cms.string("fromPV"))
process.ak4PFJetsCHS = ak4PFJets.clone(src = 'chs', doAreaFastjet = True)

process.corrPfMetType1CHS = process.corrPfMetType1.clone()
process.corrPfMetType1CHS.src = cms.InputTag("ak4PFJetsCHS")
process.corrPfMetType1CHS.jetCorrLabel = cms.InputTag("ak4PFCHSL1FastL2L3Corrector")
process.corrPfMetType1CHS.offsetCorrLabel = cms.InputTag("ak4PFCHSL1FastjetCorrector")

process.pfType1CorrectedMetCHS = pfMetT1.clone()
process.pfType1CorrectedMetCHS.srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType1CHS","type1"))

#---------------------------------------------------------------
#   mixed here, full jets and take the CHS corrections

process.corrPfMetType1Mix = process.corrPfMetType1.clone()
process.corrPfMetType1Mix.src = cms.InputTag("ak4PFJets")
process.corrPfMetType1Mix.jetCorrLabel = cms.InputTag("ak4PFCHSL1FastL2L3Corrector")
process.corrPfMetType1Mix.offsetCorrLabel = cms.InputTag("ak4PFCHSL1FastjetCorrector")

process.pfType1CorrectedMetMix = pfMetT1.clone()
process.pfType1CorrectedMetMix.srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType1Mix","type1"))

#---------------------------------------------------------------

process.corrPfMetType120 = process.corrPfMetType1.clone()
process.corrPfMetType120.type1JetPtThreshold = cms.double(20.0) 
process.pfType1CorrectedMet20 = pfMetT1.clone()
process.pfType1CorrectedMet20.srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType120","type1"))

process.corrPfMetType1CHS20 = process.corrPfMetType1CHS.clone()
process.corrPfMetType1CHS20.type1JetPtThreshold = cms.double(20.0) 
process.pfType1CorrectedMetCHS20 = pfMetT1.clone()
process.pfType1CorrectedMetCHS20.srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType1CHS20","type1"))

#---------------------------------------------------------------

process.treePath = cms.Path(
    process.pfMet * process.ak4PFJets
    * process.chs * process.ak4PFJetsCHS
    * process.ak4PFL1FastL2L3Corrector * process.ak4PFCHSL1FastL2L3Corrector
    * process.corrPfMetType1 * process.pfType1CorrectedMet
    * process.corrPfMetType1CHS * process.pfType1CorrectedMetCHS
    * process.corrPfMetType120 * process.pfType1CorrectedMet20
    * process.corrPfMetType1CHS20 * process.pfType1CorrectedMetCHS20
    * process.corrPfMetType1Mix * process.pfType1CorrectedMetMix
    )

process.output = cms.OutputModule("PoolOutputModule",
                                  outputCommands = cms.untracked.vstring('keep *',
                                                                         'keep *_pfType1CorrectedMet*_*_*',
                                                                         'keep *_pfType1CorrectedMetCHS*_*_*',
                                                                         'keep *_pfType1CorrectedMetMix*_*_*'
                                                                         ),
                                  fileName       = cms.untracked.string ("Output.root")
                                  )

# schedule definition                                                                                                       
process.endpath  = cms.EndPath(process.output) 

dumpFile  = open("Type1Central_dump.py", "w")
dumpFile.write(process.dumpPython())
dumpFile.close()
