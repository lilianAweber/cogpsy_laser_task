function fh = plotSession( session, flagDegrees )
%PLOTSESSION Creates a figure with nBlocks subplots for the mean and actual
%stimulus in each block of a session in the laser task.

if flagDegrees
    val = 'valueVectorDeg';
    avg = 'meanValueVectorDeg';
else
    val = 'valueVector';
    avg = 'meanValueVector';
end

fh = figure;
for iBlock = 1:session.nBlocks
    subplot(2, 2, iBlock)
    plot(session.blocks(iBlock).stim.time, session.blocks(iBlock).stim.(val), '-k');
    hold on; 
    plot(session.blocks(iBlock).stim.time, session.blocks(iBlock).stim.(avg), '-y', 'linewidth', 2);
    title(['block type ' session.blocks(iBlock).blockType]);
end

end