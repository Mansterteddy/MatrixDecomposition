function [signals, PC, V] = pca1(data)
%PCA1: Perform PCA using covariance 
% data --- M*N matrix of input data (M dimensions, N trials)
%signals --- M*N matrix of projected data
%PC --- each column is a PC
%V --- M*1 matrix of variances
%如果要处理二维数据，那么特征值就只有两个维度，因此对二维数据的分解，应当将data的维度处理成2*n

[M, N] = size(data);

%subtract off the mean for each dimension
mn = mean(data, 2);
data = data - repmat(mn, 1, N);

%calculate the covariance matrix
covariance = 1 / (N-1) * data * data';

%find the eigenvectors and eigenvalues
[PC, V] = eig(covariance);

%extract diagonal of matrix as vector
V = diag(V);

%sort the variance in decreasing order
[junk, rindices] = sort(-1*V);
V = V(rindices);
PC = PC(:, rindices);

%project the original data set
signals = PC' * data;