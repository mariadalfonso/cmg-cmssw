from DataFormats.FWLite import Handle, Events
##events = Events("root://eoscms//eos/cms/store/relval/CMSSW_7_3_2_patch1/DoubleMuParked/MINIAOD/GR_R_73_V0_HcalExtValid_RelVal_zMu2012D-v1/00000/04805FAA-F0B3-E411-9F29-002590593872.root")
events = Events("/tmp/dalfonso/04805FAA-F0B3-E411-9F29-002590593872.root")
cands = Handle("vector<pat::PackedCandidate>")

import ROOT
hdz = ROOT.TH1F("dz", "dz", 1000, 0, 1.)
hfromPV = ROOT.TH1F("fromPV", "fromPV", 4, 0, 4.)

hdzPV2d = ROOT.TH2F("dzPV", "dzPV", 1000, 0, 1., 4, 0, 4.)

i = 0
for event in events:
    print "Event", i
    event.getByLabel("packedPFCandidates", cands)
    j = 0
    for cand in cands.product():
        if cand.charge()!=0:
            hdz.Fill(abs(cand.dz()))
            hfromPV.Fill(cand.fromPV())
            hdzPV2d.Fill(abs(cand.dz()),cand.fromPV())
#            print "    Cand", j, cand.charge(), cand.pt(), cand.dz(), cand.fromPV()
        j += 1
    i += 1
#    if event%100:
#    print 'event=',i
#    if i >= 10000: break

hfile = ROOT.TFile( 'hsimple.root', 'RECREATE', 'Demo ROOT file with histograms' )

c = ROOT.TCanvas ( "c" , "c" , 800, 800 )
c.cd()
hdzPV2d.Draw()
hdzPV2d.Write()
hdz.Write()
hfromPV.Write()
hfile.Write()
