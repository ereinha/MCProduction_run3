from CRABClient.UserUtilities import config
config = config()
# See parameter defintions here: https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile#CRAB_configuration_parameters
Mass_tag = 'm3p2To8'
# Local job directory will be created in:
config.General.requestName = 'HToAATo2Tau2Photon_Hadronic_%s_pt30To300_pythia8_GEN_SIM_v4'%Mass_tag
config.General.workArea = 'crab_MC'
config.General.transferOutputs = True
config.General.transferLogs = True

# CMS cfg file goes here:
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'GEN_SIM_HToAATo2Tau2Photon_%s_pt5To150_cfg.py'%Mass_tag
config.Data.outputPrimaryDataset = 'GEN_SIM_HToAATo2Tau2Photon_%s_pt5To150_m3p2To8'%Mass_tag

#config.JobType.maxMemoryMB = 2800

# Define units per job here:
config.JobType.allowUndistributedCMSSW = True
config.JobType.eventsPerLumi=500
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 500
NJOBS = 100
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
# config.Data.publication = True

# Output files will be stored in config.Site.storageSite at directory:
config.Data.outLFNDirBase = '/store/group/lpcml/bbbam/MCGeneration_run3'
config.Site.storageSite = 'T3_US_FNALLPC'
