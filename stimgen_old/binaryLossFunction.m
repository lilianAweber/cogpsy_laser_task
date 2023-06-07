function loss = binaryLossFunction( shieldDegrees )
loss = 2*(10^(-4) - 0.0000555556*45/shieldDegrees);
end