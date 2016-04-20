#ifndef EPCOMBINATIONTOOL_H
#define EPCOMBINATIONTOOL_H

#include <string>
#include "CondFormats/EgammaObjects/interface/GBRForest.h"
#include "EgammaAnalysis/ElectronTools/interface/SimpleElectron.h"

class GBRForest;

class EpCombinationTool
{
    public:
        EpCombinationTool();
        ~EpCombinationTool();

        bool init(const GBRForest *forest) ;
        bool init(const std::string& regressionFile, const std::string& bdtName);
	void combine(SimpleElectron & mySimpleElectron, bool applyExtraHighEnergyProtection = false);


    private:
        GBRForest* m_forest;	

};


#endif
