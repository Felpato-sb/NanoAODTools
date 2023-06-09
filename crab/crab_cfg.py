from WMCore.Configuration import Configuration

config = Configuration()
config.section_('General')
config.General.requestName = 'TprimeBToTZ_M1800_2018'
config.General.transferLogs=True
config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'PSet.py'
config.JobType.scriptExe = 'crab_script.sh'
config.JobType.inputFiles = ['crab_script.py','../scripts/haddnano.py', '../scripts/keep_and_drop.txt']
config.JobType.sendPythonFolder = True
config.section_('Data')
config.Data.inputDataset = '/TprimeBToTZ_M-1800_LH_TuneCP5_PSweights_13TeV-madgraph_pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM'
config.Data.allowNonValidInputDataset = True
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/%s/%s' % ('lfavilla', 'DM_v0')
config.Data.publication = False
config.Data.outputDatasetTag = 'TprimeBToTZ_M1800_2018'
config.section_('Site')
config.Site.storageSite = 'T2_IT_Pisa'
