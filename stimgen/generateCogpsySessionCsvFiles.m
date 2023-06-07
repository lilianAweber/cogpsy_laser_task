function generateCogpsySessionCsvFiles( seqVersion, orderIndex, taskFlag, outputRoot )
%GENERATECOGPSYSESSIONCSVFILES Generates high-level csv files for the
%COGPSY Laser task to be read into PsychoPy / Pavlovia. This function can be used to
%create sequences for the initial task practice (taskFlag = 'practice'),
% and for the main MEG task session (taskFlag = 'main').
%   IN:     seqVersion  - string referring to an available set of block
%                       stimuli, e.g. "v1" - the rest of the block file
%                       name will be determined based on taskFlag (for
%                       initial training: 'practice_v1_block1.csv', and for
%                       MEG: 'main_v1_block1.csv')
%           orderIndex  - scalar between 1 and 4, to choose one the four
%                       available orders in which sessions are presented:
%                       orders 1 and 3: stable first; orders 2 and 4:
%                       volatile first; orders 1 and 2: colour assignment
%                       1; orders 3 and 4: colour assignment 2
%           taskFlag    - string indicating the task version we are
%                       creating these for. options: 'practice',
%                       and 'main'
%           outputRoot  - subfolder in which the csv files should be saved


% Current setup
% =============
% For the main experiment, we have created 4 different 
% stimulus sequences ('blocks'), where each condition of the design
% (volatile/stable) appears two times. The 4 blocks run from 1
% to 4, and always start with condition 1:
% blocks = 1:4; % (blocks refers to the block number of the .csv file)
% conditions = [1 1 2 2]; % (conditions refers to volatility levels)

% Across participants, we will counterbalance whether they saw
% the volatile or stable condition first - this will be order1 and order2.

% Transforming the order index
% ============================
stabOrders = [1 2 1 2];
imgOrders = [1 1 2 2];
stabOrderIndex = stabOrders(orderIndex);
imgOrderIndex = imgOrders(orderIndex);

% Summary of what we have available
% =================================
% 2 different colours, in 2 different assignments
imgAssignment1 = {'radioactive2.png', 'radioactive3.png'};
imgAssignment2 = {'radioactive3.png', 'radioactive2.png'};
imgLists = {imgAssignment1, imgAssignment2};

% available block files
blocks = 1:4;
% corresponding conditions
stabilities = [1 1 2 2]; % stab: ssvv

% possible block orders (= determines stability)
blockOrder1 = [1 3 2 4];
blockOrder2 = [3 1 4 2];
% this implements these stability orders:
stabOrder1 = stabilities(blockOrder1); % s,v,s,v
stabOrder2 = stabilities(blockOrder2); % v,s,v,s

% Summary of what our orderIndex will produce
% ===========================================
% these are the 2 different condition orders we will choose from
condOrders = {stabOrder1, stabOrder2};

% these are the 2 different block orders which implement the 2 different
% stability orders we will choose from (svsv or vsvs)
blockOrders = {blockOrder1, blockOrder2};

% Create the main session csv files
% =================================
switch taskFlag
    case 'practice'
        % We only use 1 block, so no need to create a session file here
        %{ 
        % Generate 1 sequence (session), order depending on
        % orderIndex, with 4 blocks
        condList = condOrders{stabOrderIndex};
        blockList = blockOrders{stabOrderIndex};
        imageList = imgLists{imgOrderIndex};
        
        % File names and output directory depend on taskFlag and orderIndex
        sessionName = ['practice_' seqVersion];
        root2file = fullfile(outputRoot, ['peduks_' sessionName '_order' num2str(orderIndex)]);
        
        for iSess = 1
            blockIdx = (1 + (iSess-1)*4) : (4 + (iSess-1)*4);
            sessCondList = condList(blockIdx);
            sessBlockList = blockList(blockIdx);
            
            addFileString = ['s' num2str(iSess) '_'];
            
            % Save a csv file for this mini-session
            writeExpCsvFile(sessionName, sessCondList, ...
                sessBlockList, imageList, addFileString, root2file);
        end
        %}
    
     case 'main'
        % Generate 1 session, order depending on orderIndex, with 4 blocks
        condList = condOrders{stabOrderIndex};
        blockList = blockOrders{stabOrderIndex};
        imageList = imgLists{imgOrderIndex};
        
        % File names and output directory depend on taskFlag and orderIndex
        sessionName = ['main_' seqVersion];
        root2file = fullfile(outputRoot, ['cogpsy_' sessionName '_order' num2str(orderIndex)]);
        
        for iSess = 1
            blockIdx = (1 + (iSess-1)*4) : (4 + (iSess-1)*4);
            sessCondList = condList(blockIdx);
            sessBlockList = blockList(blockIdx);
            
            addFileString = ['s' num2str(iSess) '_'];
            
            % Additionally create 4 tone sequences for each block in the
            % session - here we use the same volatility levels as for the
            % main task
            toneCondList = sessCondList;
            toneBlockList = sessBlockList;
            
            % Save a csv file for this mini-session
            writeExpCsvFileWithTones(sessionName, sessCondList, sessBlockList, ...
                imageList, toneCondList, toneBlockList, addFileString, root2file);
        end
end


end