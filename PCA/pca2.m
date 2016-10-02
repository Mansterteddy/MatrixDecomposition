function[signals, PC, V] = pca2(data)
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
%PCA2: Perform PCA using SVD.
%data --- M*N matrix of input data(M dimensions, N trials)
%signals --- M*N matrix of projected data
%PC --- each column is a PC
%V --- M*1 matrix of variances

[M, N] = size(data);

%subtract off the mean for each dimension
mn = mean(data, 2);
data = data - repmat(mn, 1, N);

%construct the matrix Y
Y = data' / sqrt(N-1);

%SVD does it all
[u, S, PC] =svd(Y);

%calculate the variances
S = diag(S);
%分解出来的是奇异值，是特征值的开方。
V = S .* S;

%project the original data
signals = PC' * data;

end

