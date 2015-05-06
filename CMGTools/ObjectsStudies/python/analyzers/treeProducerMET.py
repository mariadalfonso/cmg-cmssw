from PhysicsTools.Heppy.analyzers.core.AutoFillTreeProducer  import * 

met_globalVariables = [
    NTupleVariable("rho",  lambda ev: ev.rho, float, help="kt6PFJets rho"),
    NTupleVariable("nVert",  lambda ev: len(ev.goodVertices), int, help="Number of good vertices"),
##    NTupleVariable("nPU",  lambda ev: ev.nPU, long, help="getPU_NumInteractions"),

##    NTupleVariable("ntracksPV",  lambda ev: ev.goodVertices[0].tracksSize() , int, help="Number of tracks (with weight > 0.5)"),
##    NTupleVariable("ndofPV",  lambda ev: ev.goodVertices[0].ndof() , int, help="Degrees of freedom of the fit"),

   # ----------------------- lepton info -------------------------------------------------------------------- #     

    NTupleVariable("nLeptons",   lambda x : len(x.leptons) if  hasattr(x,'leptons') else  0 , float, mcOnly=False,help="Number of associated leptons"),

    NTupleVariable("zll_pt", lambda ev : ev.zll_p4.Pt() if  hasattr(ev,'zll_p4') else  0 , help="Pt of di-lepton system"),
    NTupleVariable("zll_eta", lambda ev : ev.zll_p4.Eta() if  hasattr(ev,'zll_p4') else  0, help="Eta of di-lepton system"),
    NTupleVariable("zll_phi", lambda ev : ev.zll_p4.Phi() if  hasattr(ev,'zll_p4') else  0, help="Phi of di-lepton system"),
    NTupleVariable("zll_mass", lambda ev : ev.zll_p4.M() if  hasattr(ev,'zll_p4') else  0, help="Invariant mass of di-lepton system"),

   # ----------------------- dedicated met info -------------------------------------------------------------------- #     

    NTupleVariable("met_rawPt", lambda ev : ev.met.shiftedPt(12, 0), help="raw met p_{T}"),
    NTupleVariable("met_rawPhi", lambda ev : ev.met.shiftedPhi(12, 0), help="raw met phi"),

    NTupleVariable("met_caloPt", lambda ev : ev.met.caloMETPt(), help="raw met p_{T}"),
    NTupleVariable("met_caloPhi", lambda ev : ev.met.caloMETPhi(), help="raw met phi"),

   # ----------------------- tkMet info -------------------------------------------------------------------- #     

#    NTupleVariable("tkmet_pt", lambda ev : ev.tkMet.pt(), help="TK E_{T}^{miss} dz<0.1 pt"),
#    NTupleVariable("tkmet_phi", lambda ev : ev.tkMet.phi(), help="TK E_{T}^{miss} dz<0.1 phi"),
#    #    NTupleVariable("tkmet_sumEt", lambda ev : ev.tkSumEt, help="TK sumEt charged dz<0.1 pt"),
#    
#    #    NTupleVariable("tkmet_genPt", lambda ev : ev.tkGenMet.pt() if  hasattr(ev,'tkGenMet') else  0 , help="TK E_{T}^{miss} dz<0.1 pt"),
#    #    NTupleVariable("tkmet_genPhi", lambda ev : ev.tkGenMet.phi() if  hasattr(ev,'tkGenMet') else  0 , help="TK E_{T}^{miss} dz<0.1 phi"),
#    
#    NTupleVariable("tkmetchs_pt", lambda ev : ev.tkMetchs.pt(), help="TK E_{T}^{miss} fromPV>0 pt"),
#    NTupleVariable("tkmetchs_phi", lambda ev : ev.tkMetchs.phi(), help="TK E_{T}^{miss} fromPV>0 phi"),
#    #    NTupleVariable("tkmetchs_sumEt", lambda ev : ev.tkchsSumEt, help="TK sumEt charged fromPV>0"),
#    
#    NTupleVariable("tkmetPVLoose_pt", lambda ev : ev.tkMetPVLoose.pt(), help="TK E_{T}^{miss} fromPV>1 pt"),
#    NTupleVariable("tkmetPVLoose_phi", lambda ev : ev.tkMetPVLoose.phi(), help="TK E_{T}^{miss} fromPV>1 phi"),
#    #    NTupleVariable("tkmetPVLoose_sumEt", lambda ev : ev.tkPVLooseSumEt, help="TK sumEt charged fromPV>1"),
#    
#    NTupleVariable("tkmetPVTight_pt", lambda ev : ev.tkMetPVTight.pt(), help="TK E_{T}^{miss} fromPV>2 pt"),
#    NTupleVariable("tkmetPVTight_phi", lambda ev : ev.tkMetPVTight.phi(), help="TK E_{T}^{miss} fromPV>2 phi"),
#    #    NTupleVariable("tkmetPVTight_sumEt", lambda ev : ev.tkPVTightSumEt, help="TK sumEt charged fromPV>2"),
#    
#    #    NTupleVariable("tkmetAssQuality_pt", lambda ev : ev.tkMetAssQuality.pt(), help="TK E_{T}^{miss} UsedInFitLoose || CompatibilityDz"),
#    #    NTupleVariable("tkmetAssQuality_phi", lambda ev : ev.tkMetAssQuality.phi(), help="TK E_{T}^{miss} UsedInFitLoose || CompatibilityDz"),
#    #    NTupleVariable("tkmetAssQuality_sumEt", lambda ev : ev.tkAssQualitySumEt, help="TK sumEt charged UsedInFitLoose || CompatibilityDz"),
    
    ]

met_globalObjects = {
    "met" : NTupleObject("met", metType, help="PF E_{T}^{miss}, after type 1 corrections"),
#    "metraw" : NTupleObject("metraw", metType, help="PF E_{T}^{miss}"),
#    "metType1chs" : NTupleObject("metType1chs", metType, help="PF E_{T}^{miss}, after type 1 CHS jets"),
    #"tkMet" : NTupleObject("tkmet", metType, help="TK PF E_{T}^{miss}"),
    #"metNoPU" : NTupleObject("metNoPU", fourVectorType, help="PF noPU E_{T}^{miss}"),
    }

met_collections = {
    "genleps"         : NTupleCollection("genLep",     genParticleWithLinksType, 10, help="Generated leptons (e/mu) from W/Z decays"),
    "gentauleps"      : NTupleCollection("genLepFromTau", genParticleWithLinksType, 10, help="Generated leptons (e/mu) from decays of taus from W/Z/h decays"),
    "gentaus"         : NTupleCollection("genTau",     genParticleWithLinksType, 10, help="Generated leptons (tau) from W/Z decays"),                            
    "generatorSummary" : NTupleCollection("GenPart", genParticleWithLinksType, 100 , help="Hard scattering particles, with ancestry and links"),
    }
