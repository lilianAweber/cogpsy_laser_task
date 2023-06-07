% This is an example script for generating stimulus sequences in the Laser
% task.

% Sort out paths and source data
currentPath = fileparts(mfilename);
addpath(fullfile(fullfile(currentPath)));
outputRoot = fullfile(currentPath, 'sequences');

% First, we have to create a session, containing as many block sequences as
% we need for one run of the laser task.

% Sessions are created by the function:
% generateLaserSession.m 
% For the COGPSY studz, we use 1 session with 4 blocks for the main experiment, 
% and 1 block for the training.
% Sessions should be inspected (using the analyseSession.m function) and
% selected based on their features.

% In the main experiment, we counterbalance the order of
% stabilities (volatile versus stable) and the assignment of source colours to
% conditions across participants. Each session has 4 blocks.

%% Task intro & practice
% First, we want to create a short practice/training sequence for
% demonstrating the idea of the paradigm and first practice.
% For this, we only use 1 block stimulus with 1min duration and
% intermediate volatility, but smaller SD.
blockSequence = 3;
session = generateLaserSessionPractice(blockSequence);

% We use these plots to judge whether we like the session:
[fh1, fh2] = analyseSession(session);

% If we don't like it, we generate a new one until we're happy.
% If we like it, we write it to file as .csv and .mat:
sessionFileName = 'practice_v1';
writeSessionToCsvFile(session, sessionFileName, outputRoot);
save(fullfile(outputRoot, ['session_' sessionFileName '.mat']), 'session');
savefig(fh1, fullfile(outputRoot, ['session_' sessionFileName '_move.fig']))
savefig(fh2, fullfile(outputRoot, ['session_' sessionFileName '_steps.fig']))
fh = plotSession(session,0);
savefig(fh, fullfile(outputRoot, ['session_' sessionFileName '_sessionPlot.fig']))
% This will automatically create a .csv files named 'practice_v1_block1.csv'

%% Main experiment
% We repeat the same procedure to produce 4 new blocks with the same
% statistics that we can use for the main MEG session.
blockSequence = [1 1 2 2];
session = generateLaserSession(blockSequence);
[fh1, fh2] = analyseSession(session);
% If we like it, we write it to file as .csv and .mat:
sessionFileName = 'main_v1';
writeSessionToCsvFile(session, sessionFileName, outputRoot);
save(fullfile(outputRoot, ['session_' sessionFileName '.mat']), 'session');
savefig(fh1, fullfile(outputRoot, ['session_' sessionFileName '_move.fig']))
savefig(fh2, fullfile(outputRoot, ['session_' sessionFileName '_steps.fig']))
fh = plotSession(session,0);
savefig(fh, fullfile(outputRoot, ['session_' sessionFileName '_sessionPlot.fig']))

%% Background MMN sequence
% We also create 4 blocks of MMN, with 2 blocks stable and 2 blocks
% volatile:
generateMmnSequence
% This will implement the current MMN design and save the block .csv files
% and the session .mat file including sequence stats as "mmn_v1".

%% Session csv files and counterbalancing
% Next, we have to create a full session .csv file which will list the
% order in which we present these blocks, and the assignment of colours and
% stability conditions. These orders should be counterbalanced across
% participants (most importantly, whether they see the volatile or the
% stable block type first). For each participant, we can choose one of 4
% available orders:
% orders 1 and 3 start with a stable block, 2 and 4 start with volatile
% orders 1 and 2 get colour assignment 1, orders 3 and 4 get the other
% assignment.
% We will create a session csv file for each of these orders.

% To indicate the task version we use the taskFlag:
taskFlag = 'main';
% We have to keep track of our block file names as well:
seqVersion = 'v1';

% This function will then automatically create the overall sequence files -
% we do this for all 4 possible orders
for orderIndex = 1:4
    generateCogpsySessionCsvFiles(seqVersion, orderIndex, taskFlag, outputRoot);
end

%{
% Finally, we also create session csv file for the task practice during
% task introduction:
taskFlag = 'practice';
seqVersion = 'v1';
for orderIndex = 1:4
    generatePeduksSessionCsvFiles(seqVersion, orderIndex, taskFlag, outputRoot);
end
%}