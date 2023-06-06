function loss = computeBlockLoss( laserDist, shieldSize, lossFactor)

nBeams = numel(laserDist);
losses = NaN(nBeams,1);
for iCp = 1: nBeams
    if laserDist(iCp) > shieldSize(iCp)
        losses(iCp) = lossFactor;
    elseif shieldSize < 15
        losses(iCp) = 0;
    elseif shieldSize(iCp) > 15 && shieldSize(iCp) < 25
        losses(iCp) = lossFactor/3;
    else
        losses(iCp) = lossFactor/2;
    end
end

loss = sum(losses);

end