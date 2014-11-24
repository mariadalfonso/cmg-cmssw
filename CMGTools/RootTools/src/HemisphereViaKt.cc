#include "CMGTools/RootTools/interface/HemisphereViaKt.h"
#include "FWCore/Utilities/interface/Exception.h"

using namespace std;
using namespace fastjet;

using std::vector;
using std::cout;
using std::endl;

HemisphereViaKt::HemisphereViaKt(const std::vector<LorentzVector> & objects) : 
  ktpower(-1), status(0), dbg(1) {
  numLoop =0;

  fjInputs_.clear();
  int index=0;
  for (const LorentzVector &o : objects) {
    fastjet::PseudoJet j(o.Px(),o.Py(),o.Pz(),o.E());
    j.set_user_index(index); index++; // in case we want to know which piece ended where
    fjInputs_.push_back(j);
  }



}

HemisphereViaKt::HemisphereViaKt(const std::vector<LorentzVector> & objects,double ktpower) : 
  ktpower_(ktpower), rparam_(50.0), status(0), dbg(1) {
  numLoop =0;

  fjInputs_.clear();
  int index=0;
  for (const LorentzVector &o : objects) {
    fastjet::PseudoJet j(o.Px(),o.Py(),o.Pz(),o.E());
    j.set_user_index(index); index++; // in case we want to know which piece ended where
    fjInputs_.push_back(j);
  }

}

std::vector<math::XYZTLorentzVector > HemisphereViaKt::getGrouping(){
  this->Reconstruct();
  return JetObjectsAll_;
}

int HemisphereViaKt::Reconstruct(){

  /*
  numLoop=0; // initialize numLoop for Zero
  int vsize = (int) Object_Px.size();
  if((int) Object_Py.size() != vsize || (int) Object_Pz.size() != vsize){
    cout << "WARNING!!!!! Input vectors have different size! Fix it!" << endl;
    return 0;
  }


  ///
  // define jet inputs
  fjInputs_.clear();
  for (int i = 0; i <vsize; ++i){
    fastjet::PseudoJet j(Object_Px[i],Object_Py[i],Object_Pz[i],Object_E[i]);
    //if ( fabs(j.rap()) < inputEtaMax )
    fjInputs_.push_back(j);
  }
  */

  // choose a jet definition
  fastjet::JetDefinition jet_def;

  // prepare jet def 
  // rparam_ unused for the exclusive jets  set here to a default lenght
  if (ktpower_ == 1.0) {
    jet_def = JetDefinition(kt_algorithm, rparam_);
  }  else if (ktpower_ == 0.0) {
    jet_def = JetDefinition(cambridge_algorithm, rparam_);
  }  else if (ktpower_ == -1.0) {
    jet_def = JetDefinition(antikt_algorithm, rparam_);
  } 
  
  // print out some infos
  //  cout << "Clustering with " << jet_def.description() << endl;
  ///
  // define jet clustering sequence
  fjClusterSeq_ = ClusterSequencePtr( new fastjet::ClusterSequence( fjInputs_, jet_def)); 

  // recluster jet
  // std::vector<fastjet::PseudoJet> inclusiveJets = fastjet::sorted_by_pt( fjClusterSeq_->inclusive_jets());
  std::vector<fastjet::PseudoJet> exclusiveJets = fastjet::sorted_by_pt( fjClusterSeq_->exclusive_jets(2) );


  //  cout << "number of jets " << fjInputs_.size() << endl;
  //  cout << "number of hemispheres " << exclusiveJets.size() << endl;
  /*
  for (unsigned int i = 0; i <exclusiveJets.size(); ++i){
    
    JetObject_Px.push_back(exclusiveJets.at(i).px());
    //    cout << "i=" << i << " px=" << exclusiveJets.at(i).px() ;
    JetObject_Py.push_back(exclusiveJets.at(i).py());
    //    cout << " py=" << exclusiveJets.at(i).py() << endl;
    JetObject_Pz.push_back(exclusiveJets.at(i).pz());
    JetObject_E.push_back(exclusiveJets.at(i).e());
  }
  */

  JetObjectsAll_.clear();
  for (const fastjet::PseudoJet & pj : exclusiveJets) {
    JetObjectsAll_.push_back( LorentzVector( pj.px(), pj.py(), pj.pz(), pj.e() ) );
  }

  /*
  for (unsigned int i = 0; i < exclusiveJets.size(); i++ ) {
    std::vector<PseudoJet> constituents = exclusiveJets.at(i).constituents();
    cout << " hemisphere (" << i << ") with N=" << constituents.size() << " jets [ and pt,eta,phi,mass=" << exclusiveJets.at(i).pt() << 
      "," << exclusiveJets.at(i).eta() << ","<< exclusiveJets.at(i).phi() << ","<< exclusiveJets.at(i).m() << "]"<< endl;

    for (unsigned int j=0; j<constituents.size(); j++) {
      cout << "    pt (" << i << ")" << constituents.at(j).pt();
    }
    cout << " " << endl;
  }
  */


  if(JetObjectsAll_.size()<2) return -1;
  return 1;
    
    
}
