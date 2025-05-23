import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunesRun3ECM13p6TeV.PythiaCP5Settings_cfi import *


source = cms.Source("EmptySource")
generator = cms.EDFilter('Pythia8ConcurrentGeneratorFilter',
        comEnergy = cms.double(13600.0),
        crossSection = cms.untracked.double(1.0),
        # filterEfficiency = cms.untracked.double(0.0558),
        filterEfficiency = cms.untracked.double(1),
        maxEventsToPrint = cms.untracked.int32(0),
        pythiaHepMCVerbosity = cms.untracked.bool(False),
        pythiaPylistVerbosity = cms.untracked.int32(0),

        PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        # pythia8PSweightsSettingsBlock, ## Newline added
            # processParameters = cms.vstring(
            # 'PromptPhoton:qg2qgamma = on       ! prompt photon production',
            # 'PromptPhoton:qqbar2ggamma = on    ! prompt photon production',
            # 'PromptPhoton:gg2ggamma = on       ! prompt photon production',
            # 'PhaseSpace:pTHatMin = 40.         ! minimum pt hat for hard interactions',
            # 'PhaseSpace:pTHatMax = -1          ! maximum pt hat for hard interactions'),



            processParameters = cms.vstring('Higgs:useBSM = on',
              'HiggsBSM:gg2H2 = on',
              '35:m0 = 125.',
              '35:onMode = off',
              '35:onIfMatch = 25 25',
              '25:mMin = 3',
              '25:m0 = 10.',
              '25:onMode = off',
              '25:onIfMatch = 15 -15'
              ),
            parameterSets = cms.vstring('pythia8CommonSettings',
                                        'pythia8CP5Settings',
                                        # 'pythia8PSweightsSettings',# New line added
                                        'processParameters')
            )
)

# gj_filter = cms.EDFilter("PythiaFilterGammaGamma",
#     PtSeedThr = cms.double(5.0),
#     EtaSeedThr = cms.double(2.8),
#     PtGammaThr = cms.double(0.0),
#     EtaGammaThr = cms.double(2.8),
#     PtElThr = cms.double(2.0),
#     EtaElThr = cms.double(2.8),
#     dRSeedMax = cms.double(0.0),
#     dPhiSeedMax = cms.double(0.2),
#     dEtaSeedMax = cms.double(0.12),
#     dRNarrowCone = cms.double(0.02),
#     PtTkThr = cms.double(1.6),
#     EtaTkThr = cms.double(2.2),
#     dRTkMax = cms.double(0.2),
#     PtMinCandidate1 = cms.double(15.),
#     PtMinCandidate2 = cms.double(15.),
#     EtaMaxCandidate = cms.double(3.0),
#     NTkConeMax = cms.int32(2),
#     NTkConeSum = cms.int32(4),
#     InvMassMin = cms.double(80.0),
#     InvMassMax = cms.double(14000.0),
#     EnergyCut = cms.double(1.0),
#     AcceptPrompts = cms.bool(True),
#     PromptPtThreshold = cms.double(15.0)
#
#     )

# ProductionFilterSequence = cms.Sequence(generator*gj_filter)

ProductionFilterSequence = cms.Sequence(generator)
