function writeExpCsvFile( sessName, condList, blockList, imageList, addFileString, root2file )

if nargin < 6
    root2file = '';
end
if nargin < 5
    addFileString = '';
end

% set strings and lists to go through
blockFileNameBase = [sessName '_block'];
volatility = [0 0 1 1];
stochasticity = [0 1 0 1];

if ~exist(root2file, 'dir')
    mkdir(root2file)
end

% Write the csv file
fileID = fopen(fullfile(root2file, ['session_' addFileString sessName '.csv']), 'w');
% header
fprintf(fileID,'%7s,%11s,%10s,%13s,%13s\n', 'blockID','sourceImage','volatility', ...
    'stochasticity', 'blockFileName');

for iBlock = 1: numel(blockList)
    fprintf(fileID,'%1d,%16s,%1d,%1d,%17s\n', ...
        iBlock, imageList{condList(iBlock)},...
        volatility(condList(iBlock)), stochasticity(condList(iBlock)), ...
        [blockFileNameBase num2str(blockList(iBlock)) '.csv']);
end


fclose(fileID);

