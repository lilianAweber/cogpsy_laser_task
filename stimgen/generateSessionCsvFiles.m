function generateSessionCsvFiles( seqVersion, orderIndex, taskFlag )
%GENERATESESSIONCSVFILES Generates two high-level csv files for the PEDUKS Laser
%task to be read into PsychoPy / Pavlovia: a training sequence and a main task
%sequence. Currently, the latter is a list of 12 block files, ordered in 3 
%"sessions" (4-block chunks), the order of which can be counterbalanced across 
%participants. 
%   IN:     seqVersion  - string referring to an available set of block
%                       stimuli, e.g. "CBv3"
%           orderIndex  - scalar between 1 and 3, to choose one the three
%                       available orders in which sessions are presented
%           taskFlag    - string indicating the task version we are
%                       creating these for. options: 'online',
%                       'onlineTrain', 'EEG'

% Available lists
% 4 different colours
imageList = {'radioactive1.png', 'radioactive2.png', 'radioactive3.png',...
    'radioactive4.png'};

% We have generated 12 blocks, where each condition of the 2x2 design
% (volatility/stochasticity) appears three times. The 12 blocks run from 1
% to 12, and always start with condition 1:
% blocks = 1:12; % (blocks refers to the block number of the .csv file)
% conditions = [1:4 1:4 1:4]; % (conditions refers to volatility &
% stochasticity)

% Now we want to vary the order of conditions within each mini-session of 4
% blocks. We can vary whether participants see volatile vs stable first
% (but always starting with precise) - this will become orders 1 and 2 - or
% whether participants experience noise or volatility first (but always
% starting with stable & precice) - this will become orders 1 and 3. 

% To this end, we generate three differenty shuffled mini-sessions:
% 1 starts with stable & introduces noise first, 2 starts with volatile, 
% 3 starts with stable precise and introduces volatility first:
conditions = {[1 2 3 4], [3 4 1 2], [1 3 2 4]};
blocks = {conditions{1}, conditions{2}+4, conditions{3}+8};

% We do the same for the baseline sessions, where we only have time for two
% mini-sessions (i.e., 8 blocks)
blConditions = {[1 2 3 4], [3 4 1 2]};
% baseline blocks refers to the block number of the .csv file (...block1.csv)
blBlocks = {blConditions{1}, blConditions{2}+4};

% These are the possible orders to choose from for the three mini-sessions
% (this is what we counterbalance across participants)
orders = {[1 3 2], [3 1 2], [2 3 1]}; % order 1 starts with stable, 2 with volatile
blOrders = {[1 2], [2 1]}; % in baseline, order of stable/volatile is flipped

toneConditions = {[1 3 2 3], [3 3 2 1], [1 2 3 3]};
toneBlocks = {[1 3 2 4], [8 7 6 5], [9 10 11 11]};

toneOrders = {[1 2 3], [2 3 1], [3 1 2]};
%toneOrderIndex = 1;

switch taskFlag
    case 'online'
        % Generate one main task sequence (depends on orderIndex) with 12
        % blocks
        condList = [conditions{orders{orderIndex}}];
        blockList = [blocks{orders{orderIndex}}];

        mainSessName = ['main_' seqVersion];

        writeExpCsvFile(mainSessName, condList, blockList, imageList);
        
    case 'onlineTrain'
        % 12 additional blocks
        
        % Generate 3 different sequences (sessions), order depending on
        % orderIndex, with 4 blocks each
        for iSess = 1:3
            condList = [conditions{orders{orderIndex}(iSess)}];
            blockList = [blocks{orders{orderIndex}(iSess)}];
            
            onlineSessName = ['onlineTrain_' seqVersion];
            addFileString = ['s' num2str(iSess) '_'];
            
            writeExpCsvFile(onlineSessName, condList, blockList, imageList, addFileString);
        end
        
    case 'EEG'
        % Generate 3 different sequences (sessions), order depending on
        % orderIndex, with 4 blocks each, plus tone sequences
        for iSess = 1:3
            condList = [conditions{orders{orderIndex}(iSess)}];
            blockList = [blocks{orders{orderIndex}(iSess)}];
            
            onlineSessName = ['main_' seqVersion];
            addFileString = ['s' num2str(iSess) '_'];
            
            % Additionally create 4 tone sequences for each block in the
            % session
            toneCondList = [toneConditions{toneOrders{orderIndex}(iSess)}];
            toneBlockList = [toneBlocks{toneOrders{orderIndex}(iSess)}];
            writeExpCsvFileWithTones(onlineSessName, condList, blockList, imageList, toneCondList, toneBlockList, addFileString);
        end
        
    case 'baseline'
        % Generate 2 different sequences (sessions), order depending on
        % orderIndex, with 4 blocks each, plus tone sequences
        for iSess = 1:2
            condList = [blConditions{blOrders{orderIndex}(iSess)}];
            blockList = [blBlocks{blOrders{orderIndex}(iSess)}];
            
            onlineSessName = ['baseline_' seqVersion];
            addFileString = ['s' num2str(iSess) '_'];
            
            % Additionally create tone sequences for each block in the
            % session
            toneCondList = [toneConditions{toneOrders{orderIndex}(iSess)}];
            toneBlockList = [toneBlocks{toneOrders{orderIndex}(iSess)}];
            writeExpCsvFileWithTones(onlineSessName, condList, blockList, imageList, toneCondList, toneBlockList, addFileString);
        end        
        
end

switch taskFlag
    case {'online', 'EEG'}
        % Generate a training sequence (always 1:4)
        trainCondList = conditions{1};
        trainBlockList = trainCondList;
        trainSessName = ['training_' taskFlag '_' seqVersion];

        writeExpCsvFile(trainSessName, trainCondList, trainBlockList, imageList);
end

end