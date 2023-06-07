function writeExpCsvFileWithTones( sessName, condList, blockList, imageList, ...
    toneCondList, toneBlockList, addFileString, root2file )

if nargin < 8
    root2file = '';
end
if nargin < 7
    addFileString = '';
end
blockFileNameBase = [sessName '_block'];
toneFileNameBase = 'mmn/mmn_v1_block';

volatility = [0 1];
stochasticity = [0 0];
toneVola = [0 1];
toneStocha = [0 0];

if ~exist(root2file, 'dir')
    mkdir(root2file)
end

fileID = fopen(fullfile(root2file, ['session_' addFileString sessName '.csv']), 'w');

fprintf(fileID,'%7s,%11s,%10s,%13s,%13s,%14s,%17s,%15s\n', 'blockID','sourceImage','volatility', ...
    'stochasticity', 'blockFileName', 'toneVolatility', 'toneStochasticity', 'toneSeqFileName');

for iBlock = 1: numel(blockList)
    fprintf(fileID,'%1d,%16s,%1d,%1d,%17s,%1d,%1d,%s\n', ...
        iBlock, imageList{condList(iBlock)},...
        volatility(condList(iBlock)), stochasticity(condList(iBlock)), ...
        [blockFileNameBase num2str(blockList(iBlock)) '.csv'], ...
        toneVola(toneCondList(iBlock)), toneStocha(toneCondList(iBlock)), ...
        [toneFileNameBase num2str(toneBlockList(iBlock)) '.csv']);
end


fclose(fileID);

