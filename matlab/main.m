iterations = 100
repeats = 20
readCosts = [1 5 10]

for cost = readCosts
    energyplot("Energy per agent", "energy_per_agent", 7, iterations, repeats, cost);
end
for cost = readCosts
    energyplot("Total energy", "total_energy", 8, iterations, repeats, cost);
end
