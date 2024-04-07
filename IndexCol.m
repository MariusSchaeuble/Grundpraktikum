function res = IndexCol(n)
res = strings(n, 1);
for i=1:n
    res(i) = num2str(i);
end
end