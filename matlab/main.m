iterations = 100
repeats = 20
readCosts = [1 5 10]

% Repeat plot function for each reading cost value, and for both energy/agent and total energy
% The function energyplot will export a plot in PNG
for cost = readCosts
    energyplot("Energy per agent", "energy_per_agent", 7, iterations, repeats, cost);
end
for cost = readCosts
    energyplot("Total energy", "total_energy", 8, iterations, repeats, cost);
end
