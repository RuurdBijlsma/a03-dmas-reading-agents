results = csvread('data/test_123.csv',1,0);
agents = results(:, 3);
energy = results(:, 6);

plot(agents, energy);
title('Call me once')
xlabel('Agents')
ylabel('Energy')