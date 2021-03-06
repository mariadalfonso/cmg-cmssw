#!/bin/bash

# DEFINE FOLDER PREFIX
outfolder_prefix="PREFIX"
WlikeCharge="${1}" # 1, -1

sed_and_run()
{
    # RUN MERGE RESULTS
    sed -i "s/useBatch =.*/useBatch = 1/g;\
            s/outfolder_prefix =.*/outfolder_prefix = \"${outfolder_prefix}\"/g;\
            s/runZanalysis =.*/runZanalysis = 0/g;\
            s/mergeSigEWKbkg =.*/mergeSigEWKbkg = 0/g;\
            s/runPrepareDataCardsFast =.*/runPrepareDataCardsFast = 0/g;\
            s/runClosureTestLikeLihoodRatio =.*/runClosureTestLikeLihoodRatio = 0/g;\
            s/mergeResults =.*/mergeResults = 1/g;\
            s/WlikeCharge =.*/WlikeCharge = ${WlikeCharge}  # Charge of the Wlike (+1,-1)/g" configdir/${1}.py
    python launch_analysis.py ${1}
}

# SET ENVIRONMENT VARIABLES BEFORE TO LAUNCH. CAVEAT: IT ASSUMES BASH
eval `scramv1 runtime -sh`
source /afs/cern.ch/sw/lcg/app/releases/ROOT/5.34.24/x86_64-slc6-gcc47-opt/root/bin/thisroot.sh

# COMMENT UNWANTED SYSTEMATICS

# CENTRAL
sed_and_run config_nominal

# SYST PDF NNPDF2.3
sed_and_run config_pdf_nnpdf23

# SYST EFFICIENCIES
sed_and_run config_eff_13
sed_and_run config_eff_14
sed_and_run config_eff_15
sed_and_run config_eff_16

# SYST MUON -1 sigma
sed_and_run config_muscale_minus1
sed_and_run config_mustat_minus1

# SYST MUON +1 sigma
sed_and_run config_muscale_plus1
sed_and_run config_mustat_plus1

# SYST ALTERNATIVE RECOIL MODEL
sed_and_run config_recoilmodel

# SYST RECOIL STAT +1 sigma
sed_and_run config_recoilstat_p1_plus1
sed_and_run config_recoilstat_p2_plus1
sed_and_run config_recoilstat_p3_plus1
sed_and_run config_recoilstat_p4_plus1
sed_and_run config_recoilstat_p5_plus1
sed_and_run config_recoilstat_p6_plus1
sed_and_run config_recoilstat_p7_plus1
sed_and_run config_recoilstat_p8_plus1
sed_and_run config_recoilstat_p9_plus1
sed_and_run config_recoilstat_p10_plus1
sed_and_run config_recoilstat_p11_plus1
sed_and_run config_recoilstat_p12_plus1

# SYST RECOIL STAT -1 sigma
sed_and_run config_recoilstat_p1_minus1
sed_and_run config_recoilstat_p2_minus1
sed_and_run config_recoilstat_p3_minus1
sed_and_run config_recoilstat_p4_minus1
sed_and_run config_recoilstat_p5_minus1
sed_and_run config_recoilstat_p7_minus1
sed_and_run config_recoilstat_p8_minus1
sed_and_run config_recoilstat_p6_minus1
sed_and_run config_recoilstat_p9_minus1
sed_and_run config_recoilstat_p10_minus1
sed_and_run config_recoilstat_p11_minus1
sed_and_run config_recoilstat_p12_minus1

