function res = UnitCol(vector, unitString)
s = size(vector);
if (~(s(1) == 1 || s(2) == 1))
    disp("erwarte vektor");
    return;
end
l = length(vector);

res = strings(l, 1);
for i=1:l
    res(i) = num2strSci(vector(i)) + " \, " + "\mathrm{" + unitString + "}";
end

end