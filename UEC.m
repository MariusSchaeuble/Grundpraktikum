function res = UEC(vector, unitString, errorVector)
s = size(vector);
if (~(s(1) == 1 || s(2) == 1))
    disp("erwarte vektor bei den werten");
    return;
end
s2 = size(errorVector);
if (~(s2(1) == 1 || s2(2) == 1))
    disp("erwarte vektor bei den fehlern");
    return;
end
if length(vector) ~= length(errorVector)
    disp("ungleiche längen");
    return;
end
l = length(vector);
res = strings(l, 1);
for i=1:l
    val = num2strSci(vector(i));
    error = num2strSci(errorVector(i));
    res(i) = "(" + val + " \pm " + error + ")" + " \, " + "\mathrm{" + unitString + "}";
end
end
%COPY of UnitErrorCol, zur abkürzung