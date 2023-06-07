function [ fh1, fh2 ] = analyseSession( session )

col = laser_colours;
condColors = [col.stablePrecise; col.volatilePrecise; col.volatileNoisy];
condLabels = session.blockTypes;

if session.nBlocks > 1
    nSes = session.nBlocks/4;
else
    nSes = 1;
end

% Sum of overall mean movement - we want the volatile conditions to be
% clearly different from the stable ones (and no diff between noise levels)
fh1 = figure;
offset = [-0.1 -0.05 0.05 0.1];
for iSes = 1:nSes
    for iBlock = 1:session.nBlocks
        iBlockTotal = (iSes-1)*4 + iBlock;
        condition = session.blocks(iBlockTotal).blockID;
        move = sum(abs(diff(session.blocks(iBlockTotal).stim.meanValues)));
        %trueMean = unwrap(session.blocks(iBlockTotal).stim.meanValueVectorDeg*pi/180);
        %move = sum(abs(diff(trueMean)));
        ph(iBlock) = plot(iSes + offset(iBlock), move, 'o', 'color', condColors(condition, :), ...
            'MarkerFaceColor', condColors(condition, :));
        hold on
    end
end
if session.nBlocks > 1
    legend([ph(1) ph(2) ph(3) ph(4)], condLabels{session.blockSequence}, 'location', 'east', 'box', 'off');
else
    legend([ph(1)], condLabels{3}, 'location', 'east', 'box', 'off');
end
xticks([1:nSes]);
xlim([0.5 nSes+0.5]);
xlabel('session')
ylabel('sum(mean steps)');
title('overall movement per condition, session')
box off

% Number of steps of different sizes - we want the noisy and volatile 
% conditions to have sufficient large steps
fh2 = figure;
for iSes = 1:nSes
    subplot(1, nSes, iSes);
    for iBlock = 1:session.nBlocks
        iBlockTotal = (iSes-1)*4 + iBlock;
        condition = session.blocks(iBlockTotal).blockID;
        steps = abs(diff(session.blocks(iBlockTotal).stim.meanValues));
        nSteps(iSes, iBlock, 1) = numel(find(steps==15));
        nSteps(iSes, iBlock, 2) = numel(find(steps==30));
        nSteps(iSes, iBlock, 3) = numel(find(steps==45));
        
        ph(iBlock) = plot([1:3], squeeze(nSteps(iSes, iBlock, :)), '-o', 'color', condColors(condition, :), ...
            'MarkerFaceColor', condColors(condition, :));
        hold on
    end
    title(['session ' num2str(iSes)])
    if iSes ==1
        ylabel('number of steps')
        if session.nBlocks > 1
            legend([ph(1) ph(2) ph(3) ph(4)], condLabels{session.blockSequence}, 'box', 'off');
        else
            legend([ph(1)], condLabels{3}, 'box', 'off');
        end
    end
    xticks([1:3])
    xticklabels({'small', 'medium', 'large'});
    xlabel('step size');
    box off
end
linkaxes
yLims = ylim;
ylim([yLims(1) yLims(2)+4]);

disp('nJumps per condition:')
sum(nSteps, [1 3])

end