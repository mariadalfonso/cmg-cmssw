from PhysicsTools.Heppy.analyzers.core.AutoFillTreeProducer  import * 

met_globalVariables = [
    NTupleVariable("rho",  lambda ev: ev.rho, float, help="kt6PFJets rho"),
    NTupleVariable("nVert",  lambda ev: len(ev.goodVertices), int, help="Number of good vertices"),

    NTupleVariable("metraw_pt", lambda ev : ev.metraw, help="rawmet"),
    NTupleVariable("metType1chs_pt", lambda ev : ev.metType1chs, help="metType1chs"),

    NTupleVariable("tkmet_pt", lambda ev : ev.tkMet.pt(), help="TK E_{T}^{miss} pt"),                                                                                                    
    NTupleVariable("tkmet_phi", lambda ev : ev.tkMet.phi(), help="TK E_{T}^{miss} phi"),    

    NTupleVariable("zll_pt", lambda ev : ev.zll_p4.Pt(), help="Pt of di-lepton system"),
    NTupleVariable("zll_eta", lambda ev : ev.zll_p4.Eta(), help="Eta of di-lepton system"),
    NTupleVariable("zll_phi", lambda ev : ev.zll_p4.Phi(), help="Phi of di-lepton system"),
    NTupleVariable("zll_mass", lambda ev : ev.zll_p4.M(), help="Invariant mass of di-lepton system"),

    ]

met_globalObjects = {
    "met" : NTupleObject("met", metType, help="PF E_{T}^{miss}, after type 1 corrections"),
    #"tkMet" : NTupleObject("tkmet", metType, help="TK PF E_{T}^{miss}"),
    #"metNoPU" : NTupleObject("metNoPU", fourVectorType, help="PF noPU E_{T}^{miss}"),
    }

met_collections = {
    "genleps"         : NTupleCollection("genLep",     genParticleWithLinksType, 10, help="Generated leptons (e/mu) from W/Z decays"),
    "gentauleps"      : NTupleCollection("genLepFromTau", genParticleWithLinksType, 10, help="Generated leptons (e/mu) from decays of taus from W/Z/h decays"),
    "gentaus"         : NTupleCollection("genTau",     genParticleWithLinksType, 10, help="Generated leptons (tau) from W/Z decays"),                            
    "generatorSummary" : NTupleCollection("GenPart", genParticleWithLinksType, 100 , help="Hard scattering particles, with ancestry and links"),
    }
