results = csvread('data/test_1-400-20repeat.csv',1,0);
agents = results(:, 4);
energy = results(:, 7);

title('Test results')
xlabel('Agents')
ylabel('Energy')
plot(agents, energy);