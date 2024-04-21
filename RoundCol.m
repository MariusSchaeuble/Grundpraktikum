function res = RoundCol(vector, unitString, errorVector, factor)
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
    r = roundSci2(vector(i), errorVector(i));
    if factor == 0
        res(i) = "(" + r(1) + " \pm " + r(2) + ")" + " \, " + "\mathrm{" + unitString + "}";
    else
        val = (10^factor)*str2num(r(1));
        error = (10^factor)*str2num(r(2));
        val = sprintf("%." + num2str(max([0, str2num(r(3)) - factor])) + "f",val);
        error = sprintf("%." + num2str(max([0, str2num(r(3)) - factor])) + "f",error);
        res(i) = "(" + val + " \pm " + error + ")" + " \, " + "\mathrm{" + unitString + "}";
    end
end


end